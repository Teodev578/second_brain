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