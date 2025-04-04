# Canary Neural Docs: Mapeamento Neural para OTServers  
**Visualização Estruturada do Código-Fonte do Canary em Obsidian**  

[![GitHub repo size](https://img.shields.io/github/repo-size/Habdel-Edenfield/canary-docs)](https://github.com/Habdel-Edenfield/canary-docs)
[![GitHub](https://img.shields.io/github/license/Habdel-Edenfield/canary-docs)](https://github.com/Habdel-Edenfield/canary-docs/blob/main/LICENSE)
[![Discord](https://img.shields.io/discord/1234567890123456789?label=Suporte&logo=discord)](https://discord.gg/your-invite-link)

Ferramenta de documentação automatizada para análise do código-fonte do Canary (OTServer), convertendo-o em documentos Markdown interconectados para uso no Obsidian. Ideal para aprendizado e integração com sistemas de IA.

---

## 👋 Sobre o Projeto

Olá! Sou **Habdel Edenfield** ([GitHub](https://github.com/Habdel-Edenfield) | Discord: `Habdel_Edenfield`) e desenvolvi esta solução para:
- Facilitar o entendimento da arquitetura do Canary
- Criar base de conhecimento para treinamento de IA/RAG
- Oferecer documentação dinâmica e navegável

---

![Preview](https://i.imgur.com/jNLfYwB.png)

---

## 🛠️ Funcionalidades

- **Análise Automática de Código**
  - Extração de classes, structs e enums com links internos
  - Detecção de métodos com parâmetros e tipos de retorno
  - Mapeamento hierárquico de diretórios

- **Integração com Obsidian**
  - Links bidirecionais entre componentes
  - Visualização neural das relações internas
  - Base pronta para grafos de conhecimento

- **Suporte a Automação**
  - Saída em Markdown padronizado
  - Compatível com pipelines de CI/CD
  - Formatação otimizada para LLMs

---

## 🚀 Começando

### Pré-requisitos
- Python 3.8+
- Git instalado

### Instalação Rápida
```bash
git clone https://github.com/Habdel-Edenfield/canary-docs.git
cd canary-docs

# Cole seus arquivos .hpp em:
cp -R seus-arquivos/ input/src/

python canary_analyzer.py
```

## Estrutura de Pastas
```bash
📁 input/
└── 📁 src/
    └── ... (documentação original canary)
📁 output/
└── 📁 src_new/
    ├── account.md
    ├── player.md
    └── ... (documentação gerada)
```
