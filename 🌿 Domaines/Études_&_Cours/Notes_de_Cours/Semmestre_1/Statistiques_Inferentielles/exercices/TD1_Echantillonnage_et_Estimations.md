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

> **Matière :** [[MOC_Statistiques_Inferentielles|Statistiques Inférentielles (M1 IT)]] • **Support :** Feuille d'exercices n° 1 (p. 44–47) • **Statut :** Entièrement Résolu & Démontré

---

## 📌 Exercice 1 – Insertion professionnelle des diplômés

Soit $X$ la durée de recherche d'un premier emploi (en mois), modélisée par $X \sim \mathcal{N}(\mu = 14, \sigma^2 = 36)$, soit $\sigma = 6$ mois. On pose $Z = \frac{X - 14}{6} \sim \mathcal{N}(0, 1)$.

### 1. Limites de cette modélisation
Une variable normale prend ses valeurs sur $\mathbb{R} = ]-\infty; +\infty[$ et est symétrique autour de $\mu = 14$.
- **Support négatif impossible :** Le modèle attribue une probabilité non nulle à des durées négatives ($P(X < 0) = \Phi(-14/6) = \Phi(-2{,}33) \approx 0{,}0098$, soit près de $1\%$ des cas), ce qui n'a aucun sens physique.
- **Asymétrie réelle :** En pratique, les durées de chômage présentent une forte asymétrie à droite (queue longue vers les grandes durées), que la symétrie gaussienne ne capture pas.

### 2. Probabilité de chercher plus de 2 ans ($X > 24$ mois)
$$P(X > 24) = P\!\left(Z > \frac{24 - 14}{6}\right) = P(Z > 1{,}67) = 1 - \Phi(1{,}67)$$
Par lecture de l'Annexe A.1 : $\Phi(1{,}67) = 0{,}9525$, d'où :
$$P(X > 24) \approx 1 - 0{,}9525 = \mathbf{0{,}0475} \quad (\text{valeur exacte } z = 5/3 : 0{,}0478, \text{ soit } \mathbf{4{,}78\%})$$

### 3. Probabilité de trouver un emploi en moins de 6 mois ($X < 6$ mois)
$$P(X < 6) = P\!\left(Z < \frac{6 - 14}{6}\right) = P(Z < -1{,}33) = 1 - \Phi(1{,}33)$$
Par l'Annexe A.1 : $\Phi(1{,}33) = 0{,}9082$, d'où :
$$P(X < 6) \approx 1 - 0{,}9082 = \mathbf{0{,}0918} \quad (\text{valeur exacte } z = -4/3 : 0{,}0912, \text{ soit } \mathbf{9{,}12\%})$$

### 4. Probabilité d'une recherche entre 6 mois et 1 an ($6 \le X \le 12$)
$$P(6 \le X \le 12) = P\!\left(-1{,}33 \le Z \le \frac{12 - 14}{6}\right) = \Phi(-0{,}33) - \Phi(-1{,}33) = \Phi(1{,}33) - \Phi(0{,}33)$$
Par l'Annexe A.1 ($\Phi(0{,}33) = 0{,}6293$ et $\Phi(1{,}33) = 0{,}9082$) :
$$P(6 \le X \le 12) \approx 0{,}9082 - 0{,}6293 = \mathbf{0{,}2789} \quad (\text{valeur exacte : } 0{,}2782, \text{ soit } \mathbf{27{,}82\%})$$

---

## 📌 Exercice 2 – Qualité de service d'un réseau télécom

### 1. Probabilité qu'un SMS arrive en moins d'une minute
D'après l'engagement de l'opérateur : $p = \mathbf{0{,}95}$.

### 2. Envoi de 2 SMS de test ($X \sim \mathcal{B}(2;\, 0{,}95)$ sous indépendance)
$$P(X = k) = \binom{2}{k}(0{,}95)^k (0{,}05)^{2-k}$$
- $P(X = 0) = 1 \times 0{,}05^2 = \mathbf{0{,}0025}$ ($0{,}25\%$)
- $P(X = 1) = 2 \times 0{,}95 \times 0{,}05 = \mathbf{0{,}0950}$ ($9{,}5\%$)
- $P(X = 2) = 1 \times 0{,}95^2 = \mathbf{0{,}9025}$ ($90{,}25\%$)

### 3. Modélisation pour 20 SMS par jour
Chaque envoi étant modélisé comme une épreuve de Bernoulli de paramètre $p = 0{,}95$ (succès = transmis en moins d'une minute), indépendante d'un SMS à l'autre, le nombre de SMS arrivés en moins d'une minute suit une **loi binomiale** :
$$Y \sim \mathcal{B}(n = 20,\; p = 0{,}95)$$
*(Espérance $E(Y) = np = 19$ SMS, variance $\text{Var}(Y) = np(1-p) = 0{,}95$).*

### 4. Probabilité qu'au moins la moitié arrive en moins d'une minute ($Y \ge 10$)
$$P(Y \ge 10) = 1 - \sum_{k=0}^{9} \binom{20}{k}(0{,}95)^k (0{,}05)^{20-k} \approx 1 - 5{,}38 \times 10^{-10} \approx \mathbf{0{,}9999999995}$$
Il est **quasi certain** (à plus de $99{,}9999999\%$) qu'au moins 10 SMS sur 20 arrivent en moins d'une minute.

---

## 📌 Exercice 3 – Analyse de données de simulation sous R

Série observée ($n = 12$) : `10.7, 11.7, 11.6, 9.1, 11.1, 10.7, 10.7, 11.1, 9.5, 10.6, 12.0, 11.1`.

### 1. Estimation ponctuelle de la moyenne et de la variance
- **Somme :** $\sum_{i=1}^{12} x_i = 129{,}9$.
- **Moyenne empirique (sans biais) :**
  $$\bar{x} = \frac{129{,}9}{12} = \mathbf{10{,}825\text{ ms}}$$
- **Somme des carrés des écarts :** $\sum_{i=1}^{12} (x_i - 10{,}825)^2 = 7{,}8025$.
- **Variance empirique (biaisée) :** $\bar{s}^2 = \frac{7{,}8025}{12} \approx \mathbf{0{,}6502\text{ ms}^2}$.
- **Variance corrigée (sans biais) :**
  $$s^2 = \frac{7{,}8025}{11} \approx \mathbf{0{,}7093\text{ ms}^2} \quad \left(\text{écart-type } s = \sqrt{s^2} \approx \mathbf{0{,}8422\text{ ms}}\right)$$

### 2. Interprétation exacte de `round(rnorm(12, 10, 1), 1)`
1. `rnorm(12, 10, 1)` simule un échantillon de **12 réalisations indépendantes** d'une loi normale de moyenne $\mu = 10$ et d'**écart-type** $\sigma = 1$ *(en R, le 3e paramètre de `rnorm` est `sd`, l'écart-type, qui vaut ici $\sqrt{1}=1$)*.
2. `round(..., 1)` arrondit chacune de ces 12 valeurs à **1 chiffre après la virgule**.

---

## 📌 Exercice 4 – Modélisation du trafic de requêtes réseau

### 1. Estimation du mode, de la moyenne et de la variance ($n = \sum N_i = 53$ heures)
- **Mode :** Valeur d'effectif maximal : $\text{Mo} = \mathbf{3\text{ appels/h}}$ (observé $11$ fois).
- **Moyenne empirique :**
  $$\bar{x} = \frac{0(1) + 1(4) + 2(7) + 3(11) + 4(10) + 5(9) + 6(5) + 7(3) + 8(2) + 9(1)}{53} = \frac{212}{53} = \mathbf{4{,}00\text{ appels/h}}$$
- **Somme des carrés des écarts :** $\sum N_i (x_i - 4)^2 = 204$.
  - Variance empirique : $\bar{s}^2 = \frac{204}{53} \approx \mathbf{3{,}8491}$.
  - Variance corrigée (sans biais) : $s^2 = \frac{204}{52} \approx \mathbf{3{,}9231}$ ($s \approx 1{,}9807$).

### 2. Loi de probabilité proposée
Le nombre d'appels par heure est une variable **discrète de comptage** d'événements aléatoires sur un intervalle de temps fixe, et l'on observe que la moyenne et la variance empiriques sont quasi égales ($\bar{x} = 4{,}00 \approx s^2 = 3{,}92$). C'est la signature caractéristique d'une **loi de Poisson de paramètre $\lambda = 4$** ($\mathcal{P}(4)$).

---

## 📌 Exercice 5 – Estimation et intervalles de confiance du trafic Web

Données ($n = 10$) : `759, 750, 755, 756, 761, 765, 770, 752, 760, 767` $\sim \mathcal{N}(\mu, \sigma^2)$.

### 1. Estimations ponctuelles de $\mu$ et $\sigma^2$
- $\sum_{i=1}^{10} x_i = 7595 \implies \hat{\mu} = \bar{x} = \mathbf{759{,}5}$ connexions/jour.
- $\sum_{i=1}^{10} (x_i - 759{,}5)^2 = 378{,}5$.
- Estimation sans biais de $\sigma^2$ :
  $$s^2 = \frac{378{,}5}{9} \approx \mathbf{42{,}0556} \implies s \approx \mathbf{6{,}4850}$$
  *(Variance empirique biaisée : $\bar{s}^2 = 37{,}85$.)*

### 2. Intervalles de confiance pour $\mu$ ($\sigma$ inconnu $\implies$ Student à $\nu = 9$ ddl)
Formule : $IC_{1-\alpha}(\mu) = \left[\bar{x} \pm t_{9, 1-\alpha/2}\frac{s}{\sqrt{10}}\right]$, avec erreur standard $\frac{s}{\sqrt{10}} = \frac{6{,}4850}{3{,}1623} \approx 2{,}0507$.
- **À 90% ($\alpha = 0{,}10$, $t = 1{,}8331$ en Annexe C) :** marge $= 1{,}8331 \times 2{,}0507 = 3{,}7592$
  $$IC_{90\%}(\mu) = \mathbf{[755{,}74 \,;\, 763{,}26]}$$
- **À 99% ($\alpha = 0{,}01$, $t = 3{,}2498$ en Annexe C) :** marge $= 3{,}2498 \times 2{,}0507 = 6{,}6645$
  $$IC_{99\%}(\mu) = \mathbf{[752{,}84 \,;\, 766{,}16]}$$

### 3. Niveau de confiance pour un intervalle deux fois plus étroit qu'à 90%
On souhaite diviser la demi-largeur par $2$, ce qui revient à chercher le risque $\alpha$ tel que :
$$t_{9,\, 1-\alpha/2} = \frac{1{,}8331}{2} \approx \mathbf{0{,}9166}$$
- **Lecture de l'Annexe C ($\nu = 9$) :** Pour $\alpha = 0{,}500$ (confiance $50\%$), $t = 0{,}7027$ ; pour $\alpha = 0{,}300$ (confiance $70\%$), $t = 1{,}0997$. Le niveau de confiance est donc **compris entre 50% et 70%**.
- **Valeur exacte :** $P(|T_9| \le 0{,}91655) \approx \mathbf{61{,}67\%}$.

### 4. Taille d'échantillon $n$ pour une longueur $\le 1$ à 95%
La longueur vaut $L = 2\, t_{n-1,\, 0{,}975} \frac{s}{\sqrt{n}} \le 1$. Comme $n$ sera grand, on approxime $t_{n-1,\, 0{,}975} \approx z_{0{,}975} = 1{,}96$ :
$$n \ge (2 \times 1{,}96 \times 6{,}4850)^2 = 646{,}24 \implies \mathbf{n \ge 647\text{ jours}}$$
*(En affinant avec $t_{648, 0{,}975} \approx 1{,}9636$, on obtient $648{,}64 \implies \mathbf{649\text{ jours}}$. Si l'on utilisait $\bar{s}^2 = 37{,}85$, le calcul donnerait $582$ jours.)*

### 5. Impact si $\sigma^2 = 42$ est connue ($\sigma = \sqrt{42} \approx 6{,}4807$)
On n'estime plus $\sigma$ : la loi pivotale passe de Student $t(9)$ à la loi normale $\mathcal{N}(0, 1)$, ce qui **rétrécit les intervalles** (quantiles plus faibles pour quasi la même dispersion) :
- À 90% ($z = 1{,}6449$) : $[756{,}13 \,;\, 762{,}87]$ (largeur $6{,}74$ contre $7{,}52$ avant).
- À 99% ($z = 2{,}5758$) : $[754{,}22 \,;\, 764{,}78]$ (largeur $10{,}56$ contre $13{,}33$ avant).

---

## 📌 Exercice 6 – Comparaison de la qualité des matériaux de construction

Données : Centrale 1 ($n_1 = 25, \bar{x}_1 = 90{,}6, v_1^2 = 65{,}42$) ; Centrale 2 ($n_2 = 23, \bar{x}_2 = 94{,}4, v_2^2 = 58{,}24$).
*(Convention du cours p. 4 & 14 : la variance empirique $v^2$ est divisée par $n$, d'où $(n-1)s^2 = n v^2$. Les résultats entre parenthèses correspondent au cas alternatif où $v^2$ désignerait déjà la variance corrigée $s^2$.)*

### 1. IC à 95% pour la variabilité ($\sigma^2$ et $\sigma$) de chaque centrale
- **Centrale 1 ($\nu_1 = 24$ ddl) :** Annexe B ($\alpha = 0{,}025$ et $0{,}975$) donne $k_{\text{sup}} = 39{,}3641$ et $k_{\text{inf}} = 12{,}4012$. Numérateur $n_1 v_1^2 = 25 \times 65{,}42 = 1635{,}5$ :
  $$IC_{95\%}(\sigma_1^2) = \left[\frac{1635{,}5}{39{,}3641} \,;\, \frac{1635{,}5}{12{,}4012}\right] = \mathbf{[41{,}55 \,;\, 131{,}88]} \implies IC_{95\%}(\sigma_1) = \mathbf{[6{,}45 \,;\, 11{,}48]}$$
  *(Si $v_1^2$ déjà corrigée : $24 \times 65{,}42 = 1570{,}08 \implies [39{,}89 \,;\, 126{,}61]$).*
- **Centrale 2 ($\nu_2 = 22$ ddl) :** Annexe B donne $k_{\text{sup}} = 36{,}7807$ et $k_{\text{inf}} = 10{,}9823$. Numérateur $n_2 v_2^2 = 23 \times 58{,}24 = 1339{,}52$ :
  $$IC_{95\%}(\sigma_2^2) = \left[\frac{1339{,}52}{36{,}7807} \,;\, \frac{1339{,}52}{10{,}9823}\right] = \mathbf{[36{,}42 \,;\, 121{,}97]} \implies IC_{95\%}(\sigma_2) = \mathbf{[6{,}03 \,;\, 11{,}04]}$$
  *(Si $v_2^2$ déjà corrigée : $22 \times 58{,}24 = 1281{,}28 \implies [34{,}84 \,;\, 116{,}67]$).*

### 2. Peut-on conclure à une différence de variabilité ?
Les deux intervalles $[41{,}55 \,;\, 131{,}88]$ et $[36{,}42 \,;\, 121{,}97]$ **se recouvrent très largement**. On ne peut donc pas en déduire que les variances diffèrent ; le test rigoureux passe par le rapport de variances ci-dessous.

### 3. Intervalle de confiance à 95% pour le rapport $\sigma_1^2 / \sigma_2^2$
Variances corrigées : $s_1^2 = \frac{25}{24}(65{,}42) = 68{,}1458$ et $s_2^2 = \frac{23}{22}(58{,}24) = 60{,}8873$, d'où $\frac{s_1^2}{s_2^2} = 1{,}1192$.
Par interpolation linéaire dans l'Annexe D.2 ($\alpha = 0{,}025$) :
- $F_{0{,}025}(24, 22) \approx 2{,}39 - 0{,}4(2{,}39 - 2{,}27) = 2{,}342$
- $F_{0{,}025}(22, 24) \approx 2{,}33 - 0{,}2(2{,}33 - 2{,}21) = 2{,}306$
$$IC_{95\%}\!\left(\frac{\sigma_1^2}{\sigma_2^2}\right) = \left[\frac{1{,}1192}{2{,}342} \,;\, 1{,}1192 \times 2{,}306\right] = \mathbf{[0{,}478 \,;\, 2{,}581]}$$
*(Avec $v_1^2 / v_2^2 = 1{,}1233$ : $[0{,}480 \,;\, 2{,}590]$.)*
Comme **$1 \in [0{,}478 \,;\, 2{,}581]$**, on ne rejette pas l'égalité des variances : les deux centrales ont une variabilité homogène au seuil de 5%.

---

## 📌 Exercice 7 – Sondage d'opinion et prédiction électorale

Échantillon $n = 500$ ($n$ grand).

### 1. Estimation ponctuelle
- Candidat $C_1$ : $f_1 = \frac{150}{500} = 0{,}30 = \mathbf{30\%}$.
- Candidat $C_2$ : $f_2 = \frac{140}{500} = 0{,}28 = \mathbf{28\%}$.

### 2. Intervalles de confiance à 95% ($z = 1{,}96$)
Formule $f \pm 1{,}96\sqrt{\frac{f(1-f)}{n}}$ (identique à $10^{-4}$ près avec $n-1 = 499$) :
- **$C_1$ :** $0{,}30 \pm 1{,}96\sqrt{\frac{0{,}30 \times 0{,}70}{500}} = 0{,}30 \pm 0{,}0402 \implies \mathbf{[25{,}98\% \,;\, 34{,}02\%]}$
- **$C_2$ :** $0{,}28 \pm 1{,}96\sqrt{\frac{0{,}28 \times 0{,}72}{500}} = 0{,}28 \pm 0{,}0394 \implies \mathbf{[24{,}06\% \,;\, 31{,}94\%]}$

### 3. Prédiction électorale
**Non.** Les deux intervalles de confiance se chevauchent fortement (sur $[25{,}98\% \,;\, 31{,}94\%]$) : la marge d'erreur ($\approx \pm 4\%$) est supérieure à l'écart observé ($2\%$). On ne peut pas prédire qui arrivera en tête, ni même si l'un des deux obtiendra la majorité absolue au premier tour.

---

## 📌 Exercice 8 – Estimation par maximum de vraisemblance du flux de notifications

Soit $X \sim \mathcal{P}(\lambda)$ : $P(X = k) = e^{-\lambda}\frac{\lambda^k}{k!}$ pour $k \in \mathbb{N}$ ($\lambda > 0$).

### 1. Signification de $\lambda$
$\lambda$ représente le **nombre moyen (espérance) de notifications reçues par un étudiant pendant une séance de cours** (et également la variance de ce nombre, puisque pour une loi de Poisson $E(X) = \text{Var}(X) = \lambda$).

### 2. Fonction de vraisemblance d'un $n$-échantillon iid $(X_1, \dots, X_n)$
$$L(x_1, \dots, x_n; \lambda) = \prod_{i=1}^n P(X_i = x_i) = \prod_{i=1}^n e^{-\lambda}\frac{\lambda^{x_i}}{x_i!} = \frac{e^{-n\lambda}\, \lambda^{\sum_{i=1}^n x_i}}{\prod_{i=1}^n x_i!}$$

### 3. Application numérique ($n = 10$ : `1, 4, 1, 3, 1, 6, 3, 0, 0, 0`)
Effectifs : $k=0$ (3 fois), $k=1$ (3 fois), $k=3$ (2 fois), $k=4$ (1 fois), $k=6$ (1 fois).

**Diagramme en bâtons / Histogramme :**
```text
Effectif
  3 |  █    █
  2 |  █    █         █
  1 |  █    █         █    █         █
  0 +--0----1----2----3----4----5----6--> Nb notifications
```

$\sum_{i=1}^{10} x_i = 19$ et $\prod_{i=1}^{10} x_i! = 4!\,3!\,6!\,3! = 24 \times 6 \times 720 \times 6 = 622\,080$.
$$L(\lambda) = \frac{e^{-10\lambda}\,\lambda^{19}}{622\,080}$$
- Pour $\lambda = 1$ : $L(1) = \frac{e^{-10}}{622\,080} \approx \mathbf{7{,}298 \times 10^{-11}}$.
- Pour $\lambda = 2$ : $L(2) = \frac{e^{-20}\, 2^{19}}{622\,080} \approx \mathbf{1{,}737 \times 10^{-9}}$.
- Maximum atteint en $\hat{\lambda} = \frac{19}{10} = \mathbf{1{,}9}$ (où $L(1{,}9) \approx 1{,}782 \times 10^{-9}$).

### 4. Calcul théorique de l'EMV $T$ via la log-vraisemblance
$$\ell(\lambda) = \ln L(X_1, \dots, X_n; \lambda) = -n\lambda + \left(\sum_{i=1}^n X_i\right)\ln\lambda - \sum_{i=1}^n \ln(X_i!)$$
On dérive par rapport à $\lambda$ :
$$\frac{\partial \ell}{\partial \lambda} = -n + \frac{\sum_{i=1}^n X_i}{\lambda} = 0 \iff \hat{\lambda} = \frac{1}{n}\sum_{i=1}^n X_i = \overline{X}$$
Vérification du maximum : $\frac{\partial^2 \ell}{\partial \lambda^2} = -\frac{\sum X_i}{\lambda^2} < 0$. L'estimateur du maximum de vraisemblance est donc **$T = \overline{X}$**.

### 5. Estimation numérique
$$\hat{\lambda}_{\text{EMV}} = \bar{x} = \frac{19}{10} = \mathbf{1{,}9\text{ notifications/séance}}$$

### 6. Espérance et variance de $T = \overline{X}$
Puisque $X_i \sim \mathcal{P}(\lambda)$ ($E(X_i) = \lambda$, $\text{Var}(X_i) = \lambda$) :
$$E(T) = E(\overline{X}) = \lambda \quad (\text{estimateur sans biais}), \qquad \text{Var}(T) = \frac{\text{Var}(X)}{n} = \mathbf{\frac{\lambda}{n}}$$

### 7. Information de Fisher $I_n(\lambda)$
$$I_n(\lambda) = -E\!\left[\frac{\partial^2 \ell(\lambda)}{\partial \lambda^2}\right] = E\!\left[\frac{\sum_{i=1}^n X_i}{\lambda^2}\right] = \frac{n\lambda}{\lambda^2} = \mathbf{\frac{n}{\lambda}}$$

### 8. Efficacité de $T$ (Borne de Fréchet-Darmois-Cramér-Rao)
Pour tout estimateur sans biais $\hat{\theta}$ d'un paramètre $\lambda$ sous conditions de régularité, la borne inférieure de Cramér-Rao vaut :
$$\text{Var}(\hat{\theta}) \ge \frac{1}{I_n(\lambda)} = \frac{\lambda}{n}$$
Or $\text{Var}(T) = \frac{\lambda}{n}$ **atteint exactement cette borne minimale**. $T = \overline{X}$ est donc un **estimateur sans biais à variance minimale (efficace)** de $\lambda$. $\blacksquare$

---

## 📌 Exercice 9 – Estimation ponctuelle et par intervalle de confiance (Cacao)

Données ($n = 10$ kg) : `2.4, 3.4, 3.6, 4.1, 4.3, 4.7, 5.4, 5.9, 6.5, 6.9` $\sim \mathcal{N}(\mu, \sigma^2)$.

### 1. Estimations ponctuelles non biaisées de $\mu$ et $\sigma^2$
- $\sum_{i=1}^{10} x_i = 47{,}2 \implies \hat{\mu} = \bar{x} = \frac{47{,}2}{10} = \mathbf{4{,}72\text{ kg}}$.
- $\sum_{i=1}^{10} (x_i - 4{,}72)^2 = 18{,}716 \implies \hat{\sigma}^2 = s^2 = \frac{1}{n-1}\sum_{i=1}^n (x_i - \bar{x})^2 = \frac{18{,}716}{9} \approx \mathbf{2{,}0796\text{ kg}^2}$ ($s \approx 1{,}4421\text{ kg}$).

### 2. IC à 95% pour $\mu$ (loi de Student, $\nu = 9$)
Annexe C ($\nu = 9, \alpha = 0{,}05$) : $t_{9, 0{,}975} = 2{,}2622$.
$$IC_{95\%}(\mu) = \left[4{,}72 \pm 2{,}2622 \times \frac{1{,}4421}{\sqrt{10}}\right] = [4{,}72 \pm 1{,}0316] = \mathbf{[3{,}69 \,;\, 5{,}75]\text{ kg}}$$

### 3. IC à 95% pour $\sigma^2$ (loi du $\chi^2$, $\nu = 9$)
Annexe B ($\nu = 9$) : $k_{0{,}975} = 19{,}0228$ (col. `0,025`) et $k_{0{,}025} = 2{,}7004$ (col. `0,975`). Avec $(n-1)s^2 = 18{,}716$ :
$$IC_{95\%}(\sigma^2) = \left[\frac{18{,}716}{19{,}0228} \,;\, \frac{18{,}716}{2{,}7004}\right] = \mathbf{[0{,}98 \,;\, 6{,}93]\text{ kg}^2}$$

### 4. IC à 95% pour $\mu$ avec $\sigma = 1{,}4$ connu (loi normale)
$z_{0{,}975} = 1{,}96$ :
$$IC_{95\%}(\mu) = \left[4{,}72 \pm 1{,}96 \times \frac{1{,}4}{\sqrt{10}}\right] = [4{,}72 \pm 0{,}8677] = \mathbf{[3{,}85 \,;\, 5{,}59]\text{ kg}}$$

### 5. Nombre minimal de pieds pour précision $\pm 0{,}5$ kg à 99% ($\sigma = 1{,}4$)
On impose $z_{0{,}995}\frac{\sigma}{\sqrt{n}} \le 0{,}5$, avec $z_{0{,}995} = 2{,}5758$ (Annexe A.2) :
$$\sqrt{n} \ge \frac{2{,}5758 \times 1{,}4}{0{,}5} = 7{,}2122 \implies n \ge (7{,}2122)^2 = 52{,}016 \implies \mathbf{n_{\min} = 53\text{ pieds}}$$
*(Identique avec $z = 2{,}576$ issu du tableau du chapitre 2 : $52{,}025 \implies 53$ pieds.)*
