---
type: moc
created: 2026-11-23
matiere: "Statistiques Inférentielles"
niveau: "Master 1 - IT"
enseignant: "K. E. HOVI (Ascencia Keyce Lomé)"
tags:
  - moc
  - etudes
  - cours
  - statistiques-inferentielles
  - probabilites
  - r
parent: "[[MOC_Etudes_&_Cours]]"
---

# 📊 Statistiques Inférentielles (Master 1 – IT)

> ↖ [[MOC_Etudes_&_Cours|Retour au MOC Études & Cours]] • [[Centre_de_control|Centre de Contrôle]]
> **Enseignant :** K. E. HOVI (Ascencia Keyce, Campus de Lomé) • **Date de référence :** 20 Novembre 2026
> **Documents sources :** [[Statistique_inf_M1_IT.pdf|📄 Consulter le PDF Original]] • [[Cours_Integral_Verbatim_Statistiques_Inferentielles|📜 Transcription Intégrale & Textuelle du Cours]]

Bienvenue dans l'espace de synthèse, d'assimilation et de mise en pratique pour le module de **Statistiques Inférentielles**. Ce cours structure les fondements probabilistes et décisionnels de l'estimation, des intervalles de confiance, des tests paramétriques et non paramétriques, de la corrélation, de la régression linéaire et de leur mise en œuvre sous R.

---

## 🧭 Navigation & Structure du Module

### 📄 0. Documents de Référence (`pdf/` & `cours/`)
- 📑 [[Statistique_inf_M1_IT.pdf|Support de Cours, TD, TP & Annexes en PDF (Document Original de 71 pages)]]
- 📜 [[Cours_Integral_Verbatim_Statistiques_Inferentielles|Transcription Intégrale Verbatim (Texte exhaustif des 6 chapitres et mémo des 4 Annexes)]]

---

### 📖 I. Notes de Cours & Synthèses (`cours/`)
1. [[01_Echantillonnage_et_Estimations|01. Échantillonnage et Estimations]]
   - Modèle iid, approches paramétrique vs non paramétrique, statistique $T_n$.
   - Moyenne empirique $\overline{X}$ (Théorème 1.1.1 + TCL), variance biaisée $\overline{S}^2$ vs corrigée $S^2$, fréquence $F$.
   - Qualités d'un estimateur : biais, convergence, consistance, décomposition EQM $= \text{Var}(T) + b_\theta(T)^2$ et efficacité.
2. [[02_Intervalles_de_Confiance|02. Les Intervalles de Confiance]]
   - Niveau de confiance $1-\alpha$, marge d'erreur et arbitrage avec la taille $n$.
   - IC sur une proportion $p$ (formule exacte, grand $n$, règle rapide $f \pm 1/\sqrt{n}$).
   - IC sur l'espérance $\mu$ : $\mathcal{N}(0,1)$ ($\sigma$ connu ou TCL $n \ge 30$) vs Student $t(n-1)$ ($\sigma$ inconnu), avec arbre de décision.
   - IC sur la variance $\sigma^2$ ($\chi^2$, normalité stricte) et rapport de variances $\sigma_1^2/\sigma_2^2$ (Fisher-Snedecor et test d'homoscédasticité).
3. [[03_Generalites_Tests_Hypotheses|03. Généralités sur les Tests d'Hypothèses]]
   - Typologie des tests (conformité, ajustement, homogénéité, indépendance) et méthode en 6 étapes.
   - Dissymétrie $H_0$ / $H_1$, tests bilatéraux et unilatéraux, décision par région critique $R_c$ vs $p$-value.
   - Risques de 1re espèce ($\alpha$), 2e espèce ($\beta$) et puissance du test ($1-\beta$).
4. [[04_Tests_Parametriques|04. Les Tests Paramétriques]]
   - Moyenne ($Z$, Student), variance ($\chi^2$), fréquence et comparaison de deux proportions.
   - Comparaison de deux moyennes : apparié, grands échantillons ($Z$), petits échantillons ($\sigma_1=\sigma_2$ poolé vs Welch), égalité de deux variances ($\mathcal{F}$).
   - Analyse de la Variance (ANOVA à un facteur) : variabilités inter/intra, tableau ANOVA et loi $\mathcal{F}(k-1, N-k)$.
5. [[05_Tests_Non_Parametriques|05. Tests Non Paramétriques]]
   - Arbitrage puissance / robustesse (*distribution free*, tests de rangs).
   - Test d'indépendance du $\chi^2$ (effectifs théoriques $C_{i,j} \ge 5$, $\nu = (l-1)(k-1)$).
   - Test de Mann-Whitney ($U_1 + U_2 = n_1 n_2$, approximation normale, lien Kruskal-Wallis).
   - Test des rangs signés de Wilcoxon ($W = \min(W^+, W^-)$, gestion des zéros et des ex-æquo).
6. [[06_Correlation_et_Regression_Lineaire|06. Corrélation et Régression Linéaire]]
   - Nuage de points, Pearson ($r$) vs Spearman ($\rho$), corrélation $\ne$ causalité.
   - Test de significativité de $r$ ($t \sim t(n-2)$) et piège de l'effet de taille $n$.
   - Régression linéaire simple par MCO ($\hat{Y} = b_0 + b_1 X$), résidus, $R^2 = r^2$, test de la pente ($H_0 : \beta_1 = 0$).
   - Prédiction ponctuelle, Intervalle de Confiance (IC) vs Intervalle de Prédiction (IP) et piège de l'extrapolation.

---

### 📝 II. Travaux Dirigés & Corrigés (`exercices/`)
- [[TD1_Echantillonnage_et_Estimations|Feuille TD 1 : Échantillonnage et Estimations]] (Exercices 1 à 9 résolus)
  - Calculs gaussiens, lois binomiales, estimation sous R, loi de Poisson, IC sur $\mu$, $p$, $\sigma^2$, $\sigma_1^2/\sigma_2^2$, sondage électoral et preuve d'efficacité du maximum de vraisemblance (Cramér-Rao).
- [[TD2_Tests_Hypotheses|Feuille TD 2 : Tests d'Hypothèses]] (Exercices 1 à 16 résolus)
  - Conformité (moyenne, proportion, variance), schéma $R_c$/$p$-value, ajustement du $\chi^2$ (Poisson), comparaison de proportions, démonstration et calcul ANOVA, tests appariés Student et Wilcoxon, Mann-Whitney et $\chi^2$ d'indépendance.
- [[TD3_Regression_Lineaire|Feuille TD 3 : Corrélation et Régression Linéaire]] (Exercices 1 à 5 résolus)
  - Corrélation de Pearson, test $t$ de significativité ($r$), ajustement MCO de projets IT, décomposition ANOVA/$R^2$ sur requêtes SQL, arbitrage IC/IP et alerte d'extrapolation Cloud.

---

### 💻 III. Travaux Pratiques sous R (`tp/`)
- [[TP1_Utilisation_du_Logiciel_R|TP 1 : Utilisation du Logiciel R]] (Exercices 1 à 7 : scripts R complets & résultats vérifiés)
  - Ex. 1 : `var.test()` et `t.test()` (temps de réponse Hommes vs Femmes).
  - Ex. 2 : `boxplot()`, `ecdf()`, ANOVA `aov()` et Kruskal-Wallis `kruskal.test()` (5 régimes).
  - Ex. 3 : Mesures répétées / longitudinales (`friedman.test()` et ANOVA `Error(patient/jour)`).
  - Ex. 4 : Homogénéité ordinale (`chisq.test()` vs `wilcox.test()`).
  - Ex. 5 : Import Excel (`readxl::read_excel("dictee.xlsx")`) et analyse appariée temporelle.
  - Ex. 6 : Comparaison de 3 tests sur le temps de réaction (Student apparié, Wilcoxon, indépendant).
  - Ex. 7 : Justification du choix de test par `shapiro.test()` (outlier et Wilcoxon sur le cholestérol).

---

## 📊 Récapitulatif Dataview du Module

```dataview
TABLE chapitre AS "Chapitre / TD", type AS "Type", tags AS "Mots-clés"
FROM "🌿 Domaines/Études_&_Cours/Notes_de_Cours/Semmestre_1/Statistiques_Inferentielles"
SORT file.name ASC
```
