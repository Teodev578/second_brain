---
type: note-cours
created: 2026-11-23
matiere: "Statistiques Inférentielles"
chapitre: "04 - Les Tests Paramétriques"
enseignant: "K. E. HOVI"
tags:
  - etudes
  - cours
  - statistiques-inferentielles
  - tests-parametriques
  - student
  - anova
  - fisher
  - active-recall
parent: "[[MOC_Statistiques_Inferentielles]]"
---

# 📖 04. Les Tests Paramétriques

> **Matière :** [[MOC_Statistiques_Inferentielles|Statistiques Inférentielles (M1 IT)]] • **Date :** 23 Novembre 2026 • **Statut :** Synthétisé & Prêt pour révision active

---

## 🎯 1. Idées Clés & Thèses Centrales
Ce chapitre regroupe l'ensemble des tests classiques reposant sur la normalité (exacte ou asymptotique par TCL) :
- **Un échantillon :** Le test de la moyenne bascule de $\mathcal{N}(0,1)$ ($\sigma$ connu ou $n \ge 30$) à Student $t(n-1)$ ($\sigma$ inconnu sous normalité) ; le test de la variance suit un $\chi^2$ ($n$ ddl si $\mu$ connue, $n-1$ si $\mu$ inconnue) ; le test de fréquence s'appuie sur l'approximation normale.
- **Deux échantillons :** Les séries appariées ($n_1=n_2$) se ramènent à un test sur une moyenne nulle des différences $Z_i = X_i - Y_i$. Pour deux échantillons indépendants, la comparaison de variances utilise Fisher-Snedecor ($\mathcal{F}(n_1-1, n_2-1)$), ce qui oriente ensuite le choix du test sur les moyennes (Z, Student poolé, ou Welch).
- **Comparaison de $k \ge 3$ moyennes (ANOVA) :** L'analyse de la variance évite l'inflation du risque $\alpha$ due aux tests $t$ multiples en comparant le ratio de la variabilité *inter-groupes* sur la variabilité *intra-groupes* via la loi $\mathcal{F}(k-1, N-k)$.

---

## 📝 2. Contenu Structuré & Démonstrations

### A. Tableau Synthétique d'Orientation (Tests Paramétriques)

| Objectif / Hypothèse $H_0$ | Cadre d'application | Statistique de test | Loi sous $H_0$ | Région de rejet (bilatérale au risque $\alpha$) |
| :--- | :--- | :--- | :---: | :--- |
| **Moyenne :** $\mu = \mu_0$ | $\sigma$ connu (ou grand $n$) | $Z = \frac{\overline{X}_n - \mu_0}{\sigma / \sqrt{n}}$ | $\mathcal{N}(0, 1)$ | $]-\infty; -z_{1-\alpha/2}[ \cup ]z_{1-\alpha/2}; +\infty[$ |
| **Moyenne :** $\mu = \mu_0$ | $\sigma$ inconnu, $X \sim \mathcal{N}$ | $T = \frac{\overline{X}_n - \mu_0}{S_n / \sqrt{n}}$ | $t(n-1)$ | $]-\infty; -t_{n-1, 1-\alpha/2}[ \cup ]t_{n-1, 1-\alpha/2}; +\infty[$ |
| **Variance :** $\sigma^2 = \sigma_0^2$ | $X \sim \mathcal{N}$, $\mu$ connue | $V = \frac{n\overline{S}_n^2}{\sigma_0^2}$ | $\chi^2(n)$ | $[0; \chi^2_{\alpha/2}(n)[ \cup ]\chi^2_{1-\alpha/2}(n); +\infty[$ |
| **Variance :** $\sigma^2 = \sigma_0^2$ | $X \sim \mathcal{N}$, $\mu$ inconnue | $V = \frac{(n-1)S_n^{\prime\,2}}{\sigma_0^2}$ | $\chi^2(n-1)$ | $[0; \chi^2_{\alpha/2}(n-1)[ \cup ]\chi^2_{1-\alpha/2}(n-1); +\infty[$ |
| **Proportion :** $p = p_0$ | $n$ grand ($np_0, nq_0 \ge 5$) | $Z = \frac{f - p_0}{\sqrt{p_0(1-p_0)/n}}$ | $\mathcal{N}(0, 1)$ | $]-\infty; -z_{1-\alpha/2}[ \cup ]z_{1-\alpha/2}; +\infty[$ |
| **2 Moyennes ($\sigma$ connues) :** $\mu_1=\mu_2$ | Éch. indépendants | $U = \frac{\overline{X}_{n_1} - \overline{Y}_{n_2}}{\sqrt{\sigma_1^2/n_1 + \sigma_2^2/n_2}}$ | $\mathcal{N}(0, 1)$ | $]-\infty; -z_{1-\alpha/2}[ \cup ]z_{1-\alpha/2}; +\infty[$ |
| **2 Moyennes ($\sigma$ inconnues) :** $\mu_1=\mu_2$ | $n_1 > 30$ et $n_2 > 30$ | $N = \frac{\overline{X}_{n_1} - \overline{Y}_{n_2}}{\sqrt{S_{n_1}^{\prime\,2}/n_1 + S_{n_2}^{\prime\,2}/n_2}}$ | $\mathcal{N}(0, 1)$ | $]-\infty; -z_{1-\alpha/2}[ \cup ]z_{1-\alpha/2}; +\infty[$ |
| **2 Moyennes ($\sigma_1=\sigma_2$) :** $\mu_1=\mu_2$ | $n_1$ ou $n_2 < 30$, homoscéd. | $T = \frac{\overline{X}_{n_1} - \overline{Y}_{n_2}}{\sqrt{S_{n_1, n_2}^{\prime\,2}(1/n_1 + 1/n_2)}}$ | $t(n_1 + n_2 - 2)$ | $]-\infty; -t_{1-\alpha/2}[ \cup ]t_{1-\alpha/2}; +\infty[$ |
| **2 Moyennes ($\sigma_1 \ne \sigma_2$) :** $\mu_1=\mu_2$ | $n_1$ ou $n_2 < 30$, hétéroscéd. | $T = \frac{\overline{X}_{n_1} - \overline{Y}_{n_2}}{\sqrt{S_{n_1}^{\prime\,2}/n_1 + S_{n_2}^{\prime\,2}/n_2}}$ | $t(\nu)$ (Welch) | $]-\infty; -t_{\nu, 1-\alpha/2}[ \cup ]t_{\nu, 1-\alpha/2}; +\infty[$ |
| **2 Variances :** $\sigma_1^2 = \sigma_2^2$ | Éch. normaux indépendants | $F = S_{n_1}^{\prime\,2} / S_{n_2}^{\prime\,2}$ | $\mathcal{F}(n_1-1, n_2-1)$ | $[0; f_{\alpha/2}[ \cup ]f_{1-\alpha/2}; +\infty[$ |
| **2 Proportions :** $p_1 = p_2$ | Grands échantillons | $Z = \frac{f_1 - f_2}{\sqrt{F(1-F)(1/n_1+1/n_2)}}$ | $\mathcal{N}(0, 1)$ | $]-\infty; -z_{1-\alpha/2}[ \cup ]z_{1-\alpha/2}; +\infty[$ |
| **$k$ Moyennes (ANOVA) :** $\mu_1=\dots=\mu_k$ | Normalité & homoscéd. | $F = \text{CM}_{\text{inter}} / \text{CM}_{\text{intra}}$ | $\mathcal{F}(k-1, N-k)$ | $]F_{1-\alpha}(k-1, N-k); +\infty[$ |

> [!WARNING] Vigilance — Coquilles d'impression dans le polycopié (Chapitre 4)
> 1. **Signes moins manquants (p. 24-25) :** Dans les régions de rejet bilatérales des sections 4.4.1 et 4.4.2, le PDF imprime $]-\infty, q_{1-\alpha/2}[ \cup ]q_{1-\alpha/2}, +\infty[$ au lieu de $]-\infty, \mathbf{-}q_{1-\alpha/2}[ \cup ]q_{1-\alpha/2}, +\infty[$ (idem pour $z_{1-\alpha/2}$ et $t_{1-\alpha/2}$).
> 2. **Degrés de liberté de Fisher (section 4.5, p. 26) :** La loi sous $H_0$ du rapport de variances est $\mathcal{F}(n_1 - \mathbf{1}, \, n_2 - 1)$ (et non $n_1 - 2$).
> 3. **Dénominateur de Welch (Cas 3, p. 25) :** La formule exacte des ddl de Welch-Satterthwaite divise chaque carré d'erreur standard par son propre $n_i - 1$ :
>    $$\nu = \frac{\left(S_{n_1}^{\prime\,2}/n_1 + S_{n_2}^{\prime\,2}/n_2\right)^2}{\dfrac{(S_{n_1}^{\prime\,2}/n_1)^2}{n_1 - 1} + \dfrac{(S_{n_2}^{\prime\,2}/n_2)^2}{n_2 - 1}}$$

---

### B. Détails sur la Comparaison de Deux Moyennes et Deux Proportions

1. **Échantillons appariés :** On pose $Z_i = X_i - Y_i$ pour chaque paire $i \in \{1, \dots, n\}$, puis on réalise un test de conformité à une moyenne $\mu_Z = 0$ (Student à $n - 1$ ddl).
2. **Variance poolée (Cas 2, $\sigma_1 = \sigma_2$) :**
   $$S_{n_1, n_2}^{\prime\,2} = \frac{1}{n_1 + n_2 - 2}\left(\sum_{k=1}^{n_1}(X_k - \overline{X}_{n_1})^2 + \sum_{k=1}^{n_2}(Y_k - \overline{Y}_{n_2})^2\right) = \frac{(n_1-1)S_{n_1}^{\prime\,2} + (n_2-1)S_{n_2}^{\prime\,2}}{n_1 + n_2 - 2}$$
3. **Proportion poolée (Comparaison de 2 proportions, section 4.7) :** Sous $H_0 : p_1 = p_2 = p$, le meilleur estimateur commun de $p$ est la moyenne pondérée :
   $$F = \frac{n_1 f_1 + n_2 f_2}{n_1 + n_2}$$

---

### C. Analyse de la Variance à un Facteur (ANOVA)

#### 1. Hypothèses et logique
Pour $k$ groupes ($N = \sum_{j=1}^k n_j$), on teste $H_0 : \mu_1 = \mu_2 = \dots = \mu_k$ contre $H_1 :$ au moins une moyenne diffère.
- **3 conditions de validité :** (1) indépendance des observations, (2) normalité approximative dans chaque groupe, (3) homogénéité des variances (homoscédasticité).
- **Décomposition de la variation totale :**
  $$\text{SC}_{\text{totale}} = \text{SC}_{\text{inter}} + \text{SC}_{\text{intra}}$$
  $$\text{avec} \quad \text{SC}_{\text{inter}} = \sum_{j=1}^k n_j (\bar{x}_j - \bar{x}_T)^2, \qquad \text{SC}_{\text{intra}} = \sum_{j=1}^k \sum_{i=1}^{n_j} (x_{ij} - \bar{x}_j)^2$$

#### 2. Tableau ANOVA Standard

| Source de variation | Somme des carrés (SC) | Degrés de liberté (ddl) | Carré moyen (CM) | Statistique $F$ |
| :--- | :---: | :---: | :---: | :---: |
| **Inter-groupes (Facteur)** | $\text{SC}_{\text{inter}}$ | $k - 1$ | $\text{CM}_{\text{inter}} = \frac{\text{SC}_{\text{inter}}}{k - 1}$ | $F = \dfrac{\text{CM}_{\text{inter}}}{\text{CM}_{\text{intra}}}$ |
| **Intra-groupes (Résiduelle)** | $\text{SC}_{\text{intra}}$ | $N - k$ | $\text{CM}_{\text{intra}} = \frac{\text{SC}_{\text{intra}}}{N - k}$ | |
| **Totale** | $\text{SC}_{\text{totale}}$ | $N - 1$ | | |

- Sous $H_0$, $F \sim \mathcal{F}(k - 1, \, N - k)$. Si $F \approx 1$, l'effet du facteur est nul ; si $F > F_{1-\alpha}(k-1, N-k)$ (soit $p\text{-value} \le \alpha$), on rejette $H_0$.

#### 3. Application résolue (Exemple 4.6.1 du cours — 3 régimes, $n_j = 5$)
- Moyennes : $\bar{x}_A = 191{,}6$, $\bar{x}_B = 217{,}6$, $\bar{x}_C = 178{,}4$, moyenne globale $\bar{x}_T = \frac{2938}{15} \approx 195{,}8667$.
- $\text{SC}_{\text{inter}} \approx 3977{,}841$ ($\text{ddl} = 2 \implies \text{CM}_{\text{inter}} = 1988{,}9205$).
- $\text{SC}_{\text{intra}} = 141{,}2 + 125{,}2 + 29{,}2 = 295{,}6$ ($\text{ddl} = 12 \implies \text{CM}_{\text{intra}} = 24{,}6333$).
- $F_{\text{obs}} = \frac{1988{,}9205}{24{,}6333} \approx 80{,}74 \gg F_{0{,}05}(2, 12) = 3{,}89$ (le support arrondit à $80{,}71$). **Rejet net de $H_0$**.

---

## 🧠 3. Batterie d'Active Recall (Questions d'Auto-Évaluation)

- [ ] **Q1 : Pourquoi privilégier une ANOVA à une série de tests $t$ deux à deux pour comparer 4 algorithmes ?**
  - *Réponse flash :* Avec 4 groupes, il faudrait $\binom{4}{2} = 6$ tests $t$, ce qui ferait exploser le risque global de faux positif (à $1 - (1 - 0{,}05)^6 \approx 26{,}5\%$ au lieu de $5\%$). L'ANOVA contrôle ce risque global à $\alpha$ en un seul test.
- [ ] **Q2 : Quand choisit-on la variance poolée vs la correction de Welch pour comparer deux moyennes à petits effectifs ?**
  - *Réponse flash :* On teste d'abord l'homoscédasticité via le test de Fisher ($F = s_1^2 / s_2^2$). Si les variances peuvent être considérées égales ($\sigma_1^2 = \sigma_2^2$), on utilise le test de Student à variance poolée ($n_1+n_2-2$ ddl) ; sinon, on utilise le test de Welch à ddl réduits $\nu$.
- [ ] **Q3 : Dans le test de comparaison de deux proportions, pourquoi calcule-t-on une proportion poolée $F$ au dénominateur au lieu d'utiliser $f_1(1-f_1)/n_1 + f_2(1-f_2)/n_2$ ?**
  - *Réponse flash :* Parce que sous l'hypothèse nulle $H_0 : p_1 = p_2 = p$, il n'existe qu'une seule proportion commune $p$ dans les deux populations ; on l'estime donc de façon optimale en regroupant les deux échantillons : $F = \frac{n_1 f_1 + n_2 f_2}{n_1 + n_2}$.
- [ ] **Q4 : Dans un test de variance ($\mu$ inconnue), pourquoi perd-on 1 degré de liberté par rapport au cas $\mu$ connue ?**
  - *Réponse flash :* Parce que $\mu$ est remplacée par son estimation $\overline{X}_n$, ce qui introduit une contrainte linéaire ($\sum (X_i - \overline{X}_n) = 0$) : connaissant $n-1$ écarts, le $n$-ième est imposé. On passe de $\chi^2(n)$ à $\chi^2(n-1)$.
- [ ] **Q5 : Si l'ANOVA conclut à $F_{\text{obs}} > F_{\text{crit}}$, sait-on immédiatement quel groupe diffère des autres ?**
  - *Réponse flash :* **Non.** L'ANOVA répond uniquement « au moins une moyenne diffère » ($H_1$). Pour identifier les paires responsables, il faut ensuite procéder à des tests post-hoc.

---

## ⚡ 4. Devoirs, Lectures & Prochaines Actions
- [ ] Mettre en pratique sur la [[TD2_Tests_Hypotheses|Feuille TD 2 (Exercices 1 à 9, 11 et 12)]].
- [ ] Enchaîner avec le chapitre [[05_Tests_Non_Parametriques|05. Tests Non Paramétriques]].
