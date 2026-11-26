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
1. [[01_Cadrage_Lab_Adressage_IP_&_Fondamentaux_Windows|01. Cadrage, Architecture du Lab, Adressage IP & Fondamentaux Windows]] *(Notes du tableau oral)*
   - Décodage intégral de la séance 1 (volume horaire, prérequis CCNA/CCNP, hyperviseurs Type 1 vs Type 2, P2V).
   - Adressage IP & masque de sous-réseau pas à pas (`10.10.10.1/24` $\leftrightarrow$ `255.255.255.0`), passerelle, DNS, convention `SRV-DMAD-MSTR01` et `Local Net`.
2. [[01_Chapitre1_Architecture_Installation_Configuration_Windows_Server|01. Chapitre 1 — Architecture, Installation & Configuration de Windows Server (Fiche de révision)]]
   - Synthèse complète du polycopié officiel (Windows Server 2022) : rôle & principes, éditions (`Standard`/`Datacenter`/`Essentials`), `GUI` vs `Server Core`, noyau/services/registre/NTFS, `AD DS` vs promotion DC, dépendance DNS (`SRV`), topologie `192.168.10.0/24`, ports critiques, MMC/Sconfig, PowerShell-first, script `Inventory-Lab.ps1` et diagnostic en 4 couches.

---

### 📝 II. Travaux Dirigés, Questionnaires & TP (`exercices/` & `tp/`)
- [[Questionnaire_Revision_Chapitre_1|📝 Questionnaire de Révision, QCM & Études de Cas — Chapitre 1]]
  - 15 questions de connaissance, Mini-QCM (8 questions), exercice de conflit IP, 3 études de cas, travail PowerShell (`WinRM`/`W32Time`) et barème TP1, avec corrigés pliables.

---

### 📅 III. Syllabus, Progression & Validation du Module (20 h)

- **Évaluation :** Devoir écrit individuel (**50 %**) + Contrôle continu (**50 %** : TP et feuilles de contrôle 20 %, Projet intégrateur 20 %, Restitution & diagnostic oral 10 %).
- **Projet intégrateur :** Mini-SI Windows Server isolé (`ad.ascencia.test`) pour une PME (Direction, Comptabilité, RH, Informatique) : DC avec DNS, serveur de ressources Core, poste client Windows, OU/comptes/groupes, partages SMB/NTFS, GPO de sécurité, durcissement, script d'inventaire et dossier technique.

| Séance | Thématique | Théorie / Pratique | Livrable / Validation minimale | Fait |
| :---: | :--- | :---: | :--- | :---: |
| **1** | Installation, architecture et configuration initiale | 1h30 / 2h30 | GUI et Core démarrent ; IPv4 et noms d'hôtes vérifiés ; AD DS installé sans promotion | ☐ |
| **2** | AD DS, OU, identités, groupes et ressources | 1h30 / 2h30 | Contrôleur AD DS actif ; OU, comptes, AGDLP et accès SMB/NTFS testés | ☐ |
| **3** | DNS, DHCP, GPO et intégration des clients | 1h30 / 2h30 | Résolution DNS, bail DHCP, GPO et jonction client démontrés | ☐ |
| **4** | Sécurité, journaux, performance et WSUS | 1h30 / 2h30 | Journaux, matrice de durcissement, PerfMon et politique MAJ documentés | ☐ |
| **5** | Dépannage, automatisation et projet final | 2h / 2h | Diagnostic (`dcdiag`, `repadmin`), script CSV et dossier d'architecture présentés | ☐ |

---

## 📊 Récapitulatif Dataview du Module

```dataview
TABLE chapitre AS "Chapitre / Séance", type AS "Type", tags AS "Mots-clés"
FROM "🌿 Domaines/Études_&_Cours/Notes_de_Cours/Semmestre_1/Architecture_Systeme_et_Reseau_Windows"
SORT file.name ASC
```
