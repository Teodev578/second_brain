---
title: "Flux d'Écrans (UI/UX)"
type: doc
project: Stockly
up: "[[MOC_Stockly]]"
created: 2026-09-07
tags:
  - ux
  - ui
  - flutter
---

# 📱 Flux d'Écrans (User Flow)

> Modélisation des parcours utilisateurs principaux pour l'application Flutter.

## 1. Onboarding & Authentification
1. **Splash Screen** : Vérification du token de session local.
2. **Login / Register** : Authentification via Supabase Auth.
3. **Initial Sync** : Si c'est la première connexion, téléchargement complet des données depuis Supabase vers SQLite. Barre de progression affichée.

## 2. Dashboard Principal
1. **Home Screen** :
   - Affichage des KPIs (produits en rupture, mouvements récents).
   - Indicateur de statut de synchronisation (Cloud check / Cloud sync / Offline).
   - Bouton d'action flottant (FAB) : "Nouvelle Entrée".

## 3. Gestion de l'Inventaire
1. **Liste des Produits (List Screen)** :
   - Recherche locale (très rapide grâce à SQLite).
   - Filtres par catégorie ou statut.
2. **Détail Produit (Detail Screen)** :
   - Historique des mouvements.
   - Bouton "Éditer".
3. **Création / Édition (Form Screen)** :
   - Formulaire avec validation.
   - À la validation : Enregistrement local + Création d'une tâche dans la `sync_queue`.

## 🛠️ À Valider (Design)
- [ ] Connecter cette note aux maquettes Figma de l'application.
- [ ] Confirmer les KPIs nécessaires sur le dashboard.
