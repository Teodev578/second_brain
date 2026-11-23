---
type: note-cours
created: 2026-11-23
matiere: "Statistiques Inférentielles"
chapitre: "02 - Les Intervalles de Confiance"
enseignant: "K. E. HOVI"
tags:
  - etudes
  - cours
  - statistiques-inferentielles
  - intervalles-de-confiance
  - student
  - khi-deux
  - fisher
  - active-recall
parent: "[[MOC_Statistiques_Inferentielles]]"
---

# 📖 02. Les Intervalles de Confiance

> **Matière :** [[MOC_Statistiques_Inferentielles|Statistiques Inférentielles (M1 IT)]] • **Date :** 23 Novembre 2026 • **Statut :** Synthétisé & Prêt pour révision active

---

## 🎯 1. Idées Clés & Thèses Centrales
Une estimation ponctuelle ne dit rien sur sa précision. L'intervalle de confiance (IC) encadre le paramètre inconnu avec un **niveau de confiance** $1 - \alpha$ et une **marge d'erreur** contrôlée :
- **Arbitrages fondamentaux :** À $n$ fixé, augmenter la confiance $1 - \alpha$ **élargit** l'IC. À confiance fixée, augmenter la taille de l'échantillon $n$ **rétrécit** l'IC (proportionnellement à $1/\sqrt{n}$).
- **Loi pivotale pour $\mu$ :** Loi normale $\mathcal{N}(0, 1)$ si $\sigma$ est connu (ou $n \ge 30$ par TCL) ; loi de Student $t(n-1)$ si la population est normale et $\sigma$ inconnu.
- **Loi pivotale pour $\sigma^2$ et rapport $\sigma_1^2/\sigma_2^2$ :** Lois asymétriques du Khi-deux ($\chi^2$) pour une variance et de Fisher-Snedecor ($\mathcal{F}$) pour un rapport de variances, **strictement valables sous hypothèse de normalité**.

---

## 📝 2. Contenu Structuré & Démonstrations

### A. Estimation d'une Proportion $p$ par Intervalle de Confiance

Pour $n$ suffisamment grand ($n > 30$, et usuellement $np \ge 5, n(1-p) \ge 5$), $F \approx \mathcal{N}\!\left(p, \frac{p(1-p)}{n}\right)$.
En estimant l'écart-type corrigé par $\sigma = \sqrt{\frac{f(1-f)}{n-1}}$ (ou $\sqrt{\frac{f(1-f)}{n}}$ pour $n$ grand) :
$$IC_{1-\alpha}(p) = \left]f - z_{1-\alpha/2}\sqrt{\frac{f(1-f)}{n-1}} \,;\, f + z_{1-\alpha/2}\sqrt{\frac{f(1-f)}{n-1}}\right[$$
- **Formule courante ($n$ grand) :** $f \pm z_{1-\alpha/2}\sqrt{\frac{f(1-f)}{n}}$.
- **Approximation rapide à 95% ($\alpha=5\%$, $f \simeq 0{,}5$) :**
  $$IC_{95\%}(p) \approx \left[f - \frac{1}{\sqrt{n}} \,;\, f + \frac{1}{\sqrt{n}}\right]$$

---

### B. Intervalle de Confiance sur l'Espérance $\mu$

#### Arbre de décision complet
```text
                  ┌────────────────────────────────┐
                  │ La population est-elle normale │
                  └───────────────┬────────────────┘
                        Oui       │       Non
                  ┌───────────────┴───────────────┐
                  ▼                               ▼
     ┌─────────────────────────┐     ┌─────────────────────────┐
     │ L'écart-type σ est-il   │     │ Taille d'échantillon n  │
     │ connu ?                 │     │                         │
     └────────────┬────────────┘     └────────────┬────────────┘
          Oui     │     Non               n ≥ 30  │  n < 30
           ┌──────┴──────┐                 ┌──────┴──────┐
           ▼             ▼                 ▼             ▼
      N(0, 1)         t(n - 1)          N(0, 1)      Approche
   (z = 1,96 à 95%)   Student            (TCL)    non paramétrique
```

#### 1. Population normale, $\sigma$ connu (ou $n \ge 30$ par TCL)
Variable pivotale : $Z = \frac{\overline{X} - \mu}{\sigma / \sqrt{n}} \sim \mathcal{N}(0, 1)$.
$$IC_{1-\alpha}(\mu) = \left[\bar{x} - z_{1-\alpha/2}\frac{\sigma}{\sqrt{n}}, \; \bar{x} + z_{1-\alpha/2}\frac{\sigma}{\sqrt{n}}\right]$$
*(Si $n \ge 30$ et $\sigma$ inconnu, on remplace $\sigma$ par l'écart-type corrigé $s$ dans l'approximation normale.)*

#### 2. Population normale, $\sigma$ inconnu
Variable pivotale :
$$T_{n-1} = \frac{\overline{X} - \mu}{S / \sqrt{n}} = \frac{\frac{\overline{X} - \mu}{\sigma/\sqrt{n}}}{\sqrt{\frac{(n-1)S^2}{\sigma^2} / (n-1)}} \sim t(n - 1)$$
$$IC_{1-\alpha}(\mu) = \left[\bar{x} - t_{n-1, 1-\alpha/2}\frac{s}{\sqrt{n}}, \; \bar{x} + t_{n-1, 1-\alpha/2}\frac{s}{\sqrt{n}}\right]$$

#### Quantiles symétriques usuels ($\mathcal{N}(0,1)$ et Student)

| Niveau $1 - \alpha$ | Risque $\alpha$ | $z_{1-\alpha/2}$ ($\mathcal{N}(0,1)$) | $t_{k=5}$ | $t_{k=10}$ | $t_{k=20}$ | $t_{k=30}$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **90%** | 0,10 | 1,645 | 2,015 | 1,812 | 1,725 | 1,697 |
| **95%** | 0,05 | 1,960 | 2,571 | 2,228 | 2,086 | 2,042 |
| **99%** | 0,01 | 2,576 | 4,032 | 3,169 | 2,845 | 2,750 |

---

### C. Intervalle de Confiance sur la Variance $\sigma^2$ (Loi Normale Uniquement)

> [!CAUTION] Condition stricte de normalité
> Contrairement à l'IC sur la moyenne (sauvé par le TCL pour $n \ge 30$), les IC sur $\sigma^2$ ne sont valables **que si la population suit une loi normale**.

1. **Moyenne $\mu$ connue :** $V^2 = \frac{1}{n}\sum_{i=1}^n (X_i - \mu)^2$, et $\frac{nV^2}{\sigma^2} \sim \chi^2(n)$.
   $$IC_{1-\alpha}(\sigma^2) = \left[\frac{nV^2}{k_{1-\alpha/2}(n)}, \; \frac{nV^2}{k_{\alpha/2}(n)}\right]$$
2. **Moyenne $\mu$ inconnue :** $S^2 = \frac{1}{n-1}\sum_{i=1}^n (X_i - \overline{X})^2$, et $\frac{(n-1)S^2}{\sigma^2} \sim \chi^2(n-1)$.
   $$IC_{1-\alpha}(\sigma^2) = \left[\frac{(n-1)s^2}{k_{1-\alpha/2}(n-1)}, \; \frac{(n-1)s^2}{k_{\alpha/2}(n-1)}\right]$$

> [!WARNING] Convention de lecture de l'Annexe B ($\chi^2$) — Règle anti-erreur
> L'Annexe B du polycopié donne $k_{1-\alpha}$ tel que $P(X \ge k_{1-\alpha}) = \alpha$ (queue **droite**).
> Pour un IC à 95% ($\alpha = 0{,}05$, $\alpha/2 = 0{,}025$) :
> - Colonne `0,025` $\to$ **grand quantile** (queue droite) $\implies$ va au dénominateur de la **borne inférieure**.
> - Colonne `0,975` $\to$ **petit quantile** (queue gauche) $\implies$ va au dénominateur de la **borne supérieure**.
> *(Le support inverse parfois l'écriture des indices entre p. 13 et p. 14 : toujours vérifier que borne gauche $<$ borne droite !)*

---

### D. Intervalle de Confiance du Rapport de Deux Variances & Homoscédasticité

Pour deux échantillons normaux indépendants de variances corrigées $S_1^2$ (taille $n_1$) et $S_2^2$ (taille $n_2$), le théorème de Cochran donne :
$$F = \frac{S_1^2 / \sigma_1^2}{S_2^2 / \sigma_2^2} \sim \mathcal{F}(n_1 - 1, \, n_2 - 1)$$
En exploitant la **propriété de réversibilité** $f_{1-\alpha/2}(\nu_1, \nu_2) = \frac{1}{f_{\alpha/2}(\nu_2, \nu_1)}$ (queue droite de l'Annexe D.2 pour $\alpha = 0{,}05 \implies \alpha/2 = 0{,}025$) :
$$IC_{1-\alpha}\!\left(\frac{\sigma_1^2}{\sigma_2^2}\right) = \left[\frac{s_1^2}{s_2^2} \times \frac{1}{F_{\text{sup}}(n_1-1, n_2-1)} \,;\, \frac{s_1^2}{s_2^2} \times F_{\text{sup}}(n_2-1, n_1-1)\right]$$
*(où $F_{\text{sup}}(\nu_1, \nu_2)$ est lu dans Annexe D.2 sous $\alpha = 0{,}025$, avec $P(F \ge F_{\text{sup}}) = 0{,}025$).*

**Test d'homoscédasticité ($H_0 : \sigma_1^2 = \sigma_2^2$ vs $H_1 : \sigma_1^2 \ne \sigma_2^2$) :**
- Si $1 \in IC_{1-\alpha}(\sigma_1^2 / \sigma_2^2)$ : on ne rejette pas $H_0$ (variances compatibles avec l'égalité).
- Si $1 \notin IC_{1-\alpha}(\sigma_1^2 / \sigma_2^2)$ : on rejette $H_0$ (variances significativement différentes).

---

## 🧠 3. Batterie d'Active Recall (Questions d'Auto-Évaluation)

- [ ] **Q1 : Comment évolue la largeur d'un IC sur $\mu$ si l'on quadruple la taille d'échantillon $n$ à confiance constante ?**
  - *Réponse flash :* La demi-largeur est proportionnelle à $1/\sqrt{n}$. Quadrupler $n$ divise la largeur de l'IC par $\sqrt{4} = 2$ (pour un IC avec $\sigma$ connu).
- [ ] **Q2 : Peut-on utiliser la loi du $\chi^2$ pour un IC sur la variance d'une variable manifestement non normale quand $n = 100$ ?**
  - *Réponse flash :* **Non.** Le TCL s'applique à la moyenne empirique, pas à l'intervalle de confiance de la variance qui suppose strictement une population normale (la sensibilité au moment d'ordre 4 / kurtosis invalide le $\chi^2$).
- [ ] **Q3 : Pour un IC bilatéral à 95% de $\sigma^2$ avec $n=10$ ($\mu$ inconnue), quelles colonnes lit-on dans l'Annexe B et où place-t-on chaque valeur ?**
  - *Réponse flash :* Sur la ligne $\nu = n - 1 = 9$, on lit `0,975` ($2{,}7004$) et `0,025` ($19{,}0228$). On divise $(n-1)s^2$ par le plus grand ($19{,}0228$) pour la borne inférieure et par le plus petit ($2{,}7004$) pour la borne supérieure.
- [ ] **Q4 : Pourquoi la loi de Student converge-t-elle vers $\mathcal{N}(0,1)$ quand $n$ augmente, et pourquoi ses queues sont-elles plus épaisses à petit $n$ ?**
  - *Réponse flash :* Pour un petit $n$, l'estimation de $\sigma$ par $S$ ajoute une incertitude supplémentaire au dénominateur, élargissant les quantiles ($t_{k, 1-\alpha/2} > z_{1-\alpha/2}$). Quand $n \to \infty$, $S \xrightarrow{P} \sigma$ et $t(n-1) \xrightarrow{\mathcal{L}} \mathcal{N}(0, 1)$.

---

## ⚡ 4. Devoirs, Lectures & Prochaines Actions
- [ ] Résoudre les exercices d'IC de la [[TD1_Echantillonnage_et_Estimations|Feuille TD 1 (Exercices 5, 6, 7 et 9)]].
- [ ] Poursuivre avec le chapitre [[03_Generalites_Tests_Hypotheses|03. Généralités sur les Tests d'Hypothèses]].
