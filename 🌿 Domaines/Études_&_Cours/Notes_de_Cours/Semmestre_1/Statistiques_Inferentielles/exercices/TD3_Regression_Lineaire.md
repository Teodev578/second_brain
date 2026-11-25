---
type: note-cours
created: 2026-11-23
matiere: "Statistiques Inférentielles"
chapitre: "TD 3 - Corrélation et Régression Linéaire"
enseignant: "K. E. HOVI"
tags:
  - etudes
  - td
  - statistiques-inferentielles
  - correlation
  - pearson
  - regression-lineaire
  - mco
parent: "[[MOC_Statistiques_Inferentielles]]"
---

# 📝 TD 3. Corrélation et Régression Linéaire

> **Matière :** [[MOC_Statistiques_Inferentielles|Statistiques Inférentielles (M1 IT)]] • **Support :** Feuille d'exercices n° 3 (p. 54–56) • **Statut :** Entièrement Résolu & Démontré • 🧰 [[TD3_Formules_et_Explications_Terre_a_Terre|Guide Formules & Explications Terre à Terre]]

---

## 📌 Exercice 1 – Analyse de la charge serveur et du temps de réponse

> [!question] Énoncé résumé & Données
> On mesure sur $n = 5$ paliers le nombre de requêtes simultanées $X_i$ et le temps de réponse serveur $Y_i$ (en ms) : $(100, 150)$, $(200, 250)$, $(300, 310)$, $(400, 400)$, $(500, 490)$. On demande les moyennes, variances, covariance et le coefficient de corrélation de Pearson $r$.

### 1. Moyennes $\overline{X}$ et $\overline{Y}$
$$\overline{X} = \frac{100 + 200 + 300 + 400 + 500}{5} = \frac{1\,500}{5} = \mathbf{300\text{ requêtes}}$$
$$\overline{Y} = \frac{150 + 250 + 310 + 400 + 490}{5} = \frac{1\,600}{5} = \mathbf{320\text{ ms}}$$

### 2. Variances, écarts-types et covariance

| $i$ | $X_i$ | $Y_i$ | $X_i - 300$ | $(X_i - 300)^2$ | $Y_i - 320$ | $(Y_i - 320)^2$ | $(X_i - 300)(Y_i - 320)$ |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | $100$ | $150$ | $-200$ | $40\,000$ | $-170$ | $28\,900$ | $34\,000$ |
| 2 | $200$ | $250$ | $-100$ | $10\,000$ | $-70$ | $4\,900$ | $7\,000$ |
| 3 | $300$ | $310$ | $0$ | $0$ | $-10$ | $100$ | $0$ |
| 4 | $400$ | $400$ | $+100$ | $10\,000$ | $+80$ | $6\,400$ | $8\,000$ |
| 5 | $500$ | $490$ | $+200$ | $40\,000$ | $+170$ | $28\,900$ | $34\,000$ |
| **Total ($\sum$)** | **$1\,500$** | **$1\,600$** | **$0$** | **$100\,000$** | **$0$** | **$69\,200$** | **$83\,000$** |

Selon la convention empirique (diviseur $n = 5$) :
$$s_X^2 = \frac{100\,000}{5} = \mathbf{20\,000}, \qquad s_X = \sqrt{20\,000} \approx \mathbf{141{,}4214}$$
$$s_Y^2 = \frac{69\,200}{5} = \mathbf{13\,840}, \qquad s_Y = \sqrt{13\,840} \approx \mathbf{117{,}6435}$$
$$\text{Cov}(X, Y) = \frac{83\,000}{5} = \mathbf{16\,600}$$
*(Note : avec le diviseur sans biais $n - 1 = 4$, on obtient $s_X^{\prime\,2} = 25\,000$ ($s_X' \approx 158{,}11$), $s_Y^{\prime\,2} = 17\,300$ ($s_Y' \approx 131{,}53$) et $\text{Cov}'(X,Y) = 20\,750$. Le rapport $r$ ci-dessous est strictement identique dans les deux conventions.)*

### 3. Coefficient de corrélation de Pearson $r$
$$r = \frac{\text{Cov}(X, Y)}{s_X \cdot s_Y} = \frac{83\,000}{\sqrt{100\,000 \times 69\,200}} = \frac{16\,600}{141{,}4214 \times 117{,}6435} \approx \mathbf{0{,}9978}$$

### 4. Conclusion sur le lien
> [!success] Conclusion
> $r \approx +0{,}998$ est très proche de $+1$ : il existe une **relation linéaire positive quasi parfaite** entre le nombre de requêtes simultanées et le temps de réponse sur la plage $[100; 500]$ requêtes.

---

## 📌 Exercice 2 – Test de significativité d'une corrélation en cybersécurité

> [!question] Énoncé résumé & Données
> Sur $n = 18$ plages horaires, un analyste SOC observe une corrélation $r = 0{,}52$ entre les connexions échouées et les alertes IDS. On teste si cette corrélation est significative au seuil $\alpha = 5\%$ ($t_{\text{critique}} = 2{,}120$, $p = 0{,}027$).

### 1. Formulation des hypothèses
$$H_0 : \rho = 0 \quad (\text{aucune corrélation linéaire dans la population})$$
$$H_1 : \rho \ne 0 \quad (\text{il existe une corrélation linéaire non nulle})$$

### 2. Calcul de la statistique de test $t$ ($\text{ddl} = n - 2 = 16$)
$$t_{\text{obs}} = r\sqrt{\frac{n - 2}{1 - r^2}} = 0{,}52 \sqrt{\frac{16}{1 - 0{,}52^2}} = 0{,}52 \sqrt{\frac{16}{0{,}7296}} = 0{,}52 \times 4{,}6829 \approx \mathbf{2{,}4351}$$

### 3. Règle de décision et conclusion au seuil $\alpha = 5\%$ ($t_{\text{critique}} = 2{,}120$)
Pour un test bilatéral à $\alpha = 5\%$, on rejette $H_0$ si $|t_{\text{obs}}| > t_{\text{critique}} = 2{,}120$ (région critique $]-\infty; -2{,}120[ \cup ]2{,}120; +\infty[$). Ici $|t_{\text{obs}}| = 2{,}4351 > 2{,}120$, donc **le responsable sécurité rejette $H_0$**.

### 4. Confirmation via la $p$-value ($p = 0{,}027$)
> [!success] Conclusion
> Comme $p = 0{,}027 < \alpha = 0{,}05$ (exact : $0{,}02696$), le rejet de $H_0$ est confirmé : il n'y a que $2{,}7\%$ de chance d'observer $r = 0{,}52$ par pur hasard, ce qui justifie de corréler les règles IDS aux échecs d'authentification (détection de *brute-force*).

---

## 📌 Exercice 3 – Ajustement par MCO et estimation de projet IT

> [!question] Énoncé résumé & Données
> À partir de $n = 5$ projets passés, on relie la taille fonctionnelle $X$ (en Points de Fonction) à la charge de travail $Y$ (en jours-homme) : $\overline{X} = 120$ PF, $\overline{Y} = 450$ j-h, $s_X^2 = 800$, $s_Y^2 = 6\,800$, $\text{Cov}(X,Y) = 2\,200$. On estime le modèle MCO puis la charge pour $X_0 = 150$ PF.

### 1. Pente $b_1$ et ordonnée à l'origine $b_0$
$$b_1 = \frac{\text{Cov}(X, Y)}{s_X^2} = \frac{2\,200}{800} = \mathbf{2{,}75}$$
$$b_0 = \overline{Y} - b_1 \overline{X} = 450 - 2{,}75 \times 120 = 450 - 330 = \mathbf{120}$$

### 2. Équation du modèle estimé
$$\hat{Y} = \mathbf{120 + 2{,}75 X}$$

### 3. Interprétation métier pour le Directeur de Projet IT
**Pente ($b_1 = 2{,}75$) :**
Chaque point de fonction supplémentaire dans le périmètre d'un projet requiert en moyenne **2,75 jours-homme** de charge additionnelle.

**Ordonnée à l'origine ($b_0 = 120$) :**
Charge fixe incompressible de base estimée à **120 jours-homme** (cadrage, mise en place de l'environnement, CI/CD, chefferie de projet) indépendante de la taille fonctionnelle *(à interpréter avec prudence si $X=0$ est loin des tailles observées)*.

### 4. Estimation pour un projet de $X_0 = 150$ points de fonction
$$\hat{Y}(150) = 120 + 2{,}75 \times 150 = 120 + 412{,}5 = \mathbf{532{,}5\text{ jours-homme}}$$

> [!success] Conclusion
> Le modèle $\hat{Y} = 120 + 2{,}75 X$ prévoit une charge totale de **532,5 jours-homme** pour un projet de $150$ points de fonction.

---

## 📌 Exercice 4 – Performance d'un modèle d'optimisation SQL

> [!question] Énoncé résumé & Données
> Une équipe DBA modélise le temps d'exécution de $n = 22$ requêtes SQL complexes en fonction de la taille de la table interrogée ($b_1 > 0$), obtenant $\text{SCT} = 12\,500$ et $\text{SCR} = 2\,750$.

### 1. Somme des Carrés Expliquée (SCE)
$$\text{SCE} = \text{SCT} - \text{SCR} = 12\,500 - 2\,750 = \mathbf{9\,750}$$

### 2. Coefficient de détermination $R^2$
$$R^2 = \frac{\text{SCE}}{\text{SCT}} = \frac{9\,750}{12\,500} = \mathbf{0{,}78} \quad (78\%)$$

### 3. Interprétation métier pour l'équipe DBA
**78% de la variance totale** du temps d'exécution des requêtes complexes est expliquée linéairement par la taille de la table interrogée (en Go), indiquant un fort pouvoir explicatif.

### 4. Coefficient de corrélation de Pearson $r$
En régression simple, $R^2 = r^2 \implies |r| = \sqrt{0{,}78} \approx 0{,}8832$. Comme la pente $b_1$ est positive, $r$ est positif :
$$r = +\sqrt{0{,}78} \approx \mathbf{+0{,}8832}$$

### 5. Signification des 22% non expliqués ($1 - R^2 = 0{,}22$)
> [!success] Conclusion
> Le modèle explique $78\%$ de la variance ($r = +0{,}8832$). Les **$22\%$ restants** correspondent à la variance résiduelle due à d'autres facteurs : sélectivité des clauses `WHERE`, nombre de jointures, fragmentation des index, charge CPU/I/O concurrente ou taux de *cache hit* en RAM.

---

## 📌 Exercice 5 – Prédiction, IC/IP et limites d'un modèle Cloud

> [!question] Énoncé résumé & Données
> Un modèle MCO calibré sur $n = 25$ clients hébergés entre $[10\text{ TO} \,;\, 80\text{ TO}]$ prédit la facture mensuelle (k€) selon $\hat{Y} = 1{,}5 + 0{,}08 X$ ($R^2 = 0{,}85$). Pour $X_0 = 50$ TO, on donne deux intervalles à $95\%$ : $A = [5{,}15 \,;\, 5{,}85]$ et $B = [4{,}30 \,;\, 6{,}70]$. On teste ensuite une prédiction à $X_0 = 500$ TO.

### 1. Estimation ponctuelle pour $X_0 = 50$ TO
$$\hat{Y}_0 = 1{,}5 + 0{,}08 \times 50 = 1{,}5 + 4{,}0 = \mathbf{5{,}5\text{ k€ / mois}}$$

### 2. Identification IC vs IP et choix pour le responsable financier

| Intervalle | Bornes à 95% | Largeur | Nature statistique |
| :---: | :---: | :---: | :--- |
| **A** | $[5{,}15 \,;\, 5{,}85]$ | $0{,}70$ | **Intervalle de Confiance (IC)** du coût *moyen* $E[Y \mid X_0 = 50]$ |
| **B** | $[4{,}30 \,;\, 6{,}70]$ | $2{,}40$ | **Intervalle de Prédiction (IP)** d'une facture *individuelle* |

L'IP intègre la variabilité résiduelle individuelle ($\sigma^2$) en plus de l'erreur d'estimation du modèle $(b_0, b_1)$, ce qui le rend **systématiquement plus large** que l'IC. Pour le responsable financier qui budgète la facture *exacte* d'un client particulier, il faut lui transmettre l'**Intervalle B ($[4{,}30 \,;\, 6{,}70]$ k€)**.

### 3. Projet Big Data massif estimé à $X_0 = 500$ TO
Le calcul mécanique donne :
$$\hat{Y}(500) = 1{,}5 + 0{,}08 \times 500 = \mathbf{41{,}5\text{ k€ / mois}}$$

> [!success] Conclusion
> Pour $50$ TO, la facture attendue est de $\mathbf{5{,}5\text{ k€}}$ avec un IP individuel de **$[4{,}30 \,;\, 6{,}70]$ k€**. En revanche, le chiffre de $41{,}5$ k€ à $500$ TO est **invalide (piège d'extrapolation)** car le modèle n'est calibré que sur $[10\text{ TO} \,;\, 80\text{ TO}]$, bien en deçà des changements de régime tarifaire et d'architecture à $500$ TO.
