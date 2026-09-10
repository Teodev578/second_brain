---
parent: "[[Acceuil]]"
type: personal-project
title: Typonator
created: 2026-09-07
updated: 2026-09-07
status: En pause
deadline: 2027-06-30
priority: 🟡 P2 - Standby (Post-Stockly)
lead_coach: Raphaël & Dave
repo_path: "/home/fabien/Documents/Projets/Personnel/Pro/typonator/typonator"
stack:
  - Next.js 16 (App Router & Server Actions)
  - React 19
  - TypeScript 5
  - TensorFlow.js (Machine Learning custom)
  - Tailwind CSS v4
  - Zustand 5
  - Supabase
  - Zod
tags:
  - project
  - saas
  - typography
  - machine-learning
  - nextjs
  - design-tool
---

# 🔤 Projet : Typonator (Recommandation Typographique Intelligente)

> **Typonator** est un studio web interactif de composition et d'appairage typographique. Il permet aux designers et développeurs de tester en temps réel des combinaisons de polices issues du catalogue Google Fonts, assistés par un **moteur de recommandation basé sur un réseau de neurones (TensorFlow.js)** entraîné sur mesure.

---

## ⏸️ Décision Stratégique de Mise en Pause

> 🔒 **Règle de focalisation absolue ( Dave & Raphaël ) :** Ce projet est **délibérément mis en sommeil** pour sanctuariser 100 % de l'attention et du Deep Work sur **[[Projet_Stockly|Stockly SaaS (P0)]]**. 
> 
> **Condition de réactivation :** Lancement commercial et stabilisation du socle offline-first de Stockly. Aucune dispersion technique sur Typonator d'ici là.

---

## ⚡ Architecture Technique & Pipeline Machine Learning

```text
┌────────────────────────────────────────────────────────┐
│                   Frontend Next.js 16                  │
│   (React 19, Zustand 5, Tailwind v4, Multi-Panneaux)   │
└──────────────────────────┬─────────────────────────────┘
                           │ Inférence locale ultra-rapide
                           ▼
┌────────────────────────────────────────────────────────┐
│             Moteur TensorFlow.js (24 Ko)               │
│  - Vecteurs de 28 features (graisse, largeur, contraste)│
│  - Scoring hybride : Réseau Dense + Règles de style    │
│  - Curseur d'audace : « Pro ↔ Créatif »                │
└──────────────────────────┬─────────────────────────────┘
                           │ Validation & Cache
                           ▼
┌────────────────────────────────────────────────────────┐
│       Backend Server Actions & Google Fonts API        │
│  - ~1 900 polices filtrées et validées par Zod         │
│  - Cache mémoire + ISR (revalidate 3600)               │
│  - Télémétrie Supabase (font_pairings_log)             │
└────────────────────────────────────────────────────────┘
```

---

## 🎯 Fonctionnalités Clés & État des Lieux

| Composant | Statut | Description & Fonctionnement |
| :--- | :--- | :--- |
| **Moteur de Recommandation ML** | 🟢 Fonctionnel | Pipeline d'entraînement (`scripts/train.mjs`), inférence par batch `tf.tidy()` et échantillonnage pondéré top-15. |
| **Catalogue Typographique** | 🟢 Fonctionnel | ~1900 polices Google Fonts chargées côté serveur, cache résilient et détection de style à 3 niveaux. |
| **Éditeur Multi-Panneaux** | 🟢 Fonctionnel | Jusqu'à 4 tuiles avec `contentEditable`, verrous de polices, ajustement précis (graisse, interlignage, couleurs). |
| **Expérience UI / UX** | 🟢 Fonctionnel | Raccourci barre d'espace pour régénération, responsive design, thèmes sombre/clair sans décalage d'hydratation. |
| **Authentification & Sauvegarde Cloud** | 🟡 Placeholder | Modal d'authentification et favoris en mémoire (à relier à Supabase Auth lors de la réactivation). |

---

## 💡 Valeur Patrimoniale & Emplacement

- **Dépôt Local :** `/home/fabien/Documents/Projets/Personnel/Pro/typonator/typonator`
- **Atout Portfolio :** Illustration concrète de la double expertise : intégration poussée de Machine Learning dans une interface utilisateur moderne et soignée.
- **Potentiel Futur :** Candidat idéal pour le studio de micro-SaaS indépendants (**Horizon 3**).
