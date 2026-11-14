---
type: moc
created: 2026-11-10
matiere: "Théorie des Graphes"
niveau: "Master 1 - IT"
enseignant: "K. E. HOVI (Ascencia Keyce Lomé)"
tags:
  - moc
  - etudes
  - cours
  - theorie-des-graphes
  - mathematiques-discretes
  - algorithmique
parent: "[[MOC_Etudes_&_Cours]]"
---

# 🌐 Théorie des Graphes (Master 1 – IT)

> ↖ [[MOC_Etudes_&_Cours|Retour au MOC Études & Cours]] • [[Centre_de_control|Centre de Contrôle]]
> **Enseignant :** K. E. HOVI (Ascencia Keyce, Campus de Lomé) • **Date de référence :** 10 Novembre 2026
> **Documents sources :** [[Support_Cours_Theorie_des_Graphes.pdf|📄 Consulter le PDF Original]] • [[Cours_Integral_Verbatim_Theorie_des_Graphes|📜 Transcription Intégrale & Textuelle du Cours]]

Bienvenue dans l'espace de synthèse, d'assimilation et d'exercices pratiques de **Théorie des Graphes**. Ce module d'ingénierie informatique structure les outils mathématiques et algorithmiques indispensables à l'analyse de réseaux, à la modélisation des flux, à l'ordonnancement de projets et à la résolution de problématiques NP-complètes.

---

## 🧭 Navigation & Structure du Module

### 📄 0. Documents de Référence Officiels
- 📑 [[Support_Cours_Theorie_des_Graphes.pdf|Support de Cours & TD en PDF (Document Original de 51 pages)]]
- 📜 [[Cours_Integral_Verbatim_Theorie_des_Graphes|Transcription Intégrale Verbatim (Texte exhaustif des 3 chapitres et activités)]]

---

### 📖 I. Notes de Cours Magistrales & Synthèses Actives
1. [[01_Introduction_&_Representations_des_Graphes|01. Introduction, Définitions et Représentations Mémoire]]
   - Graphes simples, multigraphes, ordre, degré et demi-degrés.
   - Lemme des poignées de main et parité des sommets impairs.
   - Chaînes, chemins et cycles.
   - Matrice d'adjacence versus listes d'adjacence (arbitrages mémoire et puissances $M^p$).
2. [[02_Proprietes_Fondamentales_des_Graphes|02. Propriétés Fondamentales (Connexité, Arbres, Planarité, Coloriage)]]
   - Connexité non orientée et forte connexité orientée (fermeture transitive).
   - Théorèmes d'Euler (chaînes et circuits) et problématique de Hamilton (TSP).
   - Arbres et forêts : 6 caractérisations équivalentes.
   - Planarité : problème des trois châtelains ($K_{3,3}$), formule d'Euler ($S - A + F = 2$), critère de Kuratowski.
   - Coloriage : nombre chromatique $\chi(G)$, heuristique DSATUR de Brélaz, théorème des 4 couleurs, cliques $\omega(G)$ et stables $\alpha(G)$.
3. [[03_Algorithmes_sur_les_Graphes|03. Algorithmes Majeurs sur les Graphes]]
   - Parcours de graphes : BFS (file FIFO, plus court chemin géodésique) et DFS (pile LIFO, estampilles $[d/f]$, classification des 4 types d'arcs).
   - Plus courts chemins à source unique : Dijkstra (glouton, poids positifs) vs Bellman-Ford (programmation dynamique, détection de circuits absorbants).
   - Arbres couvrants de poids minimal (ACPM / MST) : Kruskal (glouton par arêtes avec *Union-Find*) vs Prim (glouton par sommets).
   - Flots dans les réseaux : Réseaux de transport, algorithme de Ford-Fulkerson, réseaux résiduels et théorème de dualité Flot-Max / Coupe-Min.

---

### 📝 II. Travaux Dirigés & Exercices d'Application
- [[TD1_Introduction_&_Representations|Feuille TD 1 : Modélisation, Complexités & Topologies Réseaux]]
  - Validité de séquences de degrés (lemme des poignées de main).
  - Évaluation de complexité asymptotique (matrice vs listes d'adjacence).
  - Calcul matriciel $A^2, A^3$ et énumération formelle de chemins.
  - Topologies physiques : totalement maillée ($K_n$), anneau ($C_n$), étoile ($S_n$) et goulots d'étranglement.
- [[TD2_Proprietes_&_Applications|Feuille TD 2 : Propriétés Fondamentales & Études de Cas Réseaux]]
  - Composantes connexes et fortement connexes.
  - Parcours eulériens et conditions d'Ore / Dirac pour le cycle hamiltonien.
  - Démonstration par récurrence sur le nombre d'arêtes d'un arbre ($A = S - 1$).
  - Planarité et non-planarité de $K_5$ ($A \le 3S - 6$).
  - Coloriage d'antennes radio par algorithme de Welsh-Powell.
  - Cliques $\omega(G)$ et stables $\alpha(G)$ sur graphe complémentaire $\overline{G}$.
  - Modélisations de réseaux concrets : commutateurs optiques, collecte de déchets, distribution d'eau potable.
- [[TD3_Algorithmes_&_Routage|Feuille TD 3 : Algorithmique Avancée, Ordonnancement & Protocoles]]
  - Traces d'exécution BFS et DFS avec estampilles temporelles et classification d'arcs.
  - Calcul de plus courts chemins par Dijkstra et gestion des arcs négatifs par Bellman-Ford.
  - Construction comparée de l'ACPM (Kruskal vs Prim) et unicité de l'arbre.
  - Analyse d'ordonnancement par DAG (tri topologique DFS, dates au plus tôt/tard, chemin critique et marges).
  - Routage distribué à vecteur de distances : convergence, problème du *Count-to-Infinity*, *Split Horizon* et *Poison Reverse*, comparatif RIP / OSPF.

---

## 📊 Récapitulatif Dataview du Module

```dataview
TABLE chapitre AS "Chapitre / TD", type AS "Type", tags AS "Mots-clés"
FROM "🌿 Domaines/Études_&_Cours/Notes_de_Cours/Theorie_des_Graphes"
SORT file.name ASC
```
