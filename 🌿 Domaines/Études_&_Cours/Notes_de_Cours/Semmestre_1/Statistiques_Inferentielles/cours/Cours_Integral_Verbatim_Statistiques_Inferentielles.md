---
type: note-cours
created: 2026-11-23
matiere: "Statistiques Inférentielles"
chapitre: "Texte Intégral & Référence Officielle (Prof. K. E. HOVI)"
enseignant: "K. E. HOVI (Ascencia Keyce Lomé)"
niveau: "Master 1 - IT"
tags:
  - etudes
  - cours
  - statistiques-inferentielles
  - verbatim
  - transcription-integrale
parent: "[[MOC_Statistiques_Inferentielles]]"
---

# 📜 Support Intégral : Statistiques Inférentielles (M1 IT)

> **Document source :** `Statistique_inf_M1_IT.pdf` • **Enseignant :** K. E. HOVI (Ascencia Keyce, Campus de Lomé, 20 nov. 2026)
> **Aperçu PDF direct dans Obsidian :**
> ![[Statistique_inf_M1_IT.pdf]]

---

## Sommaire Officiel

### Partie I – COURS
1. **Échantillonnage et estimations** (p. 3)
   - 1.1 Modèle d'échantillonnage (p. 3) — 1.1.1 Moyenne et variance empiriques (p. 4), 1.1.2 Fréquence (p. 5)
   - 1.2 Estimation paramétrique ponctuelle (p. 5) — 1.2.1 Estimateur ponctuel (p. 5), 1.2.2 Qualités d'un estimateur (p. 6), 1.2.3 Quelques estimateurs classiques (p. 7)
2. **Les intervalles de confiances** (p. 9)
   - 2.1 Estimation d'une proportion par intervalle de confiance (p. 9)
   - 2.2 Intervalle de confiance sur l'espérance (p. 10) — 2.2.1 Variance connue (p. 10) / Variance inconnue (p. 11) / Loi non normale (p. 13), 2.2.2 Arbre de décision (p. 13)
   - 2.3 Intervalle de confiance sur la variance d'une loi normale (p. 13) — 2.3.1 $\mu$ connue (p. 13), 2.3.2 $\mu$ inconnue (p. 14), 2.3.3 Égalité de deux variances (p. 14)
3. **Généralités sur les tests d'hypothèses** (p. 16)
   - 3.1 Introduction (p. 16)
   - 3.2 Principe du test (p. 17) — 3.2.1 Méthodologie, 3.2.2 $H_0$ et $H_1$, 3.2.3 Statistique et niveau de signification (p. 18)
   - 3.3 Risque d'erreur (p. 19)
   - 3.4 Puissance du test (p. 20)
4. **Les tests paramétriques** (p. 21)
   - 4.1 Test de la moyenne (p. 21)
   - 4.2 Test de la variance (p. 22)
   - 4.3 Test de la fréquence (p. 23)
   - 4.4 Test de comparaison de deux moyennes (p. 23)
   - 4.5 Test de comparaison de deux variances (p. 26)
   - 4.6 Analyse de la Variance (ANOVA) (p. 26)
   - 4.7 Test de comparaison de deux proportions (p. 28)
5. **Tests non paramétriques** (p. 29)
   - 5.1 Test d'indépendance de deux variables qualitatives (p. 29)
   - 5.2 Test de Mann-Whitney (p. 31)
   - 5.3 Test de Wilcoxon (p. 32)
6. **Corrélation et régression linéaire** (p. 34)
   - 6.1 Analyse de la corrélation (p. 34)
   - 6.2 Signification statistique des coefficients de corrélation (p. 36)
   - 6.3 Régression Linéaire Simple : Modélisation et Ajustement (p. 38)
   - 6.4 Application de la Régression : Évaluation et Prédiction (p. 40)

### Partie II – TRAVAUX DIRIGÉS
- Feuille d'exercices n° 1 : Échantillonnage et estimations (p. 44, 9 exercices)
- Feuille d'exercices n° 2 : Tests d'hypothèses (p. 48, 16 exercices)
- Feuille d'exercices n° 3 : Régression linéaire (p. 54, 5 exercices)

### Partie III – TRAVAUX PRATIQUES
- TP n° 1 : Utilisation du logiciel R (p. 58, 7 exercices)

### Partie IV – ANNEXES
- A : Tables des lois associées à la loi Normale (p. 53 / 62)
- B : Tables des lois associées à la loi de Pearson (p. 55 / 64)
- C : Tables des lois associées à la loi de Student (p. 56 / 65)
- D : Tables des lois associées à la loi de Fisher-Snedecor (p. 57 / 66)

---

# PARTIE I – COURS

## Chapitre 1 : Échantillonnage et estimations

### 1.1 Modèle d'échantillonnage

Soit $(\Omega, P)$ un espace probabilisé et $\chi$ un sous-ensemble de $\mathbb{R}$. On observe une réalisation $(x_1, \dots, x_n)$ d'un vecteur aléatoire $(X_1, \dots, X_n)$. On suppose les composantes $X_1, \dots, X_n$ indépendantes et de même loi inconnue.
On dira que le vecteur $(X_1, \dots, X_n)$ est un échantillon de variables indépendantes et identiquement distribuées, en abrégé **iid**.

#### Remarque 1.1.1
On distingue l'échantillon $(X_1, \dots, X_n)$ qui est aléatoire, et les données $(x_1, \dots, x_n) = (X_1(\omega), \dots, X_n(\omega))$, qui sont la réalisation d'un événement $\omega$. Lors d'une étude statistique, on observe seulement l'image de $\omega$ par les fonctions $X_1, \dots, X_n$.

Contrairement aux statistiques descriptives qui consistent essentiellement à résumer l'information contenue dans des données à l'aide d'indicateurs (moyenne, médiane, variance, etc.) ou de représentations graphiques (diagrammes, boxplots, histogrammes, etc.), la statistique inférentielle cherche à fournir un modèle probabiliste qui explique les données observées. Les observations sont donc traitées comme des réalisations de variables aléatoires de loi inconnue, dont on cherche à retrouver certaines caractéristiques (ex : espérance, probabilité d'un événement, densité, etc.).

La statistique inférentielle permet de répondre à différentes questions :
- Le choix d'un modèle permettant de décrire le phénomène aléatoire ;
- L'estimation de la loi des observations ;
- La construction d'intervalles de confiances ;
- La vérification d'hypothèses par des tests.

Plus le modèle est précis, plus il sera facile d'évaluer la loi des observations. Par exemple, si on dispose d'un échantillon $X_1, \dots, X_n$ issu d'une loi normale $\mathcal{N}(\mu, \sigma^2)$, il suffit d'estimer la moyenne et la variance des observations pour connaître la loi. En revanche, on prend le risque de considérer un modèle qui n'est pas exact. Si les observations ne sont pas Gaussiennes, on ne retrouvera jamais leur loi en se limitant à un modèle Gaussien.

#### Définition 1.1.1
Un modèle $\mathcal{M}$ est un ensemble de lois possibles pour les observations.
Le modèle est **paramétrique** s'il est indexé par un ensemble de dimension finie :
$$\mathcal{M} = \{\mu_\theta, \theta \in \Theta\}, \quad \Theta \subseteq \mathbb{R}^d$$
Dans le cas contraire, le modèle est **non-paramétrique**.

Les familles de lois usuelles sont des exemples de modèles paramétriques (ex : modèle Gaussien $\mathcal{M} = \{\mathcal{N}(\mu, \sigma^2), \mu \in \mathbb{R}, \sigma^2 > 0\}$, modèle de Poisson $\mathcal{M} = \{\mathcal{P}(\lambda), \lambda > 0\}$, modèle exponentiel $\mathcal{M} = \{\mathcal{E}(\lambda), \lambda > 0\}$, etc.).
Les modèles non-paramétriques sont moins spécifiques et sont utilisés dans les situations où on dispose de peu d'information sur la loi $X$ des observations (ex : $X$ est une loi continue, $X$ admet un moment d'ordre deux, $\mu$ est symétrique par rapport à zéro, ou $X$ est une loi de probabilité quelconque). Lorsqu'on choisit un modèle paramétrique, on prend le risque que la vraie loi des données n'appartienne pas au modèle. Un modèle non-paramétrique permet donc une évaluation parfois moins précise mais plus robuste de cette loi.

#### Définition 1.1.2
Une **statistique** $T_n = T_n(X_1, \dots, X_n)$ est une fonction (mesurable) connue de l'échantillon.
Une statistique $T_n$ est une variable aléatoire dont on observe une réalisation $t_n = T_n(x_1, \dots, x_n)$.

#### 1.1.1 Moyenne et variance empiriques

##### Définition 1.1.3
On appelle **moyenne de l'échantillon** $(X_1, \dots, X_n)$ ou **moyenne empirique**, la statistique notée $\overline{X}$ définie par :
$$\overline{X} = \frac{1}{n} \sum_{i=1}^n X_i$$

##### Théorème 1.1.1
Soit $X$ une variable aléatoire de moyenne $\mu$ et d'écart-type $\sigma$. On a :
$$E(\overline{X}) = \mu \quad \text{et} \quad V(\overline{X}) = \frac{\sigma^2}{n}$$
De plus, par le TCL, $\overline{X}$ converge en loi vers $\mathcal{N}\!\left(\mu, \frac{\sigma^2}{n}\right)$, lorsque $n$ tend vers l'infini.

*Preuve.* On a :
$$E\!\left(\frac{1}{n} \sum_{i=1}^n X_i\right) = \frac{1}{n} \sum_{i=1}^n E(X_i) = \frac{1}{n} \sum_{i=1}^n \mu = \mu$$
et en raison de l'indépendance des $X_i$ :
$$V\!\left(\frac{1}{n} \sum_{i=1}^n X_i\right) = \frac{1}{n^2} \sum_{i=1}^n V(X_i) = \frac{1}{n^2} \sum_{i=1}^n \sigma^2 = \frac{n\sigma^2}{n^2} = \frac{\sigma^2}{n} \quad \square$$

##### Définition 1.1.4
On appelle **Variance empirique**, la statistique notée $\overline{S}^2(X)$ définie par :
$$\overline{S}^2 = \frac{1}{n} \sum_{i=1}^n (X_i - \overline{X})^2$$

##### Théorème 1.1.2
Soit $X$ une variable aléatoire d'écart-type $\sigma$ et de moment centré d'ordre 4, $\mu_4$. On a :
$$E(\overline{S}^2) = \frac{n-1}{n}\sigma^2 \quad \text{et} \quad V(\overline{S}^2) = \frac{n-1}{n}\left[(n-1)\mu_4 - (n-3)\sigma^4\right]$$
De plus, lorsque $n$ tend vers l'infini,
$$V(\overline{S}^2) \sim \frac{\mu_4 - \sigma^3}{n}$$
*(Note de relecture : dans le polycopié imprimé, le facteur $\frac{1}{n^3}$ manque dans l'expression exacte de $V(\overline{S}^2) = \frac{n-1}{n^3}\left[(n-1)\mu_4 - (n-3)\sigma^4\right]$, et à l'infini l'équivalent exact est $V(\overline{S}^2) \sim \frac{\mu_4 - \sigma^4}{n}$, cohérent avec la Remarque 1.1.2 ci-dessous.)*

##### Remarque 1.1.2
Lorsque $n$ tend vers l'infini,
$$\sqrt{n}\,\frac{\overline{S}^2 - \sigma^2}{\sqrt{\mu_4 - \sigma^4}} \quad \text{converge en loi vers} \quad \mathcal{N}(0, 1)$$

#### 1.1.2 Fréquence
Soit $(X_i)_{i=1,\dots,n}$ un échantillon aléatoire de taille $n$ ayant une loi de Bernoulli de paramètre $p$, comme loi mère. Alors :
$$F = \frac{X_1 + \dots + X_n}{n}$$
est la fréquence de la valeur 1 dans l'échantillon et $nF$ suit une loi binomiale de paramètres $n$ et $p$. Ainsi :
$$E(F) = p \quad \text{et} \quad \text{Var}(F) = \frac{pq}{n}$$
*(avec $q = 1 - p$).*
Donc, quand $n$ tend vers l'infini, $F$ converge en loi vers $\mathcal{N}\!\left(p, \frac{pq}{n}\right)$.

---

### 1.2 Estimation paramétrique ponctuelle

Cette fois il s'agit d'estimer certaines caractéristiques statistiques de la loi (moyenne, variance, fonction de répartition) au travers d'une série d'observations $x_1, \dots, x_n$. C'est la problématique inverse de l'échantillonnage.
**À partir des caractéristiques d'un échantillon, que peut-on déduire des caractéristiques de la population dont il est issu ?**
L'estimation consiste à donner des valeurs approximatives aux paramètres d'une population à l'aide d'un échantillon de $n$ observations issues de cette population. On peut se tromper sur la valeur exacte, mais on donne la « meilleure valeur » possible que l'on peut supposer.

#### 1.2.1 Estimateur ponctuel
On souhaite estimer un paramètre $\theta$ d'une population (cela peut être sa moyenne $\mu$, son écart-type $\sigma$, une proportion $p$, etc.). Un **estimateur** de $\theta$ est une statistique $T$ (donc une fonction de $(X_1, \dots, X_n)$) dont la réalisation est envisagée comme une « bonne valeur » du paramètre $\theta$. On parle d'**estimation** de $\theta$ associée à cet estimateur pour la valeur observée lors de l'expérience, c'est-à-dire la valeur prise par la fonction au point observé $(x_1, \dots, x_n)$.
À chaque fois qu'on réalise une expérience, on obtient une nouvelle réalisation de l'échantillon et donc vraisemblablement une nouvelle valeur de $T$. Ainsi $T$ est une variable aléatoire et donc suit une loi de probabilité, a une moyenne, une variance, etc.

##### Exemple 1.2.1
Pour estimer l'espérance $E(X)$ de la loi de $X$, un estimateur naturel est la moyenne empirique $\overline{X}$ qui produit une estimation $\bar{x}$, moyenne descriptive de la série des valeurs observées.

#### 1.2.2 Qualités d'un estimateur

##### Définition 1.2.1
On appelle **biais** de $T$ pour $\theta$, la valeur :
$$b_\theta(T) = E(T) - \theta$$
Un estimateur $T$ est dit **sans biais** si $E(T) = 0$.
*(Note de relecture : coquille d'impression dans le polycopié — lire « si $E(T) = \theta$ », c'est-à-dire $b_\theta(T) = 0$.)*

##### Remarque 1.2.1
Notons que :
- en utilisant un estimateur sans biais un grand nombre de fois, il donne en moyenne la valeur du paramètre recherché ;
- à l'inverse, un estimateur est biaisé si en l'utilisant un grand nombre de fois, il ne donne pas en moyenne la valeur du paramètre recherché.
On souhaite qu'un estimateur soit non biaisé !

##### Définition 1.2.2
Un estimateur $T$ est dit **convergent** si $E(T)$ tend vers $\theta$ lorsque $n$ tend vers l'infini.
Il sera dit **consistant** si $T$ converge en probabilité vers $\theta$ lorsque $n$ tend vers l'infini.
En d'autres termes, quand la taille de l'échantillon $n$ augmente, $T$ doit avoir tendance à se rapprocher de $\theta$ puisque la quantité d'information augmente.

##### Théorème 1.2.1
Si $T$ est convergent et de variance tendant vers 0 lorsque $n$ tend vers l'infini alors $T$ est consistant.

##### Remarque 1.2.2
De façon générale, on peut écrire :
$$T - \theta = [T - E(T)] + [E(T) - \theta]$$
Ainsi :
- la grandeur $T - E(T)$ représente les fluctuations de $T$ autour de sa moyenne ;
- et $E(T) - \theta$ représente l'erreur systématique (biais).

##### Définition 1.2.3
La qualité d'un estimateur se mesure également par l'**erreur quadratique moyenne** (ou risque quadratique) définie par $E\big((T - \theta)^2\big)$.

##### Théorème 1.2.2
Soit $T$ un estimateur de paramètre $\theta$ à étudier. On a :
$$E\big((T - \theta)^2\big) = \text{Var}(T) + [E(T) - \theta]^2$$

*Preuve.*
$$E\big((T - \theta)^2\big) = E\big((T - E(T) + E(T) - \theta)^2\big) = E\big((T - E(T))^2\big) + E\big((E(T) - \theta)^2\big) + 2E\big([T - E(T)][E(T) - \theta]\big)$$
$$= \text{Var}(T) + (E(T) - \theta)^2 \quad \text{car } E(T - E(T)) = 0 \quad \square$$

##### Remarque 1.2.3
Entre deux estimateurs sans biais, le « meilleur » sera celui dont la variance est minimale (on parle d'**efficacité**).
Le critère d'erreur quadratique moyenne n'est pas parfait mais il est préféré à d'autres critères qui semblent plus naturels comme l'erreur absolue moyenne $E(|T - \theta|)$ car il s'exprime en fonction de notions simples comme le biais et la variance et est relativement facile à manipuler analytiquement.

#### 1.2.3 Quelques estimateurs classiques

##### 1.2.3.1 La moyenne empirique
Soit $(X_1, \dots, X_n)$ un échantillon de v.a. iid de variable parente $X$. On veut estimer le paramètre $\theta = E(X)$.
- Un estimateur de $E(X)$ est $\overline{X} = \frac{1}{n} \sum_{i=1}^n X_i$. C'est une v.a., donc $\overline{X}$ a une moyenne, une variance, une loi de probabilité.
- Cet estimateur est convergent : $\overline{X} \xrightarrow[n \to +\infty]{} \theta$.
- Cet estimateur est sans biais : $E(\overline{X}) = \theta$.
- Sa variance satisfait : $\text{Var}(\overline{X}) = \frac{\text{Var}(X)}{n}$ ; donc la variance de $\overline{X}$ décroît vers 0 quand $n$ tend vers $+\infty$.
- Quelle que soit la loi de $X$, la loi de $\overline{X}$ converge toujours vers la loi normale. En pratique, pour $n$ assez grand ($n \ge 30$), la loi de $\overline{X}$ peut être approximée par une loi normale de moyenne $\theta$ et de variance $\frac{\text{Var}(X)}{n}$ : soit $\mathcal{N}\!\left(\theta; \frac{\text{Var}(X)}{n}\right)$.
- La loi d'échantillonnage révèle la façon dont les réalisations de $\overline{X}$ oscillent autour de $\theta$. Cette loi sert d'une part à contrôler la marge d'erreur, et d'autre part à construire une estimation par intervalle.

##### 1.2.3.2 Autres estimateurs classiques
1. $\overline{S}^2 = \frac{1}{n} \sum_{i=1}^n (X_i - \overline{X})^2$ est un estimateur consistant de $\sigma^2$ (mais biaisé).
2. $S^2 = \frac{n}{n-1}\overline{S}^2$ est un estimateur sans biais et consistant de $\sigma^2$. Son estimation est $s^2 = \frac{n}{n-1}\sigma_e^2$ où $\sigma_e^2$ est la variance observée dans une réalisation de l'échantillon *(notée $\sigma_\epsilon^2$ avec le texte « l'écart-type observé » dans le polycopié, il s'agit bien de la variance empirique observée)*.
3. Si $p$ est la fréquence d'un caractère, $F = \frac{X_1 + \dots + X_n}{n}$ constitue un estimateur sans biais et consistant de $p$. Son estimation est notée $f$.

##### Remarque 1.2.4
Si la moyenne $\mu$ de $X$ est connue, $T = \frac{1}{n} \sum_{i=1}^n (X_i - \mu)^2$ est un meilleur estimateur de $\sigma^2$ que $S^2$.

---

## Chapitre 2 : Les intervalles de confiances

Une estimation ponctuelle ne nous renseigne pas ni sur le niveau de confiance que l'on peut avoir en l'estimation, ni sur la marge d'erreur :
- le **niveau de confiance** nous dit dans quelle mesure la méthode est fiable en usage répété ;
- la **marge d'erreur** nous dit dans quelle mesure la méthode est sensible, i.e. avec quelle précision l'intervalle localise le paramètre en train d'être estimé.

Au lieu de se donner une fonction (estimateur) qui donne une estimation ponctuelle d'un paramètre, on cherche un intervalle dans lequel se trouve le paramètre étudié avec une probabilité contrôlée (et généralement grande).
- À taille d'échantillon fixée à $n$, lorsqu'on augmente le niveau de confiance $1 - \alpha$, la largeur de l'IC augmente.
- À niveau de confiance fixé à $(1 - \alpha)$, lorsqu'on augmente la taille de l'échantillon $n$, la largeur de l'IC diminue.

### 2.1 Estimation d'une proportion par intervalle de confiance

On considère une population telle que pour le caractère observé la proportion $p$ d'une certaine catégorie est inconnue. On souhaite estimer cette proportion $p$ à partir d'un échantillon de taille $n$ dont la fréquence de la catégorie étudiée est $f$.
Soit $F$ la variable aléatoire qui à chaque échantillon de taille $n$ associe la fréquence du nombre d'éléments qui appartiennent à la catégorie choisie. On sait que $F$ suit approximativement la loi $\mathcal{N}(p, \sigma^2)$ avec $\sigma^2 = \frac{pq}{n}$, pour $n$ suffisamment grand ($n > 30$). On dispose de :
$$\sigma' = \sqrt{\frac{f(1-f)}{n}}$$
l'écart-type associé à la fréquence $f$ de l'échantillon de taille $n$. On se sert de l'estimation ponctuelle de $\sigma$ puisque $p$ est inconnue :
$$\sigma = \sigma'\sqrt{\frac{n}{n-1}} = \sqrt{\frac{f(1-f)}{n}} \cdot \sqrt{\frac{n}{n-1}} = \sqrt{\frac{f(1-f)}{n-1}}$$
Donc la variable aléatoire $Z$ définie par $Z = \frac{F - p}{\sigma}$ suit approximativement une loi normale centrée réduite $\mathcal{N}(0, 1)$.

On cherche un intervalle de confiance de la proportion $p$, c'est-à-dire un intervalle tel que la probabilité que la proportion $p$ n'appartienne pas à cet intervalle soit égale à $\alpha$ où $\alpha \in [0; 1]$. On appelle cet intervalle de confiance avec le risque $\alpha$ ou avec le coefficient de confiance $c = 1 - \alpha$.
On définit $z_{\alpha/2}$ comme étant la valeur telle que $P(Z > z_{\alpha/2}) = \alpha/2$ où $Z \sim \mathcal{N}(0, 1)$. Par symétrie :
$$P(Z < -z_{\alpha/2}) = \alpha/2 \quad \text{et} \quad P(-z_{\alpha/2} < Z < z_{\alpha/2}) = 1 - \frac{\alpha}{2} - \frac{\alpha}{2} = 1 - \alpha$$
D'où :
$$P(-z_{\alpha/2} < Z < z_{\alpha/2}) = 1 - \alpha \iff P\!\left(F - z_{\alpha/2}\sqrt{\frac{f(1-f)}{n-1}} < p < F + z_{\alpha/2}\sqrt{\frac{f(1-f)}{n-1}}\right) = 1 - \alpha$$
L'intervalle de confiance de la proportion $p$ avec un niveau de confiance de $1 - \alpha$ est :
$$\left]f - z_{\alpha/2}\sqrt{\frac{f(1-f)}{n-1}} \,;\, f + z_{\alpha/2}\sqrt{\frac{f(1-f)}{n-1}}\right[$$

#### Remarque 2.1.1
Lorsque $n$ est grand, la différence entre $n$ et $n - 1$ devient négligeable, aussi la formule devient :
$$IC(p) = \left]f - z_{\alpha/2}\sqrt{\frac{f(1-f)}{n}} \,;\, f + z_{\alpha/2}\sqrt{\frac{f(1-f)}{n}}\right[$$
C'est la formule la plus couramment utilisée.
On peut encore simplifier : avec un risque $\alpha = 5\%$ ($z_{\alpha/2} \approx 1{,}96 \approx 2$) et $f \simeq 0{,}5$, la formule peut être approchée par :
$$IC(p) = \left[f - \frac{1}{\sqrt{n}} \,;\, f + \frac{1}{\sqrt{n}}\right[$$

### 2.2 Intervalle de confiance sur l'espérance

#### 2.2.1 Intervalle de confiance sur l'espérance d'une loi normale avec variance connue
Soit $X \sim \mathcal{N}(\mu, \sigma^2)$ avec $\sigma$ connu. Le meilleur estimateur de $\mu$ est $\overline{X}$. Comme $X$ est de loi normale, on a :
$$T = \frac{\overline{X} - \mu}{\sigma / \sqrt{n}} \sim \mathcal{N}(0, 1)$$
En prenant des risques symétriques, on peut lire dans les tables les quantiles $u_{\alpha/2}$ et $u_{1-\alpha/2}$ de la loi normale centrée réduite tels que $P(u_{\alpha/2} \le T \le u_{1-\alpha/2}) = 1 - \alpha$.
*(Note : dans l'équation suivante du polycopié, $u_{\alpha/2}$ désigne le quantile positif $z_{1-\alpha/2}$ tel que $P(-u_{\alpha/2} \le T \le u_{\alpha/2}) = 1 - \alpha$.)*
On tire alors l'intervalle de confiance :
$$IC_{1-\alpha}(\mu) = \left[\overline{X} - u_{\alpha/2}\frac{\sigma}{\sqrt{n}}, \; \overline{X} + u_{\alpha/2}\frac{\sigma}{\sqrt{n}}\right]$$

##### Définition 2.2.1
Pour une variable aléatoire continue $X$, le nombre $q_\alpha$ tel que $P(X \le q_\alpha) = \alpha$ est le **quantile d'ordre $\alpha$** de la loi de $X$.
Ces quantiles sont notés de différentes façons : $u_\alpha$ pour la loi normale, $t_\alpha^n$ pour la loi de Student à $n$ degrés de liberté, $\chi_\alpha^2$ pour la loi du $\chi^2$, etc.
Comme la loi normale est symétrique : $u_{1-\alpha/2} = -u_{\alpha/2}$ *(au sens de la fonction quantile cumulée $P(Z \le u_\alpha) = \alpha$ ; ex : pour $\alpha = 0{,}05$, $u_{\alpha/2} = -1{,}96$ et $u_{1-\alpha/2} = +1{,}96$)*.

**Quantiles usuels $z_{\alpha/2}$ (positifs, i.e. $P(Z > z_{\alpha/2}) = \alpha/2$) pour la loi normale $\mathcal{N}(0, 1)$ :**

| Niveau de confiance $(1-\alpha)$ | 90% | 95% | 98% | 99% | 99,9% |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Risque $\alpha$** | 0,10 | 0,05 | 0,02 | 0,01 | 0,001 |
| **Quantile $z_{\alpha/2} = \Phi^{-1}(1 - \alpha/2)$** | 1,645 | 1,960 | 2,326 | 2,576 | 3,291 |

##### 2.2.1.1 Intervalle de confiance sur l'espérance d'une loi normale avec variance inconnue
Si la variance $\sigma^2$ est inconnue, on utilise son meilleur estimateur $S^2$. Comme on sait que $\frac{n\overline{S}^2}{\sigma^2}$ suit une loi du $\chi^2$ à $n-1$ degrés de liberté, il en résulte que $\frac{n-1}{\sigma^2}S^2$ suit aussi un $\chi^2_{n-1}$.
La statistique que l'on utilise est :
$$T_{n-1} = \frac{\overline{X} - \mu}{S/\sqrt{n}} = \frac{\frac{\overline{X}-\mu}{\sigma/\sqrt{n}}}{\sqrt{\frac{n-1}{\sigma^2}S^2 / (n-1)}}$$
Elle suit une **loi de Student à $n-1$ degrés de liberté**, comme rapport d'une loi normale centrée réduite sur la racine d'un $\chi^2$ divisé par son degré de liberté.
*(Figures 2.2.1 et 2.2.2 du support : densités symétriques de $\mathcal{N}(0,1)$ et Student avec aire centrale $1-\alpha$ et queues symétriques $\alpha/2$.)*

Comme précédemment, on obtient l'intervalle de confiance :
$$IC_{1-\alpha}(\mu) = \left[\bar{x} - t_{n-1, \alpha/2}\frac{S}{\sqrt{n}}, \; \bar{x} + t_{n-1, \alpha/2}\frac{S}{\sqrt{n}}\right]$$
où $t_{n-1, \alpha/2}$ est le quantile d'ordre $1 - \alpha/2$ (queue supérieure $\alpha/2$) de la loi de Student à $n-1$ degrés de liberté.

##### 2.2.1.2 Si la loi de $X$ n'est pas une loi normale
Dans ce cas, lorsque la taille de l'échantillon $n$ est supérieure ou égale à 30, le théorème central limite nous permet d'utiliser le fait que $\overline{X}$ suit approximativement une loi normale, et donc les résultats précédents restent applicables.

**Extrait de la table de Student $t_{\alpha/2, k}$ :**

| Degrés de liberté ($k = n - 1$) | $k=5$ | $k=10$ | $k=15$ | $k=20$ | $k=30$ | $k \to \infty$ ($\mathcal{N}(0,1)$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Niveau 90% ($\alpha = 0{,}10$)** | 2,015 | 1,812 | 1,753 | 1,725 | 1,697 | 1,645 |
| **Niveau 95% ($\alpha = 0{,}05$)** | 2,571 | 2,228 | 2,131 | 2,086 | 2,042 | 1,960 |
| **Niveau 99% ($\alpha = 0{,}01$)** | 4,032 | 3,169 | 2,947 | 2,845 | 2,750 | 2,576 |

#### 2.2.2 Arbre de décision
- La population est-elle normale ?
  - **Oui** $\to$ L'écart-type $\sigma$ est-il connu ?
    - **Oui** $\to$ $\mathcal{N}(0,1)$ ($z_{\alpha/2} = 1{,}96$ pour 95%).
    - **Non** $\to$ $t(n-1)$ (Loi de Student).
  - **Non** $\to$ Taille d'échantillon ?
    - **$n \ge 30$** $\to$ $\mathcal{N}(0,1)$ (TCL).
    - **$n < 30$** $\to$ Approche non paramétrique.

### 2.3 Intervalle de confiance sur la variance d'une loi normale

#### 2.3.1 Intervalle de confiance sur la variance d'une loi normale lorsque $\mu$ est connue
Comme $\mu$ est connue, le meilleur estimateur de la variance est la statistique :
$$V^2 = \frac{\sum_{i=1}^n (X_i - \mu)^2}{n}$$
Or $\frac{\sum (X_i - \mu)^2}{\sigma^2} = \frac{nV^2}{\sigma^2}$ suit une loi du $\chi^2$ à $n$ degrés de liberté, en tant que somme de $n$ carrés de lois normales centrées réduites indépendantes.
*(Figure 2.3.1 : représentation asymétrique du $\chi^2$ avec aires $\alpha/2$ aux deux extrémités.)*
En notant $\chi^2_{n, 1-\alpha/2}$ (queue gauche, petit quantile) et $\chi^2_{n, \alpha/2}$ (queue droite, grand quantile) :
$$\mathbb{P}\!\left(\chi^2_{n, 1-\alpha/2} \le \frac{nV^2}{\sigma^2} \le \chi^2_{n, \alpha/2}\right) = 1 - \alpha \implies IC_{1-\alpha}(\sigma^2) = \left[\frac{nV^2}{\chi^2_{n, \alpha/2}}, \; \frac{nV^2}{\chi^2_{n, 1-\alpha/2}}\right]$$
*(Note de relecture : dans le polycopié p. 13-14, l'indice $\alpha/2$ désigne le quantile de queue supérieure $P(X \ge q) = \alpha/2$ (grand quantile, colonne `0,025` en Annexe B), tandis qu'à la section 2.3.2 p. 14 l'ordre des bornes dans l'écriture est inversé par notation de fonction de répartition : retenir la règle invariante que la borne inférieure divise toujours par le **plus grand** quantile $\chi^2$ et la borne supérieure par le **plus petit** quantile $\chi^2$.)*

#### 2.3.2 Intervalle de confiance sur la variance d'une loi normale lorsque $\mu$ est inconnue
Si $\mu$ est inconnue, on utilise l'estimateur sans biais de $\sigma^2$ :
$$S^2 = \frac{\sum_{i=1}^n (X_i - \overline{X})^2}{n-1}$$
La propriété qui assure que $\frac{(n-1)S^2}{\sigma^2}$ suit une loi du $\chi^2_{n-1}$ permet de construire l'intervalle de confiance :
$$IC_{1-\alpha}(\sigma^2) = \left[\frac{(n-1)s^2}{\chi^2_{\text{grand}}}, \; \frac{(n-1)s^2}{\chi^2_{\text{petit}}}\right]$$
*(Dans le polycopié : $\left[\frac{(n-1)s^2}{\chi^2_{n-1, 1-\alpha/2}}, \frac{(n-1)s^2}{\chi^2_{n-1, \alpha/2}}\right]$ en notation fonction de répartition cumulée.)*

##### Remarque 2.3.1
Ces intervalles de confiance ne sont valables que pour une loi normale. Il n'est pas possible d'étendre ces résultats au cas d'une autre loi comme pour les intervalles de confiance sur la moyenne.

#### 2.3.3 Intervalle de confiance et test d'égalité de deux variances

##### 2.3.3.1 Cadre théorique et hypothèses
Soient deux populations normales et indépendantes :
- $X \sim \mathcal{N}(\mu_1, \sigma_1^2)$ avec un échantillon de taille $n_1$ et de variance corrigée $S_1^2$ ;
- $Y \sim \mathcal{N}(\mu_2, \sigma_2^2)$ avec un échantillon de taille $n_2$ et de variance corrigée $S_2^2$.

##### 2.3.3.2 Variable pivotale
D'après le théorème de Cochran, la variable pivotale construite sur le rapport des variances échantillonnaires et théoriques suit une **loi de Fisher-Snedecor** à $n_1 - 1$ et $n_2 - 1$ degrés de liberté :
$$F = \frac{S_1^2 / \sigma_1^2}{S_2^2 / \sigma_2^2} = \frac{S_1^2}{S_2^2} \times \frac{\sigma_2^2}{\sigma_1^2} \sim \mathcal{F}(n_1 - 1, n_2 - 1)$$

##### 2.3.3.3 Représentation graphique de la loi de Fisher-Snedecor
*(Figure 2.3.2 : densité asymétrique positive avec valeurs critiques $f_{1-\alpha/2}$ à gauche et $f_{\alpha/2}$ à droite laissant $\alpha/2$ dans chaque queue.)*

##### 2.3.3.4 Expression de l'intervalle de confiance
Au niveau de confiance $1-\alpha$, l'intervalle pour le rapport des variances $\frac{\sigma_1^2}{\sigma_2^2}$ est donné par :
$$IC_{1-\alpha}\!\left(\frac{\sigma_1^2}{\sigma_2^2}\right) = \left[\frac{S_1^2}{S_2^2} \times \frac{1}{F_{\alpha/2}(n_1 - 1, n_2 - 1)} \,;\, \frac{S_1^2}{S_2^2} \times F_{\alpha/2}(n_2 - 1, n_1 - 1)\right]$$
Rappel de la propriété de réversibilité des quantiles de Fisher :
$$f_{1-\alpha/2}(n_1 - 1, n_2 - 1) = \frac{1}{f_{\alpha/2}(n_2 - 1, n_1 - 1)}$$

##### 2.3.3.5 Règle de décision pour le test d'homoscédasticité
Pour tester $H_0 : \sigma_1^2 = \sigma_2^2$ contre $H_1 : \sigma_1^2 \ne \sigma_2^2$ au seuil de signification $\alpha$ :
- **Si $1 \in IC_{1-\alpha}\!\left(\frac{\sigma_1^2}{\sigma_2^2}\right)$ :** On ne rejette pas $H_0$. Les deux variances sont considérées comme égales au seuil $\alpha$.
- **Si $1 \notin IC_{1-\alpha}\!\left(\frac{\sigma_1^2}{\sigma_2^2}\right)$ :** On rejette $H_0$. Il existe une différence statistiquement significative entre les deux variances.

---

## Chapitre 3 : Généralités sur les tests d'hypothèses

### 3.1 Introduction

Un **test d'hypothèse** est un procédé d'inférence permettant de contrôler (accepter ou rejeter), à partir de l'étude d'un ou plusieurs échantillons aléatoires, la validité d'hypothèses relatives à une ou plusieurs populations. Les méthodes de l'inférence statistique permettent de déterminer, avec une probabilité donnée, si les différences constatées au niveau des échantillons peuvent être imputables au hasard ou si elles sont suffisamment importantes pour signifier que les échantillons proviennent de populations vraisemblablement différentes.

On distinguera deux classes de tests :
- **Les tests paramétriques** requièrent un modèle à fortes contraintes (normalité des distributions ou approximation normale pour des grands échantillons). Ces hypothèses sont d'autant plus difficiles à vérifier que les effectifs étudiés sont plus réduits.
- **Les tests non paramétriques** sont des tests dont le modèle ne précise pas les conditions que doivent remplir les paramètres de la population dont a été extrait l'échantillon. Il n'y a pas d'hypothèse de normalité au préalable.

Les tests paramétriques, quand leurs conditions sont remplies, sont plus puissants que les tests non paramétriques. Les tests non paramétriques s'emploient lorsque les conditions d'application des autres méthodes ne sont pas satisfaites, même après d'éventuelles transformations de variables ; ils peuvent s'utiliser même pour des échantillons de taille très faible.

On distingue les tests suivants :
- **Le test de conformité** consiste à confronter un paramètre calculé sur l'échantillon à une valeur préétablie (moyenne, variance, proportion). Ex. : lancer 100 fois un dé à 6 faces et tester si la fréquence de la face 3 est compatible avec $1/6$.
- **Le test d'ajustement ou d'adéquation** consiste à vérifier la compatibilité des données avec une distribution choisie a priori (ex. : ajustement à la loi normale avant un test paramétrique).
- **Le test d'homogénéité ou de comparaison** consiste à vérifier que $K$ ($K \ge 2$) échantillons (groupes) proviennent de la même population ou que la distribution de la variable d'intérêt est la même dans les $K$ échantillons (ex. : taux de glucose moyen sous deux traitements différents).
- **Le test d'indépendance ou d'association** consiste à éprouver l'existence d'une liaison entre 2 variables (techniques selon variables qualitatives nominales, ordinales ou quantitatives). Ex. : couleur des yeux indépendante du sexe.

### 3.2 Principe du test

#### 3.2.1 Méthodologie
Différentes étapes doivent être suivies pour tester une hypothèse :
1. Définir l'hypothèse nulle, notée $H_0$, à contrôler ;
2. Choisir une statistique pour contrôler $H_0$ ;
3. Définir la distribution de la statistique sous l'hypothèse « $H_0$ est réalisée » ;
4. Définir le niveau de signification du test $\alpha$ et la région critique associée ;
5. Calculer, à partir des données fournies par l'échantillon, la valeur de la statistique ;
6. Prendre une décision concernant l'hypothèse posée.

#### 3.2.2 Hypothèse nulle – hypothèse alternative
L'**hypothèse nulle** notée $H_0$ est l'hypothèse que l'on désire contrôler : elle consiste à dire qu'il n'existe pas de différence entre les paramètres comparés ou que la différence observée n'est pas significative et est due aux fluctuations d'échantillonnage. Cette hypothèse est formulée dans le but d'être rejetée.
L'**hypothèse alternative** notée $H_1$ est la « négation » de $H_0$, équivalente à dire « $H_0$ est fausse ». La décision de rejeter $H_0$ signifie que $H_1$ est réalisée ou $H_1$ est vraie.

##### Remarque 3.2.1
Il existe une dissymétrie importante dans les conclusions des tests. En effet, la décision d'accepter $H_0$ n'est pas équivalente à « $H_0$ est vraie et $H_1$ est fausse ». Cela traduit seulement l'opinion selon laquelle il n'y a pas d'évidence nette pour que $H_0$ soit fausse. Un test conduit à rejeter ou à ne pas rejeter une hypothèse nulle, jamais à l'accepter d'emblée.

La nature de $H_0$ détermine la façon de formuler $H_1$ et par conséquent la nature unilatérale ou bilatérale du test :
- **Test bilatéral :** lorsque $H_1$ se « décompose en deux parties », ex. $H_0 : p = p_0$ et $H_1 : p \ne p_0$.
- **Test unilatéral :** lorsque $H_1$ se « compose d'une seule partie », ex. $H_0 : p = p_0$ et $H_1 : p > p_0$ (ou $H_1 : p < p_0$).

#### 3.2.3 Statistique et niveau de signification
Connaissant la loi de probabilité suivie par la statistique $S$ sous l'hypothèse $H_0$, on établit une valeur seuil $S_{\text{seuil}}$ pour une probabilité donnée appelée **niveau de signification $\alpha$** du test. La **région critique** $R_c = f(S_{\text{seuil}})$ correspond à l'ensemble des valeurs telles que $P(S \in R_c) = \alpha$.

| Test | Unilatéral ($H_0 : t = t_0$) | Unilatéral ($H_0 : t = t_0$) | Bilatéral ($H_0 : t = t_0$) |
| :--- | :---: | :---: | :---: |
| **Hypothèse alternative** | $H_1 : t > t_0$ | $H_1 : t < t_0$ | $H_1 : t \ne t_0$ |
| **Niveau de signification** | $P(S > S_{\text{seuil}}) = \alpha$ | $P(S < S_{\text{seuil}}) = \alpha$ | $P(|S| > S_{\text{seuil}}) = \alpha$ |

Il existe deux stratégies de décision :
- **Règle de décision 1 (a priori sur $R_c$) :** Pour un seuil $\alpha$ fixé :
  - si $S_{\text{obs}} \in R_c$, l'hypothèse $H_0$ est rejetée au risque d'erreur $\alpha$ et $H_1$ est acceptée ;
  - si $S_{\text{obs}} \notin R_c$, l'hypothèse $H_0$ ne peut être rejetée.
  *(Remarque 3.2.2 : on choisit en général $\alpha = 0{,}05$, $0{,}01$ ou $0{,}001$.)*
- **Règle de décision 2 (a posteriori via la probabilité critique $\alpha_{\text{obs}}$ / $p$-value) :** La probabilité critique telle que $P(S \ge S_{\text{obs}}) = \alpha_{\text{obs}}$ *(adaptée à la forme de $H_1$)* est évaluée :
  - si $\alpha_{\text{obs}} \ge \alpha$, $H_0$ n'est pas rejetée ;
  - si $\alpha_{\text{obs}} < \alpha$, $H_0$ est rejetée car le risque de rejeter $H_0$ à tort est très faible.

### 3.3 Risque d'erreur

#### Définition 3.3.1
On appelle **risque d'erreur de première espèce** la probabilité $\alpha$ de rejeter $H_0$ et d'accepter $H_1$ alors que $H_0$ est vraie (probabilité de rejeter l'hypothèse nulle à tort).

#### Remarque 3.3.1
La valeur du risque $\alpha$ doit être fixée a priori par l'expérimentateur et jamais en fonction des données. C'est un compromis entre le risque de conclure à tort et la faculté de conclure. La région critique diminue lorsque $\alpha$ décroît et donc on rejette moins fréquemment $H_0$. À vouloir commettre moins d'erreurs, on conclut plus rarement.

#### Exemple 3.3.1 & 3.3.2
Test d'une pièce de monnaie lancée 100 fois ($X =$ nombre de faces). $H_0 :$ pièce non truquée, acceptée si $X \in [40; 60]$, rejetée si $X \notin [40; 60]$.
- Risque d'erreur de première espèce : $\alpha = P(\mathcal{B}(100; 1/2) \notin [40; 60])$.
- Si sous $H_1$ la pièce est truquée avec $p = 0{,}6$, le risque d'erreur de seconde espèce est $\beta = P(\mathcal{B}(100; 0{,}6) \in [40; 60])$.
*(Note de relecture : le polycopié imprime $\mathcal{B}(10, \dots)$ au lieu de $\mathcal{B}(100, \dots)$, $\in$ au lieu de $\notin$ dans l'Exemple 3.3.1, et la lettre $\alpha$ au lieu de $\beta$ dans l'Exemple 3.3.2.)*

#### Définition 3.3.2 & Remarque 3.3.2
On appelle **risque d'erreur de seconde espèce**, noté $\beta$, la probabilité de rejeter $H_1$ et d'accepter $H_0$ alors que $H_1$ est vraie. Pour quantifier le risque $\beta$, il faut connaître la loi de probabilité de la statistique sous l'hypothèse $H_1$.

### 3.4 Puissance du test

Rappelons que les tests ne sont pas faits pour « démontrer » $H_0$ mais pour « rejeter » $H_0$. L'aptitude d'un test à rejeter $H_0$ alors qu'elle est fausse constitue la **puissance du test**.

#### Définition 3.4.1
On appelle **puissance d'un test**, la probabilité de rejeter $H_0$ et d'accepter $H_1$ alors que $H_1$ est vraie. Sa valeur est $1 - \beta$.

La puissance d'un test est fonction de la nature de $H_1$ : un test unilatéral est plus puissant qu'un test bilatéral. Elle augmente avec la taille de l'échantillon $N$ étudié, et diminue lorsque $\alpha$ diminue.
La **robustesse** d'une technique statistique représente sa sensibilité à des écarts aux hypothèses faites.

| Décision \ Réalité | $H_0$ vraie | $H_1$ vraie |
| :--- | :---: | :---: |
| **$H_0$ acceptée** | Correct ($1-\alpha$) | Manque de puissance — risque de 2e espèce $\beta$ |
| **$H_1$ acceptée** | Rejet à tort — risque de 1re espèce $\alpha$ | Puissance du test ($1 - \beta$) |

---

## Chapitre 4 : Les tests paramétriques

On suppose dans ce chapitre que les échantillons sont issus d'une loi normale ou peuvent être approximés par une loi normale.

### 4.1 Test de la moyenne

#### 4.1.1 Variance connue
Échantillon de loi $\mathcal{N}(\mu, \sigma^2)$ avec $\sigma^2$ connue. On teste $H_0 : \mu = \mu_0$ contre $H_1 : \mu \ne \mu_0$.
Sous $H_0$, $\overline{X}_n \sim \mathcal{N}(\mu_0, \sigma^2/n)$, donc :
$$Z = \frac{\overline{X}_n - \mu_0}{\sqrt{\sigma^2 / n}} \sim \mathcal{N}(0, 1)$$
- **Cas bilatéral ($H_1 : \mu \ne \mu_0$) :** $P(|Z| \le z_{1-\alpha/2}) = 1 - \alpha$, région de rejet : $]-\infty; -z_{1-\alpha/2}[ \cup ]z_{1-\alpha/2}; +\infty[$.
- **Cas unilatéral ($H_1 : \mu > \mu_0$) :** $P(Z \le z_{1-\alpha}) = 1 - \alpha$, région de rejet : $]z_{1-\alpha}; +\infty[$.

#### 4.1.2 Variance inconnue
On estime la variance par la variance empirique corrigée $S_n^2 = \frac{1}{n-1}\sum_{i=1}^n (X_i - \overline{X}_n)^2$.
Sous $H_0$, la variable :
$$T = \frac{\overline{X}_n - \mu_0}{\sqrt{S_n^2 / n}}$$
suit une **loi de Student à $n - 1$ degrés de liberté**.
Pour un risque $\alpha$ (cas bilatéral) : $P(|T| \le t_{1-\alpha/2}) = 1 - \alpha$, région de rejet : $]-\infty; -t_{1-\alpha/2}[ \cup ]t_{1-\alpha/2}; +\infty[$.

### 4.2 Test de la variance

#### 4.2.1 Moyenne connue
Échantillon de loi $\mathcal{N}(\mu, \sigma^2)$ avec $\mu$ connue. On teste $H_0 : \sigma^2 = \sigma_0^2$ contre $H_1 : \sigma^2 \ne \sigma_0^2$.
Sous $H_0$, la statistique :
$$V = \frac{n\overline{S}_n^2}{\sigma_0^2} = \sum_{k=1}^n \left(\frac{X_k - \mu}{\sigma_0}\right)^2$$
suit une **loi du Khi-deux à $n$ ddl** ($\chi^2(n)$).
- **Bilatéral :** $P(\chi^2_{\alpha/2}(n) \le V \le \chi^2_{1-\alpha/2}(n)) = 1 - \alpha$, région de rejet : $[0, \chi^2_{\alpha/2}(n)[ \cup ]\chi^2_{1-\alpha/2}(n), +\infty[$.
- **Unilatéral ($H_1 : \sigma^2 > \sigma_0^2$) :** $P(V \le \chi^2_{1-\alpha}(n)) = 1 - \alpha$, région de rejet : $]\chi^2_{1-\alpha}(n), +\infty[$.

#### 4.2.2 Moyenne inconnue
On teste $H_0 : \sigma^2 = \sigma_0^2$ contre $H_1 : \sigma^2 \ne \sigma_0^2$.
Sous $H_0$, la statistique :
$$V = \frac{n\overline{S}_n^2}{\sigma_0^2} = \frac{(n-1)S_n^{\prime\,2}}{\sigma_0^2} = \sum_{k=1}^n \left(\frac{X_k - \overline{X}_n}{\sigma_0}\right)^2$$
suit une **loi du Khi-deux à $n - 1$ ddl** ($\chi^2(n-1)$).
Région de rejet bilatérale : $[0, \chi^2_{\alpha/2}(n-1)[ \cup ]\chi^2_{1-\alpha/2}(n-1), +\infty[$.

### 4.3 Test de la fréquence

On extrait un échantillon de taille $n$ d'une population où la proportion d'un caractère est $p$. Pour $n$ assez grand, la fréquence observée $f$ est la réalisation d'une v.a. assimilable à $\mathcal{N}(p, p(1-p)/n)$ (écart-type $\sqrt{p(1-p)/n}$).
Pour $H_0 : p = p_0$ contre $H_1 : p \ne p_0$, la région de rejet bilatérale au risque $\alpha$ sur $f$ est :
$$\left]-\infty, \; p_0 - q_{1-\alpha/2}\frac{\sqrt{p_0(1-p_0)}}{\sqrt{n}}\right[ \cup \left]p_0 + q_{1-\alpha/2}\frac{\sqrt{p_0(1-p_0)}}{\sqrt{n}}, \; +\infty\right[$$
avec $q_{1-\alpha/2}$ le quantile d'ordre $1-\alpha/2$ de $\mathcal{N}(0, 1)$.

### 4.4 Test de comparaison de deux moyennes

Si les deux échantillons sont appariés de même taille $n_1 = n_2 = n$, le test se ramène à un test à une moyenne nulle de l'échantillon $(Z_1, \dots, Z_n)$ avec $Z_i = X_i - Y_i$.

#### 4.4.1 Variance connue
Deux échantillons indépendants $(X_1, \dots, X_{n_1}) \sim \mathcal{N}(\mu_1, \sigma_1^2)$ et $(Y_1, \dots, Y_{n_2}) \sim \mathcal{N}(\mu_2, \sigma_2^2)$ avec variances connues. On teste $H_0 : \mu_1 = \mu_2$ contre $H_1 : \mu_1 \ne \mu_2$.
Sous $H_0$ :
$$U = \frac{\overline{X}_{n_1} - \overline{Y}_{n_2}}{\sqrt{\sigma_1^2/n_1 + \sigma_2^2/n_2}} \sim \mathcal{N}(0, 1)$$
- **Bilatéral :** région de rejet $]-\infty, -q_{1-\alpha/2}[ \cup ]q_{1-\alpha/2}, +\infty[$. *(Note : le signe moins devant le premier $q_{1-\alpha/2}$ était omis dans l'impression du polycopié, de même dans les trois régions bilatérales suivantes.)*
- **Unilatéral ($H_1 : \mu_1 > \mu_2$) :** région de rejet $]q_{1-\alpha}, +\infty[$.

#### 4.4.2 Variance inconnue
- **Cas 1 : $n_1$ et $n_2$ supérieurs à 30.** On estime les variances par $S_{n_1}^{\prime\,2}$ et $S_{n_2}^{\prime\,2}$ (diviseurs $n_1-1$ et $n_2-1$). La statistique :
  $$N = \frac{\overline{X}_{n_1} - \overline{Y}_{n_2}}{\sqrt{S_{n_1}^{\prime\,2}/n_1 + S_{n_2}^{\prime\,2}/n_2}}$$
  est approximée par $\mathcal{N}(0, 1)$.
- **Cas 2 : $n_1$ ou $n_2$ inférieur à 30 et $\sigma_1 = \sigma_2$.** On calcule la variance empirique corrigée commune (poolée) :
  $$S_{n_1, n_2}^{\prime\,2} = \frac{1}{n_1 + n_2 - 2}\left(\sum_{k=1}^{n_1}(X_k - \overline{X}_{n_1})^2 + \sum_{k=1}^{n_2}(Y_k - \overline{Y}_{n_2})^2\right)$$
  La statistique :
  $$T = \frac{\overline{X}_{n_1} - \overline{Y}_{n_2}}{\sqrt{S_{n_1, n_2}^{\prime\,2}(1/n_1 + 1/n_2)}}$$
  suit une **loi de Student à $n_1 + n_2 - 2$ ddl**.
- **Cas 3 : $n_1$ ou $n_2$ inférieur à 30 et $\sigma_1 \ne \sigma_2$ (Test de Welch).** La statistique :
  $$T = \frac{\overline{X}_{n_1} - \overline{Y}_{n_2}}{\sqrt{S_{n_1}^{\prime\,2}/n_1 + S_{n_2}^{\prime\,2}/n_2}}$$
  suit approximativement une loi de Student à $\nu$ ddl, où $\nu$ est l'entier le plus proche de :
  $$\nu = \frac{\left(S_{n_1}^{\prime\,2}/n_1 + S_{n_2}^{\prime\,2}/n_2\right)^2}{\frac{(S_{n_1}^{\prime\,2}/n_1)^2}{n_1 - 1} + \frac{(S_{n_2}^{\prime\,2}/n_2)^2}{n_2 - 1}}$$
  *(Note de relecture : dans le polycopié p. 25, le dénominateur est imprimé $(n_1-1)S^{\prime 4}_{n_1}/n_1^4$ au lieu de la formule standard de Welch-Satterthwaite avec division par $(n_1-1)$.)*

### 4.5 Test de comparaison de deux variances

On teste $H_0 : \sigma_1^2 = \sigma_2^2$ contre $H_1 : \sigma_1^2 \ne \sigma_2^2$ avec la statistique :
$$Z = \frac{S_{n_1}^{\prime\,2}}{S_{n_2}^{\prime\,2}}$$
Sous $H_0$, $Z$ suit une loi de Fisher-Snedecor à $n_1 - 1$ et $n_2 - 1$ ddl : $\mathcal{F}(n_1 - 1, n_2 - 1)$ *(imprimé par erreur $n_1-2$ dans la notation entre parenthèses p. 26 alors que le texte juste à côté précise bien « à $n_1 - 1$ et $n_2 - 1$ ddl »)*.
Région de rejet bilatérale au risque $\alpha$ : $[0, f_{\alpha/2}[ \cup ]f_{1-\alpha/2}, +\infty[$.

### 4.6 Analyse de la Variance (ANOVA)

#### 4.6.1–4.6.3 Introduction, idée générale et hypothèses
L'ANOVA (*Analysis of Variance*) compare les moyennes de $k$ groupes ($H_0 : \mu_1 = \mu_2 = \dots = \mu_k$ contre $H_1 :$ au moins une moyenne est différente). Utilisée en informatique pour comparer performances d'algorithmes, débits réseau, interfaces ou paramètres d'un programme.
Elle compare la **variabilité entre les groupes** (entre les moyennes) et la **variabilité dans les groupes** (dispersion autour de chaque moyenne).
**Conditions d'application :**
- Indépendance des observations ;
- Normalité approximative des données dans chaque groupe ;
- Homogénéité des variances entre les groupes (homoscédasticité).

#### 4.6.4–4.6.6 Formulation, statistique et décision
$$F = \frac{\text{Variabilité entre groupes}}{\text{Variabilité dans les groupes}} = \frac{\text{CM}_{\text{inter}}}{\text{CM}_{\text{intra}}}$$
Sous $H_0$, $F \sim \mathcal{F}(k - 1, N - k)$ (où $N$ est l'effectif total).
- Si $F \approx 1$, les moyennes semblent similaires ; si $F$ est grand, une différence entre groupes est probable.
- Si $p\text{-value} \le 0{,}05$ (ou $F_{\text{obs}} > F_{\text{crit}}$), rejet de $H_0$. La $p$-value est l'aire de la queue de la loi de Fisher au-delà de $F_{\text{obs}}$.

#### Exemple 4.6.1 (Trois régimes alimentaires, $n_j = 5$, $N = 15$)
- $A : 190, 185, 195, 200, 188 \implies \text{moy}_A = 191{,}6$
- $B : 210, 220, 215, 225, 218 \implies \text{moy}_B = 217{,}6$
- $C : 180, 175, 178, 182, 177 \implies \text{moy}_C = 178{,}4$
- Moyenne globale : $\text{moy}_T = \frac{2938}{15} \approx 195{,}8667$.
- $\text{SC}_{\text{inter}} = \sum n_j (\text{moy}_j - \text{moy}_T)^2 \approx 91{,}066 + 2361{,}78 + 1524{,}995 = 3977{,}841$.
- $\text{SC}_{\text{intra}} = \sum (x_i - \text{moy}_{\text{groupe}})^2 = 141{,}2 + 125{,}2 + 29{,}2 = 295{,}6$.

| Source | SC | ddl | CM | $F$ |
| :--- | :---: | :---: | :---: | :---: |
| Inter | 3977,841 | 2 | 1988,9205 | $1988{,}9205 / 24{,}6333 \approx 80{,}71$ |
| Intra | 295,6 | 12 | 24,6333 | |
| Total | 4273,441 | 14 | | |

$F \approx 80{,}71 \gg F_{0{,}05}(2, 12) = 3{,}89$ : on rejette $H_0$, les moyennes diffèrent significativement.

### 4.7 Test de comparaison de deux proportions

On veut tester $H_0 : p_1 = p_2$ contre $H_1 : p_1 \ne p_2$ à partir des proportions $f_1, f_2$ et tailles $n_1, n_2$. On utilise la statistique :
$$Z = \frac{f_1 - f_2}{\sqrt{F(1 - F)(1/n_1 + 1/n_2)}} \quad \text{avec} \quad F = \frac{n_1 f_1 + n_2 f_2}{n_1 + n_2}$$
Région de rejet au risque $\alpha$ : $]-\infty, -z_{1-\alpha/2}[ \cup ]z_{1-\alpha/2}, +\infty[$.

---

## Chapitre 5 : Tests non paramétriques

Contrairement aux tests paramétriques, les tests non paramétriques ne font aucune hypothèse sur la distribution sous-jacente des données (*distribution free*). Ils sont moins puissants lorsque les conditions paramétriques sont réunies, mais s'emploient pour de petits effectifs, des données ordinales/qualitatives ou non normales. Lorsque les données sont quantitatives, ils transforment les valeurs en **rangs** (*tests de rangs*).

### 5.1 Test d'indépendance de deux variables qualitatives (Test du $\chi^2$)

On dispose de $X$ en $l$ modalités et $Y$ en $k$ modalités, avec effectifs observés $n_{i,j}$ et total $n = \sum_{i=1}^l \sum_{j=1}^k n_{i,j}$.
Hypothèse testée $H_0$ : « Les variables $X$ et $Y$ sont indépendantes ».
- Effectifs marginaux : $S_i = \sum_j n_{i,j}$ (lignes) et $T_j = \sum_i n_{i,j}$ (colonnes).
- Effectifs théoriques sous $H_0$ : $C_{i,j} = \frac{S_i T_j}{n}$.
- Statistique de test :
  $$\chi_c^2 = \sum_{i,j} \frac{(n_{i,j} - C_{i,j})^2}{C_{i,j}}$$
- Degrés de liberté : $\nu = (l - 1) \times (k - 1)$.
- Décision : si $\chi_c^2 < \chi_\alpha^2$, on ne rejette pas $H_0$ ; sinon on la rejette.
- Condition d'application a posteriori : **$C_{i,j} \ge 5$ pour tous $i, j$**.

#### Exemple 5.1.1 (Médicament vs Générique)
Tableau observé : Médicament (48 guérisons, 6 aucun effet ; total 54), Générique (158 guérisons, 44 aucun effet ; total 202) ; total général $n = 256$ (206 guérisons, 50 aucun effet).
Effectifs théoriques : $(43{,}45; 162{,}55; 10{,}55; 39{,}45)$ (tous $\ge 5$).
$$\chi_c^2 = \frac{(48-43{,}45)^2}{43{,}45} + \frac{(158-162{,}55)^2}{162{,}55} + \frac{(6-10{,}55)^2}{10{,}55} + \frac{(44-39{,}45)^2}{39{,}45} \simeq 3{,}1$$
Pour $\nu = 1$ et $\alpha = 5\%$, $\chi^2_{\text{crit}} = 3{,}84$. Comme $3{,}1 < 3{,}84$, on ne rejette pas $H_0$ : le taux de guérison ne dépend pas du choix du médicament.

### 5.2 Test de Mann-Whitney

Test non paramétrique comparant deux échantillons indépendants $x_1, \dots, x_n$ et $y_1, \dots, y_m$ issus de variables numériques ou ordinales sous $H_0 : \mathcal{L}_X = \mathcal{L}_Y$ ($F_X = F_Y$).
Statistique de comptage des couples :
$$U_{n,m} = \sum_{i=1}^n \sum_{j=1}^m \mathbf{1}_{\{x < y\}}(X_i, Y_j)$$
où $\mathbf{1}_{\{x < y\}}(X_i, Y_j)$ vaut 1 si $X_i < Y_j$, $0{,}5$ si $X_i = Y_j$, et 0 sinon.
Équivalent par la somme des rangs conjoints $R_1$ (groupe 1, taille $n_1$) et $R_2$ (groupe 2, taille $n_2$, avec $N = n_1 + n_2$) :
$$U_1 = R_1 - \frac{n_1(n_1 + 1)}{2}, \qquad U_2 = R_2 - \frac{n_2(n_2 + 1)}{2}, \qquad U_1 + U_2 = n_1 n_2$$
**Règle de décision (test bilatéral) :** $u = \min(u_1, u_2)$. On rejette $H_0$ si $u \in [0; m_\alpha]$ (i.e. $u \le u_{\text{crit}}$).
Pour de grands échantillons, sous $H_0$ :
$$E(U) = \frac{n_1 n_2}{2}, \qquad \text{Var}(U) = \frac{n_1 n_2 (n_1 + n_2 + 1)}{12}, \qquad Z = \frac{U - \frac{n_1 n_2}{2}}{\sqrt{\frac{n_1 n_2 (n_1 + n_2 + 1)}{12}}} \xrightarrow{\text{approx.}} \mathcal{N}(0, 1)$$
*(Remarque 5.2.1 : le test de Kruskal-Wallis étend Mann-Whitney à plus de deux échantillons, comme l'ANOVA étend le test $t$.)*

### 5.3 Test de Wilcoxon

Test non paramétrique comparant deux populations **appariées**. Sur $N$ paires observées, on élimine les différences nulles pour ne conserver que $n$ différences non nulles $d_i$ ($1 \le i \le n$). On classe les rangs $r_i$ des valeurs absolues $|d_i|$ (en attribuant le rang moyen aux ex-æquo).
La statistique de rangs signés de Wilcoxon est :
$$W = \min\!\left(\sum_{d_i > 0} r_i, \; \sum_{d_i < 0} r_i\right)$$
**Règle de décision :** Dans le cas bilatéral, on rejette $H_0$ lorsque $W < W_{\alpha/2}$ (ou $W \le W_{\alpha/2}$ selon la convention de table ; en complément, la zone de non-rejet est $]W_{\alpha/2}, W_{1-\alpha/2}[$ avec $W_{1-\alpha/2} = \frac{n(n+1)}{2} - W_{\alpha/2}$).
*(Note de relecture : le polycopié imprime « On peut rejeter $H_0$ si $W \in ]W_{\alpha/2}, W_{1-\alpha/2}[$ » alors que la phrase suivante précise correctement « on rejette $H_0$ lorsque $W < W_{\alpha/2}$ dans le cas bilatéral ».)*
Pour les grands échantillons ($n > 25$) :
$$Z = \frac{W - \frac{n(n+1)}{4}}{\sqrt{\frac{n(n+1)(2n+1)}{24}}} \leadsto \mathcal{N}(0, 1)$$
*(Remarque 5.3.1 : le test de Wilcoxon est plus puissant que le test des signes car il tient compte de l'amplitude des différences en plus de leur signe.)*

#### Exemple 5.3.1 (Test à l'aveugle : bière locale vs importée, 10 étudiants)
Différences $(\text{Locale} - \text{Import})$ : $-4; -2; 1; 0; 2; -4; -6; -2; 1; -3$.
On retire le $0$ ($n = 9$ paires non nulles). Tri par valeur absolue croissante : $1, 1, -2, 2, -2, -3, -4, -4, -6$.
Rangs moyens : $(1{,}5 ; 1{,}5 ; 4 ; 4 ; 4 ; 6 ; 7{,}5 ; 7{,}5 ; 9)$.
- $\sum_{d_i > 0} r_i = 1{,}5 + 1{,}5 + 4 = 7$
- $\sum_{d_i < 0} r_i = 4 + 4 + 6 + 7{,}5 + 7{,}5 + 9 = 38$
- $W = \min(7, 38) = 7$. Comme $W_{0{,}05} = 8$ (test unilatéral pour $n=9$) et $7 \le 8$, on rejette $H_0$ : préférence significative pour la bière d'importation.

---

## Chapitre 6 : Corrélation et régression linéaire

### 6.1 Analyse de la corrélation

#### 6.1.1 Principes fondamentaux et nuage de points
La **corrélation** mesure le degré d'association statistique entre deux variables (si les variations de $X$ accompagnent systématiquement celles de $Y$). Avant tout calcul, l'inspection visuelle par un **nuage de points (scatter plot)** est obligatoire pour identifier : (1) la forme de la relation (linéaire, monotone non linéaire, non monotone), (2) la présence d'*outliers*, (3) la dispersion des points.

#### 6.1.2 Coefficient de corrélation de Pearson ($r$)
Mesure la force d'une relation **strictement linéaire** entre deux variables quantitatives continues (hypothèses : variables d'intervalle/ratio, linéarité, normalité bivariée ou $n \ge 30$, absence d'*outliers*).
$$r = \frac{\text{Cov}(X, Y)}{\sigma_X \sigma_Y} = \frac{\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_{i=1}^n (x_i - \bar{x})^2}\sqrt{\sum_{i=1}^n (y_i - \bar{y})^2}}$$
Grille de lecture ($r \in [-1; +1]$) : $r = \pm 1$ parfaite ; $0{,}7 \le |r| < 1$ forte ; $0{,}3 \le |r| < 0{,}7$ modérée ; $|r| < 0{,}3$ faible ou inexistante.

#### 6.1.3 Coefficient de corrélation de Spearman ($\rho$ ou $r_s$)
Coefficient non paramétrique préconisé pour les variables ordinales ou les relations **monotones** non linéaires, robuste aux *outliers*. C'est le coefficient de Pearson appliqué aux rangs :
$$\rho = 1 - \frac{6 \sum_{i=1}^n d_i^2}{n(n^2 - 1)} \quad \text{où } d_i = \text{rg}(x_i) - \text{rg}(y_i)$$

#### 6.1.4–6.1.5 Guide de choix, mise en garde et R
- **Pearson :** quantitatives continues, relation strictement linéaire, sensible aux *outliers* et à la normalité.
- **Spearman :** ordinales ou quantitatives, monotone, robuste aux *outliers*, non paramétrique.
- **Mise en garde : Corrélation $\ne$ Causalité** (risque de facteur de confusion / variable tierce).
- R : `plot(data$X, data$Y)` puis `cor.test(data$X, data$Y, method = "pearson")` ou `"spearman"`.

### 6.2 Signification statistique des coefficients de corrélation

Test bilatéral : $H_0 : \rho = 0$ (aucune corrélation dans la population) contre $H_1 : \rho \ne 0$.
Statistique de test suivant une loi de Student à $n - 2$ ddl :
$$t = r\sqrt{\frac{n - 2}{1 - r^2}}$$
Décision au seuil $\alpha$ (ex. $0{,}05$) : si $p\text{-value} < \alpha$ (ou $|t| > t_{\text{crit}}$), on rejette $H_0$.
**Pièges d'interprétation :**
- Sur très petits échantillons ($n < 10$), un $r$ élevé ($0{,}80$) peut être non significatif.
- Sur de très grands échantillons ($n > 100\,000$), un $r$ minuscule ($0{,}05$) devient statistiquement significatif sans portée métier pratique.

### 6.3 Régression Linéaire Simple : Modélisation et Ajustement

Équation du modèle estimé : $\hat{Y} = b_0 + b_1 X$, où $\hat{Y}$ est la valeur prédite, $b_0$ l'ordonnée à l'origine (*intercept*) et $b_1$ la pente (coefficient de régression).
Pour chaque observation $i$, le **résidu** est $e_i = Y_i - \hat{Y}_i = Y_i - (b_0 + b_1 X_i)$.
La **Méthode des Moindres Carrés Ordinaires (MCO)** minimise la somme des carrés des résidus :
$$\min_{b_0, b_1} \sum_{i=1}^n e_i^2 = \min_{b_0, b_1} \sum_{i=1}^n (Y_i - (b_0 + b_1 X_i))^2$$
Estimateurs MCO :
$$b_1 = \frac{\text{Cov}(X, Y)}{s_X^2} = r_{X,Y} \cdot \left(\frac{s_Y}{s_X}\right), \qquad b_0 = \overline{Y} - b_1 \overline{X}$$
- **Interprétation métier de $b_1$ :** variation moyenne attendue de $Y$ quand $X$ augmente d'une unité.
- **Interprétation métier de $b_0$ :** valeur moyenne prédite de $Y$ quand $X = 0$ (valide uniquement si $X=0$ a un sens physique/métier et se situe à proximité de la plage $[X_{\min}, X_{\max}]$ — alerte contre le **piège de l'extrapolation**).

### 6.4 Application de la Régression : Évaluation et Prédiction

#### 6.4.1 Coefficient de détermination ($R^2$)
Proportion de la variance totale de $Y$ expliquée par $X$ à travers le modèle linéaire :
$$R^2 = \frac{\text{SCE}}{\text{SCT}} = 1 - \frac{\text{SCR}}{\text{SCT}}$$
où $\text{SCT} = \text{SCE} + \text{SCR}$ (Somme des Carrés Totale = Expliquée + Résiduelle).
$R^2 \in [0, 1]$, et en régression linéaire simple, **$R^2 = r^2$**.

#### 6.4.2 Test de significativité de la pente ($H_0 : \beta_1 = 0$)
Statistique $t = \frac{b_1}{s_{b_1}}$ ($s_{b_1}$ = erreur standard de la pente). Si $p\text{-value} < 0{,}05$, on rejette $H_0$ : $X$ influe significativement sur $Y$.

#### 6.4.3 Prédiction ponctuelle, Intervalle de Confiance (IC) vs Intervalle de Prédiction (IP)
Prédiction ponctuelle pour $X_0$ : $\hat{Y}_0 = b_0 + b_1 X_0$.

| Caractéristique | Intervalle de Confiance (IC) | Intervalle de Prédiction (IP) |
| :--- | :--- | :--- |
| **Objet ciblé** | Estimé autour de la **valeur moyenne** $E[Y \mid X_0]$ | Estimé pour **une valeur individuelle** $Y_0$ |
| **Incertitude** | Erreur d'estimation du modèle $(b_0, b_1)$ uniquement | Erreur du modèle $+$ variabilité résiduelle de l'individu ($\sigma^2$) |
| **Largeur** | Plus étroit | Toujours plus large que l'IC |
| **Usage** | Estimer la latence moyenne d'un serveur sur un mois | Prédire la latence exacte de la *prochaine* requête |

**Alerte extrapolation :** Il est extrêmement risqué d'utiliser l'équation de régression pour prédire en dehors de la plage d'apprentissage $[X_{\min}, X_{\max}]$.

---

# PARTIE IV – MÉMO DE LECTURE DES ANNEXES (TABLES STATISTIQUES)

| Annexe | Loi | Convention exacte de la table dans le PDF | Valeurs repères à $\alpha = 5\%$ (bilatéral / unilatéral) |
| :--- | :--- | :--- | :--- |
| **A.1** | Normale $\mathcal{N}(0,1)$ | $\Phi(z) = P(Z \le z)$ pour $z \ge 0$ ; symétrie $\Phi(-z) = 1 - \Phi(z)$ | $\Phi(1{,}96) = 0{,}9750$ ; $\Phi(1{,}645) \approx 0{,}95$ |
| **A.2** | Quantiles $\mathcal{N}(0,1)$ | Table 2° : $z_\alpha = \Phi^{-1}(\alpha)$ ; Table 3° (bis) : $z_{1-\alpha/2}$ tel que $P(\|Z\| \ge z_{1-\alpha/2}) = \alpha$ | $z_{0{,}95} = 1{,}6449$ ; $z_{0{,}975} = 1{,}9600$ ; $z_{0{,}995} = 2{,}5758$ |
| **B** | Pearson $\chi^2(\nu)$ | Donne $k_{1-\alpha}$ tel que $P(X \ge k_{1-\alpha}) = \alpha$ (aire **à droite**) | $\nu=1, \alpha=0{,}05 \implies 3{,}8415$ ; $\nu=9, \alpha=0{,}975 \text{ vs } 0{,}025 \implies 2{,}7004 \text{ et } 19{,}0228$ |
| **C** | Student $t(\nu)$ | Donne $t_{1-\alpha/2}$ tel que $P(\|T\| \ge t_{1-\alpha/2}) = \alpha$ (risque **bilatéral** en tête de colonne) | $\nu=9, \alpha=0{,}05 \implies 2{,}2622$ ; $\nu=\infty, \alpha=0{,}05 \implies 1{,}9600$ |
| **D.1 / D.2** | Fisher-Snedecor $\mathcal{F}(\nu_1, \nu_2)$ | Donne $f_{1-\alpha}$ tel que $P(F \ge f_{1-\alpha}) = \alpha$ ($\nu_1$ en colonne, $\nu_2$ en ligne). D.1 : $\alpha=0{,}05$ ; D.2 : $\alpha=0{,}025$ | D.1 $(2, 12) \implies 3{,}89$ ; $(3, 20) \text{ non listé ici (D.1 : } 3{,}10)$, D.1 $(6,40) \implies 2{,}34$ |
