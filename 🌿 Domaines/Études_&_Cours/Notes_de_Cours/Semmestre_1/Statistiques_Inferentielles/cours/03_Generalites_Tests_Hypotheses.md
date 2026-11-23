---
type: note-cours
created: 2026-11-23
matiere: "Statistiques Inférentielles"
chapitre: "03 - Généralités sur les Tests d'Hypothèses"
enseignant: "K. E. HOVI"
tags:
  - etudes
  - cours
  - statistiques-inferentielles
  - tests-hypotheses
  - p-value
  - puissance
  - active-recall
parent: "[[MOC_Statistiques_Inferentielles]]"
---

# 📖 03. Généralités sur les Tests d'Hypothèses

> **Matière :** [[MOC_Statistiques_Inferentielles|Statistiques Inférentielles (M1 IT)]] • **Date :** 23 Novembre 2026 • **Statut :** Synthétisé & Prêt pour révision active

---

## 🎯 1. Idées Clés & Thèses Centrales
Un test d'hypothèse décide si l'écart observé sur un échantillon relève du hasard d'échantillonnage ou traduit une différence réelle dans la population :
- **Dissymétrie fondamentale :** On formule $H_0$ pour être potentiellement **rejetée**. Un non-rejet ne « démontre » jamais que $H_0$ est vraie ; il signifie seulement l'absence de preuve statistique suffisante contre elle.
- **Arbitrage Paramétrique vs Non-paramétrique :** Les tests paramétriques sont **plus puissants** quand leurs hypothèses (normalité, homoscédasticité) tiennent ; les non-paramétriques sont plus **robustes** sur petits effectifs ou distributions quelconques.
- **Deux modes de décision équivalents :** Comparaison de la statistique $S_{\text{obs}}$ à la région critique $R_c$ (fixée a priori pour $\alpha$), ou comparaison de la $p$-value ($\alpha_{\text{obs}}$) au seuil $\alpha$ (rejet si $p\text{-value} < \alpha$).
- **Compromis $\alpha / \beta$ et puissance :** Diminuer $\alpha$ (risque de rejeter $H_0$ à tort) augmente mécaniquement $\beta$ (risque de rater un effet réel), ce qui réduit la puissance $1 - \beta$.

---

## 📝 2. Contenu Structuré & Démonstrations

### A. Typologie des Tests Statistiques

1. **Test de conformité :** Compare un paramètre d'échantillon ($\bar{x}, s^2, f$) à une valeur théorique de référence ($\mu_0, \sigma_0^2, p_0$).
2. **Test d'ajustement (adéquation) :** Vérifie la compatibilité des données avec une loi choisie a priori (ex. ajustement à une loi normale ou de Poisson par le $\chi^2$).
3. **Test d'homogénéité (comparaison) :** Compare $K \ge 2$ groupes pour vérifier s'ils proviennent de populations de même loi / même moyenne (test $t$, ANOVA, Mann-Whitney, Kruskal-Wallis).
4. **Test d'indépendance (association) :** Teste l'existence d'une liaison entre deux variables (ex. $\chi^2$ d'indépendance pour variables qualitatives, corrélation pour variables quantitatives).

---

### B. Méthodologie Standard en 6 Étapes

1. Formuler l'hypothèse nulle $H_0$ (absence d'effet / égalité) et l'hypothèse alternative $H_1$ (unilatérale ou bilatérale).
2. Choisir la statistique de test $S$ adaptée à la nature des données et aux hypothèses.
3. Déterminer la **loi de probabilité exacte ou asymptotique de $S$ sous $H_0$**.
4. Fixer a priori le seuil de signification $\alpha$ (typiquement $0{,}05$, $0{,}01$ ou $0{,}001$) et en déduire la **région critique $R_c$** telle que $P(S \in R_c \mid H_0) = \alpha$.
5. Calculer la réalisation $S_{\text{obs}}$ (ou la $p$-value) sur l'échantillon.
6. Prendre et formuler la décision statistique et métier.

| Type de test | Bilatéral ($H_0 : \theta = \theta_0$) | Unilatéral droit ($H_0 : \theta = \theta_0$) | Unilatéral gauche ($H_0 : \theta = \theta_0$) |
| :--- | :---: | :---: | :---: |
| **Hypothèse alternative $H_1$** | $\theta \ne \theta_0$ | $\theta > \theta_0$ | $\theta < \theta_0$ |
| **Définition de $R_c$** | $P(\|S\| > S_{\text{seuil}}) = \alpha$ | $P(S > S_{\text{seuil}}) = \alpha$ | $P(S < S_{\text{seuil}}) = \alpha$ |

---

### C. Stratégies de Décision : Seuil Critique vs $p$-value

- **Règle 1 (Région critique fixée a priori) :**
  - Si $S_{\text{obs}} \in R_c$ $\implies$ **Rejet de $H_0$** au risque $\alpha$.
  - Si $S_{\text{obs}} \notin R_c$ $\implies$ **Non-rejet de $H_0$**.
- **Règle 2 (Probabilité critique / $p$-value a posteriori) :**
  La $p$-value ($\alpha_{\text{obs}}$) est la probabilité, **sous $H_0$**, d'observer une valeur de statistique au moins aussi extrême que $S_{\text{obs}}$.
  - Si $p\text{-value} < \alpha$ (ou $\le \alpha$) $\implies$ **Rejet de $H_0$** (le résultat observé est trop improbable sous $H_0$).
  - Si $p\text{-value} \ge \alpha$ $\implies$ **Non-rejet de $H_0$** (écart compatible avec les fluctuations d'échantillonnage).

---

### D. Erreurs de 1re / 2e Espèce et Puissance du Test

| Décision \ Réalité | $H_0$ est vraie | $H_1$ est vraie |
| :--- | :---: | :---: |
| **Ne pas rejeter $H_0$** | Décision correcte ($1 - \alpha$) | **Erreur de 2e espèce ($\beta$)** — *Faux négatif* |
| **Rejeter $H_0$** | **Erreur de 1re espèce ($\alpha$)** — *Faux positif* | **Puissance du test ($1 - \beta$)** — *Détection juste* |

- **Risque $\alpha$ (1re espèce) :** Probabilité de rejeter $H_0$ à tort. Fixé **a priori** avant de regarder les données.
- **Risque $\beta$ (2e espèce) :** Probabilité de ne pas rejeter $H_0$ alors que $H_1$ est vraie. Dépend de la loi sous $H_1$.
- **Puissance ($1 - \beta$) :** Aptitude à détecter un effet réel. Elle **augmente** quand :
  1. la taille de l'échantillon $N$ augmente ;
  2. l'écart réel entre $H_0$ et $H_1$ est grand ;
  3. le seuil $\alpha$ est moins strict ;
  4. le test est **unilatéral** plutôt que bilatéral (à $\alpha$ égal).

> [!WARNING] Vigilance — Coquilles dans les Exemples 3.3.1 et 3.3.2 du PDF (p. 19)
> Pour une pièce lancée **100 fois** ($X \sim \mathcal{B}(100; p)$) avec zone d'acceptation $[40; 60]$ :
> - Le risque de 1re espèce est $\alpha = P(\mathcal{B}(\mathbf{100}; 1/2) \notin [40; 60])$ (le PDF écrit par erreur $\mathcal{B}(10, 1/2) \in [40; 60]$).
> - Pour $p = 0{,}6$ sous $H_1$, le risque de 2e espèce est noté **$\beta$** $= P(\mathcal{B}(\mathbf{100}; 0{,}6) \in [40; 60])$ (le PDF imprime $\alpha$ et $10$).

---

## 🧠 3. Batterie d'Active Recall (Questions d'Auto-Évaluation)

- [ ] **Q1 : Pourquoi un résultat non significatif ($p = 0{,}18$) ne prouve-t-il pas que $H_0$ est vraie ?**
  - *Réponse flash :* Le test contrôle uniquement $\alpha$ (le risque de rejeter à tort $H_0$), pas $\beta$ (le risque de rater $H_1$, souvent faute d'un échantillon assez grand). Ne pas rejeter $H_0$ signifie « pas assez de preuves pour rejeter », pas « preuve d'égalité ».
- [ ] **Q2 : Pourquoi le seuil $\alpha$ doit-il impérativement être fixé avant l'analyse des données ?**
  - *Réponse flash :* Choisir $\alpha$ après avoir vu la $p$-value reviendrait à adapter la règle du jeu au résultat (biais de confirmation / *p-hacking*), ce qui invaliderait la garantie théorique du taux d'erreur de première espèce.
- [ ] **Q3 : Comment peut-on diminuer simultanément $\alpha$ et $\beta$ ?**
  - *Réponse flash :* À taille d'échantillon fixée, baisser $\alpha$ augmente $\beta$. La seule manière de réduire simultanément les deux risques (donc d'augmenter la puissance à $\alpha$ fixé) est d'**augmenter la taille de l'échantillon $N$** (ou d'utiliser un test plus puissant si ses hypothèses sont satisfaites).
- [ ] **Q4 : À quoi correspond concrètement la $p$-value sur le schéma de la densité de la statistique sous $H_0$ ?**
  - *Réponse flash :* C'est l'aire (probabilité) sous la courbe de densité sous $H_0$ située au-delà de la valeur observée $S_{\text{obs}}$ (et son symétrique dans le cas bilatéral).

---

## ⚡ 4. Devoirs, Lectures & Prochaines Actions
- [ ] Appliquer cette méthodologie à la [[TD2_Tests_Hypotheses|Feuille TD 2 (notamment Exercice 1 : schéma & p-value)]].
- [ ] Enchaîner avec le chapitre [[04_Tests_Parametriques|04. Les Tests Paramétriques]].
