import os
import re
from pathlib import Path
from typing import List, Dict

class FileAnalyzer:
    def __init__(self):
        self.current_data = {
            'classes': [],
            'structs': [],
            'methods': [],
            'properties': [],
            'enums': []
        }
        self.current_file = None

    def reset(self):
        self.current_data = {
            'classes': [],
            'structs': [],
            'methods': [],
            'properties': [],
            'enums': []
        }

    def analyze_file(self, file_path: Path):
        self.reset()
        self.current_file = file_path.stem
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
        self._extract_classes_and_structs(content)
        self._extract_methods(content)  # Método atualizado
        self._extract_enums(content)

    def _extract_classes_and_structs(self, content: str):
        pattern = re.compile(
            r'(class|struct)\s+(\w+)\s*{([^}]*)};?',
            re.DOTALL
        )
        
        for match in pattern.finditer(content):
            type_, name, body = match.groups()
            if type_ == 'class':
                self.current_data['classes'].append(name)
            else:
                self.current_data['structs'].append(name)
            self._extract_class_properties(body, name)

    def _extract_class_properties(self, body: str, class_name: str):
        prop_pattern = re.compile(
            r'(\w+)\s+(\w+)\s*;'
        )
        
        for match in prop_pattern.finditer(body):
            type_, name = match.groups()
            self.current_data['properties'].append({
                'class': class_name,
                'type': type_,
                'name': name
            })

    def _extract_methods(self, content: str):
        # Nova regex aprimorada
        method_pattern = re.compile(
            r'(?:(?:static|const|inline|virtual)\s+)*'  # Captura modificadores
            r'([\w:<>\s]+?)\s+'  # Tipos complexos com templates
            r'(\w+)\s*'          # Nome do método
            r'\((.*?)\)\s*'       # Parâmetros
            r'(?:const\s*)?'     # Const no final
            r'(?:\=?\s*(?:default|delete)\s*)?'  # Especificadores especiais
            r'[;{]', 
            re.DOTALL
        )
        
        for match in method_pattern.finditer(content):
            return_type = match.group(1).strip()
            name = match.group(2).strip()
            params = match.group(3).strip()
            
            self.current_data['methods'].append({
                'name': name,
                'return_type': return_type,
                'params': params
            })

    def _extract_enums(self, content: str):
        enum_pattern = re.compile(
            r'enum\s+(\w+_t)\s*{([^}]*)}',
            re.DOTALL
        )
        
        for match in enum_pattern.finditer(content):
            name, values = match.groups()
            self.current_data['enums'].append({
                'name': name,
                'values': [v.strip() for v in values.split(',') if v.strip()]
            })

    def generate_markdown(self) -> str:
        md = f"# {self.current_file}\n\n"
        md += f"### Localização\n`{self.current_file}.hpp`\n\n"
        
        if self.current_data['methods']:
            md += "### Funções Lua\n"
            for method in self.current_data['methods']:
                md += f"#{method['name']}\n"  # Alterado para o formato solicitado
            md += "\n"
        
        if self.current_data['structs']:
            md += "### Estruturas\n"
            for struct in self.current_data['structs']:
                md += f"- [[{struct}]]\n"
            md += "\n"
        
        if self.current_data['classes']:
            md += "### Classes\n"
            for cls in self.current_data['classes']:
                md += f"- [[{cls}]]\n" 
            md += "\n"
        
        if self.current_data['enums']:
            md += "### Enums\n"
            for enum in self.current_data['enums']:
                md += f"- [[{enum['name']}]]\n"
            md += "\n"
        
        return md

def setup_directories():
    current_dir = Path.cwd()
    input_dir = current_dir / 'input' / 'src'
    output_dir = current_dir / 'output' / 'src_new'
    
    input_dir.mkdir(parents=True, exist_ok=True)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    return input_dir, output_dir

def create_obsidian_notes():
    input_dir, output_dir = setup_directories()
    analyzer = FileAnalyzer()
    
    for hpp_file in input_dir.rglob('*.hpp'):
        analyzer.analyze_file(hpp_file)
        
        relative_path = hpp_file.relative_to(input_dir)
        output_path = output_dir / relative_path.with_suffix('.md')
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as md_file:
            md_content = analyzer.generate_markdown()
            
            # Adicionar links hierárquicos
            parent_links = []
            for part in reversed(relative_path.parent.parts):
                parent_links.append(f"[[{part}]]")
            
            if parent_links:
                md_content += "### Hierarquia\n" + " ➔ ".join(reversed(parent_links)) + "\n"
            
            md_file.write(md_content)

if __name__ == "__main__":
    create_obsidian_notes()
    print("Documentação Obsidian gerada com sucesso!")