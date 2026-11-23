---
type: note-cours
created: 2026-11-09
matiere: "Gestion de Projet & Business Analysis"
chapitre: "01 - Analyse des besoins et cahier des charges fonctionnel"
tags:
  - etudes
  - cours
  - business-analysis
  - gestion-de-projet
  - active-recall
parent: "[[MOC_Etudes_&_Cours]]"
---

# 📖 Analyse des Besoins & Cahier des Charges Fonctionnel

> **Matière :** [[MOC_Etudes_&_Cours|Gestion de Projet & Business Analysis]] • **Date :** 09 Novembre 2026 • **Statut :** Synthétisé & Prêt pour révision active

---

## 🎯 1. Idées Clés & Vue d'Ensemble
Ce cours pose les fondations de l'ingénierie des exigences logicielles : comment capter l'expression brute d'un besoin client, la traduire par le travail d'analyse d'un Business Analyst (BA) en fonctionnalités précises pour l'équipe de développement, et consigner le tout dans un cahier des charges fonctionnel tout en maîtrisant les risques d'échec projet (dérive budgétaire, retards et désalignement UX/UI).

---

## 📑 2. Sommaire du Module
1. Problématique, cadrage et compréhension des termes fondamentaux
2. La collecte des besoins (techniques et méthodologies)
3. Organisation et périmètre d'intervention des acteurs

---

## 🔍 3. Transcription & Structuration Approfondie

### I. Cadrage : Pourquoi les Projets Échouent-ils ?
L'absence de rigueur en amont du développement est la première cause de mortalité des projets logiciels :
- **Défaut de cadrage initial (*Kickoff*) :** Périmètre mal défini ou besoins non exprimés par les commanditaires.
- **Collecte défaillante des données :** Mauvaise interprétation du contexte métier.
- **Organisation & Ressources inadaptées :** Flou sur les livrables intermédiaires et responsabilités éclatées.
- **Pression calendaire et financière :** Dépassements de budget et retards de livraison conduisant à l'insatisfaction client.

> [!TIP] Posture Professionnelle en Entreprise
> - **Périmètre d'intervention :** Déterminer précisément sa zone d'action pour ne pas se disperser.
> - **Fiche de poste :** En tant que salarié ou intervenant, exiger et étudier la fiche de poste afin de construire et calibrer son plan d'action opérationnel.

---

### II. Les Acteurs Clés du Projet & la Chaîne de Traduction

```text
[ Client / Sponsor ] ──(Exprime le besoin brut)──► [ Business Analyst (BA) ]
                                                            │
                                                   (Analyse & Formalise)
                                                            ▼
[ Développeur ] ◄──(Coordonne / PMO)── [ Chef de Projet ]
(Réalise la solution)
```

1. **Client / Customer / Sponsor :** Porte la vision métier ou le besoin commercial initial.
2. **Business Analyst (BA) :** Analyse, clarifie et traduit le besoin métier brut en spécifications logiques compréhensibles par les équipes techniques.
3. **Chef de Projet (PM / PMO) :** Coordonne le planning, orchestre les ressources et garantit le respect des engagements (délais/coûts).
4. **Développeurs :** Conçoivent l'architecture logicielle, codent et déploient la solution technique.
*(Note : selon la taille des structures, une même personne peut cumuler plusieurs de ces casquettes).*

> [!NOTE] Veille & Spécialisation
> - Mention stratégique notée en cours : opportunité d'une **spécialisation IA**, notamment orientée vers les **bases de données vectorielles et la recherche sémantique (IA orientée vecteur)**.

---

### III. Définition des Termes Techniques

#### 1. Le Triptyque : Besoin ➔ Analyse ➔ Fonctionnalité
1. **Besoin (Nécessité brute) :** Ce que ressent ou demande le client.  
   *Exemple :* « J'ai besoin de traiter une facture. »
2. **Analyse (Traitement par le BA) :** Déconstruction analytique du besoin pour dégager les règles de gestion et la logique métier.
3. **Fonctionnalité (Action logicielle concrète) :** Traduction opérationnelle implémentée par le dev.  
   *Exemples :* Capacité de *Drag & Drop* pour téléverser le document PDF, module d'édition/modification des champs de la facture, moteur d'export.

#### 2. Cahier des Charges & Distinction Fonctionnel / Non-Fonctionnel

> [!IMPORTANT] Point Examen
> Maîtriser impérativement la frontière entre exigences fonctionnelles et non fonctionnelles.

- **Cahier des Charges Fonctionnel (CDCF) :** Document contractuel décrivant précisément le comportement attendu de l'ensemble des fonctionnalités du système.
- **Besoin Fonctionnel :** Décrit ce que le produit ou service **doit faire** (actions, fonctions principales, entrées/sorties).  
  *Exemple :* « Permettre à l'utilisateur de s'authentifier par email et mot de passe. »
- **Besoin Non-Fonctionnel :** Décrit **comment** le système doit le faire (performance, sécurité, ergonomie, robustesse, contraintes techniques).  
  *Exception / Nuance :* Si le client **exige formellement** une contrainte ergonomique ou technique dans l'expression de ses besoins (ex: « Le nom d'utilisateur doit être validé avant la saisie du mot de passe »), cette règle devient une exigence fonctionnelle stricte à implémenter.

#### 3. Pourquoi les Besoins Fonctionnels sont Déterminants ?
- **Planification & Livrables :** Fixer des jalons précis (*deadlines*) pour chaque fonctionnalité.  
  *Arbitrage de flux :* La fonctionnalité brute est prioritaire dans un premier temps pour valider le flux technique ; l'optimisation UI/UX vient consolider l'expérience dans un second temps.
- **Budget :** Anticiper l'intervention des compétences requises (ex: recours à un UI/UX Designer extérieur et impact sur l'enveloppe budgétaire globale).
- **Satisfaction Client & Risques :** Réduire le temps de livraison (*time to market*) pour éviter la déception du commanditaire.

---

### IV. La Collecte des Besoins

#### Étape 1 : Délimitation du Périmètre
La collecte permet de recadrer les objectifs réels du projet en clarifiant :
- **Le Processus :** L'enchaînement global des activités orientées vers une finalité métier.
- **La Procédure :** Les étapes séquentielles opératoires et détaillées pour exécuter chaque tâche.

#### Les 4 Techniques Majeures de Collecte
1. **Entretien individuel (*One-to-One*) :** Tête-à-tête direct avec le commanditaire ou un utilisateur clé pour cerner les attentes individuelles.
2. **Réunion de travail (*Workshop*) :** Session collaborative d'idéation et de confrontation des points de vue (méthode la plus riche et interactive).
3. **Questionnaire & Étude de marché :** Collecte quantitative auprès d'un panel plus large pour dégager des tendances et repérer les meilleures pratiques.
4. **Analyse documentaire & Observation directe :** Étude des manuels de procédures internes, documents comptables et observation du travail réel des équipes pour formaliser le cahier des charges sur des faits vérifiables.

---

## 🧠 4. Batterie d'Active Recall (Questions d'Auto-Évaluation)

> *Ferme la section 3 et réponds à ces questions pour ancrer la matière dans ta mémoire à long terme :*

- [ ] **1. Pourquoi les projets informatiques échouent-ils majoritairement lors de la phase initiale ?**
  - *Réponse flash :* Mauvais cadrage/kickoff, besoins implicites non exprimés, mauvaise collecte des données, responsabilités éclatées et dérive coûts/délais.
- [ ] **2. Quel est le rôle exact du Business Analyst vis-à-vis du client et des développeurs ?**
  - *Réponse flash :* Il sert de pont : il collecte l'expression brute du besoin client, l'analyse et la traduit en spécifications fonctionnelles logiques pour le développeur.
- [ ] **3. Comment différencier un besoin fonctionnel d'un besoin non fonctionnel ? Donne un exemple d'exception.**
  - *Réponse flash :* Le fonctionnel définit **ce que fait** l'application (ex: exporter une facture) ; le non-fonctionnel définit **comment** elle se comporte (sécurité, temps de réponse). L'exception : si le client impose explicitement une contrainte ergonomique ou d'ordre de saisie, elle acquiert un caractère fonctionnel obligatoire.
- [ ] **4. Quelles sont les 4 techniques de collecte des besoins et quelle est la plus collaborative ?**
  - *Réponse flash :* One-to-one, Workshop (la plus interactive/intéressante), Questionnaire/étude de marché, Analyse documentaire/observation.
- [ ] **5. Quelle est la différence entre un processus et une procédure ?**
  - *Réponse flash :* Le processus est la vue d'ensemble orientée résultat global ; la procédure est la suite opératoire d'instructions détaillées.
