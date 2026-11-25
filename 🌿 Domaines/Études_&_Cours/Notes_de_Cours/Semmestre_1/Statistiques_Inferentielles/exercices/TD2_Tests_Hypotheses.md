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

> **Matière :** [[MOC_Statistiques_Inferentielles|Statistiques Inférentielles (M1 IT)]] • **Support :** Feuille d'exercices n° 2 (p. 48–53) • **Statut :** Entièrement Résolu & Démontré • 🧰 [[TD2_Formules_et_Explications_Terre_a_Terre|Guide Formules & Explications Terre à Terre]]

---

## 📌 Exercice 1 – Montant moyen des remboursements de crédit

> [!question] Énoncé résumé & Données
> Un ingénieur risque crédit à Lomé veut vérifier si la mensualité moyenne de remboursement des clients vaut $\mu_0 = 200$ €. Sur un échantillon de $n = 144$ clients, il observe $\bar{x} = 193{,}74$ € et un écart-type corrigé $s = 48{,}24$ €.

### 1. Hypothèses et type de test
On pose un **test bilatéral de conformité** sur une moyenne :
$$H_0 : \mu = 200\text{ €} \qquad \text{contre} \qquad H_1 : \mu \ne 200\text{ €}$$
Comme $n = 144 \ge 30$ (grand échantillon), par le TCL, la statistique $Z$ suit approximativement $\mathcal{N}(0, 1)$ sous $H_0$.

### 2. Décision au risque $\alpha = 5\%$
On calcule l'erreur standard puis la statistique observée :
$$\text{Erreur standard} = \frac{s}{\sqrt{n}} = \frac{48{,}24}{\sqrt{144}} = \frac{48{,}24}{12} = 4{,}02\text{ €}$$
$$z_{\text{obs}} = \frac{193{,}74 - 200}{4{,}02} = \frac{-6{,}26}{4{,}02} \approx \mathbf{-1{,}5572}$$

À $\alpha = 5\%$ en bilatéral, les seuils critiques sont $z_{\text{crit}} = \pm 1{,}96$ (soit en euros : $200 \pm 1{,}96 \times 4{,}02 = \mathbf{[192{,}12 \,;\, 207{,}88]}$ €). Comme $|z_{\text{obs}}| = 1{,}5572 < 1{,}96$ (et $193{,}74 \in [192{,}12 \,;\, 207{,}88]$), **on ne rejette pas $H_0$**.

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
Par lecture de l'Annexe A.1 ($\Phi(1{,}56) = 0{,}9406$) :
$$p\text{-value} = P(|Z| \ge 1{,}5572) = 2\big(1 - \Phi(1{,}5572)\big) \approx 2(1 - 0{,}9406) = 0{,}1188 \quad (\text{exact : } \mathbf{0{,}1194}, \text{ soit } 11{,}94\%)$$

### 5. Réponse pour $\alpha = 10\%$
Comme $p\text{-value} = 0{,}1194 > \alpha = 0{,}10$ (équivalent à $|z_{\text{obs}}| = 1{,}5572 < z_{0{,}95} = 1{,}6449$), **on ne rejette toujours pas $H_0$** au risque de $10\%$.

> [!success] Conclusion
> Au seuil de $5\%$ comme à $10\%$, l'écart observé ($193{,}74$ € vs $200$ €) est compatible avec les fluctuations d'échantillonnage : la valeur moyenne postulée de $200$ € reste plausible.

---

## 📌 Exercice 2 – Parité dans les filières informatiques

> [!question] Énoncé résumé & Données
> Dans une promotion de Master IT à Lomé de $n = 64$ étudiants, on compte $k = 28$ femmes, soit une proportion observée $f = \frac{28}{64} = 0{,}4375$ ($43{,}75\%$). Peut-on soutenir que la filière attire autant les hommes que les femmes ($p_0 = 0{,}50$, $\alpha = 5\%$) ?

On formule un **test bilatéral de conformité d'une proportion** :
$$H_0 : p = 0{,}50 \qquad \text{contre} \qquad H_1 : p \ne 0{,}50$$

Les conditions de l'approximation normale sont satisfaites ($n p_0 = 32 \ge 5$ et $n(1 - p_0) = 32 \ge 5$). Sous $H_0$ :
$$z_{\text{obs}} = \frac{f - p_0}{\sqrt{\dfrac{p_0(1 - p_0)}{n}}} = \frac{0{,}4375 - 0{,}50}{\sqrt{\dfrac{0{,}50 \times 0{,}50}{64}}} = \frac{-0{,}0625}{0{,}0625} = \mathbf{-1{,}00}$$
$$p\text{-value} = 2\big(1 - \Phi(1{,}00)\big) = 2(1 - 0{,}8413) = \mathbf{0{,}3174}$$

> [!success] Conclusion
> Comme $|z_{\text{obs}}| = 1{,}00 < 1{,}96$ ($p = 0{,}3174 > 0{,}05$), **on ne rejette pas $H_0$** : l'écart observé ne permet pas de contester l'égale attractivité de la filière auprès des hommes et des femmes.

---

## 📌 Exercice 3 – Variabilité sur les scores d'évaluation

> [!question] Énoncé résumé & Données
> La Direction de l'Évaluation sélectionne $n = 30$ étudiants pour un test standardisé dont l'écart-type ne doit pas dépasser $\sigma_0 = 20$ points ($\sigma_0^2 = 400$), au risque $\alpha = 5\%$.

### 1. Estimation sans biais de $\sigma$ ($n = 30$)

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

$$\bar{x} = \frac{3\,120}{30} = \mathbf{104{,}00}$$
$$s^2 = \frac{7\,132}{29} = \frac{331\,612 - 30 \times 104^2}{29} \approx \mathbf{245{,}9310}$$
$$s = \sqrt{245{,}9310} \approx \mathbf{15{,}6822\text{ points}} \quad (\text{variance biaisée : } \bar{s}^2 = 237{,}7333)$$

### 2. Test sur l'écart-type ($\sigma_0 = 20 \implies \sigma_0^2 = 400$, $\alpha = 5\%$)
**Hypothèse préalable indispensable :**
Les $30$ scores doivent former un échantillon iid issu d'une **loi normale** pour que la loi du $\chi^2$ soit valide.

On teste unilatéralement à droite :
$$H_0 : \sigma \le 20 \ (\sigma^2 \le 400) \qquad \text{contre} \qquad H_1 : \sigma > 20 \ (\sigma^2 > 400)$$
$$V = \frac{(n - 1)s^2}{\sigma_0^2} = \frac{7\,132}{400} = \mathbf{17{,}8300} \sim \chi^2(29)$$

En Annexe B ($\nu = 29, \alpha = 0{,}05$), le seuil critique vaut $\chi^2_{0{,}95}(29) = \mathbf{42{,}5570}$.

> [!success] Conclusion
> Comme $V = 17{,}8300 < 42{,}5570$ ($p = 0{,}9477$), **on ne rejette pas $H_0$** : l'exigence d'homogénéité ($\sigma \le 20$) est largement respectée.

---

## 📌 Exercice 4 – Conformité d'une norme d'aménagement municipal

> [!question] Énoncé résumé & Données
> Une réglementation impose aux communes de consacrer au moins $25\%$ de leur budget aux infrastructures numériques. On relève ces pourcentages dans $n = 10$ communes (supposés normaux) au risque $\alpha = 2{,}5\%$ :
> `25.6, 24.5, 24.3, 25.0, 29.5, 24.1, 24.8, 24.7, 25.2, 24.9`

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

$$\bar{x} = \frac{252{,}6}{10} = \mathbf{25{,}26\%}$$
$$s^2 = \frac{21{,}664}{9} = \frac{6\,402{,}34 - 10 \times 25{,}26^2}{9} = 2{,}4071 \implies s = \mathbf{1{,}5515\%}$$
$$t_{\text{obs}} = \frac{25{,}26 - 25}{1{,}5515 / \sqrt{10}} = \frac{0{,}26}{0{,}4906} \approx \mathbf{+0{,}5299} \sim t(9)$$

En unilatéral gauche à $\alpha = 2{,}5\%$ (Annexe C, col. bilatérale `0,050`, $\nu = 9$), la valeur critique vaut $-t_{9, 0{,}975} = -2{,}2622$.

> [!success] Conclusion
> Comme $t_{\text{obs}} = +0{,}53 > -2{,}2622$ ($p = 0{,}6090$ en bilatéral), **on ne rejette pas $H_0$** : les communes respectent statistiquement le quota en moyenne à $\alpha = 2{,}5\%$ *(nuance critique : $7$ communes sur $10$ sont légèrement sous $25\%$, la moyenne étant tirée vers le haut par l'observation extrême à $29{,}5\%$)*.

---

## 📌 Exercice 5 – Test d'ajustement du Khi-deux et dimensionnement

> [!question] Énoncé résumé & Données
> Une plateforme d'assistance à Lomé relève le nombre d'appels reçus par heure sur $n = 53$ heures (données de TD 1 Ex. 4). On demande d'estimer l'espérance et la variance, de tester l'ajustement à la loi candidate au risque $5\%$, puis de trouver combien d'opérateurs (capacité $7$ appels/h chacun) couvrent au moins $95\%$ des appels.

### 1. Espérance, variance et loi candidate ($n = 53$ heures)
D'après TD 1 Ex. 4 :
$$\bar{x} = \frac{212}{53} = \mathbf{4{,}00\text{ appels/h}}, \qquad \bar{s}^2 = 3{,}8491, \qquad s^2 = 3{,}9231$$
Comme $\bar{x} \approx s^2$ sur un comptage discret, on teste l'ajustement à une **loi de Poisson $\mathcal{P}(\lambda = 4)$**.

### 2. Test d'ajustement du $\chi^2$ au risque $\alpha = 5\%$
Probabilités théoriques $p_k = e^{-4}\frac{4^k}{k!}$ et effectifs attendus $E_k = 53 p_k$ avant regroupement :
$E_0 = 0{,}971$, $E_1 = 3{,}883$, $E_2 = 7{,}766$, $E_3 = 10{,}354$, $E_4 = 10{,}354$, $E_5 = 8{,}284$, $E_6 = 5{,}522$, $E_7 = 3{,}156$, $E_8 = 1{,}578$, $E_{9+} = 1{,}132$.

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

Nombre de degrés de liberté ($\lambda$ estimé sur les données) :
$$\nu = (\text{nb classes}) - 1 - (\text{nb paramètres estimés}) = 6 - 1 - 1 = \mathbf{4}$$

En Annexe B ($\nu=4, \alpha=0{,}05$), $\chi^2_{0{,}95}(4) = \mathbf{9{,}4877}$. Comme $\chi^2_{\text{obs}} = 0{,}1972 \ll 9{,}4877$ ($p = 0{,}9954$), on ne rejette pas $H_0$ : l'ajustement à $\mathcal{P}(4)$ est excellent. *(Avec le regroupement $\{0,1\}$ [$E=4{,}85$] et $\{6+\}$, $\chi^2 = 0{,}2075$, même conclusion.)*

### 3. Nombre d'opérateurs pour répondre à au moins 95% des appels
Sous $X \sim \mathcal{P}(4)$ :
$$P(X \le 7) = 0{,}94887 < 0{,}95 \quad (\text{1 opérateur insuffisant : } 94{,}89\%)$$
$$P(X \le 8) = 0{,}97864 \ge 0{,}95$$

> [!success] Conclusion
> L'ajustement à $\mathcal{P}(4)$ est validé ($\chi^2 = 0{,}1972 < 9{,}4877$) et il faut employer **2 opérateurs** (capacité cumulée de $14$ appels/h, couvrant $99{,}998\%$ des heures).

---

## 📌 Exercice 6 – Comparaison de deux proportions (Tmoney / Flooz)

> [!question] Énoncé résumé & Données
> À Lomé, $1\,040$ personnes sur $2\,000$ utilisent régulièrement le paiement mobile ($f_1 = 0{,}52$). À Kara, elles sont $915$ sur $1\,500$ ($f_2 = 0{,}61$). Ces taux diffèrent-ils au risque $\alpha = 5\%$ ?

On teste $H_0 : p_1 = p_2$ contre $H_1 : p_1 \ne p_2$ (bilatéral). Sous $H_0$, la proportion poolée vaut :
$$F = \frac{1\,040 + 915}{2\,000 + 1\,500} = \frac{1\,955}{3\,500} \approx \mathbf{0{,}5586}$$

La statistique de test vaut :
$$z_{\text{obs}} = \frac{0{,}52 - 0{,}61}{\sqrt{0{,}5586 \times 0{,}4414 \times \left(\dfrac{1}{2\,000} + \dfrac{1}{1\,500}\right)}} = \frac{-0{,}09}{0{,}01696} \approx \mathbf{-5{,}3064}$$

> [!success] Conclusion
> Comme $|z_{\text{obs}}| = 5{,}31 > 1{,}96$ ($p < 10^{-6}$), on **rejette catégoriquement $H_0$** : le taux d'utilisation du paiement mobile est significativement plus élevé à Kara ($61\%$) qu'à Lomé ($52\%$).

---

## 📌 Exercice 7 – ANOVA : Impact d'une campagne publicitaire (7 régions)

> [!question] Énoncé résumé & Données
> Une compagnie d'assurance étudie le nombre de nouveaux clients obtenus par $n = 48$ agents généraux répartis dans $K = 7$ régions du Togo. On demande d'interpréter $\overline{X}_k$ et $\overline{X}$, de démontrer l'équation de décomposition de variance, de calculer $V_T^2, V_A^2, V_R^2$ et de conclure l'ANOVA au seuil $\alpha = 5\%$.

### 1. Interprétation de $\overline{X}_k$ et $\overline{X}$
$\overline{X}_k$ est le **nombre moyen de nouveaux clients par agent général dans la région $k$**.
$\overline{X}$ est la **moyenne globale** (tous agents confondus sur l'ensemble des $n = 48$ agents des $7$ zones).

### 2. Démonstration de l'équation d'analyse de variance ($V_T^2 = V_R^2 + V_A^2$)
Partons de $X_k^i - \overline{X} = (X_k^i - \overline{X}_k) + (\overline{X}_k - \overline{X})$. En élevant au carré et en sommant sur $k=1 \dots K$ et $i = 1 \dots n_k$ :
$$\sum_{k=1}^K \sum_{i=1}^{n_k} (X_k^i - \overline{X})^2 = \sum_{k=1}^K \sum_{i=1}^{n_k} (X_k^i - \overline{X}_k)^2 + \sum_{k=1}^K \sum_{i=1}^{n_k} (\overline{X}_k - \overline{X})^2 + 2\sum_{k=1}^K (\overline{X}_k - \overline{X})\underbrace{\sum_{i=1}^{n_k} (X_k^i - \overline{X}_k)}_{= 0}$$
Or, par définition de la moyenne $\overline{X}_k$, $\sum_{i=1}^{n_k} (X_k^i - \overline{X}_k) = n_k\overline{X}_k - n_k\overline{X}_k = 0$ pour tout $k$. Le terme rectangle s'annule donc identiquement. Comme $(\overline{X}_k - \overline{X})^2$ ne dépend pas de $i$, sa somme sur $i=1 \dots n_k$ vaut $n_k(\overline{X}_k - \overline{X})^2$. En divisant par $n$ :
$$\underbrace{\frac{1}{n}\sum_{k=1}^K \sum_{i=1}^{n_k} (X_k^i - \overline{X})^2}_{V_T^2} = \underbrace{\frac{1}{n}\sum_{k=1}^K \sum_{i=1}^{n_k} (X_k^i - \overline{X}_k)^2}_{V_R^2} + \underbrace{\frac{1}{n}\sum_{k=1}^K n_k (\overline{X}_k - \overline{X})^2}_{V_A^2} \quad \blacksquare$$

### 3. Calcul numérique de $V_T^2$, $V_A^2$ et $V_R^2$

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

$$\overline{X} = \frac{1\,148{,}51}{48} \approx \mathbf{23{,}9273}$$
$$V_A^2 = \frac{495{,}0154}{48} \approx \mathbf{10{,}3128}, \qquad V_R^2 = \frac{623{,}99}{48} \approx \mathbf{12{,}9998}, \qquad V_T^2 = 10{,}3128 + 12{,}9998 = \mathbf{23{,}3126}$$
*(Note : si les variances du tableau étaient déjà corrigées par $n_k - 1$, on aurait $V_R^2 = \frac{533{,}20}{48} = 11{,}1083$ et $V_T^2 = 21{,}4212$.)*

### 4. Finalisation de l'ANOVA ($\alpha = 5\%$)

| Source de variation | Somme des carrés (SC) | ddl | Carré moyen (MS) | Statistique $F_{\text{obs}}$ |
| :--- | :---: | :---: | :---: | :---: |
| **Inter-groupes (Région)** | $495{,}0154$ | $K - 1 = 6$ | $82{,}5026$ | **$\mathbf{5{,}4209}$** ($p = 0{,}00034$) |
| **Résiduelle (Intra)** | $623{,}9900$ | $n - K = 41$ | $15{,}2193$ | — |

*(Avec la variante $s_k^2$ corrigée : $F_{\text{obs}} = \mathbf{6{,}3440}$, $p = 8{,}8 \times 10^{-5}$.)*
En Annexe D.1 ($\nu_1 = 6, \nu_2 = 40$), $F_{0{,}05}(6, 40) = 2{,}34$ (soit $F_{0{,}05}(6, 41) \approx 2{,}33$).

> [!success] Conclusion
> Comme $F_{\text{obs}} = 5{,}42 > 2{,}33$, **on rejette $H_0$** : la campagne publicitaire n'a pas eu le même impact dans toutes les régions.

---

## 📌 Exercice 8 – Taille des garçons vs filles en CP

> [!question] Énoncé résumé & Données
> Dans une école primaire de Lomé, on mesure $n_1 = 41$ garçons ($\bar{x}_1 = 107\text{ cm}$, $v_1 = 8\text{ cm}$, Shapiro-Wilk $p_1 = 0{,}82$) et $n_2 = 61$ filles ($\bar{x}_2 = 104\text{ cm}$, $v_2 = 9\text{ cm}$, Shapiro-Wilk $p_2 = 0{,}21$). Peut-on affirmer que les garçons sont plus grands au risque $\alpha = 5\%$ ?

**Vérification des prérequis :**
Shapiro-Wilk donne $p_1 = 0{,}82 > 0{,}05$ et $p_2 = 0{,}21 > 0{,}05$ (normalité compatible). L'égalité des variances donne en Annexe D.2 :
$$F = \frac{9^2}{8^2} = 1{,}2656 < F_{0{,}025}(60, 40) \approx 1{,}84 \quad (\text{homoscédasticité acceptée})$$

**Hypothèses et statistique (unilatéral droit, grands échantillons) :**
$$H_0 : \mu_1 = \mu_2 \qquad \text{contre} \qquad H_1 : \mu_1 > \mu_2$$
$$N_{\text{obs}} = \frac{107 - 104}{\sqrt{\dfrac{8^2}{41} + \dfrac{9^2}{61}}} = \frac{3}{\sqrt{1{,}5610 + 1{,}3279}} = \frac{3}{1{,}6997} \approx \mathbf{1{,}7651}$$
*(Avec le test $t$ poolé à $n_1 + n_2 - 2 = 100$ ddl : $s_p = 8{,}613$, $t_{\text{obs}} = 1{,}7246$, $p_{\text{unilat}} = 0{,}0438$.)*

> [!success] Conclusion
> Comme $N_{\text{obs}} = 1{,}7651 > z_{0{,}95} = 1{,}6449$ ($p = 0{,}0388 < 0{,}05$), **on rejette $H_0$** : au seuil de $5\%$, les garçons de CP sont en moyenne plus grands que les filles.

---

## 📌 Exercice 9 – Sécurité routière : alcool et temps de réaction

> [!question] Énoncé résumé & Données
> On mesure en simulateur le temps de réaction (en s) de conducteurs sans alcool puis avec alcool sur $n = 15$ paires d'observations *(bien que l'énoncé introductif mentionne 30 chauffeurs)*. L'alcool a-t-il un effet au risque $\alpha = 5\%$ ?

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

$$\bar{d} = \frac{1{,}18}{15} \approx \mathbf{0{,}0787\text{ s}}, \qquad s_d^2 = \frac{0{,}053573}{14} = \frac{0{,}1464 - 15 \times (1{,}18/15)^2}{14} \approx 0{,}003827 \implies s_d \approx \mathbf{0{,}0619\text{ s}}$$
$$t_{\text{obs}} = \frac{0{,}07867}{0{,}06186 / \sqrt{15}} = \frac{0{,}07867}{0{,}01597} \approx \mathbf{4{,}9252} \sim t(14)$$

En Annexe C ($\nu = 14, \alpha = 0{,}05$), $t_{\text{crit}} = 2{,}1448$.

> [!success] Conclusion
> Comme $4{,}9252 > 2{,}1448$ ($p = 0{,}00022$), **on rejette $H_0$** : l'alcool augmente très significativement le temps de réaction au volant *(même si l'on traitait les deux lignes en groupes indépendants, $t = 2{,}6571 > 2{,}0484$ avec $\nu = 28$ donne le même rejet)*.

---

## 📌 Exercice 10 – Efficacité d'un programme nutritionnel

> [!question] Énoncé résumé & Données
> On pèse $N = 10$ participants (en kg) avant et après un programme nutritionnel et sportif. Le programme a-t-il un effet significatif sur la masse corporelle ?

**Constat préalable critique :**
L'individu n° 3 passe de $158$ à $121$ kg ($d_3 = -37$ kg), créant une **valeur aberrante massive** qui viole la normalité des différences. Un test $t$ de Student apparié donne $\bar{d} = -4{,}8$ kg et $s_d = 11{,}45$ kg, soit $t = -1{,}3259$ ($p = 0{,}2175$), non significatif car l'outlier gonfle artificiellement $s_d$.

**Choix méthodologique adapté :**
On applique le **test des rangs signés de Wilcoxon** (non paramétrique, robuste aux outliers). On retire d'abord la différence nulle (individu 6 : $58 \to 58$), ce qui laisse $n = 9$ paires non nulles :

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

Les ex-æquo $\lvert d \rvert = 1$ (rangs $1,2,3,4$) reçoivent le rang moyen $2{,}5$, et $\lvert d \rvert = 2$ (rangs $5,6,7$) reçoivent le rang moyen $6{,}0$. On vérifie $W^+ + W^- = 5{,}0 + 40{,}0 = 45{,}0 = \frac{9 \times 10}{2}$ et on retient :
$$W = \min(W^+, W^-) = \min(5, 40) = \mathbf{5{,}0}$$

> [!success] Conclusion
> Pour $n = 9$ à $\alpha = 5\%$ (bilatéral), $W_{\text{crit}} = 5$ et la $p$-value exacte vaut $\frac{22}{512} = \mathbf{0{,}0430} < 0{,}05$. Comme $W \le W_{\text{crit}}$, **on rejette $H_0$** : le programme a un effet significatif à la baisse ($7$ participants sur $10$ ont perdu du poids).

---

## 📌 Exercice 11 – ANOVA : Temps de traitement selon le SGBD

> [!question] Énoncé résumé & Données
> On compare les temps de traitement de $k = 3$ SGBD (PostgreSQL, MongoDB, MySQL) avec $n_j = 5$ exécutions par groupe ($\text{SC}_{\text{Facteur}} = 320$, $\text{SC}_{\text{Résiduelle}} = 240$, $F_{0{,}05}(2, 12) = 3{,}89$).

Nombre total d'observations : $N = 3 \times 5 = \mathbf{15}$.

| Source de variation | SC | ddl | Carré moyen (MS) | Statistique $F$ |
| :--- | :---: | :---: | :---: | :---: |
| **Facteur (SGBD)** | $320$ | $k - 1 = \mathbf{2}$ | $\dfrac{320}{2} = \mathbf{160}$ | $\dfrac{160}{20} = \mathbf{8{,}00}$ ($p = 0{,}0062$) |
| **Résiduelle (Intra)** | $240$ | $N - k = \mathbf{12}$ | $\dfrac{240}{12} = \mathbf{20}$ | — |

> [!success] Conclusion
> Comme $F = 8{,}00 > F_{0{,}05}(2, 12) = 3{,}89$, **on rejette $H_0$** : le choix du SGBD a un impact statistiquement significatif sur le temps de traitement au seuil de $5\%$.

---

## 📌 Exercice 12 – ANOVA : Consommation RAM selon le langage

> [!question] Énoncé résumé & Données
> Un audit Green IT mesure la RAM d'un microservice en $k = 4$ langages ($6$ mesures par langage, $N = 24$), donnant $\text{SCT} = 1\,200$ et $\text{SCR} = 300$. On teste l'influence du langage à $\alpha = 1\%$ ($F_{0{,}01}(3, 20) = 4{,}94$).

On déduit d'abord $\text{SCE} = \text{SCT} - \text{SCR} = 1\,200 - 300 = \mathbf{900}$.

| Source de variation | SC | ddl | Carré moyen (MS) | Statistique $F$ |
| :--- | :---: | :---: | :---: | :---: |
| **Facteur (Langage)** | $900$ | $4 - 1 = \mathbf{3}$ | $\dfrac{900}{3} = \mathbf{300}$ | $\dfrac{300}{15} = \mathbf{20{,}00}$ ($p = 3{,}1 \times 10^{-6}$) |
| **Résiduelle (Intra)** | $300$ | $24 - 4 = \mathbf{20}$ | $\dfrac{300}{20} = \mathbf{15}$ | — |
| **Total** | $1\,200$ | $23$ | — | — |

> [!success] Conclusion
> Comme $F = 20{,}00 > F_{0{,}01}(3, 20) = 4{,}94$, **on rejette $H_0$ au seuil de $1\%$** : le langage de programmation influence très significativement la consommation mémoire.

---

## 📌 Exercice 13 – Mann-Whitney : Formation Agile (Présentiel vs E-learning)

> [!question] Énoncé résumé & Données
> Deux groupes de $n_1 = n_2 = 5$ développeurs passent un test Agile : Méthode A Présentiel (`78, 85, 90, 92, 96`) et Méthode B E-learning (`60, 70, 75, 80, 88`). On réalise le test de Mann-Whitney à $\alpha = 5\%$ ($U_{\text{critique}} = 2$).

1. **Classement conjoint croissant (aucun ex-æquo) :**

| Rang | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Note** | $60$ | $70$ | $75$ | $78$ | $80$ | $85$ | $88$ | $90$ | $92$ | $96$ |
| **Groupe** | **B** | **B** | **B** | **A** | **B** | **A** | **B** | **A** | **A** | **A** |

$$R_1 = 4 + 6 + 8 + 9 + 10 = \mathbf{37} \quad (R_2 = 18, \text{ vérif. } 37 + 18 = 55)$$

2. **Calcul de $U_1$ :**
$$U_1 = R_1 - \frac{n_1(n_1 + 1)}{2} = 37 - \frac{5 \times 6}{2} = 37 - 15 = \mathbf{22}$$

3. **Calcul de $U_2$ et $U$ :**
$$U_2 = n_1 n_2 - U_1 = 25 - 22 = \mathbf{3}, \qquad U = \min(22, 3) = \mathbf{3}$$

4. **Décision ($\alpha = 5\%$ bilatéral) :**

> [!success] Conclusion
> Comme $U = 3 > U_{\text{critique}} = 2$, **on ne rejette pas $H_0$** au seuil de $5\%$ : l'écart de notes en faveur du présentiel n'est pas statistiquement suffisant avec seulement $5$ développeurs par groupe.

---

## 📌 Exercice 14 – Mann-Whitney : Temps de résolution d'incidents

> [!question] Énoncé résumé & Données
> On compare les temps de résolution d'incidents ITIL entre $n_1 = 6$ Juniors ($R_1 = 51$) et $n_2 = 6$ Seniors ($R_2 = 27$), soit $N = 12$ observations ($U_{\text{critique}} = 5$ à $\alpha = 5\%$).

1. **Vérification de la somme des rangs :**
$$\sum \text{Rangs} = R_1 + R_2 = 51 + 27 = 78, \qquad \frac{N(N+1)}{2} = \frac{12 \times 13}{2} = \mathbf{78} \quad (\text{vérifié})$$

2. **Calcul des statistiques :**
$$U_1 = 51 - \frac{6 \times 7}{2} = 51 - 21 = \mathbf{30}, \qquad U_2 = 27 - 21 = \mathbf{6} \quad (\text{vérif. } 30 + 6 = 36 = 6 \times 6)$$

3. **Statistique du test :**
$$U = \min(30, 6) = \mathbf{6}$$

> [!success] Conclusion
> Comme $U = 6 > U_{\text{critique}} = 5$, **on ne rejette pas $H_0$** au seuil bilatéral de $5\%$ *(résultat très proche de la limite critique, où un test unilatéral à $5\%$ aurait rejeté ; les effectifs sont trop faibles pour conclure formellement en bilatéral)*.

---

## 📌 Exercice 15 – Chi-Deux : OS mobile et validation 2FA ($n = 100$)

> [!question] Énoncé résumé & Données
> Un RSSI croise l'OS mobile (iOS $50$, Android $50$) et le mode de validation 2FA choisi (App Mobile $60$, SMS $40$) sur $n = 100$ salariés ($\chi^2_{\text{critique}} = 3{,}841$ à $\alpha = 5\%$).

### 1 & 2. Effectifs théoriques $E_i$ et contributions $\frac{(O_i - E_i)^2}{E_i}$

| OS \ 2FA | App Mobile ($T_1 = 60$) | SMS ($T_2 = 40$) | Total |
| :--- | :---: | :---: | :---: |
| **iOS** ($S_1 = 50$) | $O=35$, $E=\frac{50\times 60}{100}=\mathbf{30}$ <br> Contrib $= \frac{(35-30)^2}{30} = \mathbf{0{,}8333}$ | $O=15$, $E=\frac{50\times 40}{100}=\mathbf{20}$ <br> Contrib $= \frac{(15-20)^2}{20} = \mathbf{1{,}2500}$ | 50 |
| **Android** ($S_2 = 50$) | $O=25$, $E=\mathbf{30}$ <br> Contrib $= \frac{(25-30)^2}{30} = \mathbf{0{,}8333}$ | $O=25$, $E=\mathbf{20}$ <br> Contrib $= \frac{(25-20)^2}{20} = \mathbf{1{,}2500}$ | 50 |
| **Total** | **60** | **40** | **100** |

*(Condition vérifiée : tous les $E_i \ge 5$.)*

### 3 & 4. Statistique $\chi^2$, ddl et décision ($\alpha = 5\%$)
$$\chi^2_{\text{obs}} = 0{,}8333 + 1{,}2500 + 0{,}8333 + 1{,}2500 = \mathbf{4{,}1667} \quad (p = 0{,}0412)$$
$$\text{ddl} = (2 - 1)(2 - 1) = \mathbf{1}$$

> [!success] Conclusion
> Comme $\chi^2_{\text{obs}} = 4{,}1667 > \chi^2_{\text{critique}} = 3{,}841$, **on rejette l'hypothèse d'indépendance $H_0$** : le choix du mode 2FA dépend significativement de l'OS (les utilisateurs iOS privilégient davantage l'app d'authentification que ceux d'Android).

---

## 📌 Exercice 16 – Chi-Deux : Architecture SI et satisfaction du DSI ($n = 200$)

> [!question] Énoncé résumé & Données
> Une étude auprès de $200$ entreprises croise le type d'architecture SI (Monolithe, Microservices, Serverless) et la satisfaction du DSI (Satisfait / Non satisfait), avec les effectifs observés et attendus fournis ($\chi^2_{0{,}05}(2) = 5{,}991$).

### 1. Calcul de la statistique globale du $\chi^2$

| Architecture / Satisfaction | $O_i$ | $E_i$ | $(O_i - E_i)^2$ | $\dfrac{(O_i - E_i)^2}{E_i}$ |
| :--- | :---: | :---: | :---: | :---: |
| **Monolithe / Satisfait** | $30$ | $45$ | $225$ | $5{,}0000$ |
| **Monolithe / Non satisfait** | $30$ | $15$ | $225$ | $15{,}0000$ |
| **Microservices / Satisfait** | $70$ | $60$ | $100$ | $1{,}6667$ |
| **Microservices / Non satisfait** | $10$ | $20$ | $100$ | $5{,}0000$ |
| **Serverless / Satisfait** | $50$ | $45$ | $25$ | $0{,}5556$ |
| **Serverless / Non satisfait** | $10$ | $15$ | $25$ | $1{,}6667$ |
| **Total ($\sum$)** | **$200$** | **$200$** | — | **$\mathbf{28{,}8889}$** |

$$\chi^2_{\text{obs}} = \frac{260}{9} \approx \mathbf{28{,}8889} \quad (p = 5{,}3 \times 10^{-7})$$

### 2. Degrés de liberté
Pour un tableau $3 \times 2$ (avec tous les $E_i \ge 15 \ge 5$) :
$$\text{ddl} = (3 - 1)(2 - 1) = \mathbf{2}$$

### 3. Conclusion au seuil $\alpha = 5\%$
> [!success] Conclusion
> Comme $\chi^2_{\text{obs}} = 28{,}89 \gg \chi^2_{0{,}05}(2) = 5{,}991$, **on rejette très nettement $H_0$** : il existe une association forte entre l'architecture SI et la satisfaction du DSI (Microservices à $87{,}5\%$ de satisfaits et Serverless à $83{,}3\%$, contre seulement $50\%$ pour le Monolithe).
