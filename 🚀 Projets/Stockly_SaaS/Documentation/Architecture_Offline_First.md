---
title: "Architecture Offline-First"
type: doc
project: Stockly
up: "[[MOC_Stockly]]"
created: 2026-09-07
tags:
  - architecture
  - flutter
  - offline-first
---

# 🏗️ Architecture Offline-First (Stockly)

## 1. Philosophie Core
* **Le local est la source de vérité absolue** : L'interface UI lit et écrit *exclusivement* dans la base SQLite locale.
* **Synchronisation asynchrone** : Les données locales sont poussées vers Supabase en arrière-plan lorsque la connexion est disponible.

## 2. Stack Technique
* **Frontend** : Flutter
* **Base de données locale** : SQLite (via package `sqflite` ou `drift`)
* **Backend / Auth / Remote DB** : Supabase (PostgreSQL)

## 3. Stratégie de Synchronisation (Sync Engine)
### Gestion des conflits (Conflict Resolution)
- Stratégie recommandée : *Last Write Wins (LWW)* basée sur un timestamp `updated_at`.
- Les entités doivent avoir un `id` UUID généré localement pour éviter les conflits d'auto-incrémentation.

### File d'attente des mutations (Outbox Pattern)
- Chaque action de l'utilisateur (Créer, Modifier, Supprimer) est enregistrée dans une table SQLite `sync_queue`.
- Un worker (ex: `workmanager` en Flutter) traite la file d'attente et envoie les paquets à Supabase dès que le réseau (WiFi/4G) est disponible.

## 4. Points d'attention pour l'implémentation
- [ ] Mettre en place un UUID v4 local pour toutes les clés primaires.
- [ ] Gérer les suppressions logiques (soft deletes : `deleted_at`) au lieu de suppressions physiques pour permettre la synchronisation.
- [ ] Gérer l'état de synchronisation dans l'UI (ex: icône nuage avec coche ou flèches tournantes).
