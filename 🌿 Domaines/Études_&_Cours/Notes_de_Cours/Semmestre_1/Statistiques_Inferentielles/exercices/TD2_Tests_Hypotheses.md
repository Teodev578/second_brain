---
type: note-cours
created: 2026-11-23
matiere: "Statistiques Inférentielles"
chapitre: "TD 2 - Tests d'Hypothèses"
enseignant: "K. E. HOVI"
tags:
  - etudes
  - td
  - statistiques-inferentielles
  - tests-parametriques
  - tests-non-parametriques
  - anova
  - khi-deux
  - wilcoxon
  - mann-whitney
parent: "[[MOC_Statistiques_Inferentielles]]"
---

# 📝 TD 2. Tests d'Hypothèses

> **Matière :** [[MOC_Statistiques_Inferentielles|Statistiques Inférentielles (M1 IT)]] • **Support :** Feuille d'exercices n° 2 (p. 48–53) • **Statut :** Entièrement Résolu & Démontré

---

## 📌 Exercice 1 – Montant moyen des remboursements de crédit

Données : $n = 144$, $\bar{x} = 193{,}74$ €, $s = 48{,}24$ €, valeur postulée $\mu_0 = 200$ €.

### 1. Hypothèses et type de test
- $H_0 : \mu = 200$ € contre $H_1 : \mu \ne 200$ € (**test bilatéral** de conformité sur une moyenne).
- Comme $n = 144 \ge 30$ (grand échantillon), par le TCL, la statistique $Z = \frac{\overline{X} - \mu_0}{s/\sqrt{n}}$ suit approximativement $\mathcal{N}(0, 1)$ sous $H_0$.

### 2. Décision au risque $\alpha = 5\%$
- Erreur standard : $\frac{s}{\sqrt{n}} = \frac{48{,}24}{\sqrt{144}} = \frac{48{,}24}{12} = 4{,}02$ €.
- Statistique observée :
  $$z_{\text{obs}} = \frac{193{,}74 - 200}{4{,}02} = \frac{-6{,}26}{4{,}02} \approx \mathbf{-1{,}5572}$$
- Seuils critiques à $\alpha = 5\%$ (bilatéral) : $z_{\text{crit}} = \pm 1{,}96$ (soit en euros : $200 \pm 1{,}96 \times 4{,}02 = \mathbf{[192{,}12 \,;\, 207{,}88]}$ €).
- **Conclusion :** $|z_{\text{obs}}| = 1{,}5572 < 1{,}96$ (et $193{,}74 \in [192{,}12 \,;\, 207{,}88]$). **On ne rejette pas $H_0$** : l'écart observé est compatible avec les fluctuations d'échantillonnage.

### 3 & 4. Schéma des régions et $p$-value
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
$$p\text{-value} = P(|Z| \ge 1{,}5572) = 2\big(1 - \Phi(1{,}5572)\big)$$
Par l'Annexe A.1 ($\Phi(1{,}56) = 0{,}9406$) : $p \approx 2(1 - 0{,}9406) = 0{,}1188$ (valeur exacte : **$\mathbf{0{,}1194}$**, soit $11{,}94\%$).

### 5. Réponse pour $\alpha = 10\%$
Comme $p\text{-value} = 0{,}1194 > \alpha = 0{,}10$ (équivalent à $|z_{\text{obs}}| = 1{,}5572 < z_{0{,}95} = 1{,}6449$), **on ne rejette toujours pas $H_0$** au risque de $10\%$.

---

## 📌 Exercice 2 – Parité dans les filières informatiques

Données : $n = 64$, nombre de femmes $= 28 \implies f = \frac{28}{64} = 0{,}4375$ ($43{,}75\%$).
- **Hypothèses (test bilatéral de conformité d'une proportion) :** $H_0 : p = 0{,}50$ vs $H_1 : p \ne 0{,}50$.
- **Conditions :** $n p_0 = 32 \ge 5$ et $n(1 - p_0) = 32 \ge 5 \implies$ approximation normale valide.
- **Statistique sous $H_0$ :**
  $$z_{\text{obs}} = \frac{f - p_0}{\sqrt{p_0(1 - p_0)/n}} = \frac{0{,}4375 - 0{,}50}{\sqrt{0{,}25 / 64}} = \frac{-0{,}0625}{0{,}0625} = \mathbf{-1{,}00}$$
- **Décision ($\alpha = 5\%$) :** $|z_{\text{obs}}| = 1{,}00 < 1{,}96$ ($p\text{-value} = 2(1 - \Phi(1{,}00)) = 2(1 - 0{,}8413) = \mathbf{0{,}3174}$). **On ne rejette pas $H_0$** : l'écart observé ne permet pas de contester l'égale attractivité de la filière auprès des hommes et des femmes.

---

## 📌 Exercice 3 – Variabilité sur les scores d'évaluation

### 1. Estimation sans biais de $\sigma$ ($n = 30$)
- $\sum_{i=1}^{30} x_i = 3120 \implies \bar{x} = \frac{3120}{30} = 104{,}00$.
- $\sum_{i=1}^{30} (x_i - 104)^2 = 7132$.
- Variance corrigée (sans biais) : $s^2 = \frac{7132}{29} \approx \mathbf{245{,}9310}$.
- Estimation de l'écart-type : $s = \sqrt{245{,}9310} \approx \mathbf{15{,}6822}$ points *(variance biaisée : $\bar{s}^2 = 237{,}7333$)*.

### 2. Test sur l'écart-type ($\sigma_0 = 20 \implies \sigma_0^2 = 400$, $\alpha = 5\%$)
- **Hypothèse préalable indispensable :** Les 30 scores forment un échantillon iid issu d'une **loi normale** (condition requise pour que la statistique du $\chi^2$ soit valide).
- **Hypothèses (unilatéral droit) :** $H_0 : \sigma \le 20$ ($\sigma^2 \le 400$) vs $H_1 : \sigma > 20$ ($\sigma^2 > 400$).
- **Statistique sous $H_0$ :**
  $$V = \frac{(n - 1)s^2}{\sigma_0^2} = \frac{7132}{400} = \mathbf{17{,}8300} \sim \chi^2(29)$$
- **Seuil critique :** En Annexe B ($\nu = 29, \alpha = 0{,}05$), $\chi^2_{0{,}95}(29) = \mathbf{42{,}5570}$.
- **Décision :** $V = 17{,}8300 < 42{,}5570$ ($p = 0{,}9477$). **On ne rejette pas $H_0$** : l'exigence d'homogénéité ($\sigma \le 20$) est largement respectée.

---

## 📌 Exercice 4 – Conformité d'une norme d'aménagement municipal

Données ($n = 10$) : `25.6, 24.5, 24.3, 25.0, 29.5, 24.1, 24.8, 24.7, 25.2, 24.9` (en %).
- **Hypothèses :** On suppose que le pourcentage suit une loi normale (petit effectif $n=10$).
  - Test unilatéral gauche : $H_0 : \mu \ge 25\%$ (norme respectée en moyenne) contre $H_1 : \mu < 25\%$ (quota non respecté).
- **Calculs :** $\sum x_i = 252{,}6 \implies \bar{x} = \mathbf{25{,}26\%}$ ; $\sum (x_i - 25{,}26)^2 = 21{,}664 \implies s^2 = \frac{21{,}664}{9} = 2{,}4071 \implies s = \mathbf{1{,}5515\%}$.
- **Statistique :**
  $$t_{\text{obs}} = \frac{25{,}26 - 25}{1{,}5515 / \sqrt{10}} = \frac{0{,}26}{0{,}4906} \approx \mathbf{+0{,}5299} \sim t(9)$$
- **Décision ($\alpha = 2{,}5\%$) :**
  - En unilatéral gauche, la valeur critique à $2{,}5\%$ (Annexe C, col. bilatérale `0,050`, $\nu = 9$) vaut $-t_{9, 0{,}975} = -2{,}2622$. Comme $t_{\text{obs}} = +0{,}53 > -2{,}2622$ (la moyenne est même au-dessus de $25\%$), **on ne rejette pas $H_0$**.
  - *(Même en bilatéral à $\alpha = 2{,}5\%$, $p = 0{,}6090 \gg 0{,}025$.)*
- **Conclusion & nuance :** Les communes respectent statistiquement le quota en moyenne au seuil de $2{,}5\%$. *(Note critique : 7 communes sur 10 sont légèrement sous $25\%$, la moyenne de $25{,}26\%$ étant tirée vers le haut par une seule valeur extrême à $29{,}5\%$.)*

---

## 📌 Exercice 5 – Test d'ajustement du Khi-deux et dimensionnement

### 1. Espérance, variance et loi candidate ($n = 53$ heures)
Reprendre le tableau de TD 1 Ex. 4 : $\bar{x} = \frac{212}{53} = \mathbf{4{,}00}$ appels/h, $\bar{s}^2 = 3{,}8491$, $s^2 = 3{,}9231$.
Comme $\bar{x} \approx s^2$ sur un comptage discret, on teste l'ajustement à une **loi de Poisson $\mathcal{P}(\lambda = 4)$**.

### 2. Test d'ajustement du $\chi^2$ au risque $\alpha = 5\%$
Probabilités théoriques $p_k = e^{-4}\frac{4^k}{k!}$ et effectifs attendus $E_k = 53 p_k$ :
- $k=0$ : $E_0 = 0{,}971$ ; $k=1$ : $E_1 = 3{,}883$ ; $k=2$ : $E_2 = 7{,}766$ ; $k=3$ : $E_3 = 10{,}354$ ; $k=4$ : $E_4 = 10{,}354$ ; $k=5$ : $E_5 = 8{,}284$ ; $k=6$ : $E_6 = 5{,}522$ ; $k=7$ : $E_7 = 3{,}156$ ; $k=8$ : $E_8 = 1{,}578$ ; $k \ge 9$ : $E_{9+} = 1{,}132$.

Pour respecter strictement la condition **$E_i \ge 5$** dans chaque classe, on regroupe les classes extrêmes $\{0, 1, 2\}$ ($E = 12{,}62$) et $\{7, 8, 9+\}$ ($E = 5{,}87$) :

| Classe | $O_i$ | $E_i$ | $\dfrac{(O_i - E_i)^2}{E_i}$ |
| :--- | :---: | :---: | :---: |
| **0–2** | 12 | 12,6195 | 0,0304 |
| **3** | 11 | 10,3544 | 0,0402 |
| **4** | 10 | 10,3544 | 0,0121 |
| **5** | 9 | 8,2836 | 0,0620 |
| **6** | 5 | 5,5224 | 0,0494 |
| **7 et +** | 6 | 5,8657 | 0,0031 |
| **Total** | **53** | **53,0000** | **$\chi^2_{\text{obs}} = 0{,}1972$** |

- **Degrés de liberté :** $\nu = (\text{nb classes}) - 1 - (\text{nb paramètres estimés}) = 6 - 1 - 1 = \mathbf{4}$ (car $\lambda$ a été estimé).
- **Valeur critique (Annexe B, $\nu=4, \alpha=0{,}05$) :** $\chi^2_{0{,}95}(4) = \mathbf{9{,}4877}$.
- **Décision :** $\chi^2_{\text{obs}} = 0{,}1972 \ll 9{,}4877$ ($p = 0{,}9954$). On ne rejette pas $H_0$ : l'ajustement à $\mathcal{P}(4)$ est excellent. *(Avec le regroupement $\{0,1\}$ [$E=4{,}85$] et $\{6+\}$, on obtient $\chi^2 = 0{,}2075$, même conclusion.)*

### 3. Nombre d'opérateurs pour répondre à au moins 95% des appels
Sous $X \sim \mathcal{P}(4)$ :
- $P(X \le 7) = 0{,}94887 < 0{,}95$ (un seul opérateur à 7 appels/h est légèrement insuffisant : $94{,}89\%$).
- $P(X \le 8) = 0{,}97864 \ge 0{,}95$.
Il faut donc employer **2 opérateurs** (capacité cumulée de 14 appels/h, couvrant $99{,}998\%$ des heures).

---

## 📌 Exercice 6 – Comparaison de deux proportions (Tmoney / Flooz)

- Lomé : $n_1 = 2000$, $k_1 = 1040 \implies f_1 = 0{,}52$.
- Kara : $n_2 = 1500$, $k_2 = 915 \implies f_2 = 0{,}61$.
- **Hypothèses :** $H_0 : p_1 = p_2$ vs $H_1 : p_1 \ne p_2$ (bilatéral, $\alpha = 5\%$).
- **Proportion poolée sous $H_0$ :** $F = \frac{1040 + 915}{2000 + 1500} = \frac{1955}{3500} \approx \mathbf{0{,}5586}$.
- **Statistique :**
  $$z_{\text{obs}} = \frac{0{,}52 - 0{,}61}{\sqrt{0{,}5586 \times 0{,}4414 \times \left(\frac{1}{2000} + \frac{1}{1500}\right)}} = \frac{-0{,}09}{0{,}01696} \approx \mathbf{-5{,}3064}$$
- **Décision :** $|z_{\text{obs}}| = 5{,}31 > 1{,}96$ ($p < 10^{-6}$). **Rejet catégorique de $H_0$** : le taux d'utilisation du paiement mobile diffère significativement (plus élevé à Kara : $61\%$ vs $52\%$).

---

## 📌 Exercice 7 – ANOVA : Impact d'une campagne publicitaire (7 régions)

### 1. Interprétation de $\overline{X}_k$ et $\overline{X}$
- $\overline{X}_k$ est le **nombre moyen de nouveaux clients par agent général dans la région $k$**.
- $\overline{X}$ est la **moyenne globale** (tous agents confondus sur l'ensemble des $n = 48$ agents des 7 zones).

### 2. Démonstration de l'équation d'analyse de variance ($V_T^2 = V_R^2 + V_A^2$)
Partons de $X_k^i - \overline{X} = (X_k^i - \overline{X}_k) + (\overline{X}_k - \overline{X})$. En élevant au carré et en sommant sur $k=1 \dots K$ et $i = 1 \dots n_k$ :
$$\sum_{k=1}^K \sum_{i=1}^{n_k} (X_k^i - \overline{X})^2 = \sum_{k=1}^K \sum_{i=1}^{n_k} (X_k^i - \overline{X}_k)^2 + \sum_{k=1}^K \sum_{i=1}^{n_k} (\overline{X}_k - \overline{X})^2 + 2\sum_{k=1}^K (\overline{X}_k - \overline{X})\underbrace{\sum_{i=1}^{n_k} (X_k^i - \overline{X}_k)}_{= 0}$$
Or, par définition de la moyenne $\overline{X}_k$, $\sum_{i=1}^{n_k} (X_k^i - \overline{X}_k) = n_k\overline{X}_k - n_k\overline{X}_k = 0$ pour tout $k$. Le terme rectangle s'annule donc identiquement. Comme $(\overline{X}_k - \overline{X})^2$ ne dépend pas de $i$, sa somme sur $i=1 \dots n_k$ vaut $n_k(\overline{X}_k - \overline{X})^2$. En divisant par $n$ :
$$\underbrace{\frac{1}{n}\sum_{k=1}^K \sum_{i=1}^{n_k} (X_k^i - \overline{X})^2}_{V_T^2} = \underbrace{\frac{1}{n}\sum_{k=1}^K \sum_{i=1}^{n_k} (X_k^i - \overline{X}_k)^2}_{V_R^2} + \underbrace{\frac{1}{n}\sum_{k=1}^K n_k (\overline{X}_k - \overline{X})^2}_{V_A^2} \quad \blacksquare$$

### 3. Calcul numérique de $V_T^2$, $V_A^2$ et $V_R^2$
- Effectif total : $n = 9 + 7 + 7 + 6 + 7 + 6 + 6 = \mathbf{48}$ agents.
- Moyenne globale pondérée :
  $$\overline{X} = \frac{9(26{,}88) + 7(22{,}34) + 7(19{,}54) + 6(18{,}95) + 7(27{,}17) + 6(25{,}87) + 6(25{,}72)}{48} = \frac{1148{,}51}{48} \approx \mathbf{23{,}9273}$$
- Variance inter-groupes :
  $$V_A^2 = \frac{1}{48}\sum_{k=1}^7 n_k(\overline{X}_k - 23{,}9273)^2 = \frac{495{,}0154}{48} \approx \mathbf{10{,}3128}$$
- Variance résiduelle (en retenant que les variances du tableau sont les variances intra-groupe $v_k^2 = \frac{1}{n_k}\sum_i (X_k^i - \overline{X}_k)^2$) :
  $$V_R^2 = \frac{1}{48}\sum_{k=1}^7 n_k v_k^2 = \frac{623{,}99}{48} \approx \mathbf{12{,}9998}$$
- Variance totale : $V_T^2 = V_A^2 + V_R^2 = 10{,}3128 + 12{,}9998 = \mathbf{23{,}3126}$.
*(Note : si les variances du tableau étaient déjà corrigées par $n_k - 1$, on aurait $V_R^2 = \frac{533{,}20}{48} = 11{,}1083$ et $V_T^2 = 21{,}4212$.)*

### 4. Finalisation de l'ANOVA ($\alpha = 5\%$)
- Sommes des carrés : $\text{SC}_A = n V_A^2 = 495{,}0154$ ($\text{ddl}_A = K - 1 = 6$) ; $\text{SC}_R = n V_R^2 = 623{,}99$ ($\text{ddl}_R = n - K = 41$).
- Statistique de Fisher :
  $$F_{\text{obs}} = \frac{\text{SC}_A / 6}{\text{SC}_R / 41} = \frac{82{,}5026}{15{,}2193} \approx \mathbf{5{,}4209} \quad (p = 0{,}00034)$$
  *(Avec la variante $s_k^2$ corrigée : $F_{\text{obs}} = \mathbf{6{,}3440}$, $p = 8{,}8 \times 10^{-5}$.)*
- Valeur critique à $5\%$ : Annexe D.1 pour $\nu_1 = 6$, $\nu_2 = 40$ donne $F_{0{,}05}(6, 40) = 2{,}34$ (donc $F_{0{,}05}(6, 41) \approx 2{,}33$).
- **Décision :** $F_{\text{obs}} = 5{,}42 > 2{,}33$ $\implies$ **Rejet de $H_0$**. La campagne publicitaire n'a pas eu le même impact dans toutes les régions.

---

## 📌 Exercice 8 – Taille des garçons vs filles en CP

Données : Garçons ($n_1 = 41, \bar{x}_1 = 107\text{ cm}, v_1 = 8\text{ cm}$) ; Filles ($n_2 = 61, \bar{x}_2 = 104\text{ cm}, v_2 = 9\text{ cm}$).
- **Normalité vérifiée :** Shapiro-Wilk donne $p_1 = 0{,}82 > 0{,}05$ et $p_2 = 0{,}21 > 0{,}05 \implies$ compatibilité avec la loi normale dans les deux groupes.
- **Égalité des variances :** $F = \frac{9^2}{8^2} = 1{,}2656 < F_{0{,}025}(60, 40) \approx 1{,}84$ (Annexe D.2) $\implies$ homoscédasticité acceptée.
- **Hypothèses (unilatéral droit) :** $H_0 : \mu_1 = \mu_2$ contre $H_1 : \mu_1 > \mu_2$ au risque $\alpha = 5\%$.
- **Statistique (grands échantillons $n_1, n_2 > 30$) :**
  $$N_{\text{obs}} = \frac{107 - 104}{\sqrt{\frac{8^2}{41} + \frac{9^2}{61}}} = \frac{3}{\sqrt{1{,}5610 + 1{,}3279}} = \frac{3}{1{,}6997} \approx \mathbf{1{,}7651}$$
  *(Avec le test $t$ poolé à $n_1+n_2-2 = 100$ ddl : $s_p = 8{,}613$, $t_{\text{obs}} = 1{,}7246$, $p_{\text{unilat}} = 0{,}0438$.)*
- **Décision ($\alpha = 5\%$ unilatéral) :** $z_{0{,}95} = 1{,}6449$ (et $t_{100, 0{,}95} \approx 1{,}660$). Comme $1{,}7651 > 1{,}6449$ ($p = 0{,}0388 < 0{,}05$), **on rejette $H_0$** : on peut affirmer au seuil de 5% que les garçons de CP sont en moyenne plus grands que les filles.

---

## 📌 Exercice 9 – Sécurité routière : alcool et temps de réaction

Le tableau comporte $n = 15$ paires d'observations *(bien que l'énoncé introductif mentionne 30 chauffeurs)*. On pose $d_i = \text{Avec}_i - \text{Sans}_i$ (test **apparié bilatéral** : $H_0 : \mu_d = 0$ vs $H_1 : \mu_d \ne 0$, $\alpha = 5\%$).

- **Différences $d_i$ :** `0.05, -0.02, 0.08, 0.10, 0.10, 0.07, 0.05, 0.05, 0.04, 0.06, 0.07, 0.21, 0.00, 0.19, 0.13`.
- $\bar{d} = \frac{1{,}18}{15} \approx \mathbf{0{,}0787\text{ s}}$, écart-type corrigé $s_d \approx \mathbf{0{,}0619\text{ s}}$.
- **Statistique de Student apparié ($\nu = 14$ ddl) :**
  $$t_{\text{obs}} = \frac{0{,}07867}{0{,}06186 / \sqrt{15}} = \frac{0{,}07867}{0{,}01597} \approx \mathbf{4{,}9252}$$
- **Décision :** Annexe C ($\nu = 14, \alpha = 0{,}05$) donne $t_{\text{crit}} = 2{,}1448$. Comme $4{,}9252 > 2{,}1448$ ($p = 0{,}00022$), **on rejette $H_0$** : l'alcool augmente très significativement le temps de réaction au volant.
*(Note : si les deux lignes étaient traitées comme 2 groupes indépendants de taille 15, on obtiendrait $t = 2{,}6571 > 2{,}0484$ avec $\nu = 28$ et $p = 0{,}0129$, conduisant au même rejet de $H_0$.)*

---

## 📌 Exercice 10 – Efficacité d'un programme nutritionnel

Différences $d_i = \text{Après}_i - \text{Avant}_i$ (en kg, $N = 10$) : `-1, +1, -37, -2, -5, 0, -2, +1, -1, -2`.
- **Constat préalable critique :** L'individu n° 3 passe de $158$ à $121$ kg ($d_3 = -37$ kg), créant une **valeur aberrante massive** qui viole la normalité des différences.
  - Un test $t$ de Student apparié donne $\bar{d} = -4{,}8$ kg, $s_d = 11{,}45$ kg $\implies t = -1{,}3259$ ($p = 0{,}2175$), non significatif car l'outlier gonfle artificiellement $s_d$.
- **Choix méthodologique adapté : Test des rangs signés de Wilcoxon (non paramétrique, robuste aux outliers).**
  1. On retire la différence nulle ($58 \to 58$) : il reste $n = 9$ paires non nulles.
  2. Classement des $|d_i|$ :
     - $|d|=1$ (4 valeurs : $-1, +1, +1, -1$) $\to$ rangs $1,2,3,4 \implies$ rang moyen **$2{,}5$**.
     - $|d|=2$ (3 valeurs : $-2, -2, -2$) $\to$ rangs $5,6,7 \implies$ rang moyen **$6{,}0$**.
     - $|d|=5$ (1 valeur : $-5$) $\to$ rang **$8{,}0$**.
     - $|d|=37$ (1 valeur : $-37$) $\to$ rang **$9{,}0$**.
  3. Sommes des rangs :
     - $W^+ = \sum_{d_i > 0} r_i = 2{,}5 + 2{,}5 = \mathbf{5{,}0}$
     - $W^- = \sum_{d_i < 0} r_i = 2{,}5 + 2{,}5 + 6 + 6 + 6 + 8 + 9 = \mathbf{40{,}0}$ *(vérif. $5 + 40 = 45 = \frac{9 \times 10}{2}$)*
     - $W = \min(5, 40) = \mathbf{5{,}0}$.
  4. **Décision ($\alpha = 5\%$ bilatéral) :** Pour $n = 9$, la valeur critique bilatérale de Wilcoxon à $5\%$ est $W_{\text{crit}} = 5$ (et la $p$-value exacte tenant compte des ex-æquo est $22/512 = \mathbf{0{,}0430} < 0{,}05$). On **rejette $H_0$** au seuil de $5\%$ : le programme a un effet significatif à la baisse sur la masse corporelle (7 participants sur 10 ont perdu du poids).

---

## 📌 Exercice 11 – ANOVA : Temps de traitement selon le SGBD

$k = 3$ SGBD, $n_j = 5$ exécutions par groupe, $\text{SC}_{\text{Facteur}} = 320$, $\text{SC}_{\text{Résiduelle}} = 240$.
1. $N = 3 \times 5 = \mathbf{15}$ observations ; $\text{ddl}_{\text{facteur}} = k - 1 = \mathbf{2}$ ; $\text{ddl}_{\text{résiduelle}} = N - k = \mathbf{12}$.
2. $\text{MS}_{\text{facteur}} = \frac{320}{2} = \mathbf{160}$ ; $\text{MS}_{\text{résiduelle}} = \frac{240}{12} = \mathbf{20}$.
3. Statistique de Fisher : $F = \frac{160}{20} = \mathbf{8{,}00}$ ($p = 0{,}0062$).
4. Comme $F = 8{,}00 > F_{0{,}05}(2, 12) = 3{,}89$, **on rejette $H_0$** : le choix du SGBD a un impact statistiquement significatif sur le temps de traitement au seuil de 5%.

---

## 📌 Exercice 12 – ANOVA : Consommation RAM selon le langage

$k = 4$ langages, $N = 24$ mesures, $\text{SCT} = 1200$, $\text{SCR} = 300$.
1. $\text{SCE} = \text{SCT} - \text{SCR} = 1200 - 300 = \mathbf{900}$.
2. $\text{ddl}_{\text{facteur}} = 4 - 1 = 3$ ; $\text{ddl}_{\text{résiduelle}} = 24 - 4 = 20$.
   $\text{MS}_{\text{facteur}} = \frac{900}{3} = \mathbf{300}$ ; $\text{MS}_{\text{résiduelle}} = \frac{300}{20} = \mathbf{15}$.
3. $F = \frac{300}{15} = \mathbf{20{,}00}$ ($p = 3{,}1 \times 10^{-6}$).
4. Comme $F = 20{,}00 > F_{0{,}01}(3, 20) = 4{,}94$, **on rejette $H_0$ au seuil de 1%** : le langage de programmation influence très significativement la consommation mémoire.

---

## 📌 Exercice 13 – Mann-Whitney : Formation Agile (Présentiel vs E-learning)

$A : 78, 85, 90, 92, 96$ ($n_1 = 5$) ; $B : 60, 70, 75, 80, 88$ ($n_2 = 5$).
1. **Classement conjoint croissant (aucun ex-æquo) :**
   `60(B:1), 70(B:2), 75(B:3), 78(A:4), 80(B:5), 85(A:6), 88(B:7), 90(A:8), 92(A:9), 96(A:10)`.
   Somme des rangs du groupe A : $R_1 = 4 + 6 + 8 + 9 + 10 = \mathbf{37}$ *(et $R_2 = 18$, vérif. $37+18=55$)*.
2. $U_1 = R_1 - \frac{n_1(n_1+1)}{2} = 37 - \frac{5 \times 6}{2} = 37 - 15 = \mathbf{22}$.
3. $U_2 = n_1 n_2 - U_1 = 25 - 22 = \mathbf{3}$, d'où $U = \min(22, 3) = \mathbf{3}$.
4. **Décision ($\alpha = 5\%$ bilatéral) :** Comme $U = 3 > U_{\text{critique}} = 2$, **on ne rejette pas $H_0$** au seuil de 5% : l'écart de notes observé en faveur du présentiel n'est pas statistiquement suffisant avec seulement 5 développeurs par groupe.

---

## 📌 Exercice 14 – Mann-Whitney : Temps de résolution d'incidents

$n_1 = 6$ (Juniors, $R_1 = 51$), $n_2 = 6$ (Seniors, $R_2 = 27$), $N = 12$.
1. $\sum \text{Rangs} = R_1 + R_2 = 51 + 27 = 78$, et $\frac{N(N+1)}{2} = \frac{12 \times 13}{2} = \mathbf{78}$ (égalité vérifiée).
2. $U_1 = 51 - \frac{6 \times 7}{2} = 51 - 21 = \mathbf{30}$ ; $U_2 = 27 - 21 = \mathbf{6}$ *(vérif. $30 + 6 = 36 = 6 \times 6$)*.
3. $U = \min(30, 6) = \mathbf{6}$.
4. **Décision ($\alpha = 5\%$ bilatéral) :** $U = 6 > U_{\text{critique}} = 5$ $\implies$ **on ne rejette pas $H_0$** au seuil bilatéral de 5% *(résultat très proche de la limite critique, où un test unilatéral à 5% aurait rejeté ; les effectifs sont trop faibles pour conclure formellement en bilatéral)*.

---

## 📌 Exercice 15 – Chi-Deux : OS mobile et validation 2FA ($n = 100$)

### 1 & 2. Effectifs théoriques $E_i$ et contributions $\frac{(O_i - E_i)^2}{E_i}$

| OS \ 2FA | App Mobile ($T_1 = 60$) | SMS ($T_2 = 40$) | Total |
| :--- | :---: | :---: | :---: |
| **iOS** ($S_1 = 50$) | $O=35$, $E=\frac{50\times 60}{100}=\mathbf{30}$ <br> Contrib $= \frac{(35-30)^2}{30} = \mathbf{0{,}8333}$ | $O=15$, $E=\frac{50\times 40}{100}=\mathbf{20}$ <br> Contrib $= \frac{(15-20)^2}{20} = \mathbf{1{,}2500}$ | 50 |
| **Android** ($S_2 = 50$) | $O=25$, $E=\mathbf{30}$ <br> Contrib $= \frac{(25-30)^2}{30} = \mathbf{0{,}8333}$ | $O=25$, $E=\mathbf{20}$ <br> Contrib $= \frac{(25-20)^2}{20} = \mathbf{1{,}2500}$ | 50 |
| **Total** | **60** | **40** | **100** |

*(Condition vérifiée : tous les $E_i \ge 5$.)*

### 3 & 4. Statistique $\chi^2$, ddl et décision ($\alpha = 5\%$)
- $\chi^2_{\text{obs}} = 0{,}8333 + 1{,}2500 + 0{,}8333 + 1{,}2500 = \mathbf{4{,}1667}$ ($p = 0{,}0412$).
- $\text{ddl} = (2 - 1)(2 - 1) = \mathbf{1}$.
- Comme $\chi^2_{\text{obs}} = 4{,}1667 > \chi^2_{\text{critique}} = 3{,}841$, **on rejette l'hypothèse d'indépendance $H_0$** : le choix du mode 2FA dépend significativement du système d'exploitation (les utilisateurs iOS privilégient davantage l'app d'authentification que les utilisateurs Android).

---

## 📌 Exercice 16 – Chi-Deux : Architecture SI et satisfaction du DSI ($n = 200$)

### 1. Calcul de la statistique globale du $\chi^2$
- Monolithe / Satisfait : $\frac{(30 - 45)^2}{45} = \frac{225}{45} = 5{,}0000$
- Monolithe / Non satisfait : $\frac{(30 - 15)^2}{15} = \frac{225}{15} = 15{,}0000$
- Microservices / Satisfait : $\frac{(70 - 60)^2}{60} = \frac{100}{60} = 1{,}6667$
- Microservices / Non satisfait : $\frac{(10 - 20)^2}{20} = \frac{100}{20} = 5{,}0000$
- Serverless / Satisfait : $\frac{(50 - 45)^2}{45} = \frac{25}{45} = 0{,}5556$
- Serverless / Non satisfait : $\frac{(10 - 15)^2}{15} = \frac{25}{15} = 1{,}6667$

$$\chi^2_{\text{obs}} = 5 + 15 + 1{,}6667 + 5 + 0{,}5556 + 1{,}6667 = \frac{260}{9} \approx \mathbf{28{,}8889} \quad (p = 5{,}3 \times 10^{-7})$$

### 2. Degrés de liberté
Tableau $3 \times 2$ : $\text{ddl} = (3 - 1)(2 - 1) = \mathbf{2}$ *(tous les effectifs théoriques sont $\ge 15 \ge 5$)*.

### 3. Conclusion au seuil $\alpha = 5\%$
$\chi^2_{\text{obs}} = 28{,}89 \gg \chi^2_{0{,}05}(2) = 5{,}991$. **On rejette très nettement $H_0$** : il existe une association forte entre le type d'architecture et la satisfaction du DSI (les architectures Microservices [$87{,}5\%$ de satisfaits] et Serverless [$83{,}3\%$] sont associées à une satisfaction nettement supérieure au Monolithe [$50\%$]).
