---
type: note-cours
created: 2026-11-23
matiere: "Statistiques Inférentielles"
chapitre: "01 - Échantillonnage et Estimations"
enseignant: "K. E. HOVI"
tags:
  - etudes
  - cours
  - statistiques-inferentielles
  - echantillonnage
  - estimation-ponctuelle
  - active-recall
parent: "[[MOC_Statistiques_Inferentielles]]"
---

# 📖 01. Échantillonnage et Estimations

> **Matière :** [[MOC_Statistiques_Inferentielles|Statistiques Inférentielles (M1 IT)]] • **Date :** 23 Novembre 2026 • **Statut :** Synthétisé & Prêt pour révision active

---

## 🎯 1. Idées Clés & Thèses Centrales
Ce premier chapitre pose le passage de l'observation brute à la modélisation probabiliste :
- **Dualité échantillon / données :** Un échantillon $(X_1, \dots, X_n)$ est un vecteur de variables aléatoires **iid** (indépendantes et identiquement distribuées), tandis que la série mesurée $(x_1, \dots, x_n)$ n'en est qu'une réalisation particulière.
- **Paramétrique vs Non-paramétrique :** Un modèle paramétrique ($\Theta \subseteq \mathbb{R}^d$, ex. loi normale, Poisson) est précis mais risqué si l'hypothèse de loi est fausse ; un modèle non-paramétrique est moins précis mais robuste.
- **Lois d'échantillonnage et TCL :** Quelle que soit la loi mère de $X$ (de variance finie $\sigma^2$), la moyenne empirique $\overline{X}$ est sans biais ($E(\overline{X})=\mu$) et converge en loi vers $\mathcal{N}(\mu, \sigma^2/n)$ lorsque $n$ est grand ($n \ge 30$).
- **Arbitrage Biais / Variance (EQM) :** La qualité globale d'un estimateur $T$ de $\theta$ se mesure par l'erreur quadratique moyenne : $\text{EQM}(T) = \text{Var}(T) + b_\theta(T)^2$.

---

## 📝 2. Contenu Structuré & Démonstrations

### A. Modèle d'échantillonnage et Statistique
- **Échantillon iid :** $(X_1, \dots, X_n)$ variables indépendantes de même loi parente $X$ sur un espace probabilisé $(\Omega, P)$.
- **Modèle statistique $\mathcal{M}$ :** Ensemble des lois possibles pour les observations.
  - *Paramétrique :* $\mathcal{M} = \{\mu_\theta, \theta \in \Theta\}$ avec $\Theta \subseteq \mathbb{R}^d$ (dimension finie : $\mathcal{N}(\mu, \sigma^2)$, $\mathcal{P}(\lambda)$, $\mathcal{E}(\lambda)$).
  - *Non-paramétrique :* Pas de paramétrisation en dimension finie (ex. « loi continue à densité », « loi symétrique autour de 0 »).
- **Statistique :** Toute fonction mesurable connue de l'échantillon $T_n = T_n(X_1, \dots, X_n)$. C'est une **variable aléatoire** dont on observe une réalisation numérique $t_n = T_n(x_1, \dots, x_n)$.

---

### B. Moyenne Empirique, Variance Empirique et Fréquence

#### 1. Moyenne empirique $\overline{X}$
$$\overline{X} = \frac{1}{n}\sum_{i=1}^n X_i$$

> [!IMPORTANT] Théorème 1.1.1 — Espérance, Variance et Convergence (TCL)
> Si $X_1, \dots, X_n$ sont iid de moyenne $\mu$ et d'écart-type $\sigma$, alors :
> $$E(\overline{X}) = \mu, \qquad V(\overline{X}) = \frac{\sigma^2}{n}$$
> De plus, par le Théorème Central Limite (TCL), $\overline{X} \xrightarrow{\mathcal{L}} \mathcal{N}\!\left(\mu, \frac{\sigma^2}{n}\right)$ quand $n \to +\infty$ (en pratique, approximation valide dès $n \ge 30$).

**Démonstration :**
- Linéarité de l'espérance : $E(\overline{X}) = \frac{1}{n}\sum_{i=1}^n E(X_i) = \frac{1}{n}(n\mu) = \mu$.
- Indépendance des $X_i$ : $V(\overline{X}) = \frac{1}{n^2}\sum_{i=1}^n V(X_i) = \frac{1}{n^2}(n\sigma^2) = \frac{\sigma^2}{n}$. $\blacksquare$

#### 2. Variance empirique $\overline{S}^2$ vs Variance corrigée $S^2$
- **Variance empirique (biaisée) :** $\overline{S}^2 = \frac{1}{n}\sum_{i=1}^n (X_i - \overline{X})^2$, d'espérance $E(\overline{S}^2) = \frac{n-1}{n}\sigma^2$.
- **Variance corrigée (sans biais) :**
  $$S^2 = \frac{n}{n-1}\overline{S}^2 = \frac{1}{n-1}\sum_{i=1}^n (X_i - \overline{X})^2, \qquad E(S^2) = \sigma^2$$

> [!WARNING] Vigilance — Coquilles d'impression dans le polycopié (p. 5)
> Dans le Théorème 1.1.2 du support PDF :
> 1. La variance exacte de $\overline{S}^2$ comporte un facteur $\frac{1}{n^3}$ (et non $\frac{1}{n}$) : $V(\overline{S}^2) = \frac{n-1}{n^3}\left[(n-1)\mu_4 - (n-3)\sigma^4\right]$.
> 2. À l'infini, l'équivalent est $V(\overline{S}^2) \sim \frac{\mu_4 - \sigma^4}{n}$ (et non $\sigma^3$ ; la Remarque 1.1.2 donne d'ailleurs le bon terme $\sqrt{\mu_4 - \sigma^4}$).

#### 3. Fréquence empirique $F$
Si $X_i \sim \text{Bernoulli}(p)$, alors $nF = \sum_{i=1}^n X_i \sim \mathcal{B}(n, p)$ et :
$$F = \frac{X_1 + \dots + X_n}{n}, \qquad E(F) = p, \qquad \text{Var}(F) = \frac{pq}{n} \quad (q = 1-p)$$
Lorsque $n \to +\infty$, $F \xrightarrow{\mathcal{L}} \mathcal{N}\!\left(p, \frac{pq}{n}\right)$.

---

### C. Qualités d'un Estimateur Ponctuel

Soit $T = T(X_1, \dots, X_n)$ un estimateur d'un paramètre inconnu $\theta$.

1. **Biais :** $b_\theta(T) = E(T) - \theta$.
   - $T$ est **sans biais** si $\forall \theta, \, E(T) = \theta \iff b_\theta(T) = 0$.
   > [!WARNING] Coquille du polycopié (Définition 1.2.1, p. 6)
   > Le support écrit « sans biais si $E(T) = 0$ » : il faut lire **$E(T) = \theta$** (c'est le biais $b_\theta(T)$ qui vaut $0$).
2. **Convergence en moyenne / Asymptotiquement sans biais :** $\lim_{n \to +\infty} E(T) = \theta$.
3. **Consistance (convergence en probabilité) :** $T \xrightarrow{P} \theta$ quand $n \to +\infty$.
   - *Critère suffisant (Théorème 1.2.1) :* Si $\lim_{n\to\infty} E(T) = \theta$ et $\lim_{n\to\infty} \text{Var}(T) = 0$, alors $T$ est **consistant**.
4. **Erreur Quadratique Moyenne (EQM / Risque quadratique) :**
   $$\text{EQM}(T) = E\big((T - \theta)^2\big) = \text{Var}(T) + \big[E(T) - \theta\big]^2 = \text{Var}(T) + b_\theta(T)^2$$
   **Preuve (Théorème 1.2.2) :** En écrivant $T - \theta = [T - E(T)] + [E(T) - \theta]$ et en développant le carré, le double produit $2[E(T) - \theta]\,E[T - E(T)]$ est nul car $E[T - E(T)] = 0$. $\blacksquare$
5. **Efficacité :** Entre deux estimateurs sans biais, le plus **efficace** est celui qui possède la **variance minimale**.

#### Tableau récapitulatif des estimateurs classiques

| Paramètre cible | Estimateur | Formule | Sans biais ? | Consistant ? | Remarque |
| :--- | :--- | :--- | :---: | :---: | :--- |
| Espérance $\mu$ | $\overline{X}$ | $\frac{1}{n}\sum X_i$ | Oui | Oui | Variance $\sigma^2/n \to 0$ |
| Variance $\sigma^2$ ($\mu$ inconnue) | $\overline{S}^2$ | $\frac{1}{n}\sum (X_i - \overline{X})^2$ | **Non** ($\frac{n-1}{n}\sigma^2$) | Oui | Sous-estime $\sigma^2$ en moyenne |
| Variance $\sigma^2$ ($\mu$ inconnue) | $S^2$ | $\frac{1}{n-1}\sum (X_i - \overline{X})^2$ | **Oui** | Oui | Estimateur usuel corrigé |
| Variance $\sigma^2$ ($\mu$ connue) | $V^2$ | $\frac{1}{n}\sum (X_i - \mu)^2$ | **Oui** | Oui | Meilleur que $S^2$ si $\mu$ est connue |
| Proportion $p$ | $F$ | $\frac{1}{n}\sum X_i$ | **Oui** | Oui | Variance $p(1-p)/n \to 0$ |

---

## 🧠 3. Batterie d'Active Recall (Questions d'Auto-Évaluation)

- [ ] **Q1 : Quelle est la différence conceptuelle entre un estimateur $T$ et une estimation $t$ ?**
  - *Réponse flash :* L'estimateur $T = T(X_1, \dots, X_n)$ est une **variable aléatoire** (fonction de l'échantillon aléatoire) qui possède une loi, une moyenne et une variance. L'estimation $t = T(x_1, \dots, x_n)$ est une **valeur numérique fixe** calculée sur les données observées.
- [ ] **Q2 : Pourquoi divise-t-on par $n - 1$ dans $S^2$ plutôt que par $n$ lorsque $\mu$ est inconnue ?**
  - *Réponse flash :* Car $E(\overline{S}^2) = \frac{n-1}{n}\sigma^2 < \sigma^2$ : mesurer les écarts autour de la moyenne empirique $\overline{X}$ (et non de la vraie moyenne $\mu$) réduit mécaniquement la somme des carrés (perte d'un degré de liberté). Multiplier par $\frac{n}{n-1}$ supprime ce biais.
- [ ] **Q3 : Quelle est la décomposition de l'EQM et que signifie chaque terme ?**
  - *Réponse flash :* $\text{EQM}(T) = \text{Var}(T) + [E(T) - \theta]^2$. Le premier terme mesure la dispersion due aux fluctuations d'échantillonnage (variance) ; le second mesure l'erreur systématique au carré ($\text{biais}^2$).
- [ ] **Q4 : Sous quelles conditions simples un estimateur biaisé pour $n$ fini reste-t-il utilisable en grand échantillon ?**
  - *Réponse flash :* S'il est asymptotiquement sans biais ($\lim_{n\to\infty} E(T) = \theta$) et que $\lim_{n\to\infty}\text{Var}(T) = 0$ : il est alors **consistant** (ex. $\overline{S}^2$).

---

## ⚡ 4. Devoirs, Lectures & Prochaines Actions
- [ ] Mettre en pratique sur la [[TD1_Echantillonnage_et_Estimations|Feuille TD 1 (Exercices 1 à 4 et 8)]].
- [ ] Enchaîner avec le chapitre [[02_Intervalles_de_Confiance|02. Les Intervalles de Confiance]].
