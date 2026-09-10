---
title: "Modèle de Données (SQLite & Supabase)"
type: doc
project: Stockly
up: "[[MOC_Stockly]]"
created: 2026-09-07
tags:
  - database
  - schema
---

# 🗄️ Modèle de Données (Draft)

> **Règle d'or** : Toutes les tables doivent inclure `id` (UUID), `created_at`, `updated_at`, et `deleted_at` (pour le soft-delete et la synchronisation).

## Tables Principales (à compléter selon le domaine de Stockly)

### 1. `users` (Géré via Supabase Auth + Profil local)
- `id` (UUID, PK)
- `email` (String)
- `display_name` (String)
- `created_at` (DateTime)

### 2. `items` (Exemple de table métier d'inventaire/stock)
- `id` (UUID, PK)
- `user_id` (UUID, FK -> users.id)
- `name` (String)
- `quantity` (Integer)
- `sku` (String, nullable)
- `created_at` (DateTime)
- `updated_at` (DateTime)
- `deleted_at` (DateTime, nullable) - *Critique pour le offline sync*

### 3. `sync_queue` (Table système pour l'Outbox Pattern)
- `id` (Integer, Auto-increment)
- `entity` (String) - ex: 'items'
- `entity_id` (UUID)
- `operation` (String) - 'INSERT', 'UPDATE', 'DELETE'
- `payload` (JSON) - Snapshot des données
- `status` (String) - 'PENDING', 'FAILED'
- `created_at` (DateTime)

---

## 🛠️ À Valider
- [ ] Définir les entités métiers précises (Produits, Catégories, Mouvements de stock ?).
- [ ] Valider le modèle relationnel.
