---
type: note-cours
created: 2026-11-10
matiere: "Théorie des Graphes"
chapitre: "01 - Introduction, Définitions et Représentations des Graphes"
enseignant: "K. E. HOVI"
tags:
  - etudes
  - cours
  - theorie-des-graphes
  - matrices-adjacence
  - listes-adjacence
  - active-recall
parent: "[[MOC_Theorie_des_Graphes]]"
---

# 📖 01. Introduction, Définitions & Représentations des Graphes

> **Matière :** [[MOC_Theorie_des_Graphes|Théorie des Graphes (M1 IT)]] • **Date :** 10 Novembre 2026 • **Statut :** Synthétisé & Prêt pour révision active

---

## 🎯 1. Idées Clés & Thèses Centrales
Un graphe $G=(V, E)$ est une structure discrète modélisant des relations binaires au sein d'un ensemble fini d'entités. Ce premier chapitre établit la rigueur formelle de la discipline :
- La conservation structurelle des arêtes impose le **lemme des poignées de main** ($\sum d(v) = 2m$), d'où découle la parité obligatoire du nombre de sommets de degré impair.
- Le choix de représentation en mémoire (matrice d'adjacence en $O(n^2)$ versus listes d'adjacence en $O(n+m)$) conditionne drastiquement la complexité spatiale et temporelle des traitements algorithmiques selon la densité du réseau.
- L'algèbre linéaire s'articule directement avec la combinatoire des graphes : le coefficient $(i,j)$ de la puissance $p$-ième de la matrice d'adjacence ($M^p$) dénombre exactement les chemins de longueur $p$ entre $i$ et $j$.

---

## 📝 2. Contenu Structuré & Démonstrations

### A. Définitions Formelles et Typologie
Un graphe fini est un couple $G = (V, E)$ où :
- $V = \{v_1, \dots, v_n\}$ est l'ensemble fini des sommets (*vertices*), de cardinal $|V| = n$ désignant l'**ordre** du graphe.
- $E = \{e_1, \dots, e_m\}$ est l'ensemble fini des arêtes (*edges*) ou arcs, de cardinal $|E| = m$.

On distingue formellement :
1. **Graphe non orienté simple :** Chaque arête $e$ est une paire non ordonnée $\{a, b\}$ avec $a \ne b$. Il ne contient ni boucle (arête reliant un sommet à lui-même) ni arêtes parallèles multiples.
2. **Multigraphe :** Structure admettant des arêtes multiples entre une même paire de sommets (dans ce cas, $E$ est un multi-ensemble).
3. **Graphe orienté ($p$-graphe) :** Les connexions sont ordonnées sous forme d'arcs $(u, v)$ où $u$ est l'origine et $v$ l'extrémité. Un $1$-graphe admet au plus un arc orienté d'un sommet $u$ vers un sommet $v$.
4. **Graphe partiel vs Sous-graphe :**
   - *Graphe partiel :* Même ensemble de sommets $V$, mais un sous-ensemble d'arêtes $E' \subseteq E$.
   - *Sous-graphe induit :* Restriction à un sous-ensemble de sommets $V' \subset V$, conservant toutes les arêtes de $E$ dont les deux extrémités appartiennent à $V'$.
5. **Graphe complet ($K_n$) :** Graphe simple non orienté où chaque paire de sommets distincts est reliée par une arête. Le nombre total d'arêtes est :
   $$m = \binom{n}{2} = \frac{n(n-1)}{2}$$

---

### B. Adjacence, Voisinage et Degrés
- **Adjacence :**
  - Dans un graphe non orienté, $v_j \in \text{adj}(v_i) \iff (v_i, v_j) \in E$.
  - Dans un graphe orienté, on segmente les successeurs $\text{succ}(v_i) = \{v_j \mid (v_i, v_j) \in E\}$ et les prédécesseurs $\text{pred}(v_i) = \{v_j \mid (v_j, v_i) \in E\}$.
- **Degré d'un sommet :**
  - Non orienté : $d(v) = |\text{adj}(v)|$ (dans un multigraphe, une boucle ajoute 2 au degré).
  - Orienté : demi-degré extérieur $d^+(v) = |\text{succ}(v)|$ et demi-degré intérieur $d^-(v) = |\text{pred}(v)|$. Le degré total vaut $d(v) = d^+(v) + d^-(v)$.
- **Graphe régulier :** Un graphe est $k$-régulier si $\forall v \in V, d(v) = k$.
- **Degré d'un graphe :** $\Delta(G) = \max_{v \in V} d(v)$. Le degré minimal est noté $\delta(G) = \min_{v \in V} d(v)$.

---

### C. Théorème Fondamental : Lemme des Poignées de Main
> [!IMPORTANT] Théorème des Degrés (Euler)
> Pour tout graphe non orienté $G = (V, E)$ :
> $$\sum_{v \in V} d(v) = 2|E| = 2m$$

**Démonstration :**
Chaque arête relie exactement deux sommets. Lors du calcul de la somme des degrés, chaque arête est comptabilisée exactement deux fois (une fois à chaque extrémité). La somme est donc nécessairement un entier pair.

**Corollaire immédiat :**
Dans tout graphe, **le nombre de sommets de degré impair est pair**.
*Preuve :* Partitionnons $V$ en sommets de degrés pairs $V_{\text{pair}}$ et impairs $V_{\text{impair}}$ :
$$\sum_{v \in V} d(v) = \sum_{u \in V_{\text{pair}}} d(u) + \sum_{w \in V_{\text{impair}}} d(w) = 2m$$
Comme $\sum_{u \in V_{\text{pair}}} d(u)$ est paire et que $2m$ est pair, la somme $\sum_{w \in V_{\text{impair}}} d(w)$ est obligatoirement paire. La somme d'un ensemble de nombres impairs n'étant paire que si leur effectif est pair, le cardinal $|V_{\text{impair}}|$ est pair.

---

### D. Chaînes, Chemins et Cycles
- **Chaîne (non orienté) / Chemin (orienté) :** Séquence ordonnée de sommets $(v_0, v_1, \dots, v_k)$ telle que $(v_i, v_{i+1}) \in E$ pour tout $0 \le i < k$. La longueur est le nombre d'arêtes $k$.
- **Chaîne simple :** Ne contient aucune arête répétée.
- **Chaîne élémentaire :** Ne contient aucun sommet répété.
- **Cycle :** Chaîne fermée ($v_0 = v_k$) élémentaire, de longueur $k \ge 3$.

---

### E. Représentations en Machine et Arbitrages Techniques

#### 1. Matrice d'Adjacence
Matrice binaire $M \in \{0, 1\}^{n \times n}$ définie par :
$$M[i][j] = \begin{cases} 1 & \text{si } (v_i, v_j) \in E \\ 0 & \text{sinon} \end{cases}$$
- **Propriétés :**
  - Graphe non orienté : $M$ est symétrique ($M = M^T$).
  - Graphe valué : coefficients égaux au poids $w(i,j)$, ou $\infty / 0$ en l'absence d'arête.
  - Calcul des degrés : $d^+(v_i) = \sum_j M[i][j]$ et $d^-(v_i) = \sum_j M[j][i]$.
- **Théorème des Puissances :**
  > Le nombre de chemins de longueur $p$ reliant le sommet $i$ au sommet $j$ est donné par le coefficient $(M^p)_{i,j}$.

#### 2. Listes d'Adjacence
Tableau $T$ de $n$ listes chaînées où l'entrée $T[u]$ énumère les voisins ou successeurs directs de $u$.

#### 3. Tableau Comparatif d'Efficacité Asymptotique

| Critère / Opération | Matrice d'Adjacence ($M$) | Listes d'Adjacence ($L$) | Justification & Préconisation |
| :--- | :--- | :--- | :--- |
| **Espace mémoire** | $\Theta(n^2)$ | $\Theta(n + m)$ | Liste optimale si graphe creux ($m \ll n^2$) ; matrice compétitive si dense ($m \approx n^2$). |
| **Tester l'existence de $(u, v)$** | $O(1)$ | $O(d(u))$ | Accès direct par indexation matricielle. |
| **Énumérer les voisins de $u$** | $\Theta(n)$ | $\Theta(d(u))$ | La matrice contraint à scanner toute la ligne. |
| **Degré sortant $d^+(u)$** | $\Theta(n)$ | $O(1)$ ou $O(d^+(u))$ | Immédiat par la taille de la liste chaînée. |
| **Degré entrant $d^-(u)$** | $\Theta(n)$ | $\Theta(n + m)$ | La liste standard nécessite un parcours global (sauf liste miroir inverse). |

---

## 🧠 3. Batterie d'Active Recall (Questions d'Auto-Évaluation)

- [ ] **Q1 : Pourquoi un graphe simple d'ordre $n \ge 2$ contient-il nécessairement au moins deux sommets de même degré ?**
  - *Réponse flash :* Les degrés possibles appartiennent à $\{0, 1, \dots, n-1\}$, soit $n$ valeurs. Or les degrés $0$ (sommet isolé) et $n-1$ (connecté à tous) sont mutuellement exclusifs. Il n'y a donc qu'au plus $n-1$ degrés distincts pour $n$ sommets. Par le principe des tiroirs de Dirichlet, deux sommets partagent le même degré.
- [ ] **Q2 : Quelle est la signification algébrique de la trace de la matrice $M^3$ (notée $\text{Tr}(M^3)$) pour un graphe non orienté ?**
  - *Réponse flash :* Le terme $(M^3)_{i,i}$ donne le nombre de cycles fermés de longueur 3 partant et revenant en $i$. Chaque triangle est comptabilisé $3 \times 2 = 6$ fois (3 choix de point de départ et 2 sens de parcours). Le nombre de triangles vaut donc $\frac{1}{6} \text{Tr}(M^3)$.
- [ ] **Q3 : Dans un réseau WAN de 100 000 routeurs où chaque routeur est lié en moyenne à 4 voisins, pourquoi la matrice d'adjacence est-elle formellement proscrite ?**
  - *Réponse flash :* L'espace de la matrice requiert $100\,000^2 = 10^{10}$ cases (soit environ 10 Go en binaire), alors que la liste d'adjacence ne stocke que $V + 2E \approx 100\,000 + 400\,000 = 500\,000$ nœuds (quelques mégaoctets).

---

## ⚡ 4. Devoirs, Lectures & Prochaines Actions
- [ ] Résoudre la totalité de la [[TD1_Introduction_&_Representations|Feuille TD 1]].
- [ ] Enchaîner avec le chapitre [[02_Proprietes_Fondamentales_des_Graphes|02. Propriétés Fondamentales des Graphes]].
