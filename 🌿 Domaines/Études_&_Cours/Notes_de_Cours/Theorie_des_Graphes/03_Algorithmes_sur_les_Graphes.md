---
type: note-cours
created: 2026-11-10
matiere: "Théorie des Graphes"
chapitre: "03 - Les Algorithmes sur les Graphes"
enseignant: "K. E. HOVI"
tags:
  - etudes
  - cours
  - theorie-des-graphes
  - algorithmique
  - bfs-dfs
  - dijkstra
  - bellman-ford
  - kruskal-prim
  - ford-fulkerson
  - active-recall
parent: "[[MOC_Theorie_des_Graphes]]"
---

# 📖 03. Algorithmes Majeurs sur les Graphes

> **Matière :** [[MOC_Theorie_des_Graphes|Théorie des Graphes (M1 IT)]] • **Date :** 10 Novembre 2026 • **Statut :** Synthétisé & Prêt pour révision active

---

## 🎯 1. Idées Clés & Thèses Centrales
Ce chapitre condense les algorithmes d'ingénierie et d'optimisation combinatoire sur réseaux :
- **Parcours structurants :** Le BFS procède par ondes concentriques via une file FIFO (optimalité géodésique non pondérée), tandis que le DFS explore en profondeur par pile récursive LIFO, produisant un parenthésage temporel $[d, f]$ indispensable à la classification des cycles et au tri topologique.
- **Routage et Plus courts chemins :** Dijkstra privilégie l'efficacité gloutonne sur métriques positives ($O((n+m)\log n)$), alors que Bellman-Ford résout par programmation dynamique les graphes avec pondérations négatives ($O(n \cdot m)$) et caractérise formellement les circuits absorbants.
- **Arbres Couvrants de Poids Minimum (ACPM) :** Kruskal déploie une stratégie gloutonne centrée sur les arêtes adossée à l'algèbre des ensembles disjoints (*Union-Find*), face à Prim qui procède par expansion centripète d'un arbre unique.
- **Théorie des Réseaux et Flots :** L'algorithme de Ford-Fulkerson et sa variante polynomiale d'Edmonds-Karp résolvent l'acheminement maximal à travers le réseau résiduel, scellant le théorème fondamental de dualité Flot-Max / Coupe-Min.

---

## 📝 2. Contenu Structuré & Démonstrations

### A. Parcours Fondamentaux : BFS et DFS

```
┌──────────────────────────────────────┬──────────────────────────────────────┐
│       BFS (Parcours en Largeur)      │      DFS (Parcours en Profondeur)    │
├──────────────────────────────────────┼──────────────────────────────────────┤
│ Structure : File FIFO                │ Structure : Pile LIFO (récursivité)  │
│ Exploration : Par couches / niveaux  │ Exploration : En profondeur & retour │
│ Objectif : Plus court chemin         │ Objectif : Détection de cycles,      │
│ géodésique non pondéré d[u]          │ classification d'arcs, tri topo      │
│ Complexité : O(|V| + |E|)            │ Complexité : O(|V| + |E|)            │
└──────────────────────────────────────┴──────────────────────────────────────┘
```

#### 1. BFS (Breadth-First Search)
- **États des sommets :** BLANC (non visité), GRIS (dans la file, en attente de traitement de ses voisins), NOIR (traité définitivement).
- **Invariants :** Pour tout sommet $u$, $d[u]$ est la distance géodésique minimale depuis la source $s$. L'arbre des prédécesseurs $\pi$ constitue l'arbre couvrant BFS.

#### 2. DFS (Depth-First Search) et Estampilles Temporelles
- **Estampilles :** À chaque sommet $u$ sont assignées la date de découverte $d[u]$ et la date de clôture $f[u]$ ($1 \le d[u] < f[u] \le 2|V|$).
- **Théorème des Intervalles (Parenthésage) :** Pour deux sommets $u$ et $v$, les intervalles $[d[u], f[u]]$ et $[d[v], f[v]]$ sont soit strictement disjoints, soit strictement imbriqués (signifiant une relation d'ascendance/descendance dans l'arbre DFS).
- **Classification des Arcs lors du DFS :**
  1. *Arcs d'arbre :* Menant vers un sommet BLANC (devient fils dans la forêt DFS).
  2. *Arcs arrière (Back edges) :* Menant vers un ancêtre GRIS $\implies$ **Présence formelle d'un cycle**.
  3. *Arcs avant (Forward edges) :* Menant vers un descendant NOIR.
  4. *Arcs croisés (Cross edges) :* Menant vers un sommet NOIR sans lien d'ascendance directe.

---

### B. Recherche de Plus Courts Chemins : Dijkstra vs Bellman-Ford

#### 1. Procédure de Relâchement (*Relaxation*)
L'invariant de mise à jour sur tout arc $(u, v)$ de poids $w(u, v)$ :
$$\text{Si } d[v] > d[u] + w(u, v) \implies d[v] \leftarrow d[u] + w(u, v) \quad \text{et} \quad \pi[v] \leftarrow u$$

#### 2. Algorithme de Dijkstra
- **Condition stricte :** Poids strictement positifs ou nuls ($\forall e \in E, w(e) \ge 0$).
- **Principe :** Stratégie gloutonne. On extrait à chaque pas le sommet $u \in Q$ minimisant $d[u]$, on l'insère dans l'ensemble $S$ des sommets résolus, puis on relâche tous ses voisins sortants.
- **Complexités temporelles comparées :**
  - Tableau direct : $O(|V|^2)$ (optimal pour graphe complet).
  - Tas binaire (*Binary Heap*) : $O((|V| + |E|)\log |V|)$.
  - Tas de Fibonacci : $O(|E| + |V|\log |V|)$ (optimal théorique).

#### 3. Algorithme de Bellman-Ford
- **Applicabilité :** Graphes orientés quelconques avec pondérations positives ou négatives.
- **Principe :** Programmation dynamique. Relâchement complet de **la totalité des $|E|$ arcs**, répété rigoureusement **$|V| - 1$ fois**.
- **Détection des circuits absorbants (poids strictement négatif) :**
  Lors d'une $|V|$-ième passe :
  $$\text{Si } \exists (u, v) \in E \text{ tel que } d[v] > d[u] + w(u, v) \implies \text{Présence d'un cycle négatif accessible}$$
- **Complexité :** $\Theta(|V| \cdot |E|)$.

---

### C. Arbres Couvrants de Poids Minimum (ACPM / MST)

Problème : Soit $G = (V, E)$ connexe valué non orienté. Trouver un arbre couvrant $T = (V, E_T)$ minimisant $w(T) = \sum_{e \in E_T} w(e)$.

#### 1. Algorithme de Kruskal & Algèbre *Union-Find*
- **Stratégie :** Glouton centré sur les arêtes.
- **Déroulement :**
  1. Trier l'ensemble $E$ par poids croissant ($O(|E|\log |E|)$).
  2. Initialiser chaque sommet dans son propre ensemble disjoint via `Créer-Ensemble(v)`.
  3. Parcourir les arêtes triées $(u, v)$ : si `Trouver-Ensemble(u)` $\ne$ `Trouver-Ensemble(v)`, l'arête ne crée pas de cycle ; elle est acceptée dans $E_T$ et l'on appelle `Union(u, v)`.
- **Complexité globale :** Avec compression de chemin et union par rang, les opérations Union-Find s'exécutent en $O(|E| \cdot \alpha(|V|))$. Le goulot d'étranglement est le tri initial, soit **$O(|E|\log |V|)$**.

#### 2. Algorithme de Prim
- **Stratégie :** Glouton centré sur les sommets.
- **Déroulement :** Fait croître un arbre unique depuis une racine $r$. À chaque étape, on sélectionne l'arête de poids minimal reliant un sommet déjà dans l'arbre à un sommet hors de l'arbre via une file de priorité min sur les sommets.
- **Complexité :** $O(|E|\log |V|)$ avec un tas binaire.

---

### D. Flots dans les Réseaux : Ford-Fulkerson & Théorème Min-Cut

#### 1. Modélisation d'un Réseau de Transport
Un quadruplet $\mathcal{N} = (G, c, s, t)$ avec :
- $s$ : source ($d^-(s) = 0$), $t$ : puits ($d^+(t) = 0$).
- $c(u, v) \ge 0$ : fonction de capacité.
- **Conditions de validité d'un flot $f$ :**
  1. Capacité : $0 \le f(u, v) \le c(u, v)$.
  2. Anti-symétrie : $f(u, v) = -f(v, u)$.
  3. Conservation du flot : $\forall u \in V \setminus \{s, t\}, \sum_{v} f(v, u) = \sum_{v} f(u, v)$.

#### 2. Réseau Résiduel $G_f$ et Chemin Augmentant
- **Capacité résiduelle :**
  $$c_f(u, v) = c(u, v) - f(u, v) \quad \text{et} \quad c_f(v, u) = f(u, v)$$
  *(L'arc résiduel inverse $(v, u)$ permet d'annuler ou rediriger un flux déjà engagé).*
- **Chemin augmentant $p$ :** Chemin simple orienté de $s$ à $t$ dans $G_f$ où chaque arc résiduel possède une capacité $c_f(u, v) > 0$.
- **Capacité goulot du chemin :** $c_f(p) = \min_{(u, v) \in p} c_f(u, v)$.

#### 3. Théorème Fondamental du Flot Maximal / Coupe Minimale
> [!IMPORTANT] Théorème de Ford-Fulkerson (Dualité)
> Dans tout réseau de transport, la valeur maximale d'un flot reliant $s$ à $t$ est égale à la capacité minimale d'une coupe séparant $s$ de $t$ :
> $$\max |f| = \min_{(S, T)} \text{cap}(S, T)$$
> Une coupe $(S, T)$ est une partition de $V$ telle que $s \in S$ et $t \in T$. Sa capacité est $\text{cap}(S, T) = \sum_{u \in S, v \in T} c(u, v)$.

- **Complexités :**
  - Ford-Fulkerson générique : $O(|E| \cdot |f_{\max}|)$ (peut ne pas terminer si capacités irrationnelles).
  - Algorithme d'Edmonds-Karp (sélection systématique du chemin augmentant de plus courte longueur par BFS) : $O(|V| \cdot |E|^2)$, polynomial strict.

---

## 🧠 3. Batterie d'Active Recall (Questions d'Auto-Évaluation)

- [ ] **Q1 : Pourquoi l'algorithme de Dijkstra échoue-t-il en présence d'arêtes à poids négatif ?**
  - *Réponse flash :* Dijkstra repose sur l'hypothèse gloutonne qu'une fois un sommet fixé dans l'ensemble $S$, sa distance ne pourra plus jamais décroître en allongeant le chemin. Un arc de poids négatif situé plus loin dans le graphe détruit cette monotonicité et invalide l'optimalité des distances déjà figées.
- [ ] **Q2 : Pourquoi Bellman-Ford requiert-il exactement $|V| - 1$ itérations de relaxation ?**
  - *Réponse flash :* Dans un graphe sans cycle négatif, un plus court chemin simple contient au plus $|V| - 1$ arcs. Chaque itération garantit la propagation optimale du plus court chemin sur au moins un arc supplémentaire de la chaîne.
- [ ] **Q3 : Quelle est la condition suffisante pour qu'un graphe admette un unique Arbre Couvrant de Poids Minimum ?**
  - *Réponse flash :* Si tous les poids des arêtes du graphe sont strictement distincts deux à deux, alors l'ACPM est strictement unique. Si des arêtes possèdent des poids identiques, plusieurs arbres de même coût minimal peuvent coexister.

---

## ⚡ 4. Devoirs, Lectures & Prochaines Actions
- [ ] Résoudre la [[TD3_Algorithmes_&_Routage|Feuille TD 3]] (Dijkstra, Bellman-Ford, Kruskal/Prim, DAG et PERT).
