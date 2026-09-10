---
type: workflow
title: "Sync Auto Daily Logs → Notion"
created: 2026-08-25
tags:
  - workflow
  - notion
  - sync
parent: "[[MOC_Systeme_Execution]]"
---

# 🔄 Sync Auto : Daily Logs → Notion

> **Règle** : Quand Fabien envoie son bullet journal (photo ou texte), Anaïs synchronise **automatiquement** vers Notion **ET** le Second Brain Obsidian.

---

## 📋 Workflow en 4 étapes

### Étape 1 : Recevoir le journal
Fabien envoie :
- Soit une **photo** de son Bullet Journal
- Soit un **résumé texte** de sa journée

### Étape 2 : Créer le daily log Obsidian
Créer le fichier dans :
```
second_brain/🌿 Domaines/Système/Daily_Logs/YYYY-MM-DD_Jour.md
```

### Étape 3 : Synchroniser vers Notion
Utiliser l'API Notion pour créer la page :

**Parent Page ID** : `3c736a0c-6e01-818c-bd69-d64ef1653084`
**Token** : `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`
**Notion Version** : `2022-06-28`

### Étape 4 : Confirmer à Fabien
Montrer le lien Notion créé et demander si tout est bon.

---

## 🛠️ Script de Sync

```bash
#!/bin/bash
# sync_notion.sh - Synchronise un daily log vers Notion

NOTION_TOKEN="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"
PARENT_PAGE_ID="3c736a0c-6e01-818c-bd69-d64ef1653084"
NOTION_VERSION="2022-06-28"

# Exemple d'utilisation :
# curl -X POST 'https://api.notion.com/v1/pages' \
#   -H "Authorization: Bearer $NOTION_TOKEN" \
#   -H "Notion-Version: $NOTION_VERSION" \
#   -H "Content-Type: application/json" \
#   -d @/tmp/notion_payload.json
```

---

## 📝 Template JSON pour Notion

```json
{
  "parent": {
    "type": "page_id",
    "page_id": "3c736a0c-6e01-818c-bd69-d64ef1653084"
  },
  "icon": {
    "type": "emoji",
    "emoji": "🟢"
  },
  "properties": {
    "title": {
      "title": [
        {
          "text": {
            "content": "JOUR DATE"
          }
        }
      ]
    }
  },
  "children": [
    {
      "object": "block",
      "type": "heading_2",
      "heading_2": {
        "rich_text": [{"type": "text", "text": {"content": "Titre Section"}}]
      }
    },
    {
      "object": "block",
      "type": "to_do",
      "to_do": {
        "rich_text": [{"type": "text", "text": {"content": "Tâche"}}],
        "checked": false
      }
    }
  ]
}
```

---

## 🎨 Emojis par statut

| Journée | Emoji |
|---------|-------|
| Excellente (tout fait) | 🟢 |
| Bonne (la plupart fait) | 🟡 |
| Difficile (beaucoup reporté) | 🔴 |
| Planning (lendemain) | 📋 |

---

## 📍 Pages Notion Existantes

| Page | ID | Lien |
|------|-----|------|
| Daily Logs - Août 2026 | `3c736a0c-6e01-818c-bd69-d64ef1653084` | [Ouvrir](https://app.notion.com/p/Daily-Logs-Ao-t-2026-3c736a0c6e01818cbd69d64ef1653084) |
| Lundi 24 Août | `3c736a0c-6e01-817d-9dad-ff3c610249eb` | [Ouvrir](https://app.notion.com/p/Lundi-24-Ao-t-2026-3c736a0c6e01817d9dadff3c610249eb) |
| Mardi 25 Août | `3c736a0c-6e01-8110-96b1-eea58d93d95e` | [Ouvrir](https://app.notion.com/p/Mardi-25-Ao-t-2026-3c736a0c6e01811096b1eea58d93d95e) |
| Mercredi 26 Août | `3c736a0c-6e01-819e-9959-d45d0de1ff09` | [Ouvrir](https://app.notion.com/p/Mercredi-26-Ao-t-2026-Planning-3c736a0c6e01819e9959d45d0de1ff09) |

---

> ↖ [[MOC_Systeme_Execution|Retour au Système & Exécution]]
