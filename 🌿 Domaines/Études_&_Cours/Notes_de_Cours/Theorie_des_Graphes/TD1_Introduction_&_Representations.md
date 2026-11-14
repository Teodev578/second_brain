---
type: note-cours
created: 2026-11-10
matiere: "Théorie des Graphes"
chapitre: "TD 1 - Introduction, Représentations Mémoire & Topologies Réseaux"
enseignant: "K. E. HOVI"
tags:
  - etudes
  - td
  - theorie-des-graphes
  - matrices-adjacence
  - calcul-matriciel
  - topologies-reseaux
parent: "[[MOC_Theorie_des_Graphes]]"
---

# 📝 TD 1. Introduction, Représentations Mémoire & Topologies Réseaux

> **Matière :** [[MOC_Theorie_des_Graphes|Théorie des Graphes (M1 IT)]] • **Support :** Feuille d'exercices n° 1 • **Statut :** Entièrement Résolu & Démontré

---

## 📌 Exercice 1 – Modélisation et Lemmes Fondamentaux

### 1. Analyse de faisabilité des séquences de connexions (7 serveurs, $n = 7$)
Le **Lemme des Poignées de Main** stipule que dans tout graphe non orienté $G=(V, E)$, la somme des degrés de tous les sommets est le double du nombre d'arêtes :
$$\sum_{v \in V} d(v) = 2m$$
Cette somme est donc obligatoirement un nombre **pair**, ce qui implique directement que le nombre de sommets de degré impair doit être **pair**.

- **Cas A : $(3, 3, 3, 3, 3, 3, 3)$**
  - Somme des degrés : $7 \times 3 = 21$.
  - *Verdict :* **Impossible**. La somme $21$ est impaire, ce qui contredit $\sum d(v) = 2m$. De surcroît, le réseau compterait 7 sommets de degré impair (effectif impair), ce qui est formellement impossible.
- **Cas B : $(2, 3, 4, 4, 5, 5, 5)$**
  - Somme des degrés : $2 + 3 + 4 + 4 + 5 + 5 + 5 = 28$ (nombre pair, correspondant à $m = 14$ arêtes).
  - Nombre de sommets de degré impair : 4 sommets (de degrés 3, 5, 5, 5), effectif pair.
  - *Verdict :* **Possible au regard du Lemme des Poignées de Main**. *(Note théorique : l'application du critère de Havel-Hakimi confirme l'existence d'un graphe simple pour cette suite).*
- **Cas C : $(1, 2, 2, 3, 4, 4, 4)$**
  - Somme des degrés : $1 + 2 + 2 + 3 + 4 + 4 + 4 = 20$ (nombre pair, soit $m = 10$ arêtes).
  - Nombre de sommets de degré impair : 2 sommets (de degrés 1 et 3), effectif pair.
  - *Verdict :* **Possible au regard du Lemme des Poignées de Main** (la parité globale et celle des sommets impairs sont respectées).

---

### 2. Démontrer l'existence d'au moins deux sommets de même degré ($n \ge 2$)
Soit $G = (V, E)$ un graphe simple non orienté comportant $n$ sommets ($n \ge 2$).
1. Dans un graphe simple, un sommet ne peut être relié à lui-même (pas de boucle) ni comporter d'arêtes multiples. Le degré maximal possible pour un sommet est donc $n - 1$ et le degré minimal est $0$.
2. L'ensemble des degrés possibles est a priori inclus dans $\{0, 1, 2, \dots, n - 1\}$, soit $n$ valeurs candidates.
3. Analysons l'interdépendance des valeurs extrêmes :
   - S'il existe un sommet de degré $n - 1$, il est connecté à tous les $n - 1$ autres sommets du graphe. Par conséquent, **aucun sommet ne peut être isolé** (de degré 0). Les degrés effectifs sont donc restreints à $\{1, 2, \dots, n - 1\}$, soit $n - 1$ valeurs possibles.
   - S'il existe un sommet de degré $0$, il n'est connecté à aucun autre sommet. Par conséquent, **aucun sommet ne peut être connecté à tous les autres** (de degré $n - 1$). Les degrés effectifs sont restreints à $\{0, 1, \dots, n - 2\}$, soit $n - 1$ valeurs possibles.
   - Si ni 0 ni $n-1$ n'apparaissent, les degrés appartiennent à $\{1, \dots, n-2\}$, soit $n-2$ valeurs.
4. Dans tous les cas de figure, l'ensemble des degrés effectivement pris par les sommets contient **au plus $n - 1$ valeurs distinctes**.
5. D'après le **principe des tiroirs de Dirichlet** (*Pigeonhole Principle*), en distribuant $n$ sommets sur au plus $n - 1$ valeurs de degrés possibles, il existe obligatoirement au moins deux sommets recevant la même valeur de degré. $\blacksquare$

---

### 3. Signification concrète dans un réseau informatique
Dans une infrastructure de télécommunications ou d'utilisateurs, cette propriété impose une contrainte structurelle absolue : il est matériellement impossible de concevoir un réseau où chaque équipement (ou chaque utilisateur) disposerait d'un niveau d'interconnexion strictement unique. Il y aura invariablement au moins deux nœuds partageant exactement le même nombre de liaisons actives directes.

---

## 📌 Exercice 2 – Représentations Mémoire et Complexité

### 1. Complexité spatiale en mémoire
- **Matrice d'adjacence $A$ :** Tableau à deux dimensions de taille $n \times n$. Complexité : $\Theta(n^2)$.
- **Liste d'adjacence $L$ :** Tableau de taille $n$ pointant vers des listes chaînées totalisant $m$ éléments pour un graphe orienté ($2m$ pour un non orienté). Complexité : $\Theta(n + m)$.

### 2. Comparaison de l'efficacité asymptotique des opérations

| Opération | Matrice d'adjacence ($A$) | Liste d'adjacence ($L$) | Analyse technique |
| :--- | :--- | :--- | :--- |
| **Tester l'existence de $(u, v)$** | $\Theta(1)$ | $O(d^+(u))$ | Indexation directe en matrice $A[u][v]$ contre parcours séquentiel de la liste des voisins de $u$. |
| **Calculer $d^-(u)$ (degré entrant)** | $\Theta(n)$ | $\Theta(n + m)$ | Sommation d'une colonne en matrice ; dans une liste standard, il faut scanner l'ensemble des listes d'adjacence. |
| **Calculer $d^+(u)$ (degré sortant)** | $\Theta(n)$ | $\Theta(1)$ ou $O(d^+(u))$ | Sommation d'une ligne en matrice ; immédiat par la taille de la liste chaînée $L[u]$. |

### 3. Préconisations d'architecture réseau
- **Réseau métropolitain dense ($m \approx n^2$) :** **Matrice d'adjacence recommandée.** Lorsque le graphe est presque complet, $n^2 \approx n + m$. Le surcoût mémoire est négligeable, tandis que l'on bénéficie du test d'adjacence en temps constant $\Theta(1)$ sans l'indirection des pointeurs de listes chaînées.
- **Réseau WAN très dispersé ($m \approx O(n)$) :** **Listes d'adjacence recommandées.** Pour un grand réseau de 100 000 routeurs avec quelques liens par nœud, la matrice requerrait $\approx 10^{10}$ cases (soit plusieurs dizaines de gigaoctets), alors que la liste n'occupe que $O(n)$ espace (quelques mégaoctets).

---

## 📌 Exercice 3 – Calcul Algébrique sur les Matrices d'Adjacence

Soit $G = (V, E)$ avec $V = \{1, 2, 3, 4\}$ et la matrice d'adjacence :
$$A = \begin{pmatrix} 0 & 1 & 1 & 0 \\ 0 & 0 & 1 & 1 \\ 1 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 \end{pmatrix}$$

### 1. Structure du graphe orienté $G$
Les arcs orientés présents sont :
$$E = \{(1, 2), (1, 3), (2, 3), (2, 4), (3, 1), (3, 4)\}$$
Le sommet 4 est un puits (aucun arc sortant).

### 2. Degrés entrants $d^-(i)$ et sortants $d^+(i)$
- **Sommet 1 :** $d^+(1) = 2$ (arcs $(1,2), (1,3)$), $d^-(1) = 1$ (arc $(3,1)$).
- **Sommet 2 :** $d^+(2) = 2$ (arcs $(2,3), (2,4)$), $d^-(2) = 1$ (arc $(1,2)$).
- **Sommet 3 :** $d^+(3) = 2$ (arcs $(3,1), (3,4)$), $d^-(3) = 2$ (arcs $(1,3), (2,3)$).
- **Sommet 4 :** $d^+(4) = 0$, $d^-(4) = 2$ (arcs $(2,4), (3,4)$).

### 3. Calcul matriciel de $A^2$ et $A^3$

$$A^2 = A \times A = \begin{pmatrix} 0 & 1 & 1 & 0 \\ 0 & 0 & 1 & 1 \\ 1 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 \end{pmatrix} \begin{pmatrix} 0 & 1 & 1 & 0 \\ 0 & 0 & 1 & 1 \\ 1 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 \end{pmatrix} = \begin{pmatrix} 1 & 0 & 1 & 2 \\ 1 & 0 & 0 & 1 \\ 0 & 1 & 1 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix}$$

$$A^3 = A^2 \times A = \begin{pmatrix} 1 & 0 & 1 & 2 \\ 1 & 0 & 0 & 1 \\ 0 & 1 & 1 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix} \begin{pmatrix} 0 & 1 & 1 & 0 \\ 0 & 0 & 1 & 1 \\ 1 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 \end{pmatrix} = \begin{pmatrix} 1 & 1 & 1 & 1 \\ 0 & 1 & 1 & 0 \\ 1 & 0 & 1 & 2 \\ 0 & 0 & 0 & 0 \end{pmatrix}$$

### 4. Nombre et énumération des chemins de longueur 3 de 1 vers 4
D'après le Théorème 1.2.1, le nombre de chemins de longueur 3 reliant le sommet 1 au sommet 4 est donné par le coefficient $(A^3)_{1,4}$.
Dans la matrice $A^3$, la première ligne et quatrième colonne donne :
$$(A^3)_{1,4} = 1$$
Il existe donc **exactement un seul chemin** de longueur 3 reliant 1 à 4.
- Décomposition du chemin :
  - Depuis 1, les successeurs sont 2 et 3.
  - Depuis 2, on peut aller en 3 puis en 4 : $1 \to 2 \to 3 \to 4$ (longueur 3, valide).
  - Depuis 3, on va en 1 ou 4 (aucun ne permet d'atteindre 4 en exactement 3 arcs).
- **Chemin unique :** $1 \to 2 \to 3 \to 4$.

---

## 📌 Exercice 4 – Analyse des Topologies Réseaux Usuelles

Pour $n$ équipements réseau ($n \ge 3$) :

| Topologie | Nombre d'arêtes $m$ | Degré de chaque sommet | $\Delta$ | $\delta$ | Degré moyen $\bar{d} = \frac{2m}{n}$ |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Totalement maillée ($K_n$)** | $\frac{n(n-1)}{2}$ | $d(v) = n - 1$ | $n - 1$ | $n - 1$ | $n - 1$ |
| **Anneau ($C_n$)** | $n$ | $d(v) = 2$ | $2$ | $2$ | $2$ (graphe 2-régulier) |
| **Étoile ($S_n$)** | $n - 1$ | Centre : $n - 1$, Feuilles : $1$ | $n - 1$ | $1$ | $\frac{2(n-1)}{n} = 2 - \frac{2}{n}$ |

### Risque de goulot d'étranglement
Lorsque $n$ devient très grand, la **topologie en étoile ($S_n$)** présente le risque le plus critique. Le switch central concentre un degré de $n - 1$ et traite l'intégralité du transit réseau. Sa bande passante, sa mémoire tampon et sa puissance de commutation constituent un point individuel de défaillance (*Single Point of Failure*) et un goulot d'étranglement physique majeur.

---

## 📌 Exercice 5 – Degré d'un Graphe et Analyse Matricielle

Soit $G = (V, E)$ non orienté simple, et $A = (a_{ij})_{1 \le i,j \le n}$.

1. **Expression du degré :** Dans un graphe simple, chaque coefficient $a_{ij} = 1$ si $v_i$ et $v_j$ sont reliés, et 0 sinon. Ainsi :
   $$d(v_i) = \sum_{j=1}^n a_{ij}$$
2. **Somme de tous les éléments :**
   $$\sum_{i=1}^n \sum_{j=1}^n a_{ij} = \sum_{i=1}^n d(v_i) = 2m$$
   *(Chaque arête non orientée contribue pour deux $1$ symétriques dans la matrice).*
3. **Analyse de la matrice donnée :**
   $$A = \begin{pmatrix} 0 & 1 & 1 & 1 \\ 1 & 0 & 1 & 0 \\ 1 & 1 & 0 & 1 \\ 1 & 0 & 1 & 0 \end{pmatrix}$$
   - Degrés par sommets (somme des lignes) :
     - $d(v_1) = 0 + 1 + 1 + 1 = 3$
     - $d(v_2) = 1 + 0 + 1 + 0 = 2$
     - $d(v_3) = 1 + 1 + 0 + 1 = 3$
     - $d(v_4) = 1 + 0 + 1 + 0 = 2$
   - Valeurs structurelles :
     - $\Delta(G) = \max(3, 2, 3, 2) = 3$
     - $\delta(G) = \min(3, 2, 3, 2) = 2$
     - Somme totale des degrés : $3 + 2 + 3 + 2 = 10 \implies m = 5$ arêtes.
     - Degré moyen : $\bar{d} = \frac{10}{4} = 2{,}5$.
4. **Régularité :** Le graphe **n'est pas régulier**, car tous ses sommets ne partagent pas le même degré ($d(v_1)=3 \ne d(v_2)=2$).
