---
type: note-cours
created: 2026-11-23
matiere: "Statistiques Inférentielles"
chapitre: "TD 1 - Échantillonnage et Estimations"
enseignant: "K. E. HOVI"
tags:
  - etudes
  - td
  - statistiques-inferentielles
  - echantillonnage
  - estimation-ponctuelle
  - intervalles-de-confiance
  - maximum-de-vraisemblance
parent: "[[MOC_Statistiques_Inferentielles]]"
---

# 📝 TD 1. Échantillonnage et Estimations

> **Matière :** [[MOC_Statistiques_Inferentielles|Statistiques Inférentielles (M1 IT)]] • **Support :** Feuille d'exercices n° 1 (p. 44–47) • **Statut :** Entièrement Résolu & Démontré • 🧰 [[TD1_Formules_et_Explications_Terre_a_Terre|Guide Formules & Explications Terre à Terre]]

---

## 📌 Exercice 1 – Insertion professionnelle des diplômés

> [!question] Énoncé résumé & Données
> L'ANPE étudie la durée $X$ de recherche d'un premier emploi (en mois) dans la région Maritime. On modélise cette durée par une loi normale de moyenne $\mu = 14$ mois et de variance $\sigma^2 = 36$ (soit un écart-type $\sigma = 6$ mois).
>
> On pose :
> $$Z = \frac{X - 14}{6} \sim \mathcal{N}(0, 1)$$

### 1. Limites de cette modélisation
Une variable normale prend ses valeurs sur $\mathbb{R} = ]-\infty; +\infty[$ et reste parfaitement symétrique autour de $\mu = 14$.

**Support négatif impossible :**
Le modèle attribue une probabilité non nulle à des durées négatives, ce qui n'a aucun sens physique :
$$P(X < 0) = \Phi\!\left(-\frac{14}{6}\right) = \Phi(-2{,}33) = 1 - \Phi(2{,}33) \approx \mathbf{0{,}0098}$$

**Asymétrie réelle :**
En pratique, les durées de chômage présentent une forte asymétrie à droite (queue longue vers les grandes durées), que la symétrie gaussienne ne capture pas.

### 2. Probabilité de chercher plus de 2 ans ($X > 24$ mois)
On centre et réduit la borne $24$ mois :
$$P(X > 24) = P\!\left(Z > \frac{24 - 14}{6}\right) = P(Z > 1{,}67) = 1 - \Phi(1{,}67)$$

Par lecture de l'Annexe A.1 ($\Phi(1{,}67) = 0{,}9525$) :
$$P(X > 24) \approx 1 - 0{,}9525 = \mathbf{0{,}0475} \quad (\text{valeur exacte } z = 5/3 : 0{,}0478, \text{ soit } \mathbf{4{,}78\%})$$

### 3. Probabilité de trouver un emploi en moins de 6 mois ($X < 6$ mois)
On centre et réduit la borne $6$ mois, puis on exploite la symétrie :
$$P(X < 6) = P\!\left(Z < \frac{6 - 14}{6}\right) = P(Z < -1{,}33) = 1 - \Phi(1{,}33)$$

Par lecture de l'Annexe A.1 ($\Phi(1{,}33) = 0{,}9082$) :
$$P(X < 6) \approx 1 - 0{,}9082 = \mathbf{0{,}0918} \quad (\text{valeur exacte } z = -4/3 : 0{,}0912, \text{ soit } \mathbf{9{,}12\%})$$

### 4. Probabilité d'une recherche entre 6 mois et 1 an ($6 \le X \le 12$)
On exprime l'intervalle avec la fonction de répartition $\Phi$ :
$$P(6 \le X \le 12) = P\!\left(-1{,}33 \le Z \le \frac{12 - 14}{6}\right) = \Phi(-0{,}33) - \Phi(-1{,}33) = \Phi(1{,}33) - \Phi(0{,}33)$$

Par lecture de l'Annexe A.1 ($\Phi(1{,}33) = 0{,}9082$ et $\Phi(0{,}33) = 0{,}6293$) :
$$P(6 \le X \le 12) \approx 0{,}9082 - 0{,}6293 = \mathbf{0{,}2789} \quad (\text{valeur exacte : } 0{,}2782, \text{ soit } \mathbf{27{,}82\%})$$

> [!success] Conclusion
> Le modèle prédit environ $4{,}78\%$ de recherches dépassant 2 ans, $9{,}12\%$ d'embauches en moins de 6 mois et $27{,}82\%$ entre 6 mois et 1 an, tout en restant approximatif sur les queues de distribution à cause des valeurs négatives théoriques ($0{,}98\%$).

---

## 📌 Exercice 2 – Qualité de service d'un réseau télécom

> [!question] Énoncé résumé & Données
> Un opérateur mobile au Togo s'engage à ce que $95\%$ des SMS de confirmation API arrivent en moins d'une minute ($p = 0{,}95$, échec $1 - p = 0{,}05$). On teste d'abord $n = 2$ SMS par jour, puis $n = 20$ SMS le dimanche.

### 1. Probabilité qu'un SMS arrive en moins d'une minute
D'après l'engagement de l'opérateur :
$$p = \mathbf{0{,}95}$$

### 2. Envoi de 2 SMS de test ($X \sim \mathcal{B}(2;\, 0{,}95)$ sous indépendance)
La loi binomiale donne pour $k \in \{0, 1, 2\}$ :
$$P(X = k) = \binom{2}{k}(0{,}95)^k (0{,}05)^{2-k}$$

| $k$ (SMS transmis $< 1$ min) | Calcul | Probabilité | Pourcentage |
| :---: | :--- | :---: | :---: |
| $0$ | $1 \times 0{,}05^2$ | $\mathbf{0{,}0025}$ | $0{,}25\%$ |
| $1$ | $2 \times 0{,}95 \times 0{,}05$ | $\mathbf{0{,}0950}$ | $9{,}50\%$ |
| $2$ | $1 \times 0{,}95^2$ | $\mathbf{0{,}9025}$ | $90{,}25\%$ |

### 3. Modélisation pour 20 SMS par jour
Chaque envoi étant modélisé comme une épreuve de Bernoulli de paramètre $p = 0{,}95$ indépendante d'un SMS à l'autre, le nombre $Y$ de SMS arrivés en moins d'une minute suit une **loi binomiale** :
$$Y \sim \mathcal{B}(n = 20,\; p = 0{,}95)$$

Son espérance et sa variance valent :
$$E(Y) = np = 20 \times 0{,}95 = \mathbf{19\text{ SMS}}$$
$$\text{Var}(Y) = np(1 - p) = 20 \times 0{,}95 \times 0{,}05 = \mathbf{0{,}95}$$

### 4. Probabilité qu'au moins la moitié arrive en moins d'une minute ($Y \ge 10$)
On passe par l'événement complémentaire :
$$P(Y \ge 10) = 1 - \sum_{k=0}^{9} \binom{20}{k}(0{,}95)^k (0{,}05)^{20-k} \approx 1 - 5{,}38 \times 10^{-10} \approx \mathbf{0{,}9999999995}$$

> [!success] Conclusion
> Il est **quasi certain** (probabilité supérieure à $99{,}9999999\%$) qu'au moins $10$ SMS sur $20$ soient transmis en moins d'une minute.

---

## 📌 Exercice 3 – Analyse de données de simulation sous R

> [!question] Énoncé résumé & Données
> Un administrateur système simule sous R les temps de réponse (en ms) d'une API via la commande `round(rnorm(12, 10, 1), 1)` et obtient $n = 12$ valeurs :
> `10.7, 11.7, 11.6, 9.1, 11.1, 10.7, 10.7, 11.1, 9.5, 10.6, 12.0, 11.1`

### 1. Estimation ponctuelle de la moyenne et de la variance

| Mesure $i$ | $x_i$ | $x_i - \bar{x}$ | $(x_i - \bar{x})^2$ | $x_i^2$ *(Koenig-Huygens)* |
| :---: | :---: | :---: | :---: | :---: |
| 1 | $10{,}7$ | $-0{,}125$ | $0{,}015625$ | $114{,}49$ |
| 2 | $11{,}7$ | $+0{,}875$ | $0{,}765625$ | $136{,}89$ |
| 3 | $11{,}6$ | $+0{,}775$ | $0{,}600625$ | $134{,}56$ |
| 4 | $9{,}1$ | $-1{,}725$ | $2{,}975625$ | $82{,}81$ |
| 5 | $11{,}1$ | $+0{,}275$ | $0{,}075625$ | $123{,}21$ |
| 6 | $10{,}7$ | $-0{,}125$ | $0{,}015625$ | $114{,}49$ |
| 7 | $10{,}7$ | $-0{,}125$ | $0{,}015625$ | $114{,}49$ |
| 8 | $11{,}1$ | $+0{,}275$ | $0{,}075625$ | $123{,}21$ |
| 9 | $9{,}5$ | $-1{,}325$ | $1{,}755625$ | $90{,}25$ |
| 10 | $10{,}6$ | $-0{,}225$ | $0{,}050625$ | $112{,}36$ |
| 11 | $12{,}0$ | $+1{,}175$ | $1{,}380625$ | $144{,}00$ |
| 12 | $11{,}1$ | $+0{,}275$ | $0{,}075625$ | $123{,}21$ |
| **Total ($\sum$)** | **$129{,}9$** | **$0$** | **$7{,}802500$** | **$1\,413{,}97$** |

**Moyenne empirique (sans biais) :**
$$\bar{x} = \frac{129{,}9}{12} = \mathbf{10{,}825\text{ ms}}$$

**Variance empirique (biaisée) :**
$$\bar{s}^2 = \frac{7{,}8025}{12} = \frac{1\,413{,}97}{12} - 10{,}825^2 \approx \mathbf{0{,}6502\text{ ms}^2}$$

**Variance corrigée (sans biais) et écart-type :**
$$s^2 = \frac{7{,}8025}{11} = \frac{1\,413{,}97 - 12 \times 10{,}825^2}{11} \approx \mathbf{0{,}7093\text{ ms}^2}$$
$$s = \sqrt{0{,}7093} \approx \mathbf{0{,}8422\text{ ms}}$$

### 2. Interprétation exacte de `round(rnorm(12, 10, 1), 1)`
1. `rnorm(12, 10, 1)` simule un échantillon de **12 réalisations indépendantes** d'une loi normale de moyenne $\mu = 10$ et d'**écart-type** $\sigma = 1$ *(en R, le 3e paramètre de `rnorm` est `sd`, l'écart-type, qui vaut ici $\sqrt{1}=1$)*.
2. `round(..., 1)` arrondit chacune de ces 12 valeurs à **1 chiffre après la virgule**.

> [!success] Conclusion
> Les estimations sans biais de la population simulée sont $\hat{\mu} = \mathbf{10{,}825\text{ ms}}$ et $\hat{\sigma}^2 = \mathbf{0{,}7093\text{ ms}^2}$ ($s \approx 0{,}8422\text{ ms}$), valeurs cohérentes avec les paramètres théoriques $\mu = 10$ et $\sigma^2 = 1$.

---

## 📌 Exercice 4 – Modélisation du trafic de requêtes réseau

> [!question] Énoncé résumé & Données
> Une entreprise e-commerce à Lomé relève pendant $n = 53$ heures le nombre de requêtes de service reçues par heure ($x_i \in \{0, \dots, 9\}$) ainsi que leurs occurrences $N_i$.

### 1. Estimation du mode, de la moyenne et de la variance

| $x_i$ (appels/h) | $N_i$ (heures) | $N_i x_i$ | $x_i - \bar{x}$ | $N_i(x_i - \bar{x})^2$ | $N_i x_i^2$ *(Koenig-Huygens)* |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 0 | 1 | 0 | $-4$ | 16 | 0 |
| 1 | 4 | 4 | $-3$ | 36 | 4 |
| 2 | 7 | 14 | $-2$ | 28 | 28 |
| 3 | 11 | 33 | $-1$ | 11 | 99 |
| 4 | 10 | 40 | $0$ | 0 | 160 |
| 5 | 9 | 45 | $+1$ | 9 | 225 |
| 6 | 5 | 30 | $+2$ | 20 | 180 |
| 7 | 3 | 21 | $+3$ | 27 | 147 |
| 8 | 2 | 16 | $+4$ | 32 | 128 |
| 9 | 1 | 9 | $+5$ | 25 | 81 |
| **Total ($\sum$)** | **$53$** | **$212$** | — | **$204$** | **$1\,052$** |

**Mode :**
$$\text{Mo} = \mathbf{3\text{ appels/h}} \quad (\text{effectif maximal } N_3 = 11)$$

**Moyenne empirique :**
$$\bar{x} = \frac{212}{53} = \mathbf{4{,}00\text{ appels/h}}$$

**Variances empirique et corrigée :**
$$\bar{s}^2 = \frac{204}{53} = \frac{1\,052}{53} - 4^2 \approx \mathbf{3{,}8491}$$
$$s^2 = \frac{204}{52} = \frac{1\,052 - 53 \times 4^2}{52} \approx \mathbf{3{,}9231} \quad (s \approx \mathbf{1{,}9807})$$

### 2. Loi de probabilité proposée
Le nombre d'appels par heure est une variable **discrète de comptage** sur un intervalle fixe, dont la moyenne et la variance empiriques sont quasi égales ($\bar{x} = 4{,}00 \approx s^2 = 3{,}92$).

> [!success] Conclusion
> Le trafic horaire de requêtes suit une **loi de Poisson de paramètre $\lambda = 4$**, notée $\mathcal{P}(4)$.

---

## 📌 Exercice 5 – Estimation et intervalles de confiance du trafic Web

> [!question] Énoncé résumé & Données
> Une boutique informatique en ligne relève son nombre journalier de connexions uniques sur $n = 10$ jours, supposé iid selon $\mathcal{N}(\mu, \sigma^2)$ :
> `759, 750, 755, 756, 761, 765, 770, 752, 760, 767`

### 1. Estimations ponctuelles de $\mu$ et $\sigma^2$

| Jour $i$ | $x_i$ | $x_i - \bar{x}$ | $(x_i - \bar{x})^2$ | $x_i^2$ *(Koenig-Huygens)* |
| :---: | :---: | :---: | :---: | :---: |
| 1 | $759$ | $-0{,}5$ | $0{,}25$ | $576\,081$ |
| 2 | $750$ | $-9{,}5$ | $90{,}25$ | $562\,500$ |
| 3 | $755$ | $-4{,}5$ | $20{,}25$ | $570\,025$ |
| 4 | $756$ | $-3{,}5$ | $12{,}25$ | $571\,536$ |
| 5 | $761$ | $+1{,}5$ | $2{,}25$ | $579\,121$ |
| 6 | $765$ | $+5{,}5$ | $30{,}25$ | $585\,225$ |
| 7 | $770$ | $+10{,}5$ | $110{,}25$ | $592\,900$ |
| 8 | $752$ | $-7{,}5$ | $56{,}25$ | $565\,504$ |
| 9 | $760$ | $+0{,}5$ | $0{,}25$ | $577\,600$ |
| 10 | $767$ | $+7{,}5$ | $56{,}25$ | $588\,289$ |
| **Total ($\sum$)** | **$7\,595$** | **$0$** | **$378{,}5$** | **$5\,768\,781$** |

**Espérance estimée :**
$$\hat{\mu} = \bar{x} = \frac{7\,595}{10} = \mathbf{759{,}5\text{ connexions/jour}}$$

**Variance sans biais et écart-type :**
$$s^2 = \frac{378{,}5}{9} = \frac{5\,768\,781 - 10 \times 759{,}5^2}{9} \approx \mathbf{42{,}0556}$$
$$s = \sqrt{42{,}0556} \approx \mathbf{6{,}4850} \quad (\text{variance biaisée : } \bar{s}^2 = 37{,}85)$$

### 2. Intervalles de confiance pour $\mu$ ($\sigma$ inconnu $\implies$ Student à $\nu = 9$ ddl)
On applique la loi de Student à $\nu = n - 1 = 9$ degrés de liberté :
$$IC_{1-\alpha}(\mu) = \left[\bar{x} \pm t_{9,\, 1-\alpha/2}\frac{s}{\sqrt{10}}\right]$$
$$\text{Erreur standard} = \frac{s}{\sqrt{10}} = \frac{6{,}4850}{3{,}1623} \approx 2{,}0507$$

| Niveau de confiance | $\alpha$ | Quantile $t_{9,\, 1-\alpha/2}$ (Annexe C) | Marge d'erreur | $IC_{1-\alpha}(\mu)$ |
| :---: | :---: | :---: | :---: | :---: |
| **90%** | $0{,}10$ | $1{,}8331$ | $3{,}7592$ | **$\mathbf{[755{,}74 \,;\, 763{,}26]}$** |
| **99%** | $0{,}01$ | $3{,}2498$ | $6{,}6645$ | **$\mathbf{[752{,}84 \,;\, 766{,}16]}$** |

### 3. Niveau de confiance pour un intervalle deux fois plus étroit qu'à 90%
Diviser la demi-largeur par $2$ revient à diviser le quantile de Student par $2$ :
$$t_{9,\, 1-\alpha/2} = \frac{1{,}8331}{2} \approx \mathbf{0{,}9166}$$

En Annexe C ($\nu = 9$), pour $\alpha = 0{,}500$ (confiance $50\%$) on lit $t = 0{,}7027$, et pour $\alpha = 0{,}300$ (confiance $70\%$) on lit $t = 1{,}0997$. Le niveau de confiance est donc **compris entre 50% et 70%** *(valeur exacte : $P(|T_9| \le 0{,}91655) \approx \mathbf{61{,}67\%}$)*.

### 4. Taille d'échantillon $n$ pour une longueur $\le 1$ à 95%
On impose une longueur totale $L = 2\, t_{n-1,\, 0{,}975} \frac{s}{\sqrt{n}} \le 1$. Comme $n$ sera grand, on approxime $t_{n-1,\, 0{,}975} \approx z_{0{,}975} = 1{,}96$ :
$$n \ge (2 \times 1{,}96 \times 6{,}4850)^2 = 646{,}24 \implies \mathbf{n \ge 647\text{ jours}}$$
*(En affinant avec $t_{648, 0{,}975} \approx 1{,}9636$, on obtient $648{,}64 \implies \mathbf{649\text{ jours}}$. Avec $\bar{s}^2 = 37{,}85$, le calcul donnerait $582$ jours.)*

### 5. Impact si $\sigma^2 = 42$ est connue ($\sigma = \sqrt{42} \approx 6{,}4807$)
On n'estime plus $\sigma$ : la loi pivotale passe de Student $t(9)$ à la loi normale $\mathcal{N}(0, 1)$, ce qui **rétrécit les intervalles** (quantiles plus faibles pour quasi la même dispersion).

| Niveau | Quantile $z$ | $IC(\mu)$ avec $\sigma$ connu | Largeur (vs Student) |
| :---: | :---: | :---: | :---: |
| **90%** | $1{,}6449$ | **$[756{,}13 \,;\, 762{,}87]$** | $6{,}74$ (contre $7{,}52$) |
| **99%** | $2{,}5758$ | **$[754{,}22 \,;\, 764{,}78]$** | $10{,}56$ (contre $13{,}33$) |

> [!success] Conclusion
> Avec $\sigma$ inconnu, $\mu \in [755{,}74 \,;\, 763{,}26]$ à $90\%$ et $[752{,}84 \,;\, 766{,}16]$ à $99\%$. Obtenir une largeur $\le 1$ à $95\%$ exige au moins **$647$ jours** (ou $649$ en Student exact). Connaître $\sigma$ réduit mécaniquement la largeur des intervalles.

---

## 📌 Exercice 6 – Comparaison de la qualité des matériaux de construction

> [!question] Énoncé résumé & Données
> On évalue la résistance d'un béton bitumineux issu de deux centrales (prélèvements par tranche de $115\text{ m}^3$) :
> Centrale 1 : $n_1 = 25$, $\bar{x}_1 = 90{,}6$, $v_1^2 = 65{,}42$
> Centrale 2 : $n_2 = 23$, $\bar{x}_2 = 94{,}4$, $v_2^2 = 58{,}24$
> *(Convention du cours p. 4 & 14 : $v^2$ désigne la variance empirique divisée par $n$, d'où $(n-1)s^2 = n v^2$. Les résultats entre parenthèses correspondent au cas alternatif où $v^2$ serait déjà corrigée.)*

### 1. IC à 95% pour la variabilité ($\sigma^2$ et $\sigma$) de chaque centrale
La loi pivotale suit un $\chi^2(n-1)$ :
$$IC_{95\%}(\sigma^2) = \left[\frac{n v^2}{\chi^2_{n-1,\, 0{,}975}} \;;\; \frac{n v^2}{\chi^2_{n-1,\, 0{,}025}}\right]$$

| Centrale | $\nu = n - 1$ | $n v^2$ | $\chi^2_{\text{inf}}$ ($\alpha=0{,}975$) | $\chi^2_{\text{sup}}$ ($\alpha=0{,}025$) | $IC_{95\%}(\sigma^2)$ | $IC_{95\%}(\sigma)$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Centrale 1** | 24 | $1\,635{,}50$ | $12{,}4012$ | $39{,}3641$ | **$\mathbf{[41{,}55 \,;\, 131{,}88]}$** | **$\mathbf{[6{,}45 \,;\, 11{,}48]}$** |
| **Centrale 2** | 22 | $1\,339{,}52$ | $10{,}9823$ | $36{,}7807$ | **$\mathbf{[36{,}42 \,;\, 121{,}97]}$** | **$\mathbf{[6{,}03 \,;\, 11{,}04]}$** |

*(Si $v^2$ déjà corrigée : Centrale 1 donne $24 \times 65{,}42 = 1\,570{,}08 \implies [39{,}89 \,;\, 126{,}61]$ ; Centrale 2 donne $22 \times 58{,}24 = 1\,281{,}28 \implies [34{,}84 \,;\, 116{,}67]$.)*

### 2. Peut-on conclure à une différence de variabilité ?
Les deux intervalles $[41{,}55 \,;\, 131{,}88]$ et $[36{,}42 \,;\, 121{,}97]$ **se recouvrent très largement**. On ne peut donc pas en déduire que les variances diffèrent ; le test rigoureux passe par le rapport de variances ci-dessous.

### 3. Intervalle de confiance à 95% pour le rapport $\sigma_1^2 / \sigma_2^2$
On passe d'abord aux variances corrigées :
$$s_1^2 = \frac{25}{24}(65{,}42) = 68{,}1458, \qquad s_2^2 = \frac{23}{22}(58{,}24) = 60{,}8873, \qquad \frac{s_1^2}{s_2^2} = 1{,}1192$$

Par interpolation linéaire dans l'Annexe D.2 ($\alpha = 0{,}025$) :
$$F_{0{,}025}(24, 22) \approx 2{,}39 - 0{,}4(2{,}39 - 2{,}27) = 2{,}342$$
$$F_{0{,}025}(22, 24) \approx 2{,}33 - 0{,}2(2{,}33 - 2{,}21) = 2{,}306$$

On construit l'intervalle de confiance de Fisher :
$$IC_{95\%}\!\left(\frac{\sigma_1^2}{\sigma_2^2}\right) = \left[\frac{1{,}1192}{2{,}342} \,;\, 1{,}1192 \times 2{,}306\right] = \mathbf{[0{,}478 \,;\, 2{,}581]}$$
*(Avec $v_1^2 / v_2^2 = 1{,}1233$ : $[0{,}480 \,;\, 2{,}590]$.)*

> [!success] Conclusion
> Comme **$1 \in [0{,}478 \,;\, 2{,}581]$**, on ne rejette pas l'égalité des variances : les deux centrales présentent une variabilité homogène au seuil de $5\%$.

---

## 📌 Exercice 7 – Sondage d'opinion et prédiction électorale

> [!question] Énoncé résumé & Données
> Lors d'un sondage pré-électoral sur $n = 500$ électeurs, $150$ déclarent voter pour le candidat $C_1$ et $140$ pour le candidat $C_2$.

### 1 & 2. Estimation ponctuelle et intervalles de confiance à 95% ($z = 1{,}96$)
La fréquence empirique est $f = \frac{k}{n}$ et l'intervalle à $95\%$ vaut :
$$IC_{95\%}(p) = \left[f - 1{,}96\sqrt{\frac{f(1-f)}{n}} \;;\; f + 1{,}96\sqrt{\frac{f(1-f)}{n}}\right]$$

| Candidat | Voix $k$ | Proportion $f$ | Marge d'erreur ($95\%$) | $IC_{95\%}(p)$ |
| :---: | :---: | :---: | :---: | :---: |
| **$C_1$** | $150$ | $0{,}30$ ($\mathbf{30\%}$) | $\pm 0{,}0402$ | **$\mathbf{[25{,}98\% \,;\, 34{,}02\%]}$** |
| **$C_2$** | $140$ | $0{,}28$ ($\mathbf{28\%}$) | $\pm 0{,}0394$ | **$\mathbf{[24{,}06\% \,;\, 31{,}94\%]}$** |

### 3. Prédiction électorale
> [!success] Conclusion
> **Non**, on ne peut pas prédire le vainqueur : les deux intervalles se chevauchent largement sur $[25{,}98\% \,;\, 31{,}94\%]$ et la marge d'erreur ($\approx \pm 4\%$) dépasse l'écart observé ($2\%$).

---

## 📌 Exercice 8 – Estimation par maximum de vraisemblance du flux de notifications

> [!question] Énoncé résumé & Données
> Le nombre $X$ de notifications reçues par un étudiant pendant une séance suit une loi de Poisson $\mathcal{P}(\lambda)$ :
> $$P(X = k) = e^{-\lambda}\frac{\lambda^k}{k!}, \qquad k \in \mathbb{N}, \; \lambda > 0$$
> Échantillon relevé sur $n = 10$ étudiants : `1, 4, 1, 3, 1, 6, 3, 0, 0, 0`.

### 1. Signification de $\lambda$
$\lambda$ représente le **nombre moyen (espérance) de notifications reçues par un étudiant pendant une séance de cours** (ainsi que sa variance, car pour une loi de Poisson $E(X) = \text{Var}(X) = \lambda$).

### 2. Fonction de vraisemblance d'un $n$-échantillon iid $(X_1, \dots, X_n)$
Par indépendance des observations :
$$L(x_1, \dots, x_n; \lambda) = \prod_{i=1}^n P(X_i = x_i) = \prod_{i=1}^n e^{-\lambda}\frac{\lambda^{x_i}}{x_i!} = \frac{e^{-n\lambda}\, \lambda^{\sum_{i=1}^n x_i}}{\prod_{i=1}^n x_i!}$$

### 3. Application numérique ($n = 10$)
Effectifs : $k=0$ ($3$ fois), $k=1$ ($3$ fois), $k=3$ ($2$ fois), $k=4$ ($1$ fois), $k=6$ ($1$ fois).

```text
Effectif
  3 |  █    █
  2 |  █    █         █
  1 |  █    █         █    █         █
  0 +--0----1----2----3----4----5----6--> Nb notifications
```

On calcule $\sum_{i=1}^{10} x_i = 19$ et $\prod_{i=1}^{10} x_i! = 4!\,3!\,6!\,3! = 24 \times 6 \times 720 \times 6 = 622\,080$ :
$$L(\lambda) = \frac{e^{-10\lambda}\,\lambda^{19}}{622\,080}$$
$$L(1) = \frac{e^{-10}}{622\,080} \approx \mathbf{7{,}298 \times 10^{-11}}$$
$$L(2) = \frac{e^{-20}\, 2^{19}}{622\,080} \approx \mathbf{1{,}737 \times 10^{-9}}$$
Le maximum est atteint en $\hat{\lambda} = \frac{19}{10} = \mathbf{1{,}9}$, où $L(1{,}9) \approx 1{,}782 \times 10^{-9}$.

### 4. Calcul théorique de l'EMV $T$ via la log-vraisemblance
On passe au logarithme naturel :
$$\ell(\lambda) = \ln L(X_1, \dots, X_n; \lambda) = -n\lambda + \left(\sum_{i=1}^n X_i\right)\ln\lambda - \sum_{i=1}^n \ln(X_i!)$$

On annule la dérivée première et on vérifie la concavité :
$$\frac{\partial \ell}{\partial \lambda} = -n + \frac{\sum_{i=1}^n X_i}{\lambda} = 0 \iff \hat{\lambda} = \frac{1}{n}\sum_{i=1}^n X_i = \overline{X}$$
$$\frac{\partial^2 \ell}{\partial \lambda^2} = -\frac{\sum_{i=1}^n X_i}{\lambda^2} < 0$$
L'estimateur du maximum de vraisemblance est donc **$T = \overline{X}$**.

### 5. Estimation numérique
$$\hat{\lambda}_{\text{EMV}} = \bar{x} = \frac{19}{10} = \mathbf{1{,}9\text{ notifications/séance}}$$

### 6. Espérance et variance de $T = \overline{X}$
Puisque $X_i \sim \mathcal{P}(\lambda)$ avec $E(X_i) = \lambda$ et $\text{Var}(X_i) = \lambda$ :
$$E(T) = E(\overline{X}) = \lambda \quad (\text{estimateur sans biais})$$
$$\text{Var}(T) = \frac{\text{Var}(X)}{n} = \mathbf{\frac{\lambda}{n}}$$

### 7. Information de Fisher $I_n(\lambda)$
$$I_n(\lambda) = -E\!\left[\frac{\partial^2 \ell(\lambda)}{\partial \lambda^2}\right] = E\!\left[\frac{\sum_{i=1}^n X_i}{\lambda^2}\right] = \frac{n\lambda}{\lambda^2} = \mathbf{\frac{n}{\lambda}}$$

### 8. Efficacité de $T$ (Borne de Fréchet-Darmois-Cramér-Rao)
Pour tout estimateur sans biais $\hat{\theta}$ de $\lambda$ sous conditions de régularité :
$$\text{Var}(\hat{\theta}) \ge \frac{1}{I_n(\lambda)} = \frac{\lambda}{n}$$

> [!success] Conclusion
> Comme $\text{Var}(T) = \frac{\lambda}{n}$ atteint exactement la borne inférieure de Cramér-Rao, $T = \overline{X}$ est un **estimateur sans biais à variance minimale (efficace)** de $\lambda$. $\blacksquare$

---

## 📌 Exercice 9 – Estimation ponctuelle et par intervalle de confiance (Cacao)

> [!question] Énoncé résumé & Données
> On pèse la production de cacao (en kg) de $n = 10$ pieds tirés au hasard dans la région des Plateaux, modélisée par $\mathcal{N}(\mu, \sigma^2)$ :
> `2.4, 3.4, 3.6, 4.1, 4.3, 4.7, 5.4, 5.9, 6.5, 6.9`

### 1. Estimations ponctuelles non biaisées de $\mu$ et $\sigma^2$

| Pied $i$ | $x_i$ (kg) | $x_i - \bar{x}$ | $(x_i - \bar{x})^2$ | $x_i^2$ *(Koenig-Huygens)* |
| :---: | :---: | :---: | :---: | :---: |
| 1 | $2{,}4$ | $-2{,}32$ | $5{,}3824$ | $5{,}76$ |
| 2 | $3{,}4$ | $-1{,}32$ | $1{,}7424$ | $11{,}56$ |
| 3 | $3{,}6$ | $-1{,}12$ | $1{,}2544$ | $12{,}96$ |
| 4 | $4{,}1$ | $-0{,}62$ | $0{,}3844$ | $16{,}81$ |
| 5 | $4{,}3$ | $-0{,}42$ | $0{,}1764$ | $18{,}49$ |
| 6 | $4{,}7$ | $-0{,}02$ | $0{,}0004$ | $22{,}09$ |
| 7 | $5{,}4$ | $+0{,}68$ | $0{,}4624$ | $29{,}16$ |
| 8 | $5{,}9$ | $+1{,}18$ | $1{,}3924$ | $34{,}81$ |
| 9 | $6{,}5$ | $+1{,}78$ | $3{,}1684$ | $42{,}25$ |
| 10 | $6{,}9$ | $+2{,}18$ | $4{,}7524$ | $47{,}61$ |
| **Total ($\sum$)** | **$47{,}2$** | **$0$** | **$18{,}7160$** | **$241{,}50$** |

**Moyenne et variance estimées :**
$$\hat{\mu} = \bar{x} = \frac{47{,}2}{10} = \mathbf{4{,}72\text{ kg}}$$
$$\hat{\sigma}^2 = s^2 = \frac{18{,}716}{9} = \frac{241{,}50 - 10 \times 4{,}72^2}{9} \approx \mathbf{2{,}0796\text{ kg}^2}$$
$$s = \sqrt{2{,}0796} \approx \mathbf{1{,}4421\text{ kg}}$$

### 2. IC à 95% pour $\mu$ (loi de Student, $\nu = 9$)
En Annexe C ($\nu = 9$, $\alpha = 0{,}05$), $t_{9, 0{,}975} = 2{,}2622$ :
$$IC_{95\%}(\mu) = \left[4{,}72 \pm 2{,}2622 \times \frac{1{,}4421}{\sqrt{10}}\right] = [4{,}72 \pm 1{,}0316] = \mathbf{[3{,}69 \,;\, 5{,}75]\text{ kg}}$$

### 3. IC à 95% pour $\sigma^2$ (loi du $\chi^2$, $\nu = 9$)
En Annexe B ($\nu = 9$), $k_{0{,}975} = 19{,}0228$ (col. `0,025`) et $k_{0{,}025} = 2{,}7004$ (col. `0,975`). Avec $(n-1)s^2 = 18{,}716$ :
$$IC_{95\%}(\sigma^2) = \left[\frac{18{,}716}{19{,}0228} \,;\, \frac{18{,}716}{2{,}7004}\right] = \mathbf{[0{,}98 \,;\, 6{,}93]\text{ kg}^2}$$

### 4. IC à 95% pour $\mu$ avec $\sigma = 1{,}4$ connu (loi normale)
Avec $z_{0{,}975} = 1{,}96$ :
$$IC_{95\%}(\mu) = \left[4{,}72 \pm 1{,}96 \times \frac{1{,}4}{\sqrt{10}}\right] = [4{,}72 \pm 0{,}8677] = \mathbf{[3{,}85 \,;\, 5{,}59]\text{ kg}}$$

### 5. Nombre minimal de pieds pour précision $\pm 0{,}5$ kg à 99% ($\sigma = 1{,}4$)
On impose $z_{0{,}995}\frac{\sigma}{\sqrt{n}} \le 0{,}5$, avec $z_{0{,}995} = 2{,}5758$ (Annexe A.2) :
$$\sqrt{n} \ge \frac{2{,}5758 \times 1{,}4}{0{,}5} = 7{,}2122 \implies n \ge (7{,}2122)^2 = 52{,}016 \implies \mathbf{n_{\min} = 53\text{ pieds}}$$
*(Identique avec $z = 2{,}576$ issu du tableau du chapitre 2 : $52{,}025 \implies 53$ pieds.)*

> [!success] Conclusion
> La production moyenne par pied est estimée à $\mathbf{4{,}72\text{ kg}}$ ($IC_{95\%} = [3{,}69 \,;\, 5{,}75]$ kg en Student, $[3{,}85 \,;\, 5{,}59]$ kg si $\sigma = 1{,}4$ connu) et il faut observer au moins **$53$ pieds** pour garantir $\pm 0{,}5$ kg de précision à $99\%$.
