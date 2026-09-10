---
type: documentation
title: "Configuration MCP Notion"
created: 2026-08-25
tags:
  - notion
  - mcp
  - configuration
parent: "[[MOC_Systeme_Execution]]"
---

# 🔗 Configuration MCP Notion

> Permet de connecter Notion à Freebuff / Claude Desktop pour lire et modifier tes pages Notion directement depuis l'IA.

---

## 📋 Deux Options Disponibles

### Option A : Serveur Officiel Notion (Recommandé) 🌟
- **URL** : `https://mcp.notion.com/mcp`
- **Avantages** : Hébergé par Notion, authentification OAuth, pas besoin de token
- **Inconvénient** : Nécessite un plan Notion Pro, Max, Team ou Enterprise
- **Setup** : Dans Claude Desktop → Settings → Connectors → Add Connector

### Option B : Serveur Communautaire (Gratuit) 💻
- **Package** : `@suekou/mcp-notion-server`
- **Avantages** : Open-source, tourne en local, fonctionne avec le plan gratuit
- **Setup** : Via le fichier de configuration Claude Desktop

---

## 🛠️ Installation (Option B - Communautaire)

### Étape 1 : Vérifier que Node.js est installé
```bash
node --version
# Si pas installé : sudo apt install nodejs npm
```

### Étape 2 : Copier le fichier de configuration
Le fichier `.claude_desktop_config.json` a été créé à la racine du projet.

**Pour Claude Desktop**, copie-le au bon emplacement :

```bash
# Linux
mkdir -p ~/.config/Claude
cp .claude_desktop_config.json ~/.config/Claude/claude_desktop_config.json

# macOS
mkdir -p ~/Library/Application\ Support/Claude
cp .claude_desktop_config.json ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

### Étape 3 : Redémarrer Claude Desktop
Ferme et relance complètement l'application.

### Étape 4 : Partager tes pages Notion
⚠️ **Important** : L'intégration ne voit pas ton workspace par défaut !

1. Ouvre une page Notion que tu veux connecter
2. Clique sur `⋯` (trois points) en haut à droite
3. Va dans **Connections** (ou **Intégrations**)
4. Sélectionne ton intégration

---

## 🔐 Sécurité

Ton token Notion (`ntn_...`) est stocké dans le fichier de configuration.
- ✅ Ce token est **interne** à ton workspace
- ⚠️ Ne le partage **jamais** publiquement
- 🔄 Tu peux le révoquer à tout moment depuis [notion.so/profile/integrations](https://www.notion.so/profile/integrations)

---

## 🎯 Ce que tu pourras faire avec le MCP

| Action | Description |
|--------|-------------|
| 📖 Lire des pages | Consulter le contenu de tes pages Notion |
| 🔍 Rechercher | Chercher dans tout ton workspace |
| ✏️ Créer des pages | Ajouter du contenu à tes pages |
| 📊 Lire des bases de données | Accéder aux propriétés de tes DB |
| 🔄 Modifier des propriétés | Mettre à jour les champs de tes pages |

---

## 🔗 Lien avec ton Second Brain

Une fois connecté, je pourrai :
- Lire tes objectifs depuis Notion
- Créer des pages de suivi automatiquement
- Synchroniser tes daily logs avec tes bases de données
- Mettre à jour ton planner directement

---

> ↖ [[MOC_Systeme_Execution|Retour au Système & Exécution]]
