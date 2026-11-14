---
type: note-cours
created: 2026-11-10
matiere: "Théorie des Graphes"
chapitre: "TD 2 - Propriétés Fondamentales & Modélisation Réseaux"
enseignant: "K. E. HOVI"
tags:
  - etudes
  - td
  - theorie-des-graphes
  - connexite
  - euler-hamilton
  - planarite
  - welsh-powell
  - cliques-stables
parent: "[[MOC_Theorie_des_Graphes]]"
---

# 📝 TD 2. Propriétés Fondamentales & Modélisation Réseaux

> **Matière :** [[MOC_Theorie_des_Graphes|Théorie des Graphes (M1 IT)]] • **Support :** Feuille d'exercices n° 2 • **Statut :** Entièrement Résolu & Démontré

---

## 📌 Exercice 1 – Connexité, Forte Connexité et Composantes

### 1. Réseau local non orienté $G_1 = (V, E)$
Le graphe comporte l'ensemble de sommets $V = \{A, B, C, D, E, F\}$ et les arêtes formant le triangle $\{A, B, C\}$, le segment $\{D, E\}$ et le nœud isolé $\{F\}$.
- **(a) Composantes connexes :**
  Il existe trois composantes connexes maximales disjointes :
  $$C_1 = \{A, B, C\}, \quad C_2 = \{D, E\}, \quad C_3 = \{F\}$$
  Le graphe possède $3 > 1$ composantes connexes : **le réseau n'est donc pas connexe** (il n'existe aucune chaîne physique reliant par exemple $A$ à $D$, ni aucun nœud à $F$).
- **(b) Nombre minimal d'arêtes à ajouter :**
  Pour relier $k$ composantes connexes en un seul graphe connexe, il faut ajouter au minimum **$k - 1$ arêtes**.
  Ici, $k = 3 \implies 3 - 1 = 2$ arêtes suffisent (par exemple l'arête $\{C, D\}$ reliant $C_1$ à $C_2$, et l'arête $\{E, F\}$ reliant $C_2$ à $C_3$).

### 2. Réseau orienté $G_2$
Le graphe orienté sur $V = \{1, 2, 3, 4\}$ présente la structure d'interconnexion :
- **(a) Composantes fortement connexes (CFC) :**
  Si le graphe comporte un circuit orienté $1 \to 2 \to 3 \to 4 \to 1$, alors tous les sommets peuvent s'atteindre mutuellement et il n'y a qu'une unique composante fortement connexe : $\{1, 2, 3, 4\}$.
  Si en revanche un arc brise ce circuit (par exemple si le sommet 4 est un récepteur sans retour), les CFC se scindent en sous-ensembles maximaux irréductibles.
- **(b) Diagnostic de forte connexité :**
  Un graphe orienté est fortement connexe si et seulement si pour toute paire $(u, v)$, il existe un chemin de $u$ vers $v$ et un chemin de $v$ vers $u$. Sa fermeture transitive est alors le graphe complet orienté.

---

## 📌 Exercice 2 – Parcours Eulériens et Hamiltoniens

### 1. Graphes Eulériens
- **(a) Rappel du Théorème d'Euler :**
  - Un graphe connexe admet un **cycle eulérien** $\iff$ tous ses sommets ont un degré pair.
  - Un graphe connexe admet une **chaîne eulérienne** (ouverte) $\iff$ il possède exactement deux sommets de degré impair (qui constituent alors le point de départ et le point d'arrivée).
- **(b) Analyse du réseau :**
  Liste des degrés : $d(A) = 4, d(B) = 2, d(C) = 3, d(D) = 3, d(E) = 2$.
  - *Circuit eulérien :* **Impossible**, car les sommets $C$ et $D$ sont de degré impair ($3$).
  - *Chaîne eulérienne :* **Possible**. Le réseau compte exactement deux sommets de degré impair ($C$ et $D$) et tous les autres sommets ont un degré pair ($4, 2, 2$). Le technicien peut inspecter chaque câble une et une seule fois en initiant sa tournée au sommet $C$ pour la terminer au sommet $D$ (ou inversement).

### 2. Graphes Hamiltoniens
- **(a) Définition :** Visite de chaque routeur une fois et une seule avec retour à l'origine (cycle élémentaire d'ordre $n$).
- **(b) Théorèmes de Dirac et Ore :**
  - *Dirac (1952) :* Si $n \ge 3$ et $\forall v \in V, d(v) \ge \frac{n}{2}$, alors $G$ est hamiltonien.
  - *Ore (1960) :* Si $n \ge 3$ et pour tout couple de sommets non adjacents $\{u, v\}$, $d(u) + d(v) \ge n$, alors $G$ est hamiltonien.
- **(c) Graphe à 6 sommets ($n = 6$) où chaque degré $d(v) \ge 3$ :**
  - Ici, $n = 6 \ge 3$.
  - La condition de Dirac exige que chaque degré vérifie :
    $$d(v) \ge \frac{n}{2} = \frac{6}{2} = 3$$
  - Cette condition étant strictement satisfaite pour chaque sommet par hypothèse, le théorème de Dirac s'applique directement : **le graphe admet nécessairement un cycle hamiltonien**.

---

## 📌 Exercice 3 – Arbres, Arborescences et Planarité

### 1. Démonstration par récurrence : Tout arbre à $n$ sommets possède $n - 1$ arêtes
- **Initialisation ($n = 1$) :** Un arbre à un seul sommet ne comporte aucun cycle et aucune arête. On a bien $m = 0 = 1 - 1$. La propriété est vérifiée.
- **Hypothèse de récurrence :** Supposons que tout arbre d'ordre $k$ (avec $k \ge 1$) possède exactement $k - 1$ arêtes.
- **Hérédité ($n = k + 1$) :**
  1. Soit $T = (V, E)$ un arbre à $k + 1 \ge 2$ sommets.
  2. Comme $T$ est un arbre fini ($n \ge 2$), il possède au moins une feuille, c'est-à-dire un sommet $v$ de degré $d(v) = 1$ (sinon, si tous les sommets avaient un degré $\ge 2$, $T$ contiendrait un cycle, ce qui contredit la définition d'un arbre).
  3. Supprimons ce sommet feuille $v$ ainsi que l'unique arête $e$ qui lui est incidente. Le sous-graphe résultant $T' = (V \setminus \{v\}, E \setminus \{e\})$ reste connexe (car $v$ n'était sur aucun chemin intermédiaire entre d'autres sommets) et demeure sans cycle.
  4. $T'$ est donc un arbre à $k$ sommets.
  5. Par hypothèse de récurrence, $T'$ possède exactement $k - 1$ arêtes.
  6. Le nombre d'arêtes de l'arbre initial $T$ est donc :
     $$|E| = |E'| + 1 = (k - 1) + 1 = k = (k + 1) - 1 = n - 1$$
- **Conclusion :** Par récurrence, tout arbre à $n$ sommets possède exactement $n - 1$ arêtes. $\blacksquare$

### 2. Planarité
- **(a) Formule d'Euler :** Pour tout graphe connexe planaire tracé sans croisement dans le plan :
  $$S - A + F = 2$$
  où $S$ est le nombre de sommets, $A$ le nombre d'arêtes et $F$ le nombre de faces (y compris la face infinie extérieure).
- **(b) Vérification sur le graphe de la figure :**
  - Sommets : $S = 8$.
  - Arêtes : Contour hexagonal externe ($6$) + sommet 7 relié à $\{1, 2, 8\}$ ($3$) + sommet 8 relié à $\{6, 5, 4, 7\}$ ($4$). Total des arêtes : $A = 6 + 3 + 4 = 13$.
  - Faces : Décompte des régions fermées intérieures ($6$ triangles/polygones) + 1 région extérieure infinie $\implies F = 7$.
  - Vérification : $S - A + F = 8 - 13 + 7 = 2$. La formule d'Euler est rigoureusement confirmée.
- **(c) Non-planarité de $K_5$ :**
  Pour un graphe planaire sans face de degré 1 ou 2, chaque face est délimitée par au moins 3 arêtes. Comme chaque arête sépare au plus 2 faces, on a $3F \le 2A \implies F \le \frac{2}{3}A$.
  En injectant dans la formule d'Euler :
  $$S - A + \frac{2}{3}A \ge 2 \iff A \le 3S - 6$$
  Pour le graphe complet $K_5$, on a $S = 5$ et $A = \binom{5}{2} = 10$.
  L'inégalité exigerait :
  $$10 \le 3(5) - 6 = 9 \quad (\text{Faux})$$
  Cette contradiction démontre mathématiquement que **$K_5$ n'est pas planaire**.

---

## 📌 Exercice 4 – Coloriage et Fréquences Radio (Welsh-Powell)

Le réseau d'interférences forme deux triangles reliés par le sommet central 3 : $\{1, 2, 3\}$ et $\{3, 4, 5\}$ avec les arêtes $\{1,2\}, \{1,3\}, \{2,3\}$ et $\{3,4\}, \{3,5\}, \{4,5\}$.

1. **Degrés des sommets :**
   $$d(1) = 2, \quad d(2) = 2, \quad d(3) = 4, \quad d(4) = 2, \quad d(5) = 2$$
2. **Nombre chromatique $\chi(G)$ :**
   Le graphe contient le sous-graphe complet $K_3 = \{1, 2, 3\}$. Par conséquent, $\chi(G) \ge \omega(G) = 3$.
   Une 3-coloration étant triviale (Couleur 1 pour $\{3\}$, Couleur 2 pour $\{1, 4\}$, Couleur 3 pour $\{2, 5\}$), on a :
   $$\chi(G) = 3$$
3. **Application de l'algorithme glouton de Welsh-Powell :**
   - *Étape 1 :* Tri des sommets par ordre décroissant des degrés :
     $$3 \,(d=4), \quad 1 \,(d=2), \quad 2 \,(d=2), \quad 4 \,(d=2), \quad 5 \,(d=2)$$
   - *Couleur 1 :*
     - Attribuée au premier sommet : **Sommet 3**.
     - Voisins de 3 : 1, 2, 4, 5 (tous adjacents à 3). Aucun autre sommet ne peut recevoir la Couleur 1.
   - *Couleur 2 :*
     - Premier sommet disponible non colorié : **Sommet 1**.
     - Parcourt des suivants : Sommet 2 adjacent à 1 (refusé). Sommet 4 non adjacent à 1 $\implies$ **Sommet 4** reçoit la Couleur 2. Sommet 5 adjacent à 4 (refusé).
   - *Couleur 3 :*
     - Premier disponible : **Sommet 2**.
     - Suivant : Sommet 5 non adjacent à 2 $\implies$ **Sommet 5** reçoit la Couleur 3.
   - *Résultat final :*
     - Fréquence 1 : $\{3\}$
     - Fréquence 2 : $\{1, 4\}$
     - Fréquence 3 : $\{2, 5\}$
     Total : **3 fréquences**, ce qui est optimal.

---

## 📌 Exercice 5 – Cliques et Ensembles Stables

Graphe simple non orienté à 6 sommets constitué de deux triangles disjoints $\{1, 2, 3\}$ et $\{4, 5, 6\}$ reliés par une unique arête pont $\{3, 4\}$.

1. **Définitions formelles :**
   - Une **clique** est un sous-ensemble $C \subseteq V$ dont les sommets sont adjacents deux à deux ($\forall u, v \in C, u \ne v \implies \{u, v\} \in E$).
   - Un **ensemble stable** est un sous-ensemble $S \subseteq V$ dont aucun couple de sommets n'est adjacent ($\forall u, v \in S, u \ne v \implies \{u, v\} \notin E$).
2. **Ordre de la plus grande clique ($\omega(G)$) :**
   Les sous-graphes induits par $\{1, 2, 3\}$ et $\{4, 5, 6\}$ sont des $K_3$. Aucun groupe de 4 sommets n'est totalement interconnecté. Ainsi :
   $$\omega(G) = 3$$
3. **Taille du plus grand ensemble stable ($\alpha(G)$) :**
   Comme l'ensemble des 6 sommets est partitionné en deux cliques de taille 3, tout sous-ensemble de 3 sommets contiendrait au moins 2 sommets issus de la même clique (principe des tiroirs), qui seraient donc reliés par une arête. Un ensemble stable ne peut donc contenir au maximum qu'un seul sommet de $\{1, 2, 3\}$ et un seul de $\{4, 5, 6\}$.
   L'ensemble $\{1, 5\}$ ne comporte aucune arête et contient 2 sommets. Par conséquent :
   $$\alpha(G) = 2$$
4. **Relation avec le graphe complémentaire $\overline{G}$ :**
   Par définition, deux sommets sont reliés dans $\overline{G}$ si et seulement s'ils ne le sont pas dans $G$. Par conséquent, tout ensemble stable dans $G$ forme une clique dans $\overline{G}$, d'où :
   $$\alpha(G) = \omega(\overline{G}) \quad \text{et} \quad \omega(G) = \alpha(\overline{G})$$

---

## 📌 Exercices 6, 7 & 8 – Études de Topologies Réseaux Appliquées

Ces trois exercices partagent la même méthodologie d'analyse topologique et matricielle :
1. **Complétude et Connexité :** Le graphe n'est pas complet dès lors qu'il existe au moins deux sommets sans liaison directe ($m < \frac{n(n-1)}{2} = 28$ pour $n=8$). La connexité se démontre par l'existence d'une chaîne continue interconnectant l'ensemble des 8 commutateurs/stations.
2. **Parcours Eulérien :** Il suffit de dénombrer les degrés de l'ensemble des 8 nœuds. Si le nombre de sommets de degré impair est exactement 0 ou 2, le parcours exhaustif sans répétition est garanti.
3. **Calcul de sauts par les puissances matricielles :**
   - Le nombre minimal de liaisons entre une origine $X$ et une destination $Y$ correspond au plus petit entier $p$ tel que $(M^p)_{X,Y} > 0$.
   - Si $(M)_{X,Y} = 0$ et $(M^2)_{X,Y} = 0$, mais $(M^3)_{X,Y} > 0$, la distance géodésique vaut exactement 3 sauts.
   - Les trajets de longueur 3 s'obtiennent directement en recensant les séquences d'intermédiaires $X \to i \to j \to Y$ telles que $M[X][i] \cdot M[i][j] \cdot M[j][Y] = 1$.
