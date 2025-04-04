# player_wheel

### Localização
`player_wheel.hpp`

### Funções Lua
#toString
#bool
#save
#remove
#load
#serialize
#deserialize
#PlayerWheel
#loadActiveGems
#saveActiveGems
#loadRevealedGems
#saveRevealedGems
#scrollAcquired
#unlockScroll
#loadKVScrolls
#saveKVScrolls
#loadKVModGrades
#saveKVModGrades
#loadDBPlayerSlotPointsOnLogin
#saveDBPlayerSlotPointsOnLogout
#checkSavePointsBySlotType
#saveSlotPointsHandleRetryErrors
#saveSlotPointsOnPressSaveButton
#addPromotionScrolls
#addGems
#addGradeModifiers
#improveGemGrade
#sendOpenWheelWindow
#sendGiftOfLifeCooldown
#initializePlayerData
#getSpellAdditionalTarget
#getSpellAdditionalDuration
#getSpellAdditionalArea
#handleTwinBurstsCooldown
#handleBeamMasteryCooldown
#canSelectSlotFullOrPartial
#canPlayerSelectPointOnSlot
#getWheelPoints
#getExtraPoints
#getMaxPointsPerSlot
#getUnusedPoints
#setPlayerCombatStats
#reloadPlayerData
#registerPlayerBonusData
#loadPlayerBonusData
#loadDedicationAndConvictionPerks
#addSpellToVector
#loadRevelationPerks
#getPlayerSliceStage
#getLesserGradeCost
#getGreaterGradeCost
#printPlayerWheelMethodsBonusData
#addInitialGems
#canOpenWheel
#getOptions
#gemsKV
#gemsGradeKV
#getGemGrade
#getRevealedGems
#getActiveGems
#getGemRotateCost
#getGemRevealCost
#resetPlayerData
#onThink
#checkAbilities
#checkGiftOfLife
#checkBattleInstinct
#checkPositionalTactics
#checkBallisticMastery
#checkCombatMastery
#checkDivineEmpowerment
#checkDrainBodyLeech
#checkBeamMasteryDamage
#checkBattleHealingAmount
#checkBlessingGroveHealingByTarget
#checkTwinBurstByTarget
#checkExecutionersThrow
#checkDivineGrenade
#checkAvatarSkill
#checkFocusMasteryDamage
#checkElementSensitiveReduction
#reduceAllSpellsCooldownTimer
#resetUpgradedSpells
#upgradeSpell
#downgradeSpell
#setStage
#setOnThinkTimer
#setMajorStat
#setSpecializedMagic
#setInstant
#addStat
#addResistance
#setSpellInstant
#resetResistance
#resetStats
#getInstant
#getHealingLinkUpgrade
#getStage
#getStage
#getSpellUpgrade
#getMajorStat
#getSpecializedMagic
#getStat
#getResistance
#getMajorStatConditional
#getOnThinkTimer
#getInstant
#getMitigationMultiplier
#getGiftOfLifeTotalCooldown
#getGiftOfLifeValue
#getGiftOfCooldown
#setGiftOfCooldown
#decreaseGiftOfCooldown
#sendOpenWheelWindow
#getPointsBySlotType
#setPointsBySlotType
#getCombatDataSpell
#setWheelBonusData
#getBeamAffectedTotal
#updateBeamMasteryDamage
#healIfBattleHealingActive
#adjustDamageBasedOnResistanceAndSkill
#calculateMitigation
#getGemIndex
#revealGem
#destroyGem
#switchGemDomain
#toggleGemLock
#setActiveGem
#removeActiveGem
#addRevelationBonus
#resetRevelationBonus
#addSpellBonus
#getSpellBonus
#selectBasicModifier2
#resetRevelationState
#processActiveGems
#applyStageBonuses
#applyStageBonusForColor
#applyRedStageBonus
#applyPurpleStageBonus
#applyBlueStageBonus

### Estruturas
- [[PlayerWheelMethodsBonusData]]
- [[Skills]]
- [[Leech]]
- [[Instant]]
- [[Stages]]
- [[Avatar]]
- [[PlayerWheelGem]]
- [[PromotionScroll]]

### Classes
- [[PlayerWheel]]

### Hierarquia
[[creatures]] ➔ [[players]] ➔ [[components]] ➔ [[wheel]]
