---
type: moc
created: 2026-11-23
matiere: "Architecture Système et Réseau Windows"
niveau: "Master 1 - IT"
enseignant: "M. Elom Marney-MENSAH (Ascencia Keyce Lomé)"
tags:
  - moc
  - etudes
  - cours
  - windows-server
  - reseau
  - active-directory
  - virtualisation
parent: "[[MOC_Etudes_&_Cours]]"
---

# 🖥️ Architecture Système et Réseau Windows (Master 1 – IT)

> ↖ [[MOC_Etudes_&_Cours|Retour au MOC Études & Cours]] • [[Centre_de_control|Centre de Contrôle]]
> **Enseignant :** M. Elom Marney-MENSAH (RSSI / Chef Projets en Digitalisation d'entreprise) • **Volume horaire :** 20 h
> **Structure :** `cours/` • `exercices/` • `tp/` • `media/`

Espace de synthèse, de prise de notes et de mise en pratique du module **Architecture Système et Réseau Windows** (virtualisation VMware, adressage IP/sous-réseaux, services d'infrastructure Windows Server, DNS, Active Directory et administration système).

---

## 🧭 Navigation & Structure du Module

### 🖼️ 0. Captures & Supports de Séance (`media/`)
- 📸 [[Tableau_Seance1_Cadrage_&_Lab.jpg|Photo Tableau Séance 1 — Syllabus, Cadrage du Lab & Plan d'Adressage]]

---

### 📖 I. Notes de Cours & Fiches de Révision (`cours/`)
1. [[01_Cadrage_Lab_Adressage_IP_&_Fondamentaux_Windows|01. Cadrage, Architecture du Lab, Adressage IP & Fondamentaux Windows]]
   - Décodage intégral de la séance 1 (volume horaire, prérequis CCNA/CCNP, hyperviseurs Type 1 vs Type 2, P2V).
   - Adressage IP & masque de sous-réseau pas à pas (`10.10.10.1/24` $\leftrightarrow$ `255.255.255.0`, calcul de plage et broadcast, communication directe vs routage).
   - Rôle de la passerelle (`GTW`), du `DNS 1 / DNS 2`, mariage DNS + Active Directory, convention de nommage (`SRV-DMAD-MSTR01`, `PDT-ETU-M1IABD`) et paramétrage VMware `Local Net`.

---

### 📝 II. Travaux Dirigés & TP (`exercices/` & `tp/`)
*(À compléter au fil des séances)*

---

## 📊 Récapitulatif Dataview du Module

```dataview
TABLE chapitre AS "Chapitre / Séance", type AS "Type", tags AS "Mots-clés"
FROM "🌿 Domaines/Études_&_Cours/Notes_de_Cours/Semmestre_1/Architecture_Systeme_et_Reseau_Windows"
SORT file.name ASC
```
