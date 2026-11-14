### Exercice 1 – Maintenance d'un réseau

#### 1. Représentation et degrés des sommets

Le graphe non orienté $G = (V, E)$ comporte 5 sommets ($R_1, \dots, R_5$) et 6 arêtes :

```text
R1 --- R2
  \   /
   R3
  /   \
R4 --- R5
```

Degrés des sommets :
- $d(R_1) = 2$
- $d(R_2) = 2$
- $d(R_3) = 4$
- $d(R_4) = 2$
- $d(R_5) = 2$

*(Vérification : somme des degrés $= 12 = 2 \times 6$ arêtes.)*

#### 2. Parcours eulérien fermé

**Oui.** D'après le théorème d'Euler, un graphe non orienté connexe admet un cycle eulérien (parcours passant une seule fois par chaque arête et revenant au point de départ) si et seulement si tous ses sommets sont de degré pair. Ici, le graphe est connexe et tous les degrés ($2, 2, 4, 2, 2$) sont pairs.

Par exemple : $R_1 - R_2 - R_3 - R_4 - R_5 - R_3 - R_1$.

#### 3. Nature d'arbre

**Non.** Un arbre est un graphe connexe **sans cycle** (ou vérifiant $m = n - 1$). Ce graphe contient deux cycles ($R_1 - R_2 - R_3 - R_1$ et $R_3 - R_4 - R_5 - R_3$) et possède $m = 6$ arêtes pour $n = 5$ sommets ($6 \neq 5 - 1$).

#### 4. Réseau secondaire (forêt)

Une forêt est un graphe sans cycle dont chaque composante connexe est un arbre. Le réseau secondaire possède deux composantes connexes disjointes, toutes deux connexes et acycliques :
1. $S_1 - S_2 - S_3 - S_4$ ($4$ sommets, $3$ arêtes) ;
2. $S_5 - S_6$ ($2$ sommets, $1$ arête).

On a bien un graphe sans cycle (et $m = n - c \implies 4 = 6 - 2$). Il s'agit donc d'une **forêt** contenant **2 arbres**.

### Exercice 2 – Robot de diagnostic

#### 1. Graphe des déplacements possibles

Graphe non orienté à 5 sommets ($A, B, C, D, E$) et 7 arêtes :

```text
   A --- B
  / \   /|
 E   \ / |
  \   X  |
   \ / \ |
    D --- C
```

*(Arêtes : $A-B,\; B-C,\; C-D,\; D-E,\; E-A,\; A-C,\; B-D$.)*

#### 2. Possibilité de la tournée

**Oui.** Le robot peut suivre le parcours fermé :

$$A \to B \to C \to D \to E \to A$$

Chaque serveur est visité une seule fois avant le retour au point de départ $A$, en n'empruntant que des déplacements autorisés.

#### 3. Nom du parcours

Il s'agit d'un **cycle hamiltonien**.

### Exercice 3 – Planification de tâches

#### 1. Graphe des conflits

Graphe non orienté à 6 sommets ($A, B, C, D, E, F$) et 10 arêtes :

```text
      E
    /   \
   A --- B
   |\   /|
   | \ / |
   |  X  |
   | / \ |
   D --- C
    \   /
      F
```

- **Arêtes de $\{A, B, C, D\}$ (clique $K_4$) :** $AB, AC, AD, BC, BD, CD$
- **Arêtes de $E$ :** $EA, EB$
- **Arêtes de $F$ :** $FC, FD$

#### 2. Clique de taille 4 et signification

- **Clique :** $\{A, B, C, D\}$ (ces 4 sommets sont tous reliés deux à deux).
- **Contexte :** elle représente un groupe de 4 tâches toutes mutuellement en conflit ; aucune ne peut s'exécuter en même temps qu'une autre du groupe, ce qui impose **4 créneaux différents**.

#### 3. Nombre minimal de créneaux et affectation

Il faut prévoir au minimum **4 créneaux** :
- La clique $\{A, B, C, D\}$ interdit d'utiliser moins de 4 créneaux.
- 4 créneaux suffisent, car $E$ n'est en conflit qu'avec $A$ et $B$ (il peut donc partager le créneau de $C$ ou $D$), et $F$ n'est en conflit qu'avec $C$ et $D$ (il peut partager celui de $A$ ou $B$).

**Affectation possible :**
- **Créneau 1 :** $A, F$
- **Créneau 2 :** $B$
- **Créneau 3 :** $C, E$
- **Créneau 4 :** $D$

#### 4. Nombre chromatique

Le nombre chromatique de ce graphe est **$\chi(G) = 4$** (chaque créneau correspond à une couleur).