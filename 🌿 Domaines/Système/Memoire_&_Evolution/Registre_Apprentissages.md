---
type: memory-register
created: 2026-09-13
updated: 2026-09-13
tags:
  - systeme
  - memoire
  - auto-amelioration
parent: "[[MOC_Systeme_Execution]]"
---

# 🧠 Registre des Apprentissages & Heuristiques

> Ce registre est la mémoire procédurale vivante du Second Brain. Il capitalise les leçons extraites des frictions réelles (`Daily_Logs`) et documente l'évolution des règles opérationnelles.

---

## 🧭 Cycle de Vie d'un Apprentissage

Chaque constat suit une trajectoire rigoureuse pour éviter l'encombrement mémoriel :
1. `🔵 Observé` : Signal détecté dans un ou plusieurs Daily Logs, en cours de qualification.
2. `🟡 En test` : Heuristique ou ajustement appliqué à titre expérimental.
3. `🟢 Consolidé` : Principe validé par l'usage, transcrit dans [[AGENTS]] ou les protocoles d'agents.
4. `⚪ Archivé / Obsolète` : Règle dépréciée ou fusionnée pour éviter la calcification du système.

---

## 💻 1. Ingénierie & Architecture (Stockly SaaS)

### [2026-09-07] Unification systématique des dialogues en SideSheets
- **Statut** : `🟢 Consolidé` (Inscrit dans les ADR Stockly et protocoles UI)
- **Friction d'origine** : Prolifération de boîtes de dialogue modales hétérogènes causant des ruptures ergonomiques sur desktop/web et des comportements de défilement instables.
- **Cause racine** : Absence de pattern d'édition latérale unique pour les formulaires denses.
- **Heuristique consolidée** : Toute création ou modification d'entité catalogue/logistique recourt exclusivement au composant `StocklySideSheet`. Aucun modal flottant générique.

### [2026-08-27] Sanctuaire de la Stack Offline-First
- **Statut** : `🟢 Consolidé` (Règle d'or dans [[AGENTS]])
- **Friction d'origine** : Tentations récurrentes d'ajouter des dépendances ou des solutions de synchronisation alternatives.
- **Cause racine** : Complexité inhérente à la gestion de l'état bidirectionnel SQLite / Supabase.
- **Heuristique consolidée** : La stack Flutter / Supabase / SQLite offline-first est définitive. L'effort porte sur la résilience locale (désérialisation, migrations drift/sqlite), jamais sur un changement de socle.

---

## 🐺 2. Énergie, Rythme & Chronobiologie

### [2026-08-28] Sanctuaire du créneau Deep Work Wolf (18h - 22h)
- **Statut** : `🟢 Consolidé` (Transcrit dans la routine de Dave)
- **Friction d'origine** : Épuisement cognitif lors des tentatives de travail analytique lourd l'après-midi (zone de friction biologique).
- **Cause racine** : Non-alignement avec le chronotype Wolf et le cycle naturel du cortisol.
- **Heuristique consolidée** : L'après-midi est réservé aux activités à friction basse ou régénératrices (sport à 17h, veille, dessin, respiration). Le code profond est strictement protégé sur la plage 18h-22h.

---

## 🗂️ 3. Organisation & Rituels de Vie

### [2026-09-07] Règle des trois priorités nocturnes
- **Statut** : `🟢 Consolidé` (Protocole d'Anaïs)
- **Friction d'origine** : Démarrage hésitant le matin face à une to-do list surchargée et floue.
- **Cause racine** : Report de la prise de décision au moment du réveil, quand l'énergie de décision est encore basse.
- **Heuristique consolidée** : Définir exactement 3 cibles majeures la veille au soir entre 22h et 23h. Si le lendemain est un jour de basse énergie, basculer immédiatement en Mode B sans friction mentale.

---

## 📥 4. Nouveaux Signaux en Cours d'Observation

*Les signaux bruts extraits lors des revues hebdomadaires sont temporairement consignés ici avant d'être testés ou écartés.*

- *(Section mise à jour par Anaïs lors du rituel de rétro-mining)*

---

> ↖ [[MOC_Systeme_Execution|Retour au Système & Exécution]] · [[Buffer_Mutations|Accéder au Buffer de Mutations ➔]]
