---
type: note-cours
created: 2026-11-23
matiere: "Statistiques Inférentielles"
chapitre: "06 - Corrélation et Régression Linéaire"
enseignant: "K. E. HOVI"
tags:
  - etudes
  - cours
  - statistiques-inferentielles
  - correlation
  - pearson
  - spearman
  - regression-lineaire
  - mco
  - active-recall
parent: "[[MOC_Statistiques_Inferentielles]]"
---

# 📖 06. Corrélation et Régression Linéaire

> **Matière :** [[MOC_Statistiques_Inferentielles|Statistiques Inférentielles (M1 IT)]] • **Date :** 23 Novembre 2026 • **Statut :** Synthétisé & Prêt pour révision active

---

## 🎯 1. Idées Clés & Thèses Centrales
Ce dernier chapitre passe de la détection d'une liaison statistique à la modélisation prédictive pour le pilotage décisionnel IT :
- **Inspection visuelle préalable :** Le **nuage de points** est obligatoire avant tout calcul pour détecter la forme de la relation, la dispersion et les *outliers*.
- **Pearson ($r$) vs Spearman ($\rho$) :** Pearson mesure l'intensité d'une liaison **strictement linéaire** (sensible aux *outliers*), tandis que Spearman mesure toute relation **monotone** via les rangs. Dans tous les cas, **corrélation $\ne$ causalité** (attention aux variables de confusion).
- **Moindres Carrés Ordinaires (MCO) :** La droite $\hat{Y} = b_0 + b_1 X$ minimise $\sum e_i^2$, passe par le point moyen $(\overline{X}, \overline{Y})$ et explique une fraction $R^2 = r^2$ de la variance totale de $Y$.
- **Prédire avec discernement :** Distinguer l'**Intervalle de Confiance** (pour la moyenne $E[Y \mid X_0]$) de l'**Intervalle de Prédiction** (toujours plus large, pour une observation individuelle $Y_0$), et proscrire toute **extrapolation** hors $[X_{\min}, X_{\max}]$.

---

## 📝 2. Contenu Structuré & Démonstrations

### A. Analyse de la Corrélation : Pearson ($r$) vs Spearman ($\rho$)

| Critère de choix | Coefficient de Pearson ($r$) | Coefficient de Spearman ($\rho$ ou $r_s$) |
| :--- | :--- | :--- |
| **Type de variables** | Quantitatives continues (intervalle/ratio) | Ordinales ou quantitatives |
| **Forme de la relation** | Strictement **linéaire** | **Monotone** (linéaire ou courbe croissante/décroissante) |
| **Sensibilité aux *outliers*** | Très sensible (résultats faussés) | Robuste (travaille sur les rangs) |
| **Hypothèse de normalité** | Normalité bivariée (ou $n \ge 30$) | Aucune (test non paramétrique) |
| **Formule** | $r = \dfrac{\text{Cov}(X, Y)}{s_X s_Y} = \dfrac{\sum (x_i-\bar{x})(y_i-\bar{y})}{\sqrt{\sum(x_i-\bar{x})^2}\sqrt{\sum(y_i-\bar{y})^2}}$ | $\rho = 1 - \dfrac{6\sum_{i=1}^n d_i^2}{n(n^2 - 1)}$ avec $d_i = \text{rg}(x_i) - \text{rg}(y_i)$ |

**Grille de lecture de $|r|$ :** $1$ (parfaite) ; $[0{,}7; 1[$ (forte) ; $[0{,}3; 0{,}7[$ (modérée) ; $< 0{,}3$ (faible ou nulle).

**Commandes R standards :**
```r
plot(data$X, data$Y, main = "Nuage de points", xlab = "X", ylab = "Y")
cor.test(data$X, data$Y, method = "pearson")
cor.test(data$X, data$Y, method = "spearman")
```

---

### B. Significativité Statistique d'une Corrélation

On teste $H_0 : \rho = 0$ (aucun lien linéaire dans la population) contre $H_1 : \rho \ne 0$.
Sous $H_0$, la statistique suit une **loi de Student à $n - 2$ degrés de liberté** :
$$t = r\sqrt{\frac{n - 2}{1 - r^2}} \sim t(n - 2)$$
Si $p\text{-value} < \alpha$ (ou $|t| > t_{n-2, 1-\alpha/2}$), on rejette $H_0$.

> [!IMPORTANT] Piège de l'effet de taille d'échantillon ($n$)
> - **Petit $n$ ($n < 10$) :** Un $r$ élevé (ex. $0{,}80$) peut s'avérer **non significatif**.
> - **Big Data ($n > 100\,000$) :** Un $r$ minuscule (ex. $0{,}05$) sera presque toujours statistiquement significatif, **sans aucun impact métier**. Toujours distinguer significativité statistique et taille d'effet ($r$ ou $R^2$).

---

### C. Régression Linéaire Simple par Moindres Carrés Ordinaires (MCO)

Modèle estimé : $\hat{Y} = b_0 + b_1 X$, avec résidu $e_i = Y_i - \hat{Y}_i$.
La méthode MCO minimise la somme des carrés des résidus $\min_{b_0, b_1} \sum_{i=1}^n (Y_i - b_0 - b_1 X_i)^2$.
En annulant les dérivées partielles par rapport à $b_0$ et $b_1$, on obtient les estimateurs optimaux :
$$b_1 = \frac{\text{Cov}(X, Y)}{s_X^2} = r_{X,Y} \cdot \left(\frac{s_Y}{s_X}\right), \qquad b_0 = \overline{Y} - b_1 \overline{X}$$

**Interprétation métier :**
- **Pente $b_1$ :** Variation moyenne attendue de $Y$ lorsque $X$ augmente de **1 unité** (ex. $+3{,}5$ ms de latence par utilisateur connecté supplémentaire).
- **Ordonnée à l'origine $b_0$ :** Valeur prédite de $Y$ à vide ($X = 0$). Interprétable **uniquement** si $X = 0$ a un sens métier et appartient (ou est proche) de la plage $[X_{\min}, X_{\max}]$.

---

### D. Évaluation du Modèle, Test de la Pente et Prédiction

#### 1. Coefficient de détermination $R^2$
Décomposition de la variance totale : $\text{SCT} = \text{SCE} + \text{SCR}$ (Somme des Carrés Totale = Expliquée + Résiduelle).
$$R^2 = \frac{\text{SCE}}{\text{SCT}} = 1 - \frac{\text{SCR}}{\text{SCT}}$$
En régression linéaire simple, **$R^2 = r^2$**. Il indique le pourcentage de variabilité de $Y$ expliqué par $X$ (le complément $1 - R^2$ provient des facteurs non modélisés et du bruit résiduel).

#### 2. Test de significativité de la pente ($H_0 : \beta_1 = 0$)
$$t = \frac{b_1}{s_{b_1}} \sim t(n - 2)$$
*(Note : en régression simple, ce test donne exactement la même $t$-statistique et la même $p$-value que le test de significativité du coefficient de corrélation $r$.)*

#### 3. Prédiction ponctuelle, IC vs IP et Extrapolation
Pour une nouvelle valeur $X_0$, la prédiction ponctuelle vaut $\hat{Y}_0 = b_0 + b_1 X_0$.

| Caractéristique | Intervalle de Confiance (IC) | Intervalle de Prédiction (IP) |
| :--- | :--- | :--- |
| **Cible** | Moyenne conditionnelle $E[Y \mid X_0]$ | Valeur individuelle future $Y_0$ |
| **Sources d'incertitude** | Incertitude sur $(b_0, b_1)$ uniquement | Incertitude sur $(b_0, b_1)$ **+** variance résiduelle $\sigma^2$ |
| **Largeur** | Plus étroit | **Toujours plus large** que l'IC |
| **Usage IT** | Estimer la latence *moyenne* mensuelle | Borner la latence d'une requête *spécifique* / budget client |

> [!CAUTION] Danger de l'extrapolation
> Hors de la plage d'apprentissage $[X_{\min}, X_{\max}]$, la relation linéaire peut s'effondrer (seuils de saturation serveur, non-linéarités). Ne jamais extrapoler aveuglément loin des données observées.

---

## 🧠 3. Batterie d'Active Recall (Questions d'Auto-Évaluation)

- [ ] **Q1 : Pourquoi dit-on qu'une droite de régression MCO passe toujours par le point moyen $(\overline{X}, \overline{Y})$ ?**
  - *Réponse flash :* Parce que par construction $b_0 = \overline{Y} - b_1 \overline{X}$, ce qui entraîne $\hat{Y}(\overline{X}) = b_0 + b_1 \overline{X} = \overline{Y}$. De plus, la somme des résidus $\sum e_i$ est toujours nulle.
- [ ] **Q2 : Si $R^2 = 0{,}81$ et la pente de régression est $b_1 = -2{,}4$, combien vaut le coefficient de corrélation de Pearson $r$ ?**
  - *Réponse flash :* Comme $R^2 = r^2$ en régression simple, $|r| = \sqrt{0{,}81} = 0{,}90$. Puisque la pente $b_1$ est négative ($b_1 = r \frac{s_Y}{s_X}$), $r$ a le signe de $b_1$ : **$r = -0{,}90$**.
- [ ] **Q3 : Un client demande la fourchette exacte de sa prochaine facture mensuelle Cloud. Lui fournit-on l'IC ou l'IP ? Pourquoi ?**
  - *Réponse flash :* L'**Intervalle de Prédiction (IP)** (toujours plus large), car on prédit une réalisation individuelle future ($Y_0 = \hat{Y}_0 + \varepsilon_0$) qui cumule l'incertitude de la droite estimée et la variabilité aléatoire propre à ce client.
- [ ] **Q4 : Que faut-il vérifier visuellement avant d'interpréter un coefficient de Pearson $r = 0{,}05$ ?**
  - *Réponse flash :* Tracer le nuage de points ! Un $r \approx 0$ peut masquer une relation forte mais **non linéaire** (par exemple parabolique / en U), ou être dégradé par une seule valeur aberrante (*outlier*).

---

## ⚡ 4. Devoirs, Lectures & Prochaines Actions
- [ ] Résoudre la [[TD3_Regression_Lineaire|Feuille TD 3 (Exercices 1 à 5)]].
- [ ] Passer à la pratique sous R avec [[TP1_Utilisation_du_Logiciel_R|TP 1 : Utilisation du logiciel R]].
