---
type: note-cours
created: 2026-11-23
matiere: "Statistiques Inférentielles"
chapitre: "05 - Tests Non Paramétriques"
enseignant: "K. E. HOVI"
tags:
  - etudes
  - cours
  - statistiques-inferentielles
  - tests-non-parametriques
  - khi-deux
  - mann-whitney
  - wilcoxon
  - active-recall
parent: "[[MOC_Statistiques_Inferentielles]]"
---

# 📖 05. Tests Non Paramétriques

> **Matière :** [[MOC_Statistiques_Inferentielles|Statistiques Inférentielles (M1 IT)]] • **Date :** 23 Novembre 2026 • **Statut :** Synthétisé & Prêt pour révision active

---

## 🎯 1. Idées Clés & Thèses Centrales
Les tests non paramétriques (*distribution free*) s'affranchissent de toute hypothèse de normalité sur les populations mères :
- **Substitution par les rangs :** Pour les variables quantitatives ou ordinales, les valeurs brutes sont remplacées par leurs rangs, rendant ces tests **robustes aux valeurs aberrantes (*outliers*)** et applicables sur de très petits échantillons.
- **Trois piliers du programme :** Le **$\chi^2$ d'indépendance** (variables qualitatives / tables de contingence), **Mann-Whitney** (2 groupes indépendants), et **Wilcoxon** (2 groupes appariés).
- **Arbitrage puissance / validité :** Moins puissants qu'un test paramétrique lorsque la normalité est vérifiée, mais indispensables (et parfois *plus* puissants) dès que les distributions sont asymétriques, ordinales ou polluées par des *outliers*.

---

## 📝 2. Contenu Structuré & Démonstrations

### A. Correspondance Paramétrique vs Non Paramétrique

```text
┌───────────────────────────────────────┬──────────────────────────┬────────────────────────────┐
│ Situation / Protocole expérimental    │ Test Paramétrique        │ Test Non Paramétrique      │
├───────────────────────────────────────┼──────────────────────────┼────────────────────────────┤
│ 2 groupes indépendants                │ Student / Welch (t)      │ Mann-Whitney (U)           │
│ 2 groupes appariés (avant / après)    │ Student apparié (t)      │ Rangs signés Wilcoxon (W)  │
│ K ≥ 3 groupes indépendants            │ ANOVA à un facteur (F)   │ Kruskal-Wallis (H)         │
│ Variables qualitatives (contingence)  │ — (non applicable)       │ Chi-Deux d'indépendance    │
└───────────────────────────────────────┴──────────────────────────┴────────────────────────────┘
```

---

### B. Test d'Indépendance du $\chi^2$ (Deux Variables Qualitatives)

Pour deux variables $X$ ($l$ modalités) et $Y$ ($k$ modalités), on teste $H_0 :$ « $X$ et $Y$ sont indépendantes ».
- **Effectifs marginaux :** $S_i = \sum_{j=1}^k n_{i,j}$ (ligne $i$), $T_j = \sum_{i=1}^l n_{i,j}$ (colonne $j$), total $n$.
- **Effectifs théoriques sous $H_0$ :** $C_{i,j} = \frac{S_i \, T_j}{n}$.
- **Statistique du $\chi^2$ :**
  $$\chi_c^2 = \sum_{i=1}^l \sum_{j=1}^k \frac{(n_{i,j} - C_{i,j})^2}{C_{i,j}} \xrightarrow{\text{sous } H_0} \chi^2\big((l - 1)(k - 1)\big)$$
- **Condition d'application a posteriori :** **$C_{i,j} \ge 5$ pour toutes les cases** *(sinon regrouper des modalités adjacentes)*.
- **Décision :** Si $\chi_c^2 \ge \chi^2_{1-\alpha}(\nu)$ (où $\nu = (l-1)(k-1)$), on rejette $H_0$ ; si $\chi_c^2 < \chi^2_{1-\alpha}(\nu)$, on ne rejette pas $H_0$.

**Exemple du cours (Médicament vs Générique, $n = 256$) :**
- Effectifs observés $(48, 6)$ et $(158, 44)$ $\implies$ attendus $(43{,}45; 10{,}55)$ et $(162{,}55; 39{,}45)$ (tous $\ge 5$).
- $\chi_c^2 \simeq 3{,}1 < \chi^2_{0{,}05}(1) = 3{,}8415$ $\implies$ on ne rejette pas $H_0$ (taux de guérison indépendant du choix de médicament).

---

### C. Test de Mann-Whitney (2 Échantillons Indépendants)

Compare deux échantillons indépendants $x_1, \dots, x_{n_1}$ et $y_1, \dots, y_{n_2}$ ($N = n_1 + n_2$) sous $H_0 : F_X = F_Y$.

1. **Méthode par comptage de couples :** $U_{n_1, n_2} = \sum_{i=1}^{n_1} \sum_{j=1}^{n_2} \mathbf{1}_{\{x < y\}}(X_i, Y_j)$ (1 si $X_i < Y_j$, $0{,}5$ si égalité).
2. **Méthode par classement conjoint des rangs (plus rapide) :** On classe toutes les $N$ valeurs ensemble par ordre croissant (rang moyen en cas d'ex-æquo). Soient $R_1$ et $R_2$ les sommes des rangs des deux groupes :
   $$U_1 = R_1 - \frac{n_1(n_1 + 1)}{2}, \qquad U_2 = R_2 - \frac{n_2(n_2 + 1)}{2}$$
   **Invariant de vérification :** $R_1 + R_2 = \frac{N(N+1)}{2}$ et **$U_1 + U_2 = n_1 n_2$**.
3. **Règle de décision (bilatérale) :** On retient $u = \min(u_1, u_2)$. On **rejette $H_0$ si $u \le m_\alpha$** (i.e. $u \in [0; m_\alpha]$).
4. **Approximation normale (grands échantillons) :**
   $$E(U) = \frac{n_1 n_2}{2}, \qquad \text{Var}(U) = \frac{n_1 n_2 (n_1 + n_2 + 1)}{12}, \qquad Z = \frac{U - \frac{n_1 n_2}{2}}{\sqrt{\text{Var}(U)}} \approx \mathcal{N}(0, 1)$$

---

### D. Test des Rangs Signés de Wilcoxon (2 Échantillons Appariés)

Compare deux mesures appariées (ex. Avant / Après). Plus puissant que le test des signes car il pondère par l'amplitude des écarts.

1. **Calcul des différences :** $d_i = X_i - Y_i$. On **supprime toutes les paires où $d_i = 0$**, pour conserver $n$ paires non nulles.
2. **Classement des $|d_i|$ :** On attribue les rangs $r_i \in \{1, \dots, n\}$ aux valeurs absolues $|d_i|$ par ordre croissant (rang moyen aux ex-æquo).
3. **Statistique de Wilcoxon :**
   $$W = \min\!\left(\sum_{d_i > 0} r_i, \; \sum_{d_i < 0} r_i\right)$$
   *(Vérification : $\sum_{d_i > 0} r_i + \sum_{d_i < 0} r_i = \frac{n(n+1)}{2}$.)*
4. **Règle de décision :**
   - *Petits échantillons ($n \le 25$) :* En test bilatéral, on **rejette $H_0$ si $W \le W_{\alpha/2}$** (ou $W < W_{\alpha/2}$ selon la table ; la zone de non-rejet est $]W_{\alpha/2}, \, W_{1-\alpha/2}[$).
   > [!WARNING] Coquille d'impression dans le polycopié (p. 32)
   > Le support écrit à la première ligne de la règle « On peut rejeter $H_0$ si $W \in ]W_{\alpha/2}, W_{1-\alpha/2}[$ », puis indique correctement la ligne suivante : **« on rejette $H_0$ lorsque $W < W_{\alpha/2}$ dans le cas bilatéral »**. Retenir que le rejet se produit pour les **petites valeurs** de $W$ ($W \le W_{\text{crit}}$).
   - *Grands échantillons ($n > 25$) :*
     $$Z = \frac{W - \frac{n(n+1)}{4}}{\sqrt{\frac{n(n+1)(2n+1)}{24}}} \leadsto \mathcal{N}(0, 1)$$

**Exemple résolu du cours (Bière locale vs importée, 10 étudiants) :**
Différences : $-4, -2, 1, 0, 2, -4, -6, -2, 1, -3$. Suppression du $0$ $\implies n = 9$.
Tri de $|d_i|$ : $1, 1, 2, 2, 2, 3, 4, 4, 6 \implies$ rangs moyens $1{,}5; 1{,}5; 4; 4; 4; 6; 7{,}5; 7{,}5; 9$.
$\sum_{d_i>0} r_i = 1{,}5 + 1{,}5 + 4 = 7$ ; $\sum_{d_i<0} r_i = 4 + 4 + 6 + 7{,}5 + 7{,}5 + 9 = 38$.
$W = \min(7, 38) = 7 \le W_{0{,}05} = 8$ (unilatéral) $\implies$ **rejet de $H_0$** (préférence significative pour la bière importée).

---

## 🧠 3. Batterie d'Active Recall (Questions d'Auto-Évaluation)

- [ ] **Q1 : Quelles sont les deux conditions/vérifications clés du test d'indépendance du $\chi^2$, et comment y remédier si l'une échoue ?**
  - *Réponse flash :* Tous les effectifs **théoriques** (et non observés !) $C_{i,j}$ doivent vérifier $C_{i,j} \ge 5$, et les observations doivent être indépendantes. Si certains $C_{i,j} < 5$, on regroupe des classes/modalités adjacentes (ce qui diminue le nombre de ddl).
- [ ] **Q2 : Dans le test de Mann-Whitney, comment contrôler rapidement qu'on n'a commis aucune erreur de rangs ?**
  - *Réponse flash :* Vérifier les deux invariants algébriques : $R_1 + R_2 = \frac{N(N+1)}{2}$ (somme de tous les rangs) et $U_1 + U_2 = n_1 n_2$.
- [ ] **Q3 : Quelle différence entre Mann-Whitney et Wilcoxon dans la manière d'attribuer les rangs ?**
  - *Réponse flash :* **Mann-Whitney** classe conjointement les $n_1 + n_2$ **valeurs brutes** des deux groupes indépendants. **Wilcoxon** calcule d'abord les différences appariées $d_i$, écarte les zéros, puis classe les **valeurs absolues $|d_i|$**.
- [ ] **Q4 : Pourquoi rejette-t-on $H_0$ quand $U$ ou $W$ sont *petits* (inférieurs au seuil critique) plutôt que grands ?**
  - *Réponse flash :* Car on définit $U = \min(U_1, U_2)$ et $W = \min(W^+, W^-)$. Si un groupe domine systématiquement l'autre (ou si les différences ont presque toutes le même signe), l'un des deux termes devient proche de zéro : c'est donc une valeur très petite du minimum qui témoigne d'un écart à $H_0$.

---

## ⚡ 4. Devoirs, Lectures & Prochaines Actions
- [ ] Mettre en pratique sur la [[TD2_Tests_Hypotheses|Feuille TD 2 (Exercices 5, 10, 13, 14, 15 et 16)]].
- [ ] Enchaîner avec le chapitre [[06_Correlation_et_Regression_Lineaire|06. Corrélation et Régression Linéaire]].
