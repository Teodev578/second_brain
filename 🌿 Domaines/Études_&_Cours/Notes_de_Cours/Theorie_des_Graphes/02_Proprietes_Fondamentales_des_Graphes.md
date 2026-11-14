---
type: note-cours
created: 2026-11-10
matiere: "Théorie des Graphes"
chapitre: "02 - Propriétés Fondamentales des Graphes"
enseignant: "K. E. HOVI"
tags:
  - etudes
  - cours
  - theorie-des-graphes
  - connexite
  - eulerien
  - hamiltonien
  - arbres
  - planarite
  - coloriage
  - active-recall
parent: "[[MOC_Theorie_des_Graphes]]"
---

# 📖 02. Propriétés Fondamentales des Graphes

> **Matière :** [[MOC_Theorie_des_Graphes|Théorie des Graphes (M1 IT)]] • **Date :** 10 Novembre 2026 • **Statut :** Synthétisé & Prêt pour révision active

---

## 🎯 1. Idées Clés & Thèses Centrales
Ce chapitre explore la topologie interne et la combinatoire structurelle des graphes :
- **Connexité et Transitivité :** Décomposition en composantes connexes (non orienté) et composantes fortement connexes (orienté).
- **Parcours universels :** Distinction épistémologique cruciale entre la traversée exhaustive des arêtes (**Eulérien**, résoluble en temps linéaire $O(m)$) et la traversée exhaustive des sommets (**Hamiltonien**, problème NP-complet au cœur du problème du voyageur de commerce).
- **Arbres et Minimalité :** Structures connexes acycliques canoniques régies par l'invariant $m = n - 1$.
- **Planarité et Topologie du plan :** Préservation planaire régie par la formule d'Euler ($S - A + F = 2$), l'inégalité de densité $A \le 3S - 6$ et l'obstruction par les mineurs exclus de Kuratowski ($K_5$ et $K_{3,3}$).
- **Coloration et Dualité :** Réduction du nombre chromatique $\chi(G)$ borné inférieurement par l'ordre de la plus grande clique ($\omega(G) \le \chi(G)$) et articulation avec les ensembles stables dans le graphe complémentaire.

---

## 📝 2. Contenu Structuré & Démonstrations

### A. Connexité et Forte Connexité

#### 1. Cas Non Orienté
- **Graphe connexe :** Pour toute paire de sommets distincts $\{s_i, s_j\}$, il existe au moins une chaîne reliant $s_i$ et $s_j$.
- **Composante connexe :** Sous-graphe connexe maximal pour l'inclusion.
- **Fermeture transitive :** Calculée sur un graphe à $k$ composantes connexes, la fermeture transitive engendre une union disjointe de $k$ sous-graphes complets.

#### 2. Cas Orienté
- **Forte connexité :** Un graphe orienté $G$ est fortement connexe si $\forall (u, v) \in V^2$, il existe un chemin orienté de $u$ vers $v$ **et** un chemin de $v$ vers $u$.
- **Composantes Fortement Connexes (CFC) :** Sous-graphes orientés maximaux fortement connexes.
- *Propriété de réduction :* Le graphe des composantes obtenu en condensant chaque CFC en un super-sommet est nécessairement un graphe orienté acyclique (DAG).

---

### B. Graphes Eulériens vs Graphes Hamiltoniens

```
┌───────────────────────────────────────┬───────────────────────────────────────┐
│        Graphes Eulériens              │        Graphes Hamiltoniens           │
├───────────────────────────────────────┼───────────────────────────────────────┤
│ Visite toutes les ARÊTES une seule    │ Visite tous les SOMMETS une seule     │
│ fois (chaîne / cycle).                │ fois (chaîne / cycle).                │
│ Complexité : Linéaire P : O(|E|)       │ Complexité : NP-Complet (Décision)   │
│ Condition : Nécessaire ET Suffisante  │ Condition : Seulement Suffisante      │
│ basée sur la parité des degrés.       │ (Dirac, Ore).                         │
└───────────────────────────────────────┴───────────────────────────────────────┘
```

#### 1. Théorèmes d'Euler
- **Cycle eulérien (non orienté) :** Un graphe connexe admet un cycle eulérien si et seulement si **tous ses sommets ont un degré pair**.
- **Chaîne eulérienne (non orienté) :** Un graphe connexe admet une chaîne eulérienne ouverte de $u$ à $v$ si et seulement si **les sommets $u$ et $v$ sont les seuls de degré impair** (tous les autres étant pairs).
- **Circuit eulérien (orienté) :** Fortement connexe et $\forall s \in V, d^+(s) = d^-(s)$.
- **Chemin eulérien (orienté) :** De $u$ vers $v \iff d^+(u) = d^-(u) + 1$, $d^+(v) = d^-(v) - 1$, et $\forall s \notin \{u, v\}, d^+(s) = d^-(s)$.

#### 2. Problématique Hamiltonienne & Théorèmes de Dirac et Ore
Un cycle hamiltonien est un cycle élémentaire passant une fois et une seule par chacun des $n$ sommets du graphe.
> [!NOTE] Conditions Suffisantes Classiques (Graphe simple, $n \ge 3$)
> - **Théorème de Dirac (1952) :** Si pour tout sommet $v$, $d(v) \ge \frac{n}{2}$, alors $G$ est hamiltonien.
> - **Théorème de Ore (1960) :** Si pour toute paire de sommets non adjacents $\{u, v\}$, $d(u) + d(v) \ge n$, alors $G$ est hamiltonien.
> *Remarque :* Ces conditions sont purement suffisantes et non nécessaires. Un cycle simple $C_n$ est hamiltonien bien que chaque sommet soit seulement de degré 2.

---

### C. Théorie des Arbres et Forêts

#### 1. Les 6 Caractérisations Équivalentes d'un Arbre
Pour tout graphe non orienté $G = (V, E)$ d'ordre $n$, les propositions suivantes sont strictement équivalentes :
1. $G$ est connexe et sans cycle.
2. $G$ est sans cycle et possède $m = n - 1$ arêtes.
3. $G$ est connexe et possède $m = n - 1$ arêtes.
4. $G$ est sans cycle, et l'ajout d'une arête quelconque crée un unique cycle élémentaire.
5. $G$ est connexe, et la suppression d'une arête quelconque le déconnecte (toute arête est un pont).
6. Il existe une chaîne simple et une seule entre deux sommets quelconques de $G$.

#### 2. Forêt
Une forêt est un graphe sans cycle dont chaque composante connexe est un arbre. Si une forêt comporte $n$ sommets et $c$ composantes connexes, son nombre d'arêtes vérifie :
$$m = n - c$$

---

### D. Planarité des Graphes

#### 1. Problème des Trois Châtelains et Définition
Un graphe est dit **planaire** s'il admet une représentation géométrique dans le plan telle que les arêtes ne se croisent qu'en leurs extrémités.
- Le problème consistant à relier 3 maisons à 3 usines (eau, gaz, électricité) sans croisement correspond au graphe biparti complet $K_{3,3}$. Ce graphe n'est **pas planaire**.

#### 2. Formule d'Euler pour les Graphes Connexes Plans
Pour tout graphe connexe représenté dans le plan avec $S$ sommets, $A$ arêtes et $F$ faces (en comptant la face externe infinie) :
$$S - A + F = 2$$

#### 3. Inégalités Fondamentales et Démonstration de Non-Planarité
Dans un graphe planaire simple sans triangles (cycles de longueur $\ge 4$, comme les bipartis) : $2A \ge 4F \implies A \le 2S - 4$.
Dans le cas général (cycles de longueur $\ge 3$) : chaque face est bordée par au moins 3 arêtes, et chaque arête borde au plus 2 faces, donc $2A \ge 3F \implies F \le \frac{2}{3}A$. En injectant dans la formule d'Euler :
$$S - A + \frac{2}{3}A \ge 2 \iff A \le 3S - 6$$

> [!WARNING] Démonstration que $K_5$ n'est pas planaire
> Pour le graphe complet à 5 sommets : $S = 5$ et $A = \binom{5}{2} = 10$.
> Or $3S - 6 = 3(5) - 6 = 9$.
> L'inégalité $10 \le 9$ est contredite. Donc **$K_5$ n'est pas planaire**.

- **Théorème de Kuratowski (1930) :** Un graphe est planaire si et seulement si il ne contient aucun sous-graphe homéomorphe à $K_5$ ou $K_{3,3}$.

---

### E. Coloriage, Algorithme DSATUR, Cliques et Stables

#### 1. Nombre Chromatique $\chi(G)$
Attribution d'une couleur à chaque sommet telle que deux sommets adjacents reçoivent des couleurs distinctes. Le nombre minimal requis est le nombre chromatique $\chi(G)$.
- **Théorème des 4 couleurs (Appel & Haken, 1976) :** Tout graphe planaire vérifie $\chi(G) \le 4$.

#### 2. Algorithme Glouton DSATUR (Brélaz, 1979)
Permet de borner supérieurement $\chi(G)$ par une approche heuristique efficace :
1. Calculer le degré de saturation $\text{DSAT}(v)$ de chaque sommet (nombre de couleurs différentes déjà affectées à ses voisins directs).
2. Sélectionner le sommet non colorié maximisant $\text{DSAT}(v)$ (en cas d'égalité, choisir le plus grand degré dans le sous-graphe non colorié).
3. Attribuer au sommet la plus petite couleur disponible compatible.
4. Répéter jusqu'à coloration complète.

#### 3. Cliques et Ensembles Stables
- **Clique ($S' \subseteq S$) :** Sous-ensemble de sommets deux à deux connectés (sous-graphe complet). Ordre maximal : $\omega(G)$.
- **Stable ($S' \subseteq S$) :** Sous-ensemble de sommets deux à deux indépendants (aucune arête). Ordre maximal : $\alpha(G)$.
- **Dualité fondamentale :**
  $$S' \text{ est un stable de } G \iff S' \text{ est une clique du graphe complémentaire } \overline{G}$$
- **Propriété d'encadrement :**
  $$\omega(G) \le \chi(G)$$
  *(Démonstration : dans une clique de taille $\omega(G)$, tous les sommets sont adjacents deux à deux ; il faut donc obligatoirement $\omega(G)$ couleurs distinctes pour colorier cette seule composante).*

---

## 🧠 3. Batterie d'Active Recall (Questions d'Auto-Évaluation)

- [ ] **Q1 : Pourquoi la condition d'Ore ($d(u) + d(v) \ge n$) n'est-elle pas une condition nécessaire pour qu'un graphe soit hamiltonien ?**
  - *Réponse flash :* Le cycle simple $C_n$ pour $n \ge 5$ est trivialement hamiltonien. Pourtant, pour toute paire de sommets non adjacents, $d(u) + d(v) = 2 + 2 = 4 < n$. C'est donc une condition suffisante mais nullement nécessaire.
- [ ] **Q2 : Comment prouver qu'un graphe planaire sans triangle (ex: $K_{3,3}$) viole la planarité ?**
  - *Réponse flash :* Sans triangle, chaque face possède au moins 4 arêtes : $2A \ge 4F \implies F \le \frac{A}{2}$. En injectant dans $S - A + F = 2$, on obtient $A \le 2S - 4$. Pour $K_{3,3}$, $S = 6$ et $A = 9$. Or $2(6) - 4 = 8 < 9$. Contradiction.
- [ ] **Q3 : Quelle est la relation entre coloration et partitionnement en ensembles stables ?**
  - *Réponse flash :* Colorier un graphe avec $k$ couleurs équivaut rigoureusement à partitionner l'ensemble de ses sommets en $k$ sous-ensembles stables $S_1, \dots, S_k$, puisque aucun sommet de même couleur ne peut être adjacent.

---

## ⚡ 4. Devoirs, Lectures & Prochaines Actions
- [ ] Réaliser les exercices de la [[TD2_Proprietes_&_Applications|Feuille TD 2]].
- [ ] Étudier les implémentations et traces algorithmiques dans [[03_Algorithmes_sur_les_Graphes|03. Algorithmes Majeurs sur les Graphes]].
