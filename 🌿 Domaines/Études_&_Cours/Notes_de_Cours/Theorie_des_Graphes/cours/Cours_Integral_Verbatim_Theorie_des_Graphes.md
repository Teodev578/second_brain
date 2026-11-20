---
type: note-cours
created: 2026-11-10
matiere: "Théorie des Graphes"
chapitre: "Texte Intégral & Référence Officielle (Prof. K. E. HOVI)"
enseignant: "K. E. HOVI (Ascencia Keyce Lomé)"
niveau: "Master 1 - IT"
tags:
  - etudes
  - cours
  - theorie-des-graphes
  - verbatim
  - transcription-integrale
parent: "[[MOC_Theorie_des_Graphes]]"
---

# 📜 Support Intégral : Théorie des Graphes (M1 IT)

> **Document source :** `Support_Cours_Theorie_des_Graphes.pdf` • **Enseignant :** K. E. HOVI (Campus de Lomé, 10 nov. 2026)
> **Aperçu PDF direct dans Obsidian :**
> ![[Support_Cours_Theorie_des_Graphes.pdf]]

---

## Sommaire Officiel

### Partie I – COURS
1. **Introduction à la théorie des graphes** (p. 3)
   - 1.1 Définitions et premiers exemples (p. 3)
     - 1.1.1 Notion d'adjacence entre sommets (p. 4)
     - 1.1.2 Notion de degré d'un sommet (p. 4)
   - 1.2 Représentation des graphes (p. 8)
     - 1.2.1 Matrice d'adjacence (p. 8)
     - 1.2.2 Liste d'adjacence (p. 10)
     - 1.2.3 Degré d'un sommet (p. 11)
     - 1.2.4 Degré d'un graphe (p. 12)
2. **Propriétés fondamentales des graphes** (p. 13)
   - 2.1 Connexité : composantes connexes, graphes fortement connexes (p. 13)
     - 2.1.1 Cas des graphes non orientés (p. 13)
     - 2.1.2 Cas des graphes orientés (p. 14)
   - 2.2 Graphes eulériens (p. 15)
   - 2.3 Graphe hamiltonien (p. 16)
   - 2.4 Arbre et arborescence (p. 17)
     - 2.4.1 Planarité et coloriage de graphes (p. 18)
   - 2.5 Coloriage de graphes, cliques et stables (p. 19)
     - 2.5.1 Cliques et ensembles stables (p. 20)
3. **Les algorithmes sur les graphes** (p. 22)
   - 3.1 Parcours de graphes : parcours en largeur (BFS) et en profondeur (DFS) (p. 22)
     - 3.1.1 Parcours en largeur (BFS) (p. 22)
     - 3.1.2 Parcours en profondeur (DFS) (p. 23)
     - 3.1.3 Illustration des parcours (p. 24)
   - 3.2 Algorithmes de recherche de chemins : Dijkstra, Bellman-Ford (p. 25)
     - 3.2.1 Algorithme de Dijkstra (p. 25)
     - 3.2.2 Algorithme de Bellman-Ford (p. 27)
     - 3.2.3 Illustration des algorithmes de Dijkstra et Bellman-Ford (p. 28)
   - 3.3 Algorithmes pour arbres couvrants : Kruskal, Prim (p. 30)
     - 3.3.1 Algorithme de Kruskal (p. 30)
     - 3.3.2 Algorithme de Prim (p. 31)
     - 3.3.3 Illustration des algorithmes de Kruskal et Prim (p. 31)
   - 3.4 Flots dans les réseaux : Algorithme de Ford-Fulkerson (p. 33)
     - 3.4.1 Concept de flot et propriétés fondamentales (p. 33)
     - 3.4.2 Algorithme de Ford-Fulkerson (p. 33)
     - 3.4.3 Illustration de l'algorithme de Ford-Fulkerson (p. 34)

### Partie II – TRAVAUX DIRIGÉS
- Feuille d'exercices n° 1 : Introduction à la théorie des graphes (p. 37)
- Feuille d'exercices n° 2 : Propriétés fondamentales des graphes (p. 40)
- Feuille d'exercices n° 3 : Les algorithmes sur les graphes (p. 45)

---

# PARTIE I – COURS

## Chapitre 1 : Introduction à la théorie des graphes

### Introduction historique
La théorie des graphes trouve ses origines avec les travaux d'Euler au XVIIIe siècle, notamment avec le problème des ponts de Königsberg. D'autres problèmes, comme la marche du cavalier ou le coloriage de cartes, ont également contribué à son développement. Au XXe siècle, grâce à des mathématiciens tels que Königsberg, Menger, Cayley, Berge et Erdös, cette théorie est devenue une branche des mathématiques à part entière.

Un graphe représente les relations entre les éléments d'un ensemble complexe, et il est utilisé dans de nombreux domaines : réseaux de communication, réseaux routiers, biologie, etc. Aujourd'hui, les informaticiens utilisent la théorie des graphes pour résoudre des problèmes complexes, en particulier ceux liés à l'aspect algorithmique.

---

### 1.1 Définitions et premiers exemples

#### Définition 1.1.1
Un graphe fini $G = (V, E)$ est défini par :
- un ensemble fini $V = \{v_1, v_2, \dots, v_n\}$, dont les éléments sont appelés **sommets** (*Vertices* en anglais) ;
- un ensemble fini $E = \{e_1, e_2, \dots, e_m\}$, dont les éléments sont appelés **arêtes** (*Edges* en anglais).

Chaque arête $e \in E$ est définie comme une paire non ordonnée de sommets, appelée les **extrémités** de $e$. Si une arête $e$ relie deux sommets $a$ et $b$, alors :
- $a$ et $b$ sont dits **adjacents** ou **incidents** avec $e$ ;
- l'arête $e$ est dite **incidente** avec les sommets $a$ et $b$.

Le nombre de sommets $n$ d'un graphe est appelé l'**ordre** de ce graphe.

#### Définition 1.1.2
- L'**ordre** d'un graphe est le nombre de ses sommets.
- Une **boucle** est un arc ou une arête reliant un sommet à lui-même.
- Un graphe non-orienté est dit **simple** s'il ne comporte pas de boucle, et s'il ne comporte jamais plus d'une arête entre deux sommets. Un graphe non orienté qui n'est pas simple est un **multi-graphe**. Dans le cas d'un multi-graphe, $A$ n'est plus un ensemble mais un multi-ensemble d'arêtes. On se restreindra généralement dans la suite aux graphes simples.
- Un graphe orienté est un **$p$-graphe** s'il comporte au plus $p$ arcs entre deux sommets. Le plus souvent, on étudiera des 1-graphes.
- Un **graphe partiel** d'un graphe orienté ou non est le graphe obtenu en supprimant certains arcs ou arêtes.
- Un **sous-graphe** d'un graphe orienté ou non est le graphe obtenu en supprimant certains sommets et tous les arcs ou arêtes incidents aux sommets supprimés.
- Un graphe orienté est dit **élémentaire** s'il ne contient pas de boucle.
- Un graphe orienté est dit **complet** s'il comporte un arc $(s_i, s_j)$ et un arc $(s_j, s_i)$ pour tout couple de sommets différents $s_i, s_j \in S^2$. De même, un graphe non-orienté est dit complet s'il comporte une arête $(s_i, s_j)$ pour toute paire de sommets différents $s_i, s_j \in S^2$.

#### Remarque 1.1.1
Un graphe est une structure mathématique utilisée pour modéliser des relations entre des objets. Il est défini comme suit :
- **Sommet (ou nœud) :** Un point du graphe qui représente un objet ou une entité.
- **Arête :** Une connexion entre deux sommets, représentant une relation.
- **Degré :** Le nombre d'arêtes incidentes à un sommet.
Pour les graphes dirigés, on distingue le degré entrant et le degré sortant.

#### 1.1.1 Notion d'adjacence entre sommets
- Dans un graphe non orienté, un sommet $s_i$ est dit adjacent à un autre sommet $s_j$ s'il existe une arête entre $s_i$ et $s_j$. L'ensemble des sommets adjacents à un sommet $s_i$ est défini par :
  $$\text{adj}(s_i) = \{s_j \mid (s_i, s_j) \in A \text{ ou } (s_j, s_i) \in A\}$$
- Dans un graphe orienté, on distingue les sommets **successeurs** des sommets **prédécesseurs** :
  $$\text{succ}(s_i) = \{s_j \mid (s_i, s_j) \in A\}$$
  $$\text{pred}(s_i) = \{s_j \mid (s_j, s_i) \in A\}$$

#### 1.1.2 Notion de degré d'un sommet
- Dans un graphe non orienté, le degré d'un sommet est le nombre d'arêtes incidentes à ce sommet (dans le cas d'un graphe simple, on aura $d^\circ(s_i) = |\text{adj}(s_i)|$).
- Dans un graphe orienté, le demi-degré extérieur d'un sommet $s_i$, noté $d^{\circ+}(s_i)$, est le nombre d'arcs partant de $s_i$ (dans le cas d'un 1-graphe, on aura $d^{\circ+}(s_i) = |\text{succ}(s_i)|$).
- De même, le demi-degré intérieur d'un sommet $s_i$, noté $d^{\circ-}(s_i)$, est le nombre d'arcs arrivant à $s_i$ (dans le cas d'un 1-graphe, on aura $d^{\circ-}(s_i) = |\text{pred}(s_i)|$).

---

### Activités du Chapitre 1

#### Activité 1.1.1
1. Dessiner un graphe non orienté complet à 4 sommets ($K_4$).
2. Quel est le degré des sommets de ce graphe ? *(Réponse : $d(v) = 3$)*.
3. Combien d'arêtes possède-t-il ? Généralisez ces résultats à un graphe simple complet ayant $n$ sommets. *(Réponse : $m = \frac{4 \times 3}{2} = 6$ arêtes ; pour $n$ sommets : $m = \frac{n(n-1)}{2}$)*.

#### Activité 1.1.2
On considère le graphe orienté $G = (S, A)$ tel que :
$S = \{1, 2, 3, 4, 5\}$, $A = \{(1,2), (1,4), (2,2), (2,3), (2,4), (3,5), (4,3), (5,3)\}$.
1. Représenter graphiquement ce graphe.
2. Donner le demi-degré extérieur de 2 ($d^+(2) = 3$) et le demi-degré intérieur de 4 ($d^-(4) = 2$).
3. Donner les sommets prédécesseurs de 4 ($\text{pred}(4) = \{1, 2\}$) et les sommets successeurs de 2 ($\text{succ}(2) = \{2, 3, 4\}$).
4. Donner un graphe partiel et un sous-graphe de ce graphe.

#### Activité 1.1.3 : Problème des poignées de main
Au cours d'une soirée, les convives se serrent les mains les uns les autres (jamais plusieurs fois avec la même personne). Chacun se souvient du nombre de mains qu'il a serrées.
1. Montrer qu'il y a au moins deux personnes ayant serré le même nombre de mains.
2. Montrer que le nombre total de mains serrées est pair ($\sum_{s_i \in S} d(s_i) = 2|A|$).
3. En déduire que le nombre de personnes ayant serré un nombre impair de mains est pair.

---

### Chaînes, Chemins et Cycles

#### Définition 1.1.3
Une **chaîne** (ou un chemin) dans un graphe est une séquence ordonnée de sommets, où chaque paire consécutive de sommets est reliée par une arête.
Un chemin $P$ de longueur $k$ dans un graphe $G = (V, E)$ est une séquence de sommets $P : v_0, v_1, \dots, v_k$ telle que :
- $v_i \in V, \; \forall 0 \le i \le k$ ;
- $(v_i, v_{i+1}) \in E, \; \forall 0 \le i < k$.

#### Remarque 1.1.2
- **Chaînes simples :** Les sommets sont distincts (aucun sommet visité plus d'une fois, sauf éventuellement l'extrémité).
- **Chaînes fermées :** Le point de départ $v_0$ et le point d'arrivée $v_k$ sont identiques.

#### Définition 1.1.4 & Remarque 1.1.3
Un **cycle** est une chaîne fermée $v_0, v_1, \dots, v_k, v_0$ telle que :
- $k \ge 3$ ;
- $(v_i, v_{i+1}) \in E, \; \forall 0 \le i < k$ ;
- $v_i \ne v_j, \; \forall 0 \le i, j < k \text{ si } i \ne j$.

---

### 1.2 Représentation des graphes

#### 1.2.1 Matrice d'adjacence
Soit le graphe $G = (S, A)$ avec sommets numérotés de 1 à $n$ ($n = |S|$).
La matrice d'adjacence est une matrice binaire $M$ de taille $n \times n$ telle que :
$$M[i][j] = \begin{cases} 1 & \text{si } (i, j) \in A \\ 0 & \text{sinon} \end{cases}$$
- Si le graphe est valué : $M[i][j] = \text{valeur de l'arc } (i, j)$ si $(i, j) \in A$, et $0, \infty$ ou null sinon.
- Dans le cas non orienté, la matrice est **symétrique** ($a_{ij} = a_{ji}$).
- **Degré des sommets :** $d^+(v_i) = \sum_j a_{ij}$ et $d^-(v_i) = \sum_j a_{ji}$.
- **Théorème 1.2.1 :** Le nombre de chemins de longueur $p$ reliant deux sommets $i$ et $j$ est donné par le terme de la $i$-ième ligne et $j$-ième colonne de la matrice $M^p$.

#### 1.2.2 Liste d'adjacence
Tableau $T$ de $n$ listes, une pour chaque sommet de $S$. Pour chaque sommet $s_i$, $T[s_i]$ est la liste chaînée de tous les sommets $s_j$ tels que $(s_i, s_j) \in A$.
- Représentation compacte en $\Theta(n + m)$, très performante pour graphes peu denses et algorithmes de parcours (BFS, DFS, Dijkstra).

#### 1.2.3 Degré d'un sommet & Théorème 1.2.2
Le degré $d(v)$ est le nombre d'arêtes incidentes à $v$ (une boucle compte deux fois).
$$\sum_{v \in V} d(v) = 2|E|$$

#### 1.2.4 Degré d'un graphe
Le degré d'un graphe est le degré maximum de tous ses sommets : $\Delta(G) = \max_{v \in V} d(v)$.
Un graphe est dit **$k$-régulier** si tous ses sommets ont le même degré $k$.

---

## Chapitre 2 : Propriétés fondamentales des graphes

### 2.1 Connexité
- **Graphe non orienté connexe :** Chaque sommet est accessible à partir de n'importe quel autre (existence d'une chaîne entre $s_i$ et $s_j$).
- **Composante connexe :** Sous-graphe $G'$ connexe et maximal.
- **Forte connexité (graphe orienté) :** Il existe un chemin orienté de $s_i$ vers $s_j$ et de $s_j$ vers $s_i$ pour tout couple.
- **Composante fortement connexe (CFC) :** Sous-graphe orienté maximal fortement connexe.

### 2.2 Graphes eulériens
- **Définition 2.2.1 :** Chaîne / cycle empruntant une et une seule fois chaque arête du graphe.
- **Théorème 2.2.1 :** Un graphe connexe admet un cycle eulérien $\iff$ aucun sommet de degré impair.
- **Théorème 2.2.2 :** Un graphe connexe admet une chaîne eulérienne entre $u$ et $v \iff d(u)$ et $d(v)$ sont impairs et tous les autres sommets sont de degré pair.
- **Théorème 2.2.3 (Orienté) :** Un multigraphe orienté fortement connexe admet un circuit eulérien $\iff \forall s_i \in S, d^+(s_i) = d^-(s_i)$.
- **Théorème 2.2.4 (Orienté) :** Chemin eulérien de $u$ vers $v \iff d^+(u) = d^-(u) + 1$, $d^+(v) = d^-(v) - 1$, et égalité pour les autres.

### 2.3 Graphe hamiltonien
- **Définition 2.3.1 :** Chaîne passant une et une seule fois par chacun des $n$ sommets (longueur $n-1$). Cycle hamiltonien : cycle élémentaire de longueur $n$.
- Problème NP-complet (Voyageur de commerce / TSP).

### 2.4 Arbre et arborescence
- **Définition 2.4.1 (6 caractérisations équivalentes) :**
  1. $G$ connexe et sans cycle.
  2. $G$ sans cycle et possède $n - 1$ arêtes.
  3. $G$ connexe et admet $n - 1$ arêtes.
  4. $G$ sans cycle, et l'ajout d'une arête crée un unique cycle élémentaire.
  5. $G$ connexe, et la suppression d'une arête quelconque le déconnecte.
  6. Il existe une chaîne et une seule entre 2 sommets quelconques.
- **Forêt :** Graphe dont chaque composante connexe est un arbre.

### 2.4.1 Planarité
- Un graphe est planaire s'il peut être dessiné dans le plan sans que les arêtes ne se croisent hors de leurs extrémités.
- Problème des 3 châtelains ($K_{3,3}$) non planaire.
- Graphes non planaires minimaux : $K_5$ et $K_{3,3}$.

### 2.5 Coloriage, Cliques et Stables
- Nombre chromatique $\chi(G)$ : nombre minimum de couleurs pour colorier les sommets sans que deux sommets adjacents partagent la même couleur.
- Algorithme de Brélaz (DSATUR) : heuristique gloutonne basée sur le degré de saturation.
- **Conjecture (Théorème) des 4 couleurs :** Tout graphe planaire vérifie $\chi(G) \le 4$.
- **Clique :** Sous-graphe complet ($S' \subseteq S$ connectés deux à deux). Ordre max : $\omega(G)$.
- **Stable :** Sous-ensemble de sommets non connectés deux à deux. Ordre max : $\alpha(G)$.
- Inégalité fondamentale : $\omega(G) \le \chi(G)$.

---

## Chapitre 3 : Les algorithmes sur les graphes

### 3.1 BFS et DFS
- **BFS (Breadth-First Search) :** File FIFO, exploration par couches de distance. Distance géodésique $d[u]$, pères $\pi[u]$. Complexité $O(|V| + |E|)$.
- **DFS (Depth-First Search) :** Pile LIFO récursive, estampilles temporelles `d_time[u]` et `f_time[u]`.
  - Classification des arêtes : Arbre, Arrière (*Back*), Avant (*Forward*), Croisée (*Cross*).

### 3.2 Plus courts chemins
- **Relâchement (Relaxation) :** Si $d[v] > d[u] + w(u,v)$ alors $d[v] \leftarrow d[u] + w(u,v)$ et $\pi[v] \leftarrow u$.
- **Dijkstra :** Poids strictement positifs ou nuls ($\forall e, w(e) \ge 0$). Approche gloutonne avec extraction du minimum. Complexité $O((|V|+|E|)\log |V|)$ avec tas binaire.
- **Bellman-Ford :** Accepte les poids négatifs. $|V|-1$ passes de relâchement sur tous les arcs. Contrôle à la $|V|$-ième passe pour détecter les cycles absorbants négatifs. Complexité $O(|V| \cdot |E|)$.

### 3.3 Arbres Couvrants de Poids Minimum (ACPM)
- **Kruskal :** Tri croissant des arêtes, sélection sans cycle via la structure *Union-Find* (`Créer-Ensemble`, `Trouver-Ensemble`, `Union`). Complexité $O(|E|\log |V|)$.
- **Prim :** Croissance d'un unique arbre depuis une racine $r$ par extraction de l'arête frontière de coût minimal. Complexité $O(|E|\log |V|)$.

### 3.4 Flots dans les réseaux : Ford-Fulkerson
- Réseau de transport $\mathcal{N} = (G, c, s, t)$ avec capacité $c$, source $s$, puits $t$.
- Réseau résiduel $G_f$ et chemin augmentant $p$ avec goulot $c_f(p) = \min_{(u,v) \in p} c_f(u,v)$.
- **Théorème Flot-Max / Coupe-Min :** La valeur maximale d'un flot $s-t$ est égale à la capacité minimale d'une coupe $s-t$.
