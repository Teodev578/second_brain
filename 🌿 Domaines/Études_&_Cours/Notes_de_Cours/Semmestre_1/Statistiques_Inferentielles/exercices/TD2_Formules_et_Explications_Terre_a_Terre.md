---
type: td-formules
created: 2026-11-24
matiere: "Statistiques Inférentielles"
chapitre: "TD 2 - Formules & Explications Terre à Terre (Tests d'Hypothèses)"
enseignant: "K. E. HOVI"
tags:
  - etudes
  - td
  - formules
  - terre-a-terre
  - statistiques-inferentielles
  - tests-parametriques
  - tests-non-parametriques
  - anova
  - khi-deux
  - wilcoxon
  - mann-whitney
  - revision
parent: "[[MOC_Statistiques_Inferentielles]]"
---

# 🧰 TD 2 — Formules & Explications Terre à Terre : Tests d'Hypothèses

> ↖ [[MOC_Statistiques_Inferentielles|Statistiques Inférentielles (M1 IT)]] • 📄 [[TD2_Tests_Hypotheses|Corrigé officiel TD 2]] • 📖 [[03_Generalites_Tests_Hypotheses|Ch. 03]] • [[04_Tests_Parametriques|Ch. 04]] • [[05_Tests_Non_Parametriques|Ch. 05]]

---

## 🧭 Comment choisir le bon test statistique ?

```mermaid
flowchart TD
    A["Combien de groupes ou variables compare-t-on ?"] --> B["1 échantillon contre une norme"]
    A --> C["2 groupes indépendants"]
    A --> D["2 mesures sur les mêmes individus\n(séries appariées)"]
    A --> E["3 groupes ou plus\n(ANOVA)"]
    A --> F["2 variables qualitatives\n(tableau croisé)"]

    B --> B1["Moyenne : n ≥ 30 -> Z\nn < 30 -> Student t(n-1)"]
    B --> B2["Proportion -> Z(p₀)\nVariance -> χ²(n-1)"]
    B --> B3["Loi complète -> χ² ajustement\n(regrouper Eᵢ ≥ 5)"]

    C --> C1["2 proportions -> Z poolé F"]
    C --> C2["2 moyennes normales -> Z ou t"]
    C --> C3["Petit n ou non normal -> Mann-Whitney U"]

    D --> D1["Différences normales -> Student apparié"]
    D --> D2["Outlier ou non normal -> Wilcoxon W"]

    E --> E1["Fisher F = MS_facteur ÷ MS_résiduelle"]
    F --> F1["χ² indépendance, ddl = (l-1)(c-1)"]
```

---

## 📋 Formulaire & Lexique récapitulatif du TD 2

> [!tip] Mémo rapide des formules utilisées dans le TD 2
> | Concept / Test | Formule mathématique | Formule en français simple | Quand l'utiliser ? |
> | :--- | :--- | :--- | :--- |
> | **Squelette d'un test paramétrique** | $\text{Stat} = \dfrac{\hat{\theta} - \theta_0}{\text{ES}}$ | `(Observé - Attendu sous H₀) ÷ Erreur standard` | Mesure combien d'erreurs standards séparent l'échantillon de $H_0$. |
> | **Test $Z$ sur moyenne ($n \ge 30$)** | $Z = \dfrac{\overline{X} - \mu_0}{s / \sqrt{n}} \sim \mathcal{N}(0,1)$ | `(Moyenne mesurée - Cible μ₀) ÷ (Écart-type ÷ √n)` | Conformité d'une moyenne sur grand échantillon (TCL). |
> | **Test $t$ sur moyenne ($n < 30$)** | $t = \dfrac{\overline{X} - \mu_0}{s / \sqrt{n}} \sim t(n-1)$ | Même calcul que $Z$, mais lu dans **Student** à $n-1$ ddl | Conformité d'une moyenne sur petit échantillon normal ($\sigma$ inconnu). |
> | **Test $Z$ sur proportion** | $Z = \dfrac{f - p_0}{\sqrt{\dfrac{p_0(1-p_0)}{n}}}$ | `(Fréquence observée - Taux H₀) ÷ √(p₀(1-p₀) ÷ n)` | Si $np_0 \ge 5$ et $n(1-p_0) \ge 5$. |
> | **Test $\chi^2$ sur variance** | $V = \dfrac{(n-1)s^2}{\sigma_0^2} \sim \chi^2(n-1)$ | `Somme carrés des écarts ÷ Variance cible σ₀²` | Tester si $\sigma$ respecte un seuil (normalité requise). |
> | **Test $\chi^2$ d'ajustement** | $\chi^2_{\text{obs}} = \sum_{i=1}^k \dfrac{(O_i - E_i)^2}{E_i}$, $\nu = k - 1 - p$ | `Somme de (Observé - Attendu)² ÷ Attendu` | Regrouper pour $E_i \ge 5$ ; $p$ = nb de paramètres estimés. |
> | **Comparaison 2 proportions** | $F = \dfrac{k_1 + k_2}{n_1 + n_2}$, $Z = \dfrac{f_1 - f_2}{\sqrt{F(1-F)\left(\frac{1}{n_1}+\frac{1}{n_2}\right)}}$ | `Taux commun = total succès ÷ total sondés`, puis écart ÷ erreur standard | Comparer 2 pourcentages sur 2 grands échantillons indépendants. |
> | **ANOVA à 1 facteur** | $V_T^2 = V_R^2 + V_A^2$, $F = \dfrac{\text{SC}_A / (K-1)}{\text{SC}_R / (n-K)}$ | `F = Signal moyen entre groupes ÷ Bruit moyen interne` | Comparer $K \ge 3$ moyennes simultanément (Annexe D.1). |
> | **Comparaison 2 moyennes** | $N = \dfrac{\bar{x}_1 - \bar{x}_2}{\sqrt{\frac{v_1^2}{n_1}+\frac{v_2^2}{n_2}}}$, $F_{\text{hom}} = \dfrac{s_{\max}^2}{s_{\min}^2}$ | `(Moyenne 1 - Moyenne 2) ÷ √(Var₁/n₁ + Var₂/n₂)` | Vérifier Shapiro-Wilk + homoscédasticité ($F$) avant. |
> | **Test $t$ apparié** | $d_i = X_{\text{après}, i} - X_{\text{avant}, i}$, $t = \dfrac{\bar{d}}{s_d / \sqrt{n}}$ | Calculer chaque écart $d_i$, puis tester si la moyenne des écarts vaut $0$ | Mesures Avant/Après sur les mêmes individus (normalité requise). |
> | **Wilcoxon (rangs signés)** | $W = \min(W^+, W^-)$, $W^+ + W^- = \dfrac{n(n+1)}{2}$ | Jeter les $0$, trier $\lvert d_i\rvert$, sommer rangs $+$ et $-$, prendre le min | Robuste aux outliers ; rejet si $W \le W_{\text{crit}}$. |
> | **Mann-Whitney $U$** | $U_1 = R_1 - \dfrac{n_1(n_1+1)}{2}$, $U_2 = n_1 n_2 - U_1$ | Classer tout ensemble, $U = \min(U_1, U_2)$ duels perdus/gagnés | Alternative non paramétrique à 2 moyennes ; rejet si $U \le U_{\text{crit}}$. |
> | **$\chi^2$ d'indépendance** | $E_{ij} = \dfrac{L_i \times C_j}{N}$, $\nu = (l-1)(c-1)$ | `Attendu = (Total ligne × Total colonne) ÷ Total global` | Lien entre 2 variables qualitatives (tous $E_{ij} \ge 5$). |

> [!note] Mémo rapide — D'où viennent les seuils lus dans les tables ?
> - **Loi Normale $\mathcal{N}(0, 1)$ (Annexe A.1 / A.2) :** On cherche $U_{1-\alpha/2} = z_{1-\alpha/2}$ tel que l'aire cumulée à gauche vaille $\Phi(u) = 1 - \frac{\alpha}{2}$ en **bilatéral** (ou $\Phi(u) = 1 - \alpha$ en **unilatéral**). Ex. à $\alpha = 5\%$ bilatéral : $\Phi(u) = 1 - 0{,}025 = 0{,}9750 \implies$ on repère `0,9750` *dans* l'Annexe A.1 $\to$ ligne **`1,9`** et colonne **`0,06`** $\implies \mathbf{1{,}96}$. À $\alpha = 10\%$ bilatéral (ou $5\%$ unilatéral) : $\Phi(u) = 0{,}9500 \implies \mathbf{1{,}6449}$ (entre `1,64` et `1,65`).
> - **Loi de Student (Annexe C) :** Lire la ligne $\nu = \text{ddl}$ et la colonne **bilatérale** $\alpha$. Pour un test **unilatéral** au risque $\alpha$, placer tout $\alpha$ d'un seul côté équivaut à lire la colonne bilatérale **$2\alpha$** (ex. unilatéral à $\alpha = 2{,}5\%$ $\to$ colonne bilatérale `0,050`).
> - **Loi du $\chi^2$ (Annexe B — queue droite) :** La table donne $k$ tel que $P(X \ge k) = \text{colonne}$ à la ligne $\nu = \text{ddl}$ (ex. test unilatéral droit à $\alpha = 5\%$ $\to$ colonne `0,05`).
> - **Loi de Fisher-Snedecor $\mathcal{F}$ (Annexe D.1 / D.2) :** Lire le croisement $\nu_1$ (ddl numérateur, en colonne) et $\nu_2$ (ddl dénominateur, en ligne). Utiliser Annexe D.1 pour l'ANOVA ($\alpha = 0{,}05$ ou $0{,}01$) et Annexe D.2 ($\alpha = 0{,}025$) pour le test bilatéral d'homoscédasticité.

---

## 🧠 Méthode : comment savoir quelle formule utiliser ?

### 1. Les 4 questions à se poser, dans l'ordre
1. **Que demande-t-on ?** Calculer une probabilité (loi connue), estimer un chiffre unique (estimation ponctuelle), encadrer par une fourchette (intervalle de confiance) ou trancher une affirmation (test d'hypothèse) ?
2. **Sur quel paramètre ?** Une moyenne $\mu$, une proportion $p$, une variance $\sigma^2$ (ou $\sigma$), un rapport de variances $\sigma_1^2/\sigma_2^2$, ou le lien entre deux variables ?
3. **Que sait-on sur l'échantillon et la population ?** $\sigma$ connu ou inconnu, taille $n \ge 30$ ou $n < 30$, population normale ou quelconque ?
4. **Quel sens pour le test ?** Bilatéral ou unilatéral (d'après les mots exacts de l'énoncé) ?

### 2. Tableau de traduction : Indice dans l'énoncé → Choix

| Indice lu dans l'énoncé | Choix de la loi / formule |
| :--- | :--- |
| « $\sigma = \dots$ » donné pour la population / « variance connue » | **Loi normale $\mathcal{N}(0, 1)$** ($z$) |
| $\sigma$ inconnu (on calcule $s$ soi-même), population normale, $n < 30$ | **Loi de Student $t(n - 1)$** |
| $n \ge 30$, même avec $\sigma$ inconnu (on utilise $s$) | **Loi normale $z$** par le TCL (Student $\approx$ normale) |
| « proportion », « \% », « $k$ personnes sur $n$ » | Calculer $f = k / n$, puis **loi normale $z$** (si $np \ge 5$ et $n(1-p) \ge 5$) |
| « variance », « écart-type », « variabilité », « dispersion » d'une population | **Loi du Khi-deux $\chi^2(n - 1)$** (normalité obligatoire) |
| Comparer deux variances / tester l'homoscédasticité | **Loi de Fisher $\mathcal{F}$** (rapport $s_1^2 / s_2^2$) |
| « égal à », « vaut », « différent de », « diffèrent-ils » | **Test bilatéral** ($\alpha/2$ de chaque côté, quantile $1 - \alpha/2$) |
| « au moins », « supérieur », « plus grand », « ne dépasse pas » | **Test unilatéral** ($\alpha$ d'un seul côté, quantile $1 - \alpha$) |
| Mêmes individus mesurés avant / après | **Données appariées** : travailler sur les différences $d_i$ |
| $3$ groupes ou plus à comparer simultanément | **ANOVA à 1 facteur** (statistique $F$ de Fisher) |
| Tableau croisé de deux caractères qualitatifs | **Test du $\chi^2$ d'indépendance** |
| « suit-elle une loi … ? », « loi candidate » | **Test du $\chi^2$ d'ajustement** ($E_i \ge 5$) |
| Petits effectifs, non-normalité ou valeur aberrante (outlier) | **Test non paramétrique** (Wilcoxon ou Mann-Whitney) |

> [!tip] Pourquoi Student plutôt que la loi normale ?
> Quand l'écart-type vrai $\sigma$ de la population est inconnu, on le remplace par l'estimation $s$ calculée sur l'échantillon, qui fluctue elle aussi d'un échantillon à l'autre. Cette incertitude supplémentaire élargit les queues de la distribution, et la loi de Student en tient compte grâce à ses $n - 1$ degrés de liberté (un degré de liberté a déjà été consommé pour calculer $\bar{x}$). Dès que $n$ grandit, $s \approx \sigma$ et Student rejoint la loi normale : $t(\infty) = z$, ce qui se lit directement dans l'Annexe C ($2{,}2622$ pour $\nu = 9$ contre $1{,}96$ à l'infini pour $95\%$).

> [!tip] Logique commune à tous les tests
> 1. Poser $H_0$ et $H_1$ à partir des mots exacts de l'énoncé (égalité vs différence, supériorité ou infériorité).
> 2. Choisir la statistique adaptée grâce au tableau ci-dessus.
> 3. Calculer la statistique : $\text{Stat} = (\text{Observé} - \text{Attendu sous } H_0) \div \text{Erreur standard}$.
> 4. Comparer au seuil lu dans la table (ou comparer la $p$-value à $\alpha$).
> 5. Conclure en contexte : **ne pas rejeter $H_0$ ne prouve jamais que $H_0$ est vraie**, cela signifie seulement qu'on manque de preuves contre elle.

---
## 📌 Exercice 1 – Montant moyen des remboursements de crédit

> [!question] Énoncé résumé & Données
> Un ingénieur risque crédit à Lomé veut vérifier si la mensualité moyenne de remboursement des clients vaut $\mu_0 = 200$ €. Sur un échantillon de $n = 144$ clients, il observe $\bar{x} = 193{,}74$ € et un écart-type corrigé $s = 48{,}24$ €. On demande de poser les hypothèses, de conclure au risque $\alpha = 5\%$, de tracer le schéma des régions, de calculer la $p$-value, puis de répondre pour $\alpha = 10\%$.

> [!info] Comprendre la logique (terre à terre)
> **D'où vient $U_{1-\alpha/2} = 1{,}96$ et comment trouve-t-on les bornes inf/sup ?**
> À $\alpha = 5\%$ en bilatéral, on accepte $2{,}5\%$ d'erreur à gauche et $2{,}5\%$ à droite. On cherche donc le seuil $u$ tel que $\Phi(u) = 1 - 0{,}025 = 0{,}9750$ : dans l'Annexe A.1, `0,9750` se lit à la ligne `1,9` et colonne `0,06`, d'où $U_{0{,}975} = 1{,}96$. Ensuite, on multiplie ce quantile par l'erreur standard ($4{,}02$ €) pour obtenir la **marge d'erreur** $e \approx 7{,}88$ €. Selon ce qu'on cherche :
> - **Intervalle d'acceptation de $H_0$** (centré sur $\mu_0 = 200$ €) : $\mu_0 - e = 192{,}12$ € et $\mu_0 + e = 207{,}88$ €.
> - **Intervalle de confiance à $95\%$ de $\mu$** (centré sur $\bar{x} = 193{,}74$ €) : $\bar{x} - e = 185{,}86$ € et $\bar{x} + e = 201{,}62$ €.
> Les deux approches donnent la **même** conclusion : $193{,}74 \in [192{,}12 \,;\, 207{,}88]$ tout comme $200 \in [185{,}86 \,;\, 201{,}62]$.
>
> **C'est quoi la $p$-value, concrètement ?**
> Imagine que la norme est vraie ($\mu = 200$ €). Si tu tires $144$ clients au sort, la $p$-value est la probabilité d'observer un écart d'au moins $\pm 6{,}26$ € par pur hasard. Ici elle vaut $11{,}94\%$ : c'est trop banal pour rejeter $H_0$, même à $\alpha = 10\%$.

> [!abstract] 🔎 Pourquoi cette méthode ? (indices de l'énoncé → choix)
> | Indice lu dans l'énoncé | Ce que ça implique |
> | :--- | :--- |
> | « vérifier si la mensualité moyenne vaut $\mu_0 = 200$ € » | Test de conformité d'une moyenne contre une norme ; le mot « vaut » donne un test bilatéral ($\ne 200$). |
> | $n = 144 \ge 30$, même avec $\sigma$ inconnu (on a $s$) | Grand échantillon : le TCL garantit que $Z$ suit approximativement $\mathcal{N}(0, 1)$. |
> 
> **Donc :** test $Z$ bilatéral sur moyenne, seuil critique $\pm 1{,}96$ à $5\%$.

### Les formules utilisées
**Formules mathématiques :**
$$H_0 : \mu = 200 \quad \text{vs} \quad H_1 : \mu \ne 200$$
$$\text{ES} = \frac{s}{\sqrt{n}}, \qquad z_{\text{obs}} = \frac{\bar{x} - \mu_0}{s / \sqrt{n}}, \qquad e = U_{1-\alpha/2} \cdot \frac{s}{\sqrt{n}}$$
$$\text{IC}_{1-\alpha}(\mu) = \left[\bar{x} - e \,;\, \bar{x} + e\right], \qquad \text{Zone d'acceptation de } H_0 = \left[\mu_0 - e \,;\, \mu_0 + e\right], \qquad p\text{-value} = 2\big(1 - \Phi(|z_{\text{obs}}|)\big)$$

**En français simple :**
`Erreur standard = Écart-type ÷ √Effectif`
`Score Z = (Moyenne mesurée - Moyenne prétendue) ÷ Erreur standard`
`Borne inf = Centre - (U × Erreur standard)` et `Borne sup = Centre + (U × Erreur standard)`

### Résolution détaillée pas-à-pas

#### 1. Hypothèses et type de test
On pose un **test bilatéral de conformité** sur une moyenne :
$$H_0 : \mu = 200\text{ €} \qquad \text{contre} \qquad H_1 : \mu \ne 200\text{ €}$$
Comme $n = 144 \ge 30$ (grand échantillon), par le Théorème Central Limite (TCL), la statistique $Z$ suit approximativement la loi normale centrée réduite $\mathcal{N}(0, 1)$ sous $H_0$.

#### 2. Décision au risque $\alpha = 5\%$
1. **Calcul de l'erreur standard ($\text{ES}$) :**
   $$\text{ES} = \frac{s}{\sqrt{n}} = \frac{48{,}24}{\sqrt{144}} = \frac{48{,}24}{12} = \mathbf{4{,}02\text{ €}}$$
2. **Calcul de la statistique observée ($z_{\text{obs}}$) :**
   $$z_{\text{obs}} = \frac{\bar{x} - \mu_0}{s / \sqrt{n}} = \frac{193{,}74 - 200}{4{,}02} = \frac{-6{,}26}{4{,}02} \approx \mathbf{-1{,}5572}$$
3. **Lecture du quantile et calcul de la marge d'erreur ($e$) :**
   - À $\alpha = 5\% = 0{,}05$ en bilatéral, on calcule $\Phi(U_{1-\alpha/2}) = 1 - \frac{0{,}05}{2} = 1 - 0{,}025 = 0{,}9750$. En Annexe A.1 (ligne `1,9`, col. `0,06`), on lit $U_{0{,}975} = \mathbf{1{,}96}$, d'où les seuils critiques $z_{\text{crit}} = \pm 1{,}96$.
   - Marge d'erreur :
     $$e = U_{1-\alpha/2} \times \frac{s}{\sqrt{n}} = 1{,}96 \times 4{,}02 = 7{,}8792 \approx \mathbf{7{,}88\text{ €}}$$
4. **Calcul des bornes inférieures et supérieures :**
   - **Intervalle d'acceptation de $H_0$** (centré sur $\mu_0 = 200$ €) :
     - Borne inférieure : $\mu_0 - e = 200 - 7{,}88 = \mathbf{192{,}12\text{ €}}$
     - Borne supérieure : $\mu_0 + e = 200 + 7{,}88 = \mathbf{207{,}88\text{ €}}$
   - **Intervalle de confiance à $95\%$ de $\mu$** (centré sur $\bar{x} = 193{,}74$ €) :
     - Borne inférieure : $\bar{x} - e = 193{,}74 - 7{,}88 = \mathbf{185{,}86\text{ €}}$
     - Borne supérieure : $\bar{x} + e = 193{,}74 + 7{,}88 = \mathbf{201{,}62\text{ €}}$

Comme $|z_{\text{obs}}| = 1{,}5572 < 1{,}96$ (équivalent à $193{,}74 \in [192{,}12 \,;\, 207{,}88]$ et $\mu_0 = 200 \in [185{,}86 \,;\, 201{,}62]$), **on ne rejette pas $H_0$**.

#### 3 & 4. Schéma des régions et $p$-value
```text
             Densité N(0,1) sous H0
                      ^
                     / \
                    /   \
   Rejet (α/2)     /  |  \      Rejet (α/2)
   p/2   |        /   |   \         |  p/2
  ███████░░░░░░░░/░░░░|░░░░\░░░░░░░░███████
 ────────┴───────┴────┼────┴───────┴────────> Z
       -1,96  -1,56   0  +1,56   +1,96
       (192,12€)         (207,88€)
  ████ Région de rejet α = 5% (|Z| > 1,96)
  ░░░░ Aires correspondant à la p-value totale = 2 × P(Z ≤ -1,5572)
```
Par lecture de l'Annexe A.1 (ligne `1,5`, col. `0,06`, soit $\Phi(1{,}56) = 0{,}9406$) :
$$p\text{-value} = 2\big(1 - \Phi(|z_{\text{obs}}|)\big) \approx 2(1 - 0{,}9406) = 2 \times 0{,}0594 = \mathbf{0{,}1188} \quad (\text{exact : } \mathbf{0{,}1194}, \text{ soit } \mathbf{11{,}94\%})$$

#### 5. Réponse pour $\alpha = 10\%$
À $\alpha = 10\% = 0{,}10$ en bilatéral :
- $\Phi(U_{1-\alpha/2}) = 1 - \frac{0{,}10}{2} = 0{,}9500 \implies U_{0{,}95} = \mathbf{1{,}6449}$.
- Marge d'erreur : $e = U_{0{,}95} \times \text{ES} = 1{,}6449 \times 4{,}02 = 6{,}6125 \approx \mathbf{6{,}61\text{ €}}$.
- Zone d'acceptation de $H_0$ : $[200 - 6{,}61 \,;\, 200 + 6{,}61] = \mathbf{[193{,}39 \,;\, 206{,}61]\text{ €}}$ (et $\text{IC}_{90\%}(\mu) = [193{,}74 - 6{,}61 \,;\, 193{,}74 + 6{,}61] = \mathbf{[187{,}13 \,;\, 200{,}35]\text{ €}}$).
- Comme $p\text{-value} = 0{,}1194 > \alpha = 0{,}10$ (et $|z_{\text{obs}}| = 1{,}5572 < 1{,}6449$), **on ne rejette toujours pas $H_0$** au risque de $10\%$.

> [!check] Conclusion concrète
> Au seuil de $5\%$ comme à $10\%$, l'écart observé ($193{,}74$ € vs $200$ €) est compatible avec les fluctuations d'échantillonnage : la valeur moyenne postulée de $200$ € reste plausible.

---

## 📌 Exercice 2 – Parité dans les filières informatiques

> [!question] Énoncé résumé & Données
> Dans une promotion de Master IT à Lomé de $n = 64$ étudiants, on compte $k = 28$ femmes. Peut-on soutenir que la filière attire autant les hommes que les femmes ($p_0 = 0{,}50$, $\alpha = 5\%$) ?

> [!info] Comprendre la logique (terre à terre)
> **Pourquoi mettre $p_0$ et pas $f$ sous la racine carrée ?**
> Contrairement à un intervalle de confiance (où $p$ est inconnu et remplacé par $f$), dans un test d'hypothèse on se place **dans le monde où $H_0$ est vraie** ($p = 0{,}50$). On calcule donc la variabilité théorique avec $p_0(1 - p_0)$.

> [!abstract] 🔎 Pourquoi cette méthode ? (indices de l'énoncé → choix)
> | Indice lu dans l'énoncé | Ce que ça implique |
> | :--- | :--- |
> | « $k = 28$ femmes sur $n = 64$ », « attire autant les hommes que les femmes » | Conformité d'une proportion face à $p_0 = 0{,}50$, test bilatéral ($p \ne 0{,}50$). |
> | $np_0 = 32 \ge 5$ et $n(1 - p_0) = 32 \ge 5$ | Approximation normale valide ; sous $H_0$, l'erreur standard utilise $p_0$ (et non $f$). |
> 
> **Donc :** test $Z$ bilatéral sur proportion avec $p_0(1 - p_0)$ au dénominateur.

### Les formules utilisées
**Formules mathématiques :**
$$f = \frac{k}{n}, \qquad H_0 : p = 0{,}50 \quad \text{vs} \quad H_1 : p \ne 0{,}50$$
$$\text{ES}_0 = \sqrt{\frac{p_0(1 - p_0)}{n}}, \qquad z_{\text{obs}} = \frac{f - p_0}{\text{ES}_0}, \qquad p\text{-value} = 2\big(1 - \Phi(|z_{\text{obs}}|)\big)$$

**En français simple :**
`Fréquence observée = Nb de femmes ÷ Effectif total`
`Score Z = (Fréquence observée - 0,50) ÷ √(0,50 × 0,50 ÷ Effectif)`

### Résolution détaillée pas-à-pas

#### 1. Hypothèses et conditions d'application
On calcule d'abord la proportion observée :
$$f = \frac{k}{n} = \frac{28}{64} = \mathbf{0{,}4375} \quad (43{,}75\%)$$
On formule un **test bilatéral de conformité d'une proportion** :
$$H_0 : p = 0{,}50 \qquad \text{contre} \qquad H_1 : p \ne 0{,}50$$
Vérification des conditions de l'approximation normale :
$$n p_0 = 64 \times 0{,}50 = 32 \ge 5 \qquad \text{et} \qquad n(1 - p_0) = 64 \times (1 - 0{,}50) = 32 \ge 5 \quad (\text{conditions validées})$$

#### 2. Statistique de test, seuil critique et $p$-value
1. **Erreur standard sous $H_0$ :**
   $$\text{ES}_0 = \sqrt{\frac{p_0(1 - p_0)}{n}} = \sqrt{\frac{0{,}50 \times 0{,}50}{64}} = \sqrt{\frac{0{,}25}{64}} = \frac{0{,}50}{8} = \mathbf{0{,}0625}$$
2. **Statistique observée ($z_{\text{obs}}$) :**
   $$z_{\text{obs}} = \frac{f - p_0}{\text{ES}_0} = \frac{0{,}4375 - 0{,}50}{0{,}0625} = \frac{-0{,}0625}{0{,}0625} = \mathbf{-1{,}00}$$
3. **Seuil critique et $p$-value :**
   À $\alpha = 5\%$ bilatéral ($\Phi(u) = 0{,}9750$ en Annexe A.1), $z_{\text{crit}} = \pm 1{,}96$. Avec $\Phi(1{,}00) = 0{,}8413$ (Annexe A.1, ligne `1,0`, col. `0,00`) :
   $$p\text{-value} = 2\big(1 - \Phi(|z_{\text{obs}}|)\big) = 2(1 - 0{,}8413) = 2 \times 0{,}1587 = \mathbf{0{,}3174} \quad (31{,}74\%)$$

> [!check] Conclusion concrète
> Comme $|z_{\text{obs}}| = 1{,}00 < 1{,}96$ ($p = 0{,}3174 > 0{,}05$), **on ne rejette pas $H_0$** : l'écart observé ne permet pas de contester l'égale attractivité de la filière auprès des hommes et des femmes.

---

## 📌 Exercice 3 – Variabilité sur les scores d'évaluation

> [!question] Énoncé résumé & Données
> La Direction de l'Évaluation sélectionne $n = 30$ étudiants pour un test standardisé dont l'écart-type ne doit pas dépasser $\sigma_0 = 20$ points ($\sigma_0^2 = 20^2 = 400$), au risque $\alpha = 5\%$. On demande d'estimer $\sigma$ sans biais puis de réaliser le test d'hypothèse.

> [!info] Comprendre la logique (terre à terre)
> **Attention à la condition cachée :**
> Le test du $\chi^2$ sur une variance exige impérativement que les scores suivent une **loi normale** (contrairement aux tests sur la moyenne avec $n \ge 30$, le TCL ne protège pas la variance).
>
> **Lecture de la table (Annexe B) :**
> Pour un test unilatéral droit ($H_1 : \sigma > 20$), tout le risque $\alpha = 5\%$ est placé dans la queue droite : on lit directement la ligne $\nu = n - 1 = 29$ et la colonne `0,05` ($\chi^2_{0{,}95}(29) = 42{,}5570$).

> [!abstract] 🔎 Pourquoi cette méthode ? (indices de l'énoncé → choix)
> | Indice lu dans l'énoncé | Ce que ça implique |
> | :--- | :--- |
> | « l'écart-type ne doit pas dépasser $\sigma_0 = 20$ points » | Test de conformité sur une variance ; « dépasser » impose un test unilatéral droit ($\sigma > 20$). |
> | Statistique sur la dispersion | Exige la normalité stricte de la population ; la statistique suit un $\chi^2(n - 1)$. |
> 
> **Donc :** test du $\chi^2$ unilatéral droit avec $V = \frac{(n - 1)s^2}{\sigma_0^2}$.

### Les formules utilisées
**Formules mathématiques :**
$$\bar{x} = \frac{1}{n}\sum_{i=1}^n x_i, \qquad \bar{s}^2 = \frac{1}{n}\sum_{i=1}^n (x_i - \bar{x})^2, \qquad s^2 = \frac{1}{n - 1}\sum_{i=1}^n (x_i - \bar{x})^2 = \frac{\sum_{i=1}^n x_i^2 - n\bar{x}^2}{n - 1}$$
$$s = \sqrt{s^2}, \qquad V = \frac{(n - 1)s^2}{\sigma_0^2} \sim \chi^2(n - 1)$$

**En français simple :**
`Statistique V = Somme des carrés des écarts ÷ Variance maximale tolérée (400)`

### Résolution détaillée pas-à-pas

#### 1. Estimation sans biais de $\sigma$ ($n = 30$)

| Étudiant $i$ | $x_i$ | $x_i - \bar{x}$ | $(x_i - \bar{x})^2$ | $x_i^2$ *(Koenig-Huygens)* |
| :---: | :---: | :---: | :---: | :---: |
| 1 | $131$ | $+27$ | $729$ | $17\,161$ |
| 2 | $108$ | $+4$ | $16$ | $11\,664$ |
| 3 | $85$ | $-19$ | $361$ | $7\,225$ |
| 4 | $96$ | $-8$ | $64$ | $9\,216$ |
| 5 | $86$ | $-18$ | $324$ | $7\,396$ |
| 6 | $126$ | $+22$ | $484$ | $15\,876$ |
| 7 | $128$ | $+24$ | $576$ | $16\,384$ |
| 8 | $107$ | $+3$ | $9$ | $11\,449$ |
| 9 | $119$ | $+15$ | $225$ | $14\,161$ |
| 10 | $87$ | $-17$ | $289$ | $7\,569$ |
| 11 | $103$ | $-1$ | $1$ | $10\,609$ |
| 12 | $110$ | $+6$ | $36$ | $12\,100$ |
| 13 | $125$ | $+21$ | $441$ | $15\,625$ |
| 14 | $77$ | $-27$ | $729$ | $5\,929$ |
| 15 | $90$ | $-14$ | $196$ | $8\,100$ |
| 16 | $109$ | $+5$ | $25$ | $11\,881$ |
| 17 | $109$ | $+5$ | $25$ | $11\,881$ |
| 18 | $129$ | $+25$ | $625$ | $16\,641$ |
| 19 | $95$ | $-9$ | $81$ | $9\,025$ |
| 20 | $117$ | $+13$ | $169$ | $13\,689$ |
| 21 | $107$ | $+3$ | $9$ | $11\,449$ |
| 22 | $102$ | $-2$ | $4$ | $10\,404$ |
| 23 | $83$ | $-21$ | $441$ | $6\,889$ |
| 24 | $114$ | $+10$ | $100$ | $12\,996$ |
| 25 | $72$ | $-32$ | $1\,024$ | $5\,184$ |
| 26 | $99$ | $-5$ | $25$ | $9\,801$ |
| 27 | $103$ | $-1$ | $1$ | $10\,609$ |
| 28 | $97$ | $-7$ | $49$ | $9\,409$ |
| 29 | $109$ | $+5$ | $25$ | $11\,881$ |
| 30 | $97$ | $-7$ | $49$ | $9\,409$ |
| **Total ($\sum$)** | **$3\,120$** | **$0$** | **$7\,132$** | **$331\,612$** |

- **Moyenne empirique :**
  $$\bar{x} = \frac{1}{n}\sum_{i=1}^{30} x_i = \frac{3\,120}{30} = \mathbf{104{,}00\text{ points}}$$
- **Variance corrigée (sans biais) :**
  $$s^2 = \frac{1}{n - 1}\sum_{i=1}^{30}(x_i - \bar{x})^2 = \frac{7\,132}{30 - 1} = \frac{7\,132}{29} \approx \mathbf{245{,}9310}$$
  *(Vérification par Koenig-Huygens : $s^2 = \frac{331\,612 - 30 \times 104^2}{29} = \frac{331\,612 - 324\,480}{29} = \frac{7\,132}{29} \approx 245{,}9310$. La variance biaisée vaudrait $\bar{s}^2 = \frac{7\,132}{30} \approx 237{,}7333$.)*
- **Écart-type corrigé :**
  $$s = \sqrt{s^2} = \sqrt{245{,}9310} \approx \mathbf{15{,}6822\text{ points}}$$

#### 2. Test sur l'écart-type ($\sigma_0 = 20 \implies \sigma_0^2 = 400$, $\alpha = 5\%$)
**Hypothèse préalable indispensable :**
Les $30$ scores doivent former un échantillon iid issu d'une **loi normale** pour que la loi du $\chi^2$ soit valide.

On teste unilatéralement à droite :
$$H_0 : \sigma \le 20 \ (\sigma^2 \le 400) \qquad \text{contre} \qquad H_1 : \sigma > 20 \ (\sigma^2 > 400)$$
$$V = \frac{(n - 1)s^2}{\sigma_0^2} = \frac{29 \times 245{,}9310}{20^2} = \frac{7\,132}{400} = \mathbf{17{,}8300} \sim \chi^2(29)$$
En Annexe B ($\nu = 29$, colonne `0,05`), le seuil critique vaut $\chi^2_{0{,}95}(29) = \mathbf{42{,}5570}$.

> [!check] Conclusion concrète
> Comme $V = 17{,}8300 < 42{,}5570$ ($p = 0{,}9477$), **on ne rejette pas $H_0$** : l'exigence d'homogénéité ($\sigma \le 20$) est largement respectée ($s = 15{,}68 < 20$).

---

## 📌 Exercice 4 – Conformité d'une norme d'aménagement municipal

> [!question] Énoncé résumé & Données
> Une réglementation impose aux communes de consacrer au moins $25\%$ de leur budget aux infrastructures numériques. On relève ces pourcentages dans $n = 10$ communes (supposés normaux) au risque $\alpha = 2{,}5\%$ :
> `25.6, 24.5, 24.3, 25.0, 29.5, 24.1, 24.8, 24.7, 25.2, 24.9`

> [!info] Comprendre la logique (terre à terre)
> **Comment lire la table de Student (Annexe C) pour un test unilatéral ?**
> La table indique souvent le risque **bilatéral** (les deux queues additionnées). Si ton test est **unilatéral à $\alpha = 2{,}5\%$** (une seule queue à gauche), cherche la colonne où chaque queue vaut $2{,}5\%$, donc la colonne bilatérale **$2\alpha = 5\% = 0{,}050$** !
>
> **L'esprit critique de l'ingénieur :**
> La moyenne ($25{,}26\%$) dépasse $25\%$, donc le test valide la norme. Mais regarde les $10$ lignes du tableau : **$7$ communes sur $10$ sont sous $25\%$** ! Une seule commune à $29{,}5\%$ tire toute la moyenne vers le haut.

> [!abstract] 🔎 Pourquoi cette méthode ? (indices de l'énoncé → choix)
> | Indice lu dans l'énoncé | Ce que ça implique |
> | :--- | :--- |
> | « consacrer au moins $25\%$ » | $H_0 : \mu \ge 25\%$ contre $H_1 : \mu < 25\%$ (unilatéral gauche). |
> | $n = 10 < 30$, supposés normaux, $\sigma$ inconnu | Petit échantillon normal avec écart-type estimé $s$ : loi de Student $t(9)$. |
> 
> **Donc :** test $t$ de Student unilatéral gauche, lu en colonne bilatérale $2\alpha = 0{,}050$ à $\nu = 9$.

### Les formules utilisées
**Formules mathématiques :**
$$H_0 : \mu \ge 25 \quad \text{vs} \quad H_1 : \mu < 25$$
$$\bar{x} = \frac{1}{n}\sum_{i=1}^n x_i, \qquad s^2 = \frac{1}{n - 1}\sum_{i=1}^n (x_i - \bar{x})^2, \qquad \text{ES} = \frac{s}{\sqrt{n}}, \qquad t_{\text{obs}} = \frac{\bar{x} - \mu_0}{\text{ES}} \sim t(n - 1)$$

**En français simple :**
`t_obs = (Moyenne des 10 communes - Norme 25) ÷ (Écart-type corrigé ÷ √10)`

### Résolution détaillée pas-à-pas

#### 1. Hypothèses et estimations ($n = 10$)
On réalise un test unilatéral gauche :
$$H_0 : \mu \ge 25\% \ (\text{norme respectée}) \qquad \text{contre} \qquad H_1 : \mu < 25\% \ (\text{quota non respecté})$$

| Commune $i$ | $x_i$ (%) | $x_i - \bar{x}$ | $(x_i - \bar{x})^2$ | $x_i^2$ *(Koenig-Huygens)* |
| :---: | :---: | :---: | :---: | :---: |
| 1 | $25{,}6$ | $+0{,}34$ | $0{,}1156$ | $655{,}36$ |
| 2 | $24{,}5$ | $-0{,}76$ | $0{,}5776$ | $600{,}25$ |
| 3 | $24{,}3$ | $-0{,}96$ | $0{,}9216$ | $590{,}49$ |
| 4 | $25{,}0$ | $-0{,}26$ | $0{,}0676$ | $625{,}00$ |
| 5 | $29{,}5$ | $+4{,}24$ | $17{,}9776$ | $870{,}25$ |
| 6 | $24{,}1$ | $-1{,}16$ | $1{,}3456$ | $580{,}81$ |
| 7 | $24{,}8$ | $-0{,}46$ | $0{,}2116$ | $615{,}04$ |
| 8 | $24{,}7$ | $-0{,}56$ | $0{,}3136$ | $610{,}09$ |
| 9 | $25{,}2$ | $-0{,}06$ | $0{,}0036$ | $635{,}04$ |
| 10 | $24{,}9$ | $-0{,}36$ | $0{,}1296$ | $620{,}01$ |
| **Total ($\sum$)** | **$252{,}6$** | **$0$** | **$21{,}6640$** | **$6\,402{,}34$** |

- **Moyenne empirique :**
  $$\bar{x} = \frac{1}{n}\sum_{i=1}^{10} x_i = \frac{252{,}6}{10} = \mathbf{25{,}26\%}$$
- **Variance corrigée et écart-type :**
  $$s^2 = \frac{1}{n - 1}\sum_{i=1}^{10}(x_i - \bar{x})^2 = \frac{21{,}6640}{10 - 1} = \frac{21{,}6640}{9} \approx \mathbf{2{,}4071}$$
  *(Koenig-Huygens : $s^2 = \frac{6\,402{,}34 - 10 \times 25{,}26^2}{9} = \frac{6\,402{,}34 - 6\,380{,}676}{9} = \frac{21{,}664}{9} \approx 2{,}4071$.)*
  $$s = \sqrt{2{,}4071} \approx \mathbf{1{,}5515\%}$$

#### 2. Statistique $t$, lecture de la table de Student et décision
1. **Erreur standard ($\text{ES}$) :**
   $$\text{ES} = \frac{s}{\sqrt{n}} = \frac{1{,}5515}{\sqrt{10}} = \frac{1{,}5515}{3{,}1623} \approx \mathbf{0{,}4906\%}$$
2. **Statistique observée ($t_{\text{obs}}$) :**
   $$t_{\text{obs}} = \frac{\bar{x} - \mu_0}{\text{ES}} = \frac{25{,}26 - 25}{0{,}4906} = \frac{+0{,}26}{0{,}4906} \approx \mathbf{+0{,}5299} \sim t(9)$$
3. **Seuil critique :** en unilatéral gauche à $\alpha = 2{,}5\%$, on lit l'Annexe C à la ligne $\nu = 10 - 1 = 9$ et dans la colonne bilatérale $2\alpha = 0{,}050$ : la valeur critique vaut $-t_{9,\, 0{,}975} = \mathbf{-2{,}2622}$ (région de rejet $]-\infty \,;\, -2{,}2622[$).

> [!check] Conclusion concrète
> Comme $t_{\text{obs}} = +0{,}53 > -2{,}2622$ ($p = 0{,}6090$ en bilatéral), **on ne rejette pas $H_0$** : les communes respectent statistiquement le quota en moyenne à $\alpha = 2{,}5\%$ *(nuance critique : $7$ communes sur $10$ sont légèrement sous $25\%$, la moyenne étant tirée vers le haut par l'observation extrême à $29{,}5\%$)*.

---

## 📌 Exercice 5 – Test d'ajustement du Khi-deux et dimensionnement

> [!question] Énoncé résumé & Données
> Une plateforme d'assistance à Lomé relève pendant $n = 53$ heures le nombre d'appels reçus par heure ($x_i \in \{0, \dots, 9\}$) et le nombre d'heures correspondantes ($N_i$) :
> `x_i = 0 (1h), 1 (4h), 2 (7h), 3 (11h), 4 (10h), 5 (9h), 6 (5h), 7 (3h), 8 (2h), 9 (1h)`.
> On demande d'estimer l'espérance et la variance, de tester l'ajustement à la loi candidate au risque $\alpha = 5\%$, puis de trouver combien d'opérateurs (capacité $7$ appels/h chacun) couvrent au moins $95\%$ des appels.

> [!info] Comprendre la logique (terre à terre)
> **Pourquoi fusionner les petites classes jusqu'à $E_i \ge 5$ ?**
> Regarde la fraction $\frac{(O_i - E_i)^2}{E_i}$ : si $E_i$ est minuscule (par ex. $E_0 = 0{,}97$), un écart banal de $1$ appel divise par $0{,}97$ et fait exploser artificiellement le $\chi^2$. Exiger $E_i \ge 5$ garantit que la statistique suit bien la loi du $\chi^2$.
>
> **Pourquoi retirer $1 + 1 = 2$ aux degrés de liberté ?**
> On part de $6$ classes après regroupement. On perd $1$ ddl car le total est fixé à $53$, et on perd encore $1$ ddl parce que le paramètre $\lambda = 4$ n'était pas connu d'avance mais estimé sur l'échantillon. Il reste $6 - 2 = 4$ ddl.

> [!abstract] 🔎 Pourquoi cette méthode ? (indices de l'énoncé → choix)
> | Indice lu dans l'énoncé | Ce que ça implique |
> | :--- | :--- |
> | « tester l'ajustement à la loi candidate » | Comparer des effectifs observés à une loi théorique : test d'ajustement du $\chi^2$. |
> | Comptage horaire avec $\bar{x} = 4{,}00 \approx s^2 = 3{,}92$ | Loi candidate = Poisson $\mathcal{P}(\lambda = 4)$ ; $\lambda$ estimé retire $1$ ddl ($\nu = c - 1 - 1$). |
> | « couvrent au moins $95\%$ des appels » | Additionner les probabilités $P(X \le k)$ jusqu'à atteindre $0{,}95$. |
> 
> **Donc :** $\chi^2$ d'ajustement avec regroupement $E_i \ge 5$ et $\nu = c - 1 - 1$.

### Les formules utilisées
**Formules mathématiques :**
$$\bar{x} = \frac{1}{n}\sum N_i x_i, \qquad \bar{s}^2 = \frac{1}{n}\sum N_i (x_i - \bar{x})^2 = \frac{1}{n}\sum N_i x_i^2 - \bar{x}^2, \qquad s^2 = \frac{1}{n - 1}\sum N_i (x_i - \bar{x})^2$$
$$p_k = e^{-\lambda}\frac{\lambda^k}{k!}, \qquad E_k = n \cdot p_k, \qquad \chi^2_{\text{obs}} = \sum_{i=1}^{c} \frac{(O_i - E_i)^2}{E_i}, \qquad \nu = c - 1 - p$$

**En français simple :**
`Moyenne = Somme de (Nb d'heures × Nb d'appels) ÷ 53`
`Effectif attendu E_k = 53 × Probabilité théorique de Poisson`
`χ² observé = Somme des (Nb d'heures réel - Nb d'heures théorique)² ÷ Nb d'heures théorique`

### Résolution détaillée pas-à-pas

#### 1. Espérance, variance et loi candidate ($n = 53$ heures)
On construit le tableau des effectifs pour calculer $\bar{x}$, $\bar{s}^2$ et $s^2$ :

| $x_i$ (appels/h) | $N_i$ (heures) | $N_i x_i$ | $x_i - \bar{x}$ | $N_i(x_i - \bar{x})^2$ | $N_i x_i^2$ *(Koenig-Huygens)* |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 0 | 1 | $1 \times 0 = 0$ | $0 - 4 = -4$ | $1 \times (-4)^2 = 16$ | $1 \times 0^2 = 0$ |
| 1 | 4 | $4 \times 1 = 4$ | $1 - 4 = -3$ | $4 \times (-3)^2 = 36$ | $4 \times 1^2 = 4$ |
| 2 | 7 | $7 \times 2 = 14$ | $2 - 4 = -2$ | $7 \times (-2)^2 = 28$ | $7 \times 2^2 = 28$ |
| 3 | 11 | $11 \times 3 = 33$ | $3 - 4 = -1$ | $11 \times (-1)^2 = 11$ | $11 \times 3^2 = 99$ |
| 4 | 10 | $10 \times 4 = 40$ | $4 - 4 = 0$ | $10 \times 0^2 = 0$ | $10 \times 4^2 = 160$ |
| 5 | 9 | $9 \times 5 = 45$ | $5 - 4 = +1$ | $9 \times 1^2 = 9$ | $9 \times 5^2 = 225$ |
| 6 | 5 | $5 \times 6 = 30$ | $6 - 4 = +2$ | $5 \times 2^2 = 20$ | $5 \times 6^2 = 180$ |
| 7 | 3 | $3 \times 7 = 21$ | $7 - 4 = +3$ | $3 \times 3^2 = 27$ | $3 \times 7^2 = 147$ |
| 8 | 2 | $2 \times 8 = 16$ | $8 - 4 = +4$ | $2 \times 4^2 = 32$ | $2 \times 8^2 = 128$ |
| 9 | 1 | $1 \times 9 = 9$ | $9 - 4 = +5$ | $1 \times 5^2 = 25$ | $1 \times 9^2 = 81$ |
| **Total ($\sum$)** | **$53$** | **$212$** | — | **$204$** | **$1\,052$** |

- **Espérance estimée (moyenne empirique) :**
  $$\bar{x} = \frac{1}{n}\sum N_i x_i = \frac{212}{53} = \mathbf{4{,}00\text{ appels/h}}$$
- **Variance empirique (biaisée, $\div n$) :**
  $$\bar{s}^2 = \frac{1}{n}\sum N_i(x_i - \bar{x})^2 = \frac{204}{53} \approx \mathbf{3{,}8491}$$
  *(Vérification Koenig-Huygens : $\bar{s}^2 = \frac{\sum N_i x_i^2}{n} - \bar{x}^2 = \frac{1\,052}{53} - 4^2 = 19{,}8491 - 16 = 3{,}8491$.)*
- **Variance corrigée (sans biais, $\div (n - 1)$) :**
  $$s^2 = \frac{1}{n - 1}\sum N_i(x_i - \bar{x})^2 = \frac{204}{53 - 1} = \frac{204}{52} \approx \mathbf{3{,}9231}$$
  *(Vérification Koenig-Huygens : $s^2 = \frac{1\,052 - 53 \times 4^2}{52} = \frac{1\,052 - 848}{52} = \frac{204}{52} \approx 3{,}9231$.)*

Comme $\bar{x} = 4{,}00 \approx s^2 = 3{,}9231$ sur un comptage discret d'événements par heure, on propose et teste l'ajustement à une **loi de Poisson $\mathcal{P}(\lambda = 4)$** ($H_0 : X \sim \mathcal{P}(4)$ contre $H_1 : X \not\sim \mathcal{P}(4)$).

#### 2. Test d'ajustement du $\chi^2$ au risque $\alpha = 5\%$
On calcule les probabilités théoriques $p_k = e^{-4}\frac{4^k}{k!}$ (avec $e^{-4} \approx 0{,}018316$) et les effectifs attendus $E_k = 53 \times p_k$ **avant regroupement** :

| $k$ | Calcul de $p_k = e^{-4}\dfrac{4^k}{k!}$ | Probabilité $p_k$ | Calcul de $E_k = 53 \times p_k$ | Effectif attendu $E_k$ |
| :---: | :--- | :---: | :--- | :---: |
| $0$ | $0{,}018316 \times \frac{4^0}{0!} = 0{,}018316 \times 1$ | $0{,}01832$ | $53 \times 0{,}018316$ | $0{,}9707$ *(à regrouper)* |
| $1$ | $0{,}018316 \times \frac{4^1}{1!} = 0{,}018316 \times 4$ | $0{,}07326$ | $53 \times 0{,}073263$ | $3{,}8829$ *(à regrouper)* |
| $2$ | $0{,}018316 \times \frac{4^2}{2!} = 0{,}018316 \times \frac{16}{2}$ | $0{,}14653$ | $53 \times 0{,}146525$ | $7{,}7658$ *(regroupé avec $0,1$)* |
| $3$ | $0{,}018316 \times \frac{4^3}{3!} = 0{,}018316 \times \frac{64}{6}$ | $0{,}19537$ | $53 \times 0{,}195367$ | $10{,}3544$ |
| $4$ | $0{,}018316 \times \frac{4^4}{4!} = 0{,}018316 \times \frac{256}{24}$ | $0{,}19537$ | $53 \times 0{,}195367$ | $10{,}3544$ |
| $5$ | $0{,}018316 \times \frac{4^5}{5!} = 0{,}018316 \times \frac{1\,024}{120}$ | $0{,}15629$ | $53 \times 0{,}156293$ | $8{,}2836$ |
| $6$ | $0{,}018316 \times \frac{4^6}{6!} = 0{,}018316 \times \frac{4\,096}{720}$ | $0{,}10420$ | $53 \times 0{,}104196$ | $5{,}5224$ |
| $7$ | $0{,}018316 \times \frac{4^7}{7!} = 0{,}018316 \times \frac{16\,384}{5\,040}$ | $0{,}05954$ | $53 \times 0{,}059540$ | $3{,}1556$ *(à regrouper)* |
| $8$ | $0{,}018316 \times \frac{4^8}{8!} = 0{,}018316 \times \frac{65\,536}{40\,320}$ | $0{,}02977$ | $53 \times 0{,}029770$ | $1{,}5778$ *(à regrouper)* |
| $9+$ | $1 - \sum_{k=0}^8 p_k = 1 - 0{,}97864$ | $0{,}02136$ | $53 \times 0{,}021364$ | $1{,}1323$ *(à regrouper)* |

Pour respecter strictement la condition **$E_i \ge 5$** dans chaque classe, on fusionne les classes extrêmes :
- **Classe `0–2` :** $O = 1 + 4 + 7 = \mathbf{12}$ ; $E = 0{,}9707 + 3{,}8829 + 7{,}7658 = \mathbf{12{,}6195} \ge 5$.
- **Classe `7 et +` :** $O = 3 + 2 + 1 = \mathbf{6}$ ; $E = 3{,}1556 + 1{,}5778 + 1{,}1323 = \mathbf{5{,}8657} \ge 5$.

| Classe | $O_i$ | $E_i$ | Calcul de $\dfrac{(O_i - E_i)^2}{E_i}$ | Contribution |
| :--- | :---: | :---: | :--- | :---: |
| **0–2** | 12 | 12,6195 | $\frac{(12 - 12{,}6195)^2}{12{,}6195} = \frac{(-0{,}6195)^2}{12{,}6195} = \frac{0{,}3838}{12{,}6195}$ | $0{,}0304$ |
| **3** | 11 | 10,3544 | $\frac{(11 - 10{,}3544)^2}{10{,}3544} = \frac{0{,}6456^2}{10{,}3544} = \frac{0{,}4168}{10{,}3544}$ | $0{,}0402$ |
| **4** | 10 | 10,3544 | $\frac{(10 - 10{,}3544)^2}{10{,}3544} = \frac{(-0{,}3544)^2}{10{,}3544} = \frac{0{,}1256}{10{,}3544}$ | $0{,}0121$ |
| **5** | 9 | 8,2836 | $\frac{(9 - 8{,}2836)^2}{8{,}2836} = \frac{0{,}7164^2}{8{,}2836} = \frac{0{,}5132}{8{,}2836}$ | $0{,}0620$ |
| **6** | 5 | 5,5224 | $\frac{(5 - 5{,}5224)^2}{5{,}5224} = \frac{(-0{,}5224)^2}{5{,}5224} = \frac{0{,}2729}{5{,}5224}$ | $0{,}0494$ |
| **7 et +** | 6 | 5,8657 | $\frac{(6 - 5{,}8657)^2}{5{,}8657} = \frac{0{,}1343^2}{5{,}8657} = \frac{0{,}0180}{5{,}8657}$ | $0{,}0031$ |
| **Total ($\sum$)** | **53** | **53,0000** | $0{,}0304 + 0{,}0402 + 0{,}0121 + 0{,}0620 + 0{,}0494 + 0{,}0031$ | **$\chi^2_{\text{obs}} = 0{,}1972$** |

Nombre de degrés de liberté ($c = 6$ classes après regroupement, $p = 1$ paramètre $\lambda$ estimé sur les données) :
$$\nu = c - 1 - p = 6 - 1 - 1 = \mathbf{4}$$
En Annexe B ($\nu = 4$, colonne `0,05`), $\chi^2_{0{,}95}(4) = \mathbf{9{,}4877}$. Comme $\chi^2_{\text{obs}} = 0{,}1972 \ll 9{,}4877$ ($p = 0{,}9954$), on ne rejette pas $H_0$ : l'ajustement à $\mathcal{P}(4)$ est excellent. *(Avec le regroupement $\{0,1\}$ [$E=4{,}85$] et $\{6+\}$, $\chi^2 = 0{,}2075$, même conclusion.)*

#### 3. Nombre d'opérateurs pour répondre à au moins $95\%$ des appels
Un opérateur traite au plus $7$ appels/h. Sous $X \sim \mathcal{P}(4)$, on additionne les probabilités $p_k$ calculées à la question 2 :
- **Pour $1$ opérateur ($X \le 7$) :**
  $$P(X \le 7) = \sum_{k=0}^{7} p_k = 0{,}01832 + 0{,}07326 + 0{,}14653 + 0{,}19537 + 0{,}19537 + 0{,}15629 + 0{,}10420 + 0{,}05954 = \mathbf{0{,}94887} \quad (94{,}89\% < 95\%)$$
  Un seul opérateur ne couvre que $94{,}89\%$ des heures : c'est juste en dessous de $95\%$.
- **Pour $X \le 8$ (donc $2$ opérateurs de capacité cumulée $2 \times 7 = 14$ appels/h) :**
  $$P(X \le 8) = P(X \le 7) + p_8 = 0{,}94887 + 0{,}02977 = \mathbf{0{,}97864} \quad (97{,}86\% \ge 95\%)$$
  Et avec $2$ opérateurs (capacité $14$ appels/h), la couverture réelle atteint $P(X \le 14) \approx \mathbf{99{,}998\%}$.

> [!check] Conclusion concrète
> L'ajustement à $\mathcal{P}(4)$ est validé ($\chi^2 = 0{,}1972 < 9{,}4877$) et il faut employer **2 opérateurs** (capacité cumulée de $14$ appels/h, couvrant $99{,}998\%$ des heures).

---

## 📌 Exercice 6 – Comparaison de deux proportions (Tmoney / Flooz)

> [!question] Énoncé résumé & Données
> À Lomé, $k_1 = 1\,040$ personnes sur $n_1 = 2\,000$ utilisent régulièrement le paiement mobile. À Kara, elles sont $k_2 = 915$ sur $n_2 = 1\,500$. Ces taux diffèrent-ils au risque $\alpha = 5\%$ ?

> [!info] Comprendre la logique (terre à terre)
> **À quoi sert la proportion poolée $F$ ?**
> Sous $H_0$, on suppose que Lomé et Kara ont **exactement le même taux d'usage** $p_1 = p_2 = p$. Si c'est le même taux dans les deux villes, le moyen le plus précis de l'estimer est de mélanger tout le monde dans un seul panier de $3\,500$ sondés.

> [!abstract] 🔎 Pourquoi cette méthode ? (indices de l'énoncé → choix)
> | Indice lu dans l'énoncé | Ce que ça implique |
> | :--- | :--- |
> | Deux villes indépendantes (Lomé / Kara), deux pourcentages, « diffèrent-ils ? » | Comparaison de deux proportions, test bilatéral ($p_1 \ne p_2$). |
> | Grands effectifs ($2\,000$ et $1\,500$) | Test $Z$ avec proportion poolée $F$, car sous $H_0$ on suppose $p_1 = p_2$. |
> 
> **Donc :** test $Z$ de comparaison de deux proportions avec fréquence commune $F$.

### Les formules utilisées
**Formules mathématiques :**
$$f_1 = \frac{k_1}{n_1}, \qquad f_2 = \frac{k_2}{n_2}, \qquad H_0 : p_1 = p_2 \quad \text{vs} \quad H_1 : p_1 \ne p_2$$
$$F = \frac{k_1 + k_2}{n_1 + n_2}, \qquad z_{\text{obs}} = \frac{f_1 - f_2}{\sqrt{F(1 - F)\left(\dfrac{1}{n_1} + \dfrac{1}{n_2}\right)}}$$

**En français simple :**
`Taux commun F = Total utilisateurs (Lomé + Kara) ÷ Total sondés (Lomé + Kara)`
`Score Z = (Taux Lomé - Taux Kara) ÷ Erreur standard calculée avec F`

### Résolution détaillée pas-à-pas

#### 1. Hypothèses et proportion poolée $F$
On calcule d'abord les deux proportions observées :
$$f_1 = \frac{1\,040}{2\,000} = \mathbf{0{,}52} \ (52\%), \qquad f_2 = \frac{915}{1\,500} = \mathbf{0{,}61} \ (61\%)$$
On teste $H_0 : p_1 = p_2$ contre $H_1 : p_1 \ne p_2$ (test bilatéral sur deux grands échantillons indépendants). Sous $H_0$, la proportion commune (poolée) vaut :
$$F = \frac{k_1 + k_2}{n_1 + n_2} = \frac{1\,040 + 915}{2\,000 + 1\,500} = \frac{1\,955}{3\,500} \approx \mathbf{0{,}5586} \implies 1 - F = 1 - 0{,}5586 = \mathbf{0{,}4414}$$

#### 2. Statistique $Z$ et décision ($\alpha = 5\%$)
1. **Calcul de l'erreur standard poolée (dénominateur) :**
   $$\frac{1}{n_1} + \frac{1}{n_2} = \frac{1}{2\,000} + \frac{1}{1\,500} = 0{,}0005 + 0{,}0006667 = 0{,}0011667$$
   $$\text{ES} = \sqrt{0{,}5586 \times 0{,}4414 \times 0{,}0011667} = \sqrt{0{,}0002877} \approx \mathbf{0{,}01696}$$
2. **Statistique observée ($z_{\text{obs}}$) :**
   $$z_{\text{obs}} = \frac{f_1 - f_2}{\text{ES}} = \frac{0{,}52 - 0{,}61}{0{,}01696} = \frac{-0{,}09}{0{,}01696} \approx \mathbf{-5{,}3064}$$
À $\alpha = 5\%$ bilatéral, le seuil critique lu en Annexe A.1 ($\Phi(u) = 0{,}9750$) est $z_{\text{crit}} = \pm 1{,}96$.

> [!check] Conclusion concrète
> Comme $|z_{\text{obs}}| = 5{,}31 > 1{,}96$ ($p < 10^{-6}$), **on rejette catégoriquement $H_0$** : le taux d'utilisation du paiement mobile est significativement plus élevé à Kara ($61\%$) qu'à Lomé ($52\%$).

---

## 📌 Exercice 7 – ANOVA : Impact d'une campagne publicitaire (7 régions)

> [!question] Énoncé résumé & Données
> Une compagnie d'assurance étudie le nombre de nouveaux clients obtenus par $n = 48$ agents généraux répartis dans $K = 7$ régions du Togo. On demande d'interpréter $\overline{X}_k$ et $\overline{X}$, de démontrer l'équation de décomposition de variance, de calculer $V_T^2, V_A^2, V_R^2$ et de conclure l'ANOVA au seuil $\alpha = 5\%$.

> [!info] Comprendre la logique (terre à terre)
> **Pourquoi le double produit disparaît-il dans la démonstration ?**
> Parce que dans chaque région $k$, la somme des écarts à sa propre moyenne vaut toujours **zéro** ($\sum (X_k^i - \overline{X}_k) = 0$). C'est ce qui rend la décomposition $V_T^2 = V_R^2 + V_A^2$ aussi propre que le théorème de Pythagore.
>
> **Pourquoi tester des moyennes avec un rapport de variances $F$ ?**
> Si la campagne avait le même effet partout, les moyennes des $7$ régions seraient très proches les unes des autres ($V_A^2$ petit) comparé au bruit interne entre agents d'une même région ($V_R^2$). Un grand $F$ ($5{,}42$) prouve que les écarts entre régions dépassent largement le bruit interne.

> [!abstract] 🔎 Pourquoi cette méthode ? (indices de l'énoncé → choix)
> | Indice lu dans l'énoncé | Ce que ça implique |
> | :--- | :--- |
> | $K = 7$ régions à comparer simultanément | Faire $21$ tests $t$ deux à deux ferait exploser le risque d'erreur $\alpha$ : utiliser l'ANOVA. |
> | Décomposition $V_T^2 = V_R^2 + V_A^2$ | Mesurer si la variance entre régions dépasse la variance interne résiduelle. |
> 
> **Donc :** ANOVA à 1 facteur avec $F_{\text{obs}} = \frac{\text{MS}_A}{\text{MS}_R}$.

### Les formules utilisées
**Formules mathématiques :**
$$\overline{X} = \frac{1}{n}\sum_{k=1}^K n_k \overline{X}_k, \qquad V_T^2 = V_R^2 + V_A^2$$
$$V_A^2 = \frac{1}{n}\sum_{k=1}^K n_k (\overline{X}_k - \overline{X})^2, \qquad V_R^2 = \frac{1}{n}\sum_{k=1}^K n_k v_k^2$$
$$\text{SC}_A = n V_A^2, \qquad \text{SC}_R = n V_R^2, \qquad F_{\text{obs}} = \frac{\text{MS}_A}{\text{MS}_R} = \frac{\text{SC}_A / (K - 1)}{\text{SC}_R / (n - K)}$$

**En français simple :**
`Variance Totale = Bruit interne aux régions (V_R²) + Écart entre régions (V_A²)`
`F = Variance moyenne entre régions (÷ 6) ÷ Variance moyenne interne (÷ 41)`

### Résolution détaillée pas-à-pas

#### 1. Interprétation de $\overline{X}_k$ et $\overline{X}$
- $\overline{X}_k$ est le **nombre moyen de nouveaux clients par agent général dans la région $k$**.
- $\overline{X}$ est la **moyenne globale** (tous agents confondus sur l'ensemble des $n = 48$ agents des $7$ zones).

#### 2. Démonstration de l'équation d'analyse de variance ($V_T^2 = V_R^2 + V_A^2$)
Partons de $X_k^i - \overline{X} = (X_k^i - \overline{X}_k) + (\overline{X}_k - \overline{X})$. En élevant au carré et en sommant sur $k = 1 \dots K$ et $i = 1 \dots n_k$ :
$$\sum_{k=1}^K \sum_{i=1}^{n_k} (X_k^i - \overline{X})^2 = \sum_{k=1}^K \sum_{i=1}^{n_k} (X_k^i - \overline{X}_k)^2 + \sum_{k=1}^K \sum_{i=1}^{n_k} (\overline{X}_k - \overline{X})^2 + 2\sum_{k=1}^K (\overline{X}_k - \overline{X})\underbrace{\sum_{i=1}^{n_k} (X_k^i - \overline{X}_k)}_{= 0}$$
Or, par définition de la moyenne $\overline{X}_k$, $\sum_{i=1}^{n_k} (X_k^i - \overline{X}_k) = n_k\overline{X}_k - n_k\overline{X}_k = 0$ pour tout $k$. Le terme rectangle s'annule donc identiquement. Comme $(\overline{X}_k - \overline{X})^2$ ne dépend pas de $i$, sa somme sur $i = 1 \dots n_k$ vaut $n_k(\overline{X}_k - \overline{X})^2$. En divisant par $n$ :
$$\underbrace{\frac{1}{n}\sum_{k=1}^K \sum_{i=1}^{n_k} (X_k^i - \overline{X})^2}_{V_T^2} = \underbrace{\frac{1}{n}\sum_{k=1}^K \sum_{i=1}^{n_k} (X_k^i - \overline{X}_k)^2}_{V_R^2} + \underbrace{\frac{1}{n}\sum_{k=1}^K n_k (\overline{X}_k - \overline{X})^2}_{V_A^2} \quad \blacksquare$$

#### 3. Calcul numérique de $V_T^2$, $V_A^2$ et $V_R^2$
On commence par trouver la moyenne globale $\overline{X}$ via la somme des $n_k \bar{x}_k$ :
$$\overline{X} = \frac{1}{n}\sum_{k=1}^7 n_k \bar{x}_k = \frac{241{,}92 + 156{,}38 + 136{,}78 + 113{,}70 + 190{,}19 + 155{,}22 + 154{,}32}{48} = \frac{1\,148{,}51}{48} \approx \mathbf{23{,}9273}$$

On remplit ensuite chaque ligne du tableau (ex. pour la **Région 1** : $n_1\bar{x}_1 = 9 \times 26{,}88 = 241{,}92$, $n_1(\bar{x}_1 - \bar{x})^2 = 9 \times (26{,}88 - 23{,}9273)^2 = 78{,}4664$, et $n_1 v_1^2 = 9 \times 13{,}54 = 121{,}86$) :

| Région $k$ | $n_k$ | $\bar{x}_k$ | $v_k^2$ | $n_k\bar{x}_k$ | $n_k(\bar{x}_k - \bar{x})^2$ | $n_k v_k^2$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | 9 | $26{,}88$ | $13{,}54$ | $241{,}92$ | $78{,}4664$ | $121{,}86$ |
| 2 | 7 | $22{,}34$ | $12{,}59$ | $156{,}38$ | $17{,}6365$ | $88{,}13$ |
| 3 | 7 | $19{,}54$ | $12{,}87$ | $136{,}78$ | $134{,}7383$ | $90{,}09$ |
| 4 | 6 | $18{,}95$ | $13{,}42$ | $113{,}70$ | $148{,}6406$ | $80{,}52$ |
| 5 | 7 | $27{,}17$ | $13{,}17$ | $190{,}19$ | $73{,}6061$ | $92{,}19$ |
| 6 | 6 | $25{,}87$ | $12{,}56$ | $155{,}22$ | $22{,}6447$ | $75{,}36$ |
| 7 | 6 | $25{,}72$ | $12{,}64$ | $154{,}32$ | $19{,}2828$ | $75{,}84$ |
| **Total ($\sum$)** | **$48$** | — | — | **$1\,148{,}51$** | **$495{,}0154$** | **$623{,}99$** |

On divise chaque somme des carrés par $n = 48$ :
$$V_A^2 = \frac{1}{n}\sum n_k(\bar{x}_k - \bar{x})^2 = \frac{495{,}0154}{48} \approx \mathbf{10{,}3128}$$
$$V_R^2 = \frac{1}{n}\sum n_k v_k^2 = \frac{623{,}99}{48} \approx \mathbf{12{,}9998}$$
$$V_T^2 = V_A^2 + V_R^2 = 10{,}3128 + 12{,}9998 = \mathbf{23{,}3126}$$
*(Note : si les variances du tableau étaient déjà corrigées par $n_k - 1$, on aurait $V_R^2 = \frac{533{,}20}{48} = 11{,}1083$ et $V_T^2 = 10{,}3128 + 11{,}1083 = 21{,}4212$.)*

#### 4. Finalisation de l'ANOVA ($\alpha = 5\%$)
On teste $H_0 : \mu_1 = \mu_2 = \dots = \mu_7$ contre $H_1 :$ au moins une région diffère :
- $\text{SC}_A = 495{,}0154$ avec $\text{ddl}_A = K - 1 = 7 - 1 = \mathbf{6} \implies \text{MS}_A = \frac{\text{SC}_A}{K - 1} = \frac{495{,}0154}{6} = \mathbf{82{,}5026}$
- $\text{SC}_R = 623{,}9900$ avec $\text{ddl}_R = n - K = 48 - 7 = \mathbf{41} \implies \text{MS}_R = \frac{\text{SC}_R}{n - K} = \frac{623{,}9900}{41} = \mathbf{15{,}2193}$
- Statistique de Fisher :
  $$F_{\text{obs}} = \frac{\text{MS}_A}{\text{MS}_R} = \frac{82{,}5026}{15{,}2193} \approx \mathbf{5{,}4209} \quad (p = 0{,}00034)$$

| Source de variation | Somme des carrés (SC) | ddl | Carré moyen (MS) | Statistique $F_{\text{obs}}$ |
| :--- | :---: | :---: | :---: | :---: |
| **Inter-groupes (Région)** | $495{,}0154$ | $6$ | $82{,}5026$ | **$\mathbf{5{,}4209}$** ($p = 0{,}00034$) |
| **Résiduelle (Intra)** | $623{,}9900$ | $41$ | $15{,}2193$ | — |

*(Avec la variante $s_k^2$ corrigée : $F_{\text{obs}} = \mathbf{6{,}3440}$, $p = 8{,}8 \times 10^{-5}$.)*
En Annexe D.1 ($\nu_1 = 6$, $\nu_2 = 40$), $F_{0{,}05}(6, 40) = 2{,}34$ (soit $F_{0{,}05}(6, 41) \approx \mathbf{2{,}33}$).

> [!check] Conclusion concrète
> Comme $F_{\text{obs}} = 5{,}42 > 2{,}33$, **on rejette $H_0$** : l'impact de la campagne publicitaire varie significativement d'une région à l'autre.

---

## 📌 Exercice 8 – Taille des garçons vs filles en CP

> [!question] Énoncé résumé & Données
> Dans une école primaire de Lomé, on mesure $n_1 = 41$ garçons ($\bar{x}_1 = 107\text{ cm}$, $v_1 = 8\text{ cm}$, Shapiro-Wilk $p_1 = 0{,}82$) et $n_2 = 61$ filles ($\bar{x}_2 = 104\text{ cm}$, $v_2 = 9\text{ cm}$, Shapiro-Wilk $p_2 = 0{,}21$). Peut-on affirmer que les garçons sont plus grands au risque $\alpha = 5\%$ ?

> [!info] Comprendre la logique (terre à terre)
> **À quoi servent Shapiro-Wilk et Fisher avant la formule finale ?**
> C'est le contrôle technique avant de rouler : Shapiro-Wilk vérifie la normalité de chaque groupe ($p > 0{,}05 \implies$ OK), et le quotient $F = v_{\max}^2 / v_{\min}^2$ vérifie que les deux groupes ont une dispersion comparable ($F < F_{\text{crit}} \implies$ OK).
>
> **Pourquoi $z_{\text{crit}} = 1{,}6449$ au lieu de $1{,}96$ ?**
> Le test est **unilatéral droit** ($H_1 : \mu_1 > \mu_2$) : tout le risque $\alpha = 5\%$ est concentré dans la queue droite, donc $\Phi(u) = 1 - 0{,}05 = 0{,}9500 \implies z_{0{,}95} = 1{,}6449$.

> [!abstract] 🔎 Pourquoi cette méthode ? (indices de l'énoncé → choix)
> | Indice lu dans l'énoncé | Ce que ça implique |
> | :--- | :--- |
> | Deux groupes indépendants (garçons/filles), « sont plus grands » | Comparaison de deux moyennes, test unilatéral droit ($\mu_1 > \mu_2$). |
> | $n_1 = 41$, $n_2 = 61$ (grands), Shapiro-Wilk + variances données | Vérifier normalité puis homoscédasticité ($F$) avant de calculer la statistique $N$. |
> 
> **Donc :** $N_{\text{obs}} = \frac{\bar{x}_1 - \bar{x}_2}{\sqrt{v_1^2/n_1 + v_2^2/n_2}}$ comparé au seuil unilatéral $z_{0{,}95} = 1{,}6449$.

### Les formules utilisées
**Formules mathématiques :**
$$F_{\text{hom}} = \frac{v_2^2}{v_1^2}, \qquad H_0 : \mu_1 = \mu_2 \quad \text{vs} \quad H_1 : \mu_1 > \mu_2, \qquad N_{\text{obs}} = \frac{\bar{x}_1 - \bar{x}_2}{\sqrt{\dfrac{v_1^2}{n_1} + \dfrac{v_2^2}{n_2}}}$$

**En français simple :**
`Statistique N = (Moyenne garçons - Moyenne filles) ÷ √(Var₁/n₁ + Var₂/n₂)`

### Résolution détaillée pas-à-pas

#### 1. Vérification des prérequis (normalité et homoscédasticité)
- **Normalité :** Shapiro-Wilk donne $p_1 = 0{,}82 > 0{,}05$ et $p_2 = 0{,}21 > 0{,}05$ $\implies$ normalité compatible dans les deux groupes.
- **Égalité des variances :** on met la plus grande variance au numérateur et on lit l'Annexe D.2 ($\alpha = 0{,}025$, $\nu_1 = 60$, $\nu_2 = 40$) :
  $$F_{\text{hom}} = \frac{v_2^2}{v_1^2} = \frac{9^2}{8^2} = \frac{81}{64} = \mathbf{1{,}2656} < F_{0{,}025}(60, 40) \approx 1{,}84 \quad (\text{homoscédasticité acceptée})$$

#### 2. Hypothèses, statistique de test et décision (unilatéral droit, $\alpha = 5\%$)
$$H_0 : \mu_1 = \mu_2 \qquad \text{contre} \qquad H_1 : \mu_1 > \mu_2$$
1. **Calcul de l'erreur standard (dénominateur) :**
   $$\frac{v_1^2}{n_1} = \frac{8^2}{41} = \frac{64}{41} \approx 1{,}5610, \qquad \frac{v_2^2}{n_2} = \frac{9^2}{61} = \frac{81}{61} \approx 1{,}3279$$
   $$\text{ES} = \sqrt{1{,}5610 + 1{,}3279} = \sqrt{2{,}8889} \approx \mathbf{1{,}6997}$$
2. **Statistique observée ($N_{\text{obs}}$) :**
   $$N_{\text{obs}} = \frac{\bar{x}_1 - \bar{x}_2}{\text{ES}} = \frac{107 - 104}{1{,}6997} = \frac{3}{1{,}6997} \approx \mathbf{1{,}7651}$$
En unilatéral droit à $\alpha = 5\%$ ($\Phi(u) = 0{,}9500$ en Annexe A.1), le seuil critique vaut $z_{0{,}95} = \mathbf{1{,}6449}$ ($p = 1 - \Phi(1{,}7651) = \mathbf{0{,}0388}$).
*(Avec le test $t$ poolé à $n_1 + n_2 - 2 = 100$ ddl : $s_p = 8{,}613$, $t_{\text{obs}} = 1{,}7246$, $p_{\text{unilat}} = 0{,}0438$.)*

> [!check] Conclusion concrète
> Comme $N_{\text{obs}} = 1{,}7651 > z_{0{,}95} = 1{,}6449$ ($p = 0{,}0388 < 0{,}05$), **on rejette $H_0$** : au seuil de $5\%$, les garçons de CP sont statistiquement plus grands en moyenne que les filles.

---

## 📌 Exercice 9 – Sécurité routière : alcool et temps de réaction

> [!question] Énoncé résumé & Données
> On mesure en simulateur le temps de réaction (en s) de conducteurs sans alcool puis avec alcool sur $n = 15$ paires d'observations *(bien que l'énoncé introductif mentionne 30 chauffeurs)*. L'alcool a-t-il un effet significatif au risque $\alpha = 5\%$ ?

> [!info] Comprendre la logique (terre à terre)
> **Pourquoi soustraire paire par paire au lieu de comparer les deux colonnes séparément ?**
> Un conducteur naturellement rapide met peut-être $0{,}45\text{ s}$ sans alcool et $0{,}52\text{ s}$ avec ; un conducteur lent met $0{,}80\text{ s}$ et $0{,}88\text{ s}$. Si tu mélanges les groupes, la différence entre individus noie l'effet de l'alcool. En calculant $d_i = \text{Avec}_i - \text{Sans}_i$ pour **chaque** conducteur, tu élimines le niveau de base individuel et tu isoles uniquement l'effet de l'alcool.

> [!abstract] 🔎 Pourquoi cette méthode ? (indices de l'énoncé → choix)
> | Indice lu dans l'énoncé | Ce que ça implique |
> | :--- | :--- |
> | Mêmes conducteurs mesurés sans alcool puis avec alcool | Données appariées : éliminer l'effet individuel en formant $d_i = \text{Avec}_i - \text{Sans}_i$. |
> | $n = 15$ paires ($< 30$), $\sigma_d$ inconnu, « a-t-il un effet ? » | Petit échantillon et test bilatéral ($\mu_d \ne 0$) : loi de Student $t(14)$. |
> 
> **Donc :** test $t$ de Student apparié sur les différences $d_i$.

### Les formules utilisées
**Formules mathématiques :**
$$d_i = \text{Avec}_i - \text{Sans}_i, \qquad \bar{d} = \frac{1}{n}\sum_{i=1}^n d_i, \qquad s_d^2 = \frac{1}{n - 1}\sum_{i=1}^n (d_i - \bar{d})^2 = \frac{\sum_{i=1}^n d_i^2 - n\bar{d}^2}{n - 1}$$
$$H_0 : \mu_d = 0 \quad \text{vs} \quad H_1 : \mu_d \ne 0, \qquad \text{ES} = \frac{s_d}{\sqrt{n}}, \qquad t_{\text{obs}} = \frac{\bar{d} - 0}{\text{ES}} \sim t(n - 1)$$

**En français simple :**
`t_obs = Moyenne des écarts (Avec - Sans) ÷ (Écart-type des écarts ÷ √15)`

### Résolution détaillée pas-à-pas

#### 1. Hypothèses et calcul des différences appariées ($n = 15$)
On pose $d_i = \text{Avec}_i - \text{Sans}_i$ et on réalise un test **apparié bilatéral** :
$$H_0 : \mu_d = 0 \qquad \text{contre} \qquad H_1 : \mu_d \ne 0$$

| Paire $i$ | Sans | Avec | $d_i$ | $d_i - \bar{d}$ | $(d_i - \bar{d})^2$ | $d_i^2$ *(Koenig-Huygens)* |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | $0{,}68$ | $0{,}73$ | $+0{,}05$ | $-0{,}0287$ | $0{,}000822$ | $0{,}0025$ |
| 2 | $0{,}64$ | $0{,}62$ | $-0{,}02$ | $-0{,}0987$ | $0{,}009735$ | $0{,}0004$ |
| 3 | $0{,}68$ | $0{,}76$ | $+0{,}08$ | $+0{,}0013$ | $0{,}000002$ | $0{,}0064$ |
| 4 | $0{,}82$ | $0{,}92$ | $+0{,}10$ | $+0{,}0213$ | $0{,}000455$ | $0{,}0100$ |
| 5 | $0{,}58$ | $0{,}68$ | $+0{,}10$ | $+0{,}0213$ | $0{,}000455$ | $0{,}0100$ |
| 6 | $0{,}80$ | $0{,}87$ | $+0{,}07$ | $-0{,}0087$ | $0{,}000075$ | $0{,}0049$ |
| 7 | $0{,}72$ | $0{,}77$ | $+0{,}05$ | $-0{,}0287$ | $0{,}000822$ | $0{,}0025$ |
| 8 | $0{,}65$ | $0{,}70$ | $+0{,}05$ | $-0{,}0287$ | $0{,}000822$ | $0{,}0025$ |
| 9 | $0{,}84$ | $0{,}88$ | $+0{,}04$ | $-0{,}0387$ | $0{,}001495$ | $0{,}0016$ |
| 10 | $0{,}73$ | $0{,}79$ | $+0{,}06$ | $-0{,}0187$ | $0{,}000348$ | $0{,}0036$ |
| 11 | $0{,}65$ | $0{,}72$ | $+0{,}07$ | $-0{,}0087$ | $0{,}000075$ | $0{,}0049$ |
| 12 | $0{,}59$ | $0{,}80$ | $+0{,}21$ | $+0{,}1313$ | $0{,}017248$ | $0{,}0441$ |
| 13 | $0{,}78$ | $0{,}78$ | $0$ | $-0{,}0787$ | $0{,}006188$ | $0{,}0000$ |
| 14 | $0{,}67$ | $0{,}86$ | $+0{,}19$ | $+0{,}1113$ | $0{,}012395$ | $0{,}0361$ |
| 15 | $0{,}65$ | $0{,}78$ | $+0{,}13$ | $+0{,}0513$ | $0{,}002635$ | $0{,}0169$ |
| **Total ($\sum$)** | — | — | **$1{,}18$** | **$0$** | **$0{,}053573$** | **$0{,}1464$** |

- **Moyenne des différences :**
  $$\bar{d} = \frac{1}{n}\sum_{i=1}^{15} d_i = \frac{1{,}18}{15} \approx \mathbf{0{,}0787\text{ s}}$$
- **Variance corrigée et écart-type des différences :**
  $$s_d^2 = \frac{1}{n - 1}\sum_{i=1}^{15}(d_i - \bar{d})^2 = \frac{0{,}053573}{15 - 1} = \frac{0{,}053573}{14} \approx \mathbf{0{,}003827}$$
  *(Koenig-Huygens : $s_d^2 = \frac{0{,}1464 - 15 \times (1{,}18/15)^2}{14} = \frac{0{,}1464 - 0{,}092827}{14} \approx 0{,}003827$.)*
  $$s_d = \sqrt{0{,}003827} \approx \mathbf{0{,}0619\text{ s}}$$

#### 2. Statistique $t$, lecture Annexe C et décision
1. **Erreur standard ($\text{ES}$) :**
   $$\text{ES} = \frac{s_d}{\sqrt{n}} = \frac{0{,}06186}{\sqrt{15}} = \frac{0{,}06186}{3{,}8730} \approx \mathbf{0{,}01597\text{ s}}$$
2. **Statistique observée ($t_{\text{obs}}$) :**
   $$t_{\text{obs}} = \frac{\bar{d}}{\text{ES}} = \frac{0{,}07867}{0{,}01597} \approx \mathbf{4{,}9252} \sim t(14)$$
3. **Seuil critique :** en Annexe C ($\nu = 15 - 1 = 14$, colonne bilatérale `0,050`), la valeur critique vaut $t_{\text{crit}} = \mathbf{2{,}1448}$ ($p = 0{,}00022$).

> [!check] Conclusion concrète
> Comme $4{,}9252 > 2{,}1448$ ($p = 0{,}00022$), **on rejette $H_0$** : l'alcool augmente très significativement le temps de réaction au volant *(même si l'on traitait les deux lignes en groupes indépendants, $t = 2{,}6571 > 2{,}0484$ avec $\nu = 28$ donne le même rejet)*.

---

## 📌 Exercice 10 – Efficacité d'un programme nutritionnel

> [!question] Énoncé résumé & Données
> On pèse $N = 10$ participants (en kg) avant et après un programme nutritionnel et sportif. Un participant passe de $158$ à $121$ kg ($d_3 = -37$ kg). Quel test choisir et quelle conclusion tirer au risque $\alpha = 5\%$ ?

> [!info] Comprendre la logique (terre à terre)
> **Pourquoi Student échoue et comment Wilcoxon résiste à $-37$ kg :**
> L'individu 3 ($-37$ kg) fait exploser l'écart-type $s_d = 11{,}45$ kg, ce qui écrase le test $t$ de Student ($t = -1{,}3259$, $p = 0{,}2175$). Le test de **Wilcoxon** résout ce problème en remplaçant les valeurs par leur **rang** : que la perte soit de $10$ kg ou $37$ kg, son poids dans le calcul reste le rang $9$ sur $9$.
>
> **Sens de rejet inversé :**
> Dans $Z, t, \chi^2, F$, on rejette quand la statistique dépasse le seuil. Pour **Wilcoxon ($W$) et Mann-Whitney ($U$)**, on rejette quand la statistique est **inférieure ou égale** au seuil critique ($W \le W_{\text{crit}}$) !

> [!abstract] 🔎 Pourquoi cette méthode ? (indices de l'énoncé → choix)
> | Indice lu dans l'énoncé | Ce que ça implique |
> | :--- | :--- |
> | Mesures Avant/Après sur les mêmes individus ($N = 10$) | Séries appariées. |
> | Valeur aberrante extrême ($158 \to 121$ kg, soit $d_3 = -37$ kg) | La normalité est violée et $s_d$ explose, faussant le test $t$ de Student : passer au non paramétrique. |
> 
> **Donc :** test des rangs signés de Wilcoxon (robuste aux valeurs aberrantes).

### Les formules utilisées
**Formules mathématiques :**
$$W^+ = \sum_{d_i > 0} r_i, \qquad W^- = \sum_{d_i < 0} r_i, \qquad W = \min(W^+, W^-), \qquad W^+ + W^- = \frac{n(n + 1)}{2}$$

**Procédure en français simple :**
1. Jeter les $d_i = 0$ (il reste $n = 9$ paires).
2. Trier les écarts sans le signe ($\lvert d_i\rvert$) du plus petit au plus grand, donner un rang (moyenne si ex-æquo).
3. Additionner les rangs des positifs ($W^+$) et ceux des négatifs ($W^-$) ; retenir le plus petit ($W$).

### Résolution détaillée pas-à-pas

#### 1. Constat préalable critique (échec du test $t$ face à l'outlier)
L'individu n° 3 passe de $158$ à $121$ kg ($d_3 = -37$ kg), créant une **valeur aberrante massive** qui viole la normalité des différences. Avec les $10$ différences ($-1, +1, -37, -2, -5, 0, -2, +1, -1, -2$), on aurait :
$$\bar{d} = \frac{-48}{10} = -4{,}8\text{ kg}, \qquad s_d = 11{,}45\text{ kg} \implies t = \frac{\bar{d}}{s_d / \sqrt{10}} = \frac{-4{,}8}{11{,}45 / 3{,}1623} = \frac{-4{,}8}{3{,}6208} = -1{,}3259 \quad (p = 0{,}2175)$$
Ce test $t$ est faussement non significatif car l'outlier gonfle artificiellement $s_d$.

#### 2. Choix méthodologique et calcul des rangs signés de Wilcoxon
On applique le **test des rangs signés de Wilcoxon** ($H_0 : \text{médiane des } d_i = 0$ vs $H_1 : \text{médiane} \ne 0$). On retire d'abord la différence nulle (individu 6 : $58 \to 58$), ce qui laisse $n = 9$ paires non nulles :

| Individu $i$ | Avant | Après | $d_i = \text{Après} - \text{Avant}$ | $\lvert d_i \rvert$ | Rang | $W^+$ ($d_i > 0$) | $W^-$ ($d_i < 0$) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | $67$ | $66$ | $-1$ | $1$ | $2{,}5$ | — | $2{,}5$ |
| 2 | $83$ | $84$ | $+1$ | $1$ | $2{,}5$ | $2{,}5$ | — |
| 3 | $158$ | $121$ | $-37$ | $37$ | $9{,}0$ | — | $9{,}0$ |
| 4 | $78$ | $76$ | $-2$ | $2$ | $6{,}0$ | — | $6{,}0$ |
| 5 | $87$ | $82$ | $-5$ | $5$ | $8{,}0$ | — | $8{,}0$ |
| 6 | $58$ | $58$ | $0$ | — *(exclu)* | — | — | — |
| 7 | $79$ | $77$ | $-2$ | $2$ | $6{,}0$ | — | $6{,}0$ |
| 8 | $63$ | $64$ | $+1$ | $1$ | $2{,}5$ | $2{,}5$ | — |
| 9 | $69$ | $68$ | $-1$ | $1$ | $2{,}5$ | — | $2{,}5$ |
| 10 | $72$ | $70$ | $-2$ | $2$ | $6{,}0$ | — | $6{,}0$ |
| **Total ($\sum$)** | — | — | — | — | **$45{,}0$** | **$5{,}0$** | **$40{,}0$** |

- **Calcul des rangs ex-æquo :**
  - Les $4$ valeurs $\lvert d \rvert = 1$ occupent les rangs $1, 2, 3, 4$ $\implies$ rang moyen $= \frac{1 + 2 + 3 + 4}{4} = \mathbf{2{,}5}$.
  - Les $3$ valeurs $\lvert d \rvert = 2$ occupent les rangs $5, 6, 7$ $\implies$ rang moyen $= \frac{5 + 6 + 7}{3} = \mathbf{6{,}0}$.
- **Sommes $W^+$ et $W^-$ et vérification :**
  $$W^+ = 2{,}5 + 2{,}5 = \mathbf{5{,}0}, \qquad W^- = 2{,}5 + 9{,}0 + 6{,}0 + 8{,}0 + 6{,}0 + 2{,}5 + 6{,}0 = \mathbf{40{,}0}$$
  $$\text{Vérification : } W^+ + W^- = 5{,}0 + 40{,}0 = 45{,}0 = \frac{n(n+1)}{2} = \frac{9 \times 10}{2}$$
  $$W = \min(W^+, W^-) = \min(5{,}0 \,;\, 40{,}0) = \mathbf{5{,}0}$$

#### 3. Décision au risque $\alpha = 5\%$
Pour $n = 9$ à $\alpha = 5\%$ (bilatéral), la table de Wilcoxon donne $W_{\text{crit}} = \mathbf{5}$ (et la $p$-value exacte vaut $\frac{22}{512} = \mathbf{0{,}0430} < 0{,}05$).

> [!check] Conclusion concrète
> Comme $W = 5 \le W_{\text{crit}} = 5$ ($p = 0{,}0430 < 0{,}05$), **on rejette $H_0$** : le programme a un effet significatif à la baisse ($7$ participants sur $10$ ont perdu du poids).

---

## 📌 Exercice 11 – ANOVA : Temps de traitement selon le SGBD

> [!question] Énoncé résumé & Données
> On compare les temps de traitement de $k = 3$ SGBD (PostgreSQL, MongoDB, MySQL) avec $n_j = 5$ exécutions par groupe ($\text{SC}_{\text{Facteur}} = 320$, $\text{SC}_{\text{Résiduelle}} = 240$, $F_{0{,}05}(2, 12) = 3{,}89$).

> [!info] Comprendre la logique (terre à terre)
> **Recette mécanique de tout tableau ANOVA :**
> Il n'y a que 3 divisions à connaître par cœur : $\text{SC}_F \div (k - 1)$ donne $\text{MS}_F$ ; $\text{SC}_R \div (N - k)$ donne $\text{MS}_R$ ; $\text{MS}_F \div \text{MS}_R$ donne $F$. Si $F$ dépasse $F_{\text{crit}}$, l'effet du facteur domine le bruit.

> [!abstract] 🔎 Pourquoi cette méthode ? (indices de l'énoncé → choix)
> | Indice lu dans l'énoncé | Ce que ça implique |
> | :--- | :--- |
> | $k = 3$ SGBD à comparer, $\text{SC}_{\text{Facteur}}$ et $\text{SC}_{\text{Résiduelle}}$ fournies | Comparaison de $3$ moyennes à partir des sommes de carrés : tableau ANOVA. |
> | $n_j = 5$ par groupe ($N = 15$) | Degrés de liberté $k - 1 = 2$ et $N - k = 12$. |
> 
> **Donc :** tableau ANOVA et statistique $F(2, 12)$.

### Les formules utilisées
**Formules mathématiques :**
$$\text{ddl}_F = k - 1, \qquad \text{ddl}_R = N - k, \qquad \text{MS}_F = \frac{\text{SC}_F}{\text{ddl}_F}, \qquad \text{MS}_R = \frac{\text{SC}_R}{\text{ddl}_R}, \qquad F = \frac{\text{MS}_F}{\text{MS}_R}$$

**En français simple :**
`Carré moyen (MS) = Somme des carrés ÷ Degrés de liberté`
`F = Carré moyen du SGBD ÷ Carré moyen du Bruit`

### Résolution détaillée pas-à-pas

#### 1. Hypothèses et tableau ANOVA
On teste $H_0 : \mu_{\text{PostgreSQL}} = \mu_{\text{MongoDB}} = \mu_{\text{MySQL}}$ contre $H_1 :$ au moins un SGBD diffère.
- Nombre total d'observations : $N = k \times n_j = 3 \times 5 = \mathbf{15}$.
- Degrés de liberté : $\text{ddl}_F = k - 1 = 3 - 1 = \mathbf{2}$, $\text{ddl}_R = N - k = 15 - 3 = \mathbf{12}$.
- Carrés moyens : $\text{MS}_F = \frac{\text{SC}_F}{\text{ddl}_F} = \frac{320}{2} = \mathbf{160}$, $\text{MS}_R = \frac{\text{SC}_R}{\text{ddl}_R} = \frac{240}{12} = \mathbf{20}$.
- Statistique de Fisher : $F_{\text{obs}} = \frac{\text{MS}_F}{\text{MS}_R} = \frac{160}{20} = \mathbf{8{,}00}$ ($p = 0{,}0062$).

| Source de variation | SC | ddl | Carré moyen (MS) | Statistique $F$ |
| :--- | :---: | :---: | :---: | :---: |
| **Facteur (SGBD)** | $320$ | $2$ | $160$ | **$\mathbf{8{,}00}$** ($p = 0{,}0062$) |
| **Résiduelle (Intra)** | $240$ | $12$ | $20$ | — |

#### 2. Décision au seuil $\alpha = 5\%$
On compare $F_{\text{obs}} = 8{,}00$ au seuil critique donné (Annexe D.1) : $F_{0{,}05}(2, 12) = \mathbf{3{,}89}$.

> [!check] Conclusion concrète
> Comme $F = 8{,}00 > F_{0{,}05}(2, 12) = 3{,}89$, **on rejette $H_0$** : le choix du SGBD a un impact statistiquement significatif sur le temps de traitement au seuil de $5\%$.

---

## 📌 Exercice 12 – ANOVA : Consommation RAM selon le langage

> [!question] Énoncé résumé & Données
> Un audit Green IT mesure la RAM d'un microservice en $k = 4$ langages ($6$ mesures par langage, $N = 4 \times 6 = 24$), donnant $\text{SCT} = 1\,200$ et $\text{SCR} = 300$. On teste l'influence du langage à $\alpha = 1\%$ ($F_{0{,}01}(3, 20) = 4{,}94$).

> [!info] Comprendre la logique (terre à terre)
> **Le puzzle à 3 pièces :**
> $\text{SCT} = \text{SCE} + \text{SCR}$. Dès qu'on te donne 2 des 3 sommes de carrés, tu trouves la 3e par simple soustraction, puis tu déroules le même tableau qu'à l'Exercice 11.

> [!abstract] 🔎 Pourquoi cette méthode ? (indices de l'énoncé → choix)
> | Indice lu dans l'énoncé | Ce que ça implique |
> | :--- | :--- |
> | $k = 4$ langages ($N = 24$), $\text{SCT}$ et $\text{SCR}$ fournies | Utiliser $\text{SCT} = \text{SCE} + \text{SCR}$ pour retrouver $\text{SCE}$, puis dérouler l'ANOVA. |
> | Test au risque $\alpha = 1\%$ | Comparer à $F_{0{,}01}(3, 20)$. |
> 
> **Donc :** déduire $\text{SCE} = \text{SCT} - \text{SCR}$, puis test $F(3, 20)$ à $1\%$.

### Les formules utilisées
**Formules mathématiques :**
$$\text{SCE} = \text{SCT} - \text{SCR}, \qquad \text{ddl}_F = k - 1, \qquad \text{ddl}_R = N - k, \qquad F = \frac{\text{SCE} / \text{ddl}_F}{\text{SCR} / \text{ddl}_R}$$

**En français simple :**
`Variation expliquée (langages) = Variation totale - Variation résiduelle`

### Résolution détaillée pas-à-pas

#### 1. Hypothèses et calcul de $\text{SCE}$
On teste $H_0 : \mu_1 = \mu_2 = \mu_3 = \mu_4$ contre $H_1 :$ au moins un langage diffère. On déduit d'abord :
$$\text{SCE} = \text{SCT} - \text{SCR} = 1\,200 - 300 = \mathbf{900}$$

#### 2. Tableau ANOVA et décision à $\alpha = 1\%$
- Degrés de liberté : $\text{ddl}_F = k - 1 = 4 - 1 = \mathbf{3}$, $\text{ddl}_R = N - k = 24 - 4 = \mathbf{20}$, $\text{ddl}_{\text{Total}} = N - 1 = 24 - 1 = \mathbf{23}$.
- Carrés moyens : $\text{MS}_F = \frac{\text{SCE}}{\text{ddl}_F} = \frac{900}{3} = \mathbf{300}$, $\text{MS}_R = \frac{\text{SCR}}{\text{ddl}_R} = \frac{300}{20} = \mathbf{15}$.
- Statistique de Fisher : $F_{\text{obs}} = \frac{\text{MS}_F}{\text{MS}_R} = \frac{300}{15} = \mathbf{20{,}00}$ ($p = 3{,}1 \times 10^{-6}$).

| Source de variation | SC | ddl | Carré moyen (MS) | Statistique $F$ |
| :--- | :---: | :---: | :---: | :---: |
| **Facteur (Langage)** | $900$ | $3$ | $300$ | **$\mathbf{20{,}00}$** ($p = 3{,}1 \times 10^{-6}$) |
| **Résiduelle (Intra)** | $300$ | $20$ | $15$ | — |
| **Total** | $1\,200$ | $23$ | — | — |

On compare $F_{\text{obs}} = 20{,}00$ au seuil critique $F_{0{,}01}(3, 20) = \mathbf{4{,}94}$.

> [!check] Conclusion concrète
> Comme $F = 20{,}00 > F_{0{,}01}(3, 20) = 4{,}94$, **on rejette $H_0$ au seuil de $1\%$** : le langage de programmation influence très significativement la consommation mémoire.

---

## 📌 Exercice 13 – Mann-Whitney : Formation Agile (Présentiel vs E-learning)

> [!question] Énoncé résumé & Données
> Deux groupes de $n_1 = n_2 = 5$ développeurs passent un test Agile : Méthode A Présentiel (`78, 85, 90, 92, 96`) et Méthode B E-learning (`60, 70, 75, 80, 88`). On réalise le test de Mann-Whitney à $\alpha = 5\%$ ($U_{\text{critique}} = 2$).

> [!info] Comprendre la logique (terre à terre)
> **Ce que mesure vraiment $U$ :**
> Il y a $5 \times 5 = 25$ duels possibles entre un élève de A et un élève de B. $U_1 = 22$ signifie que dans **$22$ duels sur $25$**, l'élève de A bat celui de B, et dans $U_2 = 3$ duels seulement, B bat A ($88 > 78$, $88 > 85$, $80 > 78$). Avec seulement $5$ personnes par groupe, $U = 3$ reste juste au-dessus du seuil de rejet ($2$) : trop juste pour conclure en bilatéral.

> [!abstract] 🔎 Pourquoi cette méthode ? (indices de l'énoncé → choix)
> | Indice lu dans l'énoncé | Ce que ça implique |
> | :--- | :--- |
> | Deux groupes indépendants de $n_1 = n_2 = 5$ développeurs | Effectifs très faibles ($< 30$) sans garantie de normalité : test non paramétrique. |
> | $U_{\text{critique}} = 2$ fourni | Le critère $U$ confirme le choix du test sur les rangs conjoints. |
> 
> **Donc :** test de Mann-Whitney $U = \min(U_1, U_2)$ (rejet si $U \le U_{\text{critique}}$).

### Les formules utilisées
**Formules mathématiques :**
$$U_1 = R_1 - \frac{n_1(n_1 + 1)}{2}, \qquad U_2 = n_1 n_2 - U_1, \qquad U = \min(U_1, U_2)$$

**En français simple :**
`U₁ = Somme des rangs de A - Somme minimale possible si A était tout en bas (1 + 2 + ... + n₁)`
`U₂ = (Nb total de duels n₁ × n₂) - U₁`

### Résolution détaillée pas-à-pas

#### 1. Hypothèses et classement conjoint croissant (aucun ex-æquo)
On teste $H_0 :$ les deux distributions sont identiques contre $H_1 :$ l'une des deux méthodes donne des scores systématiquement plus élevés.

| Rang | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Note** | $60$ | $70$ | $75$ | $78$ | $80$ | $85$ | $88$ | $90$ | $92$ | $96$ |
| **Groupe** | **B** | **B** | **B** | **A** | **B** | **A** | **B** | **A** | **A** | **A** |

$$R_1 = 4 + 6 + 8 + 9 + 10 = \mathbf{37} \quad \left(R_2 = 1 + 2 + 3 + 5 + 7 = 18, \text{ vérif. } 37 + 18 = 55 = \frac{10 \times 11}{2}\right)$$

#### 2. Calcul de $U_1$
$$U_1 = R_1 - \frac{n_1(n_1 + 1)}{2} = 37 - \frac{5 \times (5 + 1)}{2} = 37 - \frac{30}{2} = 37 - 15 = \mathbf{22}$$

#### 3. Calcul de $U_2$ et $U$
$$n_1 n_2 = 5 \times 5 = 25 \implies U_2 = n_1 n_2 - U_1 = 25 - 22 = \mathbf{3}$$
$$U = \min(U_1, U_2) = \min(22, 3) = \mathbf{3}$$

#### 4. Décision ($\alpha = 5\%$ bilatéral)
On compare $U = 3$ à $U_{\text{critique}} = \mathbf{2}$ (rejet si $U \le U_{\text{critique}}$).

> [!check] Conclusion concrète
> Comme $U = 3 > U_{\text{critique}} = 2$, **on ne rejette pas $H_0$** au seuil de $5\%$ : l'écart de notes en faveur du présentiel n'est pas statistiquement suffisant avec seulement $5$ développeurs par groupe.

---

## 📌 Exercice 14 – Mann-Whitney : Temps de résolution d'incidents

> [!question] Énoncé résumé & Données
> On compare les temps de résolution d'incidents ITIL entre $n_1 = 6$ Juniors ($R_1 = 51$) et $n_2 = 6$ Seniors ($R_2 = 27$), soit $N = 6 + 6 = 12$ observations ($U_{\text{critique}} = 5$ à $\alpha = 5\%$).

> [!info] Comprendre la logique (terre à terre)
> **Deux vérifications gratuites pour zéro erreur de calcul :**
> D'abord, $R_1 + R_2$ doit **toujours** égaler $\frac{N(N+1)}{2}$ ; ensuite, $U_1 + U_2$ doit **toujours** égaler $n_1 \times n_2$. Si l'une des deux échoue, il y a une erreur d'addition ou de rang.

> [!abstract] 🔎 Pourquoi cette méthode ? (indices de l'énoncé → choix)
> | Indice lu dans l'énoncé | Ce que ça implique |
> | :--- | :--- |
> | Deux groupes indépendants ($n_1 = 6$, $n_2 = 6$), sommes de rangs $R_1, R_2$ données | Petits échantillons non paramétriques déjà mis en rangs. |
> | $U_{\text{critique}} = 5$ fourni | On passe directement des rangs aux statistiques $U_1, U_2$ puis $U = \min(U_1, U_2)$. |
> 
> **Donc :** test de Mann-Whitney $U$ (rejet si $U \le U_{\text{critique}}$).

### Les formules utilisées
**Formules mathématiques :**
$$\sum \text{Rangs} = \frac{N(N + 1)}{2}, \qquad U_1 = R_1 - \frac{n_1(n_1 + 1)}{2}, \qquad U_2 = R_2 - \frac{n_2(n_2 + 1)}{2}, \qquad U = \min(U_1, U_2)$$

### Résolution détaillée pas-à-pas

#### 1. Hypothèses et vérification de la somme des rangs
On teste $H_0 :$ temps de résolution identiques (Juniors vs Seniors) contre $H_1 :$ distributions différentes :
$$\sum \text{Rangs} = R_1 + R_2 = 51 + 27 = 78, \qquad \frac{N(N + 1)}{2} = \frac{12 \times (12 + 1)}{2} = \frac{156}{2} = \mathbf{78} \quad (\text{vérifié})$$

#### 2. Calcul de $U_1$ et $U_2$
$$U_1 = R_1 - \frac{n_1(n_1 + 1)}{2} = 51 - \frac{6 \times (6 + 1)}{2} = 51 - \frac{42}{2} = 51 - 21 = \mathbf{30}$$
$$U_2 = R_2 - \frac{n_2(n_2 + 1)}{2} = 27 - \frac{6 \times (6 + 1)}{2} = 27 - 21 = \mathbf{6}$$
*(Vérification : $U_1 + U_2 = 30 + 6 = 36 = n_1 n_2 = 6 \times 6$.)*

#### 3. Statistique $U$ et décision ($\alpha = 5\%$ bilatéral)
$$U = \min(U_1, U_2) = \min(30, 6) = \mathbf{6} > U_{\text{critique}} = 5$$

> [!check] Conclusion concrète
> Comme $U = 6 > U_{\text{critique}} = 5$, **on ne rejette pas $H_0$** au seuil bilatéral de $5\%$ *(résultat très proche de la limite critique, où un test unilatéral à $5\%$ aurait rejeté ; les effectifs sont trop faibles pour conclure formellement en bilatéral)*.

---

## 📌 Exercice 15 – Chi-Deux : OS mobile et validation 2FA ($n = 100$)

> [!question] Énoncé résumé & Données
> Un RSSI croise l'OS mobile (iOS $50$, Android $50$) et le mode de validation 2FA choisi (App Mobile $60$, SMS $40$) sur $n = 100$ salariés ($\chi^2_{\text{critique}} = 3{,}841$ à $\alpha = 5\%$).

> [!info] Comprendre la logique (terre à terre)
> **Pourquoi $\frac{\text{Total ligne} \times \text{Total colonne}}{N}$ représente-t-il l'indépendance ?**
> Globalement, $60\%$ des salariés utilisent l'App ($60/100$). Si l'OS n'avait aucune influence sur ce choix, on retrouverait ces mêmes $60\%$ chez les $50$ utilisateurs iOS ($60\% \times 50 = 30$) et chez les $50$ utilisateurs Android ($30$). Le $\chi^2$ mesure l'ampleur du décalage entre ce monde neutre ($30$) et la réalité ($35$ vs $25$).

> [!abstract] 🔎 Pourquoi cette méthode ? (indices de l'énoncé → choix)
> | Indice lu dans l'énoncé | Ce que ça implique |
> | :--- | :--- |
> | Deux variables qualitatives croisées (OS mobile $\times$ mode 2FA) | Pas de moyenne ni de variance : on teste le lien entre deux caractères dans un tableau de contingence. |
> | Tableau $2 \times 2$, tous $E_{ij} \ge 5$ | Conditions du $\chi^2$ d'indépendance remplies. |
> 
> **Donc :** test du $\chi^2$ d'indépendance avec $E_{ij} = \frac{L_i \times C_j}{N}$ et $\text{ddl} = (l - 1)(c - 1)$.

### Les formules utilisées
**Formules mathématiques :**
$$E_{ij} = \frac{\text{Total ligne}_i \times \text{Total colonne}_j}{N}, \qquad \chi^2_{\text{obs}} = \sum \frac{(O_{ij} - E_{ij})^2}{E_{ij}}, \qquad \text{ddl} = (l - 1)(c - 1)$$

**En français simple :**
`Effectif attendu = (Total de sa ligne × Total de sa colonne) ÷ Effectif total`
`ddl = (Nb lignes - 1) × (Nb colonnes - 1)`

### Résolution détaillée pas-à-pas

#### 1 & 2. Hypothèses, effectifs théoriques $E_{ij}$ et contributions $\frac{(O_{ij} - E_{ij})^2}{E_{ij}}$
On teste $H_0 :$ indépendance entre l'OS mobile et le mode 2FA contre $H_1 :$ dépendance.
Calcul détaillé des 4 cases :
- **iOS / App Mobile :** $E_{11} = \frac{50 \times 60}{100} = 30 \implies \text{Contrib} = \frac{(35 - 30)^2}{30} = \frac{25}{30} = \mathbf{0{,}8333}$
- **iOS / SMS :** $E_{12} = \frac{50 \times 40}{100} = 20 \implies \text{Contrib} = \frac{(15 - 20)^2}{20} = \frac{25}{20} = \mathbf{1{,}2500}$
- **Android / App Mobile :** $E_{21} = \frac{50 \times 60}{100} = 30 \implies \text{Contrib} = \frac{(25 - 30)^2}{30} = \frac{25}{30} = \mathbf{0{,}8333}$
- **Android / SMS :** $E_{22} = \frac{50 \times 40}{100} = 20 \implies \text{Contrib} = \frac{(25 - 20)^2}{20} = \frac{25}{20} = \mathbf{1{,}2500}$

| OS \ 2FA | App Mobile ($T_1 = 60$) | SMS ($T_2 = 40$) | Total |
| :--- | :---: | :---: | :---: |
| **iOS** ($S_1 = 50$) | $O=35$, $E=\mathbf{30}$, Contrib $=\mathbf{0{,}8333}$ | $O=15$, $E=\mathbf{20}$, Contrib $=\mathbf{1{,}2500}$ | 50 |
| **Android** ($S_2 = 50$) | $O=25$, $E=\mathbf{30}$, Contrib $=\mathbf{0{,}8333}$ | $O=25$, $E=\mathbf{20}$, Contrib $=\mathbf{1{,}2500}$ | 50 |
| **Total** | **60** | **40** | **100** |

*(Condition d'application vérifiée : tous les $E_{ij} \ge 5$, car le plus petit vaut $20$.)*

#### 3 & 4. Statistique $\chi^2$, ddl et décision ($\alpha = 5\%$)
$$\chi^2_{\text{obs}} = 0{,}8333 + 1{,}2500 + 0{,}8333 + 1{,}2500 = \mathbf{4{,}1667} \quad (p = 0{,}0412)$$
$$\text{ddl} = (l - 1)(c - 1) = (2 - 1)(2 - 1) = 1 \times 1 = \mathbf{1}$$
En Annexe B ($\nu = 1$, colonne `0,05`), $\chi^2_{\text{critique}} = \mathbf{3{,}841}$.

> [!check] Conclusion concrète
> Comme $\chi^2_{\text{obs}} = 4{,}1667 > \chi^2_{\text{critique}} = 3{,}841$, **on rejette l'hypothèse d'indépendance $H_0$** : le choix du mode 2FA dépend significativement de l'OS (les utilisateurs iOS privilégient davantage l'app d'authentification que ceux d'Android).

---

## 📌 Exercice 16 – Chi-Deux : Architecture SI et satisfaction du DSI ($n = 200$)

> [!question] Énoncé résumé & Données
> Une étude auprès de $200$ entreprises croise le type d'architecture SI (Monolithe, Microservices, Serverless) et la satisfaction du DSI (Satisfait / Non satisfait), avec les effectifs observés et attendus fournis ($\chi^2_{0{,}05}(2) = 5{,}991$).

> [!info] Comprendre la logique (terre à terre)
> **Lire les contributions pour comprendre d'où vient le résultat :**
> Le $\chi^2$ total te dit « il y a un lien », mais ce sont les **contributions individuelles** qui te disent *pourquoi*. Ici, la case *Monolithe / Non satisfait* pèse à elle seule **$15{,}0$ sur $28{,}89$** (plus de la moitié du score !) : c'est l'insatisfaction massive sur le Monolithe ($30/60 = 50\%$ de mécontents contre $10/80 = 12{,}5\%$ et $10/60 = 16{,}7\%$ ailleurs) qui crée la dépendance.

> [!abstract] 🔎 Pourquoi cette méthode ? (indices de l'énoncé → choix)
> | Indice lu dans l'énoncé | Ce que ça implique |
> | :--- | :--- |
> | Architecture SI $\times$ satisfaction du DSI en tableau $3 \times 2$ | Croisement de deux variables qualitatives : test d'indépendance. |
> | Effectifs observés $O_i$ et attendus $E_i \ge 15 \ge 5$ fournis | Calcul direct des contributions au $\chi^2$ avec $\text{ddl} = (3 - 1)(2 - 1) = 2$. |
> 
> **Donc :** test du $\chi^2$ d'indépendance à $2$ degrés de liberté.

### Les formules utilisées
**Formules mathématiques :**
$$\chi^2_{\text{obs}} = \sum \frac{(O_{ij} - E_{ij})^2}{E_{ij}}, \qquad \text{ddl} = (l - 1)(c - 1)$$

### Résolution détaillée pas-à-pas

#### 1. Hypothèses et calcul de la statistique globale du $\chi^2$
On teste $H_0 :$ l'architecture SI et la satisfaction du DSI sont indépendantes contre $H_1 :$ elles sont liées.

| Architecture / Satisfaction | $O_i$ | $E_i$ | $(O_i - E_i)^2$ | $\dfrac{(O_i - E_i)^2}{E_i}$ |
| :--- | :---: | :---: | :---: | :---: |
| **Monolithe / Satisfait** | $30$ | $45$ | $(30 - 45)^2 = 225$ | $\frac{225}{45} = 5{,}0000$ |
| **Monolithe / Non satisfait** | $30$ | $15$ | $(30 - 15)^2 = 225$ | $\frac{225}{15} = 15{,}0000$ |
| **Microservices / Satisfait** | $70$ | $60$ | $(70 - 60)^2 = 100$ | $\frac{100}{60} = 1{,}6667$ |
| **Microservices / Non satisfait** | $10$ | $20$ | $(10 - 20)^2 = 100$ | $\frac{100}{20} = 5{,}0000$ |
| **Serverless / Satisfait** | $50$ | $45$ | $(50 - 45)^2 = 25$ | $\frac{25}{45} = 0{,}5556$ |
| **Serverless / Non satisfait** | $10$ | $15$ | $(10 - 15)^2 = 25$ | $\frac{25}{15} = 1{,}6667$ |
| **Total ($\sum$)** | **$200$** | **$200$** | — | **$\mathbf{28{,}8889}$** |

$$\chi^2_{\text{obs}} = 5{,}0000 + 15{,}0000 + 1{,}6667 + 5{,}0000 + 0{,}5556 + 1{,}6667 = \frac{260}{9} \approx \mathbf{28{,}8889} \quad (p = 5{,}3 \times 10^{-7})$$

#### 2. Degrés de liberté
Pour un tableau $3 \times 2$ (condition vérifiée : tous les $E_i \ge 15 \ge 5$) :
$$\text{ddl} = (l - 1)(c - 1) = (3 - 1)(2 - 1) = 2 \times 1 = \mathbf{2}$$

#### 3. Décision au seuil $\alpha = 5\%$
En Annexe B ($\nu = 2$, colonne `0,05`), $\chi^2_{0{,}05}(2) = \mathbf{5{,}991}$. Calcul des taux de satisfaction observés :
- Microservices : $\frac{70}{70 + 10} = \frac{70}{80} = \mathbf{87{,}5\%}$
- Serverless : $\frac{50}{50 + 10} = \frac{50}{60} = \mathbf{83{,}3\%}$
- Monolithe : $\frac{30}{30 + 30} = \frac{30}{60} = \mathbf{50{,}0\%}$

> [!check] Conclusion concrète
> Comme $\chi^2_{\text{obs}} = 28{,}89 \gg \chi^2_{0{,}05}(2) = 5{,}991$, **on rejette très nettement $H_0$** : il existe une association forte entre l'architecture SI et la satisfaction du DSI (Microservices à $87{,}5\%$ et Serverless à $83{,}3\%$, contre seulement $50\%$ pour le Monolithe).
