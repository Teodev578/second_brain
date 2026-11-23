---
type: note-cours
created: 2026-11-10
matiere: "Théorie des Graphes"
chapitre: "TD 3 - Algorithmique Avancée, Ordonnancement & Routage Distribué"
enseignant: "K. E. HOVI"
tags:
  - etudes
  - td
  - theorie-des-graphes
  - dijkstra
  - bellman-ford
  - kruskal-prim
  - dag-pert
  - chemin-critique
  - vecteur-de-distances
parent: "[[MOC_Theorie_des_Graphes]]"
---

# 📝 TD 3. Algorithmique Avancée, Ordonnancement & Routage Distribué

> **Matière :** [[MOC_Theorie_des_Graphes|Théorie des Graphes (M1 IT)]] • **Support :** Feuille d'exercices n° 3 • **Statut :** Entièrement Résolu & Démontré

---

## 📌 Exercice 1 – Parcours de Graphes et Classification des Arcs (BFS & DFS)

Graphe orienté de routeurs $V = \{A, B, C, D, E, F\}$ avec priorité alphabétique.

### 1. Parcours en Largeur (BFS issu de la source $A$)
- **(a) Ordre de découverte des sommets :**
  - Niveau 0 : Découverte de $A$.
  - Niveau 1 : Voisins directs de $A$ par ordre alphabétique $\implies B, C$.
  - Niveau 2 : Voisins non visités de $B$ et $C \implies D, E$.
  - Niveau 3 : Voisins non visités de $D$ et $E \implies F$.
  - *Séquence de découverte BFS :* $$A \to B \to C \to D \to E \to F$$
- **(b) Arêtes de l'arbre couvrant BFS :**
  $$E_{\text{BFS}} = \{(A, B), (A, C), (B, D), (C, E), (D, F)\}$$
- **(c) Vecteur des distances géodésiques $d$ depuis $A$ :**
  $$d[A] = 0, \quad d[B] = 1, \quad d[C] = 1, \quad d[D] = 2, \quad d[E] = 2, \quad d[F] = 3$$

### 2. Parcours en Profondeur (DFS issu de la source $A$)
- **(a) Dates de début ($d$) et de fin ($f$) sous forme $[d/f]$ :**
  - Temps 1 : Découverte de $A$ $[1/?]$
  - Temps 2 : Descente vers $B$ $[2/?]$
  - Temps 3 : Descente vers $D$ $[3/?]$
  - Temps 4 : Descente vers $F$ $[4/?]$ (F n'a aucun voisin non visité)
  - Temps 5 : Fermeture de $F$ $[4/5]$
  - Temps 6 : Fermeture de $D$ $[3/6]$
  - Temps 7 : Fermeture de $B$ $[2/7]$
  - Temps 8 : Exploration de l'autre branche depuis $A \implies C$ $[8/?]$
  - Temps 9 : Descente vers $E$ $[9/?]$
  - Temps 10 : Fermeture de $E$ $[9/10]$
  - Temps 11 : Fermeture de $C$ $[8/11]$
  - Temps 12 : Fermeture finale de $A$ $[1/12]$
  - *Estampilles finales :*
    $$A\,[1/12], \quad B\,[2/7], \quad D\,[3/6], \quad F\,[4/5], \quad C\,[8/11], \quad E\,[9/10]$$
- **(b) Classification des arcs :**
  - **Arcs d'arbre :** $(A, B), (B, D), (D, F), (A, C), (C, E)$ (arcs empruntés lors des premières découvertes).
  - **Arcs arrières (*Back edges*) :** Tout arc menant vers un ancêtre encore actif (GRIS). En l'absence de boucle rétrograde, aucun arc arrière (graphe acyclique).
  - **Arcs avant (*Forward edges*) :** Arcs reliant un ancêtre à un descendant déjà noirci (ex : $(B, E)$ ou $(C, D)$ si présents).
  - **Arcs croisés (*Cross edges*) :** Arcs reliant deux branches disjointes de la forêt DFS sans lien de filiation directe.

### 3. Propriétés algorithmiques théoriques
- **Complexité temporelle :** $\Theta(|V| + |E|)$ car chaque sommet est inséré et extrait au plus une fois, et chaque liste d'adjacence est inspectée une seule fois.
- **Complexité spatiale :** $\Theta(|V|)$ pour stocker les tableaux d'états, distances/estampilles et la pile ou file d'attente.

---

## 📌 Exercice 2 – Plus Courts Chemins : Dijkstra et Bellman-Ford

Réseau orienté à 6 routeurs $\{S, A, B, C, D, T\}$.

### 1. Algorithme de Dijkstra
- **(a) Conditions d'application :** Les poids de tous les arcs doivent être strictement positifs ou nuls ($\forall e \in E, w(e) \ge 0$).
- **(b) Trace d'exécution depuis la source $S$ :**

| Étape | Sommet extrait $u$ | Arcs relâchés | $d[S]$ | $d[A]$ | $d[B]$ | $d[C]$ | $d[D]$ | $d[T]$ | Sommets fixés |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 0 | *Init* | – | **0** | $+\infty$ | $+\infty$ | $+\infty$ | $+\infty$ | $+\infty$ | $\emptyset$ |
| 1 | **$S$** | $(S,A):4, (S,B):2$ | **0** | 4 ($S$) | 2 ($S$) | $+\infty$ | $+\infty$ | $+\infty$ | $\{S\}$ |
| 2 | **$B$** | $(B,C): 2+2=4, (B,D): 2+8=10$ | **0** | 4 ($S$) | **2** | 4 ($B$) | 10 ($B$) | $+\infty$ | $\{S, B\}$ |
| 3 | **$A$** | $(A,B): 4+1=5 > 2, (A,C): 4+3=7 > 4$ | **0** | **4** | **2** | 4 ($B$) | 10 ($B$) | $+\infty$ | $\{S, B, A\}$ |
| 4 | **$C$** | $(C,T): 4+2=6, (C,D): 4+3=7 < 10$ | **0** | **4** | **2** | **4** | 7 ($C$) | 6 ($C$) | $\{S, B, A, C\}$ |
| 5 | **$T$** | Puits (aucun arc sortant) | **0** | **4** | **2** | **4** | 7 ($C$) | **6** | $\{S, B, A, C, T\}$ |
| 6 | **$D$** | $(D,T): 7+4=11 > 6$ | **0** | **4** | **2** | **4** | **7** | **6** | Tous fixés |

- **(c) Plus court chemin de $S$ vers $T$ :**
  - Longueur minimale : **$d[T] = 6\text{ ms}$**.
  - Trajet optimal (en remontant les pères $\pi$) : **$S \to B \to C \to T$** (coût : $2 + 2 + 2 = 6$).

### 2. Algorithme de Bellman-Ford avec arc négatif $w(B, D) = -5$
- **(a) Intérêt de Bellman-Ford :** Supporte nativement les pondérations négatives et garantit la détection formelle des circuits absorbants (coût vers $-\infty$).
- **(b) Relaxation avec $w(B, D) = -5$ :**
  - La distance vers $D$ devient : $d[D] = d[B] + w(B, D) = 2 + (-5) = -3$.
  - L'arc sortant $(D, T)$ propage : $d[T] = \min(6, -3 + 4) = 1$.
  - Le nouveau plus court chemin vers $T$ devient $S \to B \to D \to T$ avec un coût total de $1\text{ ms}$.
- **(c) Détection de cycle de poids négatif :**
  Le graphe est un DAG (graphe acyclique dirigé sans boucle de retour). Aucun cycle n'existe dans le réseau. Lors de la $|V|$-ième étape de contrôle, aucun arc ne peut être relâché davantage : l'algorithme confirme l'**absence de cycle négatif**.

### 3. Comparatif de Complexité

| Algorithme | Complexité temporelle théorique | Avantage principal |
| :--- | :--- | :--- |
| **Dijkstra (Tas binaire)** | $O((|V| + |E|)\log |V|)$ | Extrêmement rapide sur métriques positives. |
| **Bellman-Ford** | $O(|V| \cdot |E|)$ | Robuste aux coûts négatifs et détecteur d'anomalies. |

---

## 📌 Exercice 3 – Arbres Couvrants Minimaux (Kruskal & Prim)

Réseau de 7 datacenters $\{A, B, C, D, E, F, G\}$.

### 1. Algorithme de Kruskal
- **(a) Principe & Rôle de Union-Find :** Kruskal sélectionne les arêtes les moins coûteuses sans jamais fermer de cycle. La structure Union-Find permet en temps quasi-constant ($O(\alpha(n))$) de vérifier si deux sommets appartiennent déjà à la même composante connexe (`Find`) et de fusionner leurs composantes (`Union`).
- **(b) Tri des arêtes par poids croissant :**
  1. $(G, D) : 2$
  2. $(G, E) : 3$
  3. $(E, F) : 4$
  4. $(A, C) : 5$
  5. $(C, E) : 5$
  6. $(D, F) : 6$
  7. $(A, B) : 7$
  8. $(B, C) : 7$
  9. $(C, G) : 7$
  10. $(B, D) : 8$
  11. $(B, G) : 9$
- **(c) Déroulement pas à pas de Kruskal :**
  - Étape 1 : $(G, D)$ de poids 2 $\implies$ **Retenue**. Composante : $\{G, D\}$.
  - Étape 2 : $(G, E)$ de poids 3 $\implies$ **Retenue**. Composante : $\{G, D, E\}$.
  - Étape 3 : $(E, F)$ de poids 4 $\implies$ **Retenue**. Composante : $\{G, D, E, F\}$.
  - Étape 4 : $(A, C)$ de poids 5 $\implies$ **Retenue**. Composante : $\{A, C\}$.
  - Étape 5 : $(C, E)$ de poids 5 $\implies$ **Retenue**. Fusionne $\{A, C\}$ et $\{G, D, E, F\} \implies \{A, C, G, D, E, F\}$.
  - Étape 6 : $(D, F)$ de poids 6 $\implies$ **Rejetée** (crée le cycle $D-G-E-F-D$).
  - Étape 7 : $(A, B)$ de poids 7 $\implies$ **Retenue**. Connecte $B \implies \{A, B, C, D, E, F, G\}$.
  - *Arrêt :* L'arbre contient $n - 1 = 6$ arêtes.

### 2. Algorithme de Prim (Racine $r = A$)
- **(a) Différence stratégique :** Kruskal gère une forêt d'arbres qui fusionnent progressivement ; Prim maintient un unique arbre connexe qui grossit par adjacence locale minimale.
- **(b) Déroulement depuis $A$ :**
  - Étape 1 : Depuis $\{A\}$, arête min vers $\{C\}$ de poids 5 $\implies$ **$(A, C)$ retenue**, arbre $\{A, C\}$.
  - Étape 2 : Depuis $\{A, C\}$, arête min vers $\{E\}$ de poids 5 $\implies$ **$(C, E)$ retenue**, arbre $\{A, C, E\}$.
  - Étape 3 : Depuis $\{A, C, E\}$, arête min vers $\{G\}$ de poids 3 $\implies$ **$(E, G)$ retenue**, arbre $\{A, C, E, G\}$.
  - Étape 4 : Depuis cet arbre, arête min vers $\{D\}$ de poids 2 $\implies$ **$(G, D)$ retenue**, arbre $\{A, C, E, G, D\}$.
  - Étape 5 : Arête min vers $\{F\}$ : $(E, F)$ de poids 4 $\implies$ **$(E, F)$ retenue**, arbre $\{A, C, E, G, D, F\}$.
  - Étape 6 : Arête min vers $\{B\}$ : $(A, B)$ ou $(C, B)$ de poids 7 $\implies$ **$(A, B)$ retenue**, tous les sommets sont couverts.

### 3. Poids Total et Unicité
- **Poids de l'ACPM :**
  $$W = 2 + 3 + 4 + 5 + 5 + 7 = 26 \text{ (soit } 260\,000 \text{ €)}$$
- **Unicité :** En raison de l'égalité de poids entre $(A, B)$ et $(B, C)$ (poids 7), l'arête $(B, C)$ aurait pu être sélectionnée à la place de $(A, B)$ pour relier le sommet $B$ avec le même coût global ($W = 26$). **L'arbre couvrant minimal n'est donc pas strictement unique**.

---

## 📌 Exercice 4 – Dépendances et Chemin Critique dans un DAG (PERT)

Projet à 7 tâches $\{T_1, \dots, T_7\}$ avec contraintes de précédence.

```
          [T2] (3j) ── 2j ──> [T4] ── 4j ──┐
         ^    \                            │
        /      \ 5j                        v
      3j        v                         [T6] ── 2j ──> [T7]
      /         [T5] ───────── 3j ────────> ^
     /          ^                          │
   [T1] ── 4j ──> [T3] ──────── 6j ────────┘
```

### 1. Tri Topologique
- **Définition :** Un ordre linéaire des sommets tel que pour tout arc $(u, v)$, $u$ précède $v$. Il existe si et seulement si le graphe est un **DAG** (orienté et sans circuit).
- **Ordre valide par DFS :** $T_1 \to T_2 \to T_3 \to T_4 \to T_5 \to T_6 \to T_7$.

### 2. Dates et Chemin Critique

| Tâche | Durée propre / arc incident | Date au plus tôt ($ES$) | Date au plus tard ($LS$) | Marge totale ($LS - ES$) | Critique ? |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **$T_1$** | Début | **0** | **0** | 0 | **OUI** |
| **$T_2$** | $w(T_1, T_2) = 3$ | 3 | 5 | 2 | Non |
| **$T_3$** | $w(T_1, T_3) = 4$ | **4** | **4** | 0 | **OUI** |
| **$T_4$** | $w(T_2, T_4) = 2$ | 5 | 9 | 4 | Non |
| **$T_5$** | $\max(3+5, 4+6) = 10$ | **10** | **10** | 0 | **OUI** |
| **$T_6$** | $\max(5+4, 10+3) = 13$ | **13** | **13** | 0 | **OUI** |
| **$T_7$** | $13 + 2 = 15$ | **15** | **15** | 0 | **OUI** |

- **Durée minimale du projet :** **15 jours**.
- **Chemin critique :** **$T_1 \to T_3 \to T_5 \to T_6 \to T_7$**. Tout retard sur l'une de ces tâches retarde immédiatement la livraison finale.

### 3. Marge et Sensibilité aux Retards
- **Marge totale de $T_4$ :** $LS(T_4) - ES(T_4) = 9 - 5 = \mathbf{4\text{ jours}}$.
- **Retard imprévu de 2 jours sur $T_2$ :**
  La marge totale de $T_2$ est égale à $LS(T_2) - ES(T_2) = 5 - 3 = 2\text{ jours}$.
  Un retard de 2 jours consomme exactement la marge disponible sur cette branche sans la dépasser. La date au plus tôt d'entrée dans $T_5$ via $T_2$ deviendrait $3 + 2 + 5 = 10\text{ jours}$, ce qui coïncide avec le chemin critique passant par $T_3$ ($4 + 6 = 10$).
  **Conclusion formelle :** **La date de livraison finale du projet (15 jours) ne sera pas modifiée**.

---

## 📌 Exercice 5 – Routage Distribué à Vecteur de Distances

### 1. Convergence des Vecteurs de Distances
- **(a) État initial $D^A$ à $t = 0$ :**
  Le routeur $A$ ne connaît que lui-même et ses liaisons physiques directes :
  $$D^A = (d(A,A)=0, \, d(A,B)=1, \, d(A,C)=4, \, d(A,D)=\infty, \, d(A,E)=\infty)$$
- **(b) Formule de mise à jour de Bellman-Ford distribuée :**
  Pour toute destination $Y$, le routeur $A$ calcule :
  $$d(A, Y) = \min_{V \in \{B, C\}} \Big( c(A, V) + d(V, Y) \Big)$$
  où $c(A, V)$ est le coût de la liaison physique directe vers le voisin $V$.

### 2. Phénomène de Comptage à l'Infini (*Count-to-Infinity*)
- **(a) Dérive lors de la rupture de $\{A, B\}$ ($w(A,B) = \infty$) :**
  $A$ cherche une route alternative vers $B$. Son voisin $C$ lui annonce une distance vers $B$ de $2$ (qui transitait en réalité par $B$ directement). $A$ met à jour sa distance à $4 + 2 = 6$ via $C$. À l'échange suivant, $C$ voyant que $A$ a augmenté, réévalue sa propre distance à $6 + 2 = 8$, et ainsi de suite.
- **(b) Conséquence :** Les estimations augmentent à chaque échange périodique jusqu'à atteindre le seuil conventionnel d'infini (ex: 16 sauts dans RIP). Durant cette phase de convergence lente, des paquets bouclent entre $A$ et $C$, saturant les liens physiques.
- **(c) Mécanismes de remédiation :**
  - **Split Horizon (Horizon divisé) :** Interdit à un routeur d'annoncer une route vers une destination au voisin même par lequel cette route a été apprise.
  - **Poison Reverse (Empoisonnement de route) :** Le routeur réémet la route vers ce voisin, mais en lui affectant explicitement un coût infini ($\infty$), prévenant instantanément les boucles de rétroaction mutuelle.

### 3. Comparatif RIP (Vecteur de distances) vs OSPF (État de liens)

| Critère d'évaluation | Vecteur de Distances (ex: RIP) | État de Liens (ex: OSPF) |
| :--- | :--- | :--- |
| **Algorithme sous-jacent** | Bellman-Ford distribué | Dijkstra (calcul sur base topologique globale) |
| **Complexité temporelle** | Faible par nœud ($O(d)$), lente convergence globale | Plus élevée localement ($O(n \log n)$), quasi-instantanée globalement |
| **Trafic de contrôle échangé** | Périodique (envoi de toute la table aux voisins directs) | Événementiel par inondation (*LSA Flooding*) lors d'une modification |
| **Comportement en cas de panne** | Vulnérable au *Count-to-Infinity*, convergence lente | Réactivité immédiate, recalcul local sans boucle |
