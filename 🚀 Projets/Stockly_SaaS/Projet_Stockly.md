---
parent: "[[My_Dev_Life]]"
type: personal-project
title: Stockly SaaS
created: 2026-08-24
updated: 2026-09-03
status: En développement
deadline: 2026-12-31
priority: 🔴 P0 - Haute
lead_coach: Raphaël & Dave
stack:
  - Flutter
  - Supabase
  - SQLite (bright_morning.db)
  - PostgreSQL
  - TypeScript
tags:
  - project
  - saas
  - stockly
  - offline-first
---

# 📦 Projet : Stockly SaaS (ERP Négoce & Carrelage)

> **Stockly** est un progiciel de gestion intégré (ERP) moderne pour quincailleries, magasins de carrelage et dépôts de matériaux. Conçu selon une architecture **Offline-First**, il garantit une réactivité instantanée au comptoir et une continuité d'activité totale sans dépendance réseau.

---

## 🧱 La Règle de la Brique Sacrée
- **Créneau quotidien :** Du lundi au vendredi, de **14h00 à 17h00** / **15h00 à 18h00** (avec un bon café) ou session de soirée dédiée.
- **Règle :** Poser une seule brique parfaite par session (sans changer de stack).

---

## 🏆 Tâches Récemment Effectuées

### 📅 Session du 3 Septembre 2026 — Refonte Shell Applicatif, Catalogue Modulaire & Multi-Entrepôts
- [x] 🧭 **Shell Applicatif & Épuration du Legacy** :
  - Extraction de la navigation monolithique de `home_page.dart` vers des composants autonomes et réutilisables (`AppDrawer`, `AppSidebar`, `NavDestination`).
  - Intégration de `notification_menu_button.dart` dans le header et relocalisation propre de `sync_connectivity_button.dart`.
  - Éradication définitive du legacy : suppression des anciens modules de livraisons obsolètes et du fichier monolithique `lib/services/services.dart` au profit de services modulaires par domaine métier.
  - Nettoyage du modèle client obsolète et propagation sur l'ensemble des composants dépendants (authentification, dashboard, enregistrement de vente).
- [x] 📦 **Modularisation du Catalogue (Articles & Catégories)** :
  - Scission de `ajouter_article_dialog.dart` en sections spécialisées (`article_basic_info_section`, `article_config_section`, `article_stock_section`, `article_form_actions`, `article_message_banner`).
  - Création de `stock_unit_converter.dart` pour la gestion des unités de conversion et tests unitaires dédiés (`stock_unit_converter_test.dart`).
  - Réécriture de `gestion_categories_page.dart` avec sous-widgets dédiés (`add_category_header`, `category_skeleton_list`, `flat_category_list_item`).
- [x] 🏭 **Module Entrepôts & Traçabilité Stock dans les Ventes** :
  - Persistance locale SQLite (`sqlite_service.dart`) avec table `entrepots` et seeding automatique d'un « Entrepôt Principal ».
  - Service `entrepot_service.dart` consolidé (CRUD complet, streams réactifs, gestion de l'entrepôt par défaut).
  - Interface logistique : `entrepot_table.dart`, `ajouter_modifier_entrepot_dialog.dart` et intégration par onglets dans `gestion_stock_page.dart`.
  - Imputation temps réel des ventes : méthode `decrementerStockArticle()` dans `stock_actuel_service.dart` reliée directement à `vente_service.dart`.
  - Couverture unitaire validée (`entrepot_test.dart`).
- [x] 🛠️ **Outillage & Structure Globale** :
  - Restructuration thématique de `lib/utils/` (`catalog/`, `sales/`, `core/`, `logistics/`).
  - Régénération du graphe d'architecture `graphify` et maintien des règles d'agents spécialisés.

### 📅 Session du 31 Août 2026 — Modules Logistique, Achats & Livraisons Offline-First
- [x] 📦 **Module Logistique & Gestion des Stocks** :
  - `StockActuelService` : multi-entrepôts et suivi par Code Lot / Bain.
  - `MouvementStockService` : journal d'audit immuable (`ENTREE`, `SORTIE`, `TRANSFERT_DEPART`, `TRANSFERT_ARRIVEE`, `AJUSTEMENT`).
  - `TransfertStockService` : flux inter-dépôts (émission $\rightarrow$ validation $\rightarrow$ réajustement des stocks).
  - Validation unitaire : `logistics_test.dart`.
- [x] 🤝 **Module Achats & Fournisseurs** :
  - Services 100% Offline-First : `FournisseursService`, `AchatFournisseurService` (calculs HT/TVA/TTC atomiques), `BonReceptionService` (incrémentation stock + mouvement) et `DecaissementService`.
  - Interface `gestion_fournisseurs.dart` avec TabBar Material 3 à 4 onglets.
  - Validation unitaire : `purchases_test.dart`.
- [x] 🚚 **Module Livraisons & Expéditions** :
  - `LivraisonService` (offline-first, sérialisation résiliente JSON $\leftrightarrow$ Map) et `BonLivraisonService`.
  - Vue calendrier interactive (`delivery_calendar_view.dart`), tables paginées et tiroirs latéraux 450px pour réceptions fournisseurs et bons d'expédition clients.
  - Validation unitaire : `livraison_test.dart`.
- [x] 📊 **Bilan Qualité & Métriques** :
  - Analyse statique : **0 erreur, 0 warning**.
  - Suite de tests unitaires : **17/17 tests réussis (100%)**.

### 📅 Session du 26 Août 2026 — Refonte Section Articles
- [x] 📊 **Tableau de Bord KPIs en temps réel** : ajout d'une barre de statistiques en haut du tableau (total articles, valeur totale du stock, stock faible, ruptures).
- [x] ✨ **Modernisation Material 3 du tableau** (`ArticleDataSource`) :
  - Avatars ronds pour les visuels d'articles.
  - Typographie *monospace* pour la lisibilité des codes-barres.
  - Badges colorés doux (vert / rouge) pour l'état instantané du stock.
  - Remplacement des icônes d'action multiples par un menu `PopupMenuButton` ("trois points") épuré.
- [x] 🛠️ **Barre d'actions groupées flottante (Bulk Actions)** : barre flottante automatique en bas d'écran avec compteur de sélection et suppression groupée.
- [x] 🪲 **Correction des bugs de rendu critique (écrans noirs)** : résolution des overflows `RenderFlex` causés par des contraintes infinies dans les cellules et scrolls.
- [x] 🎨 **Lifting Material 3 du formulaire `AjouterArticleDialog`** : retour au dialogue central flottant, coins arrondis (12px), `filled: true`, focus highlight.

### 📅 Précédemment (24-25 Août)
- [x] 🧠 **Brainstorming et création de la documentation complète** (Hub Diátaxis avec 6 fiches d'architecture et de référence métier).
- [x] 🏗️ **Refactoring de l'architecture des services** (Séparation claire `lib/`, isolation des couches SQLite / sync_queue / Supabase).
- [x] 🤖 **Création d'un Skill d'assistance au projet** pour le développement assisté par IA.
- [x] 🧭 **Discussion et définition des prochaines étapes de développement** (Roadmap et jalons).
- [x] 🎨 **Implémentation d'un indicateur de chargement (UX)** pour améliorer l'expérience utilisateur et le feedback visuel.

---

## ⚡ Macro-Architecture & 4 Piliers Invariants

```text
┌────────────────────────────────────────────────────────┐
│                   Application Flutter                  │
│       (Widgets réactifs connectés aux Streams SQLite)  │
└──────────────────────────┬─────────────────────────────┘
                           │ write (instantané)
                           ▼
┌────────────────────────────────────────────────────────┐
│                SQLite Local (bright_morning.db)        │
│    - Lecture instantanée                               │
│    - Écriture locale + insertion dans 'sync_queue'     │
└──────────────────────────┬─────────────────────────────┘
                           │ pushPendingWrites() (arrière-plan)
                           ▼
┌────────────────────────────────────────────────────────┐
│              Supabase PostgreSQL Cloud                 │
│    - Centralisation multi-entreprises (entreprise_id)  │
│    - Sécurité Row Level Security (RLS) & Auth          │
└────────────────────────────────────────────────────────┘
```

1. **Zéro Latence :** Toute opération est exécutée en local sur SQLite (`executeWrite`) avant d'être synchronisée.
2. **Règle d'Or Carrelage :** Le stock physique est géré en pièces indivisibles et cartons pleins, mais facturé au $m^2$ demandé.
3. **Traçabilité par Lot :** Saisie obligatoire du `code_bain` pour éviter tout mélange de teintes d'usine.
4. **Isolation Multi-Tenant :** Cloisonnement strict des données de chaque entreprise via `entreprise_id`.

---

## 📚 Documentation Technique Associée (Diátaxis)
- `🧮 [MÉTIER]` Calculs Carrelage, Conversion m² & Code Bain
- `🔄 [ARCHITECTURE]` Dual-Layer Offline-First & Moteur sync_queue
- `🗄️ [RÉFÉRENCE]` Schéma de Base de Données & Dictionnaire des Tables
- `💻 [RÉFÉRENCE]` Structure du Projet lib/ & Guide de Contribution
- `🛠️ [HOW-TO]` Ajouter une Entité Synchronisée Offline-First
- `🚨 [TROUBLESHOOTING]` Dépannage Connectivité, Sync & Lifecycle

---

## 🎯 Prochaines Actions Prioritaires
- [ ] Connecter l'interface utilisateur au moteur logistique (sélection entrepôt, feedback visuel temps réel et gestion des stocks)
- [ ] Finalisation des flux de synchronisation résiliente
- [ ] Tests de montée en charge et cas d'erreurs réseau
- [ ] Raffinement des interfaces de vente au comptoir
