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

> **Matière :** [[MOC_Statistiques_Inferentielles|Statistiques Inférentielles (M1 IT)]] • **Support :** Feuille d'exercices n° 3 (p. 54–56) • **Statut :** Entièrement Résolu & Démontré

---

## 📌 Exercice 1 – Analyse de la charge serveur et du temps de réponse

Données ($n = 5$) : $(100, 150)$, $(200, 250)$, $(300, 310)$, $(400, 400)$, $(500, 490)$.

### 1. Moyennes $\overline{X}$ et $\overline{Y}$
$$\overline{X} = \frac{100 + 200 + 300 + 400 + 500}{5} = \frac{1500}{5} = \mathbf{300\text{ requêtes}}$$
$$\overline{Y} = \frac{150 + 250 + 310 + 400 + 490}{5} = \frac{1600}{5} = \mathbf{320\text{ ms}}$$

### 2. Variances, écarts-types et covariance
Tableau des écarts centrés :

| $i$ | $X_i - 300$ | $(X_i - 300)^2$ | $Y_i - 320$ | $(Y_i - 320)^2$ | $(X_i - 300)(Y_i - 320)$ |
| :-: | :---: | :---: | :---: | :---: | :---: |
| 1 | $-200$ | $40\,000$ | $-170$ | $28\,900$ | $34\,000$ |
| 2 | $-100$ | $10\,000$ | $-70$ | $4\,900$ | $7\,000$ |
| 3 | $0$ | $0$ | $-10$ | $100$ | $0$ |
| 4 | $+100$ | $10\,000$ | $+80$ | $6\,400$ | $8\,000$ |
| 5 | $+200$ | $40\,000$ | $+170$ | $28\,900$ | $34\,000$ |
| **$\sum$** | **$0$** | **$100\,000$** | **$0$** | **$69\,200$** | **$83\,000$** |

- **Convention empirique (diviseur $n = 5$) :**
  - $s_X^2 = \frac{100\,000}{5} = \mathbf{20\,000}$, $s_X = \sqrt{20\,000} \approx \mathbf{141{,}4214}$.
  - $s_Y^2 = \frac{69\,200}{5} = \mathbf{13\,840}$, $s_Y = \sqrt{13\,840} \approx \mathbf{117{,}6435}$.
  - $\text{Cov}(X, Y) = \frac{83\,000}{5} = \mathbf{16\,600}$.
- *(Note : avec le diviseur sans biais $n - 1 = 4$, on obtient $s_X^{\prime\,2} = 25\,000$ ($s_X' \approx 158{,}11$), $s_Y^{\prime\,2} = 17\,300$ ($s_Y' \approx 131{,}53$) et $\text{Cov}'(X,Y) = 20\,750$. Le rapport $r$ ci-dessous est strictement identique dans les deux conventions.)*

### 3. Coefficient de corrélation de Pearson $r$
$$r = \frac{\text{Cov}(X, Y)}{s_X \cdot s_Y} = \frac{83\,000}{\sqrt{100\,000 \times 69\,200}} = \frac{16\,600}{141{,}4214 \times 117{,}6435} \approx \mathbf{0{,}9978}$$

### 4. Conclusion sur le lien
$r \approx +0{,}998$ est très proche de $+1$ : il existe une **relation linéaire positive quasi parfaite** entre le nombre de requêtes simultanées et le temps de réponse sur la plage $[100; 500]$ requêtes (chaque montée en charge augmente proportionnellement la latence).

---

## 📌 Exercice 2 – Test de significativité d'une corrélation en cybersécurité

Données : $n = 18$ plages horaires, $r = 0{,}52$.

### 1. Formulation des hypothèses
- $H_0 : \rho = 0$ (aucune corrélation linéaire dans la population entre connexions échouées et alertes IDS ; $r = 0{,}52$ dû au hasard).
- $H_1 : \rho \ne 0$ (il existe une corrélation linéaire non nulle dans la population).

### 2. Calcul de la statistique de test $t$ ($\text{ddl} = n - 2 = 16$)
$$t_{\text{obs}} = r\sqrt{\frac{n - 2}{1 - r^2}} = 0{,}52 \sqrt{\frac{16}{1 - 0{,}52^2}} = 0{,}52 \sqrt{\frac{16}{0{,}7296}} = 0{,}52 \times 4{,}6829 \approx \mathbf{2{,}4351}$$

### 3. Règle de décision et conclusion au seuil $\alpha = 5\%$ ($t_{\text{critique}} = 2{,}120$)
- **(a) Règle de décision :** Pour un test bilatéral à $\alpha = 5\%$, on rejette $H_0$ si $|t_{\text{obs}}| > t_{\text{critique}} = 2{,}120$ (région critique $]-\infty; -2{,}120[ \cup ]2{,}120; +\infty[$).
- **(b) Décision :** $|t_{\text{obs}}| = 2{,}4351 > 2{,}120$ $\implies$ **le responsable sécurité rejette $H_0$**. La corrélation positive modérée ($r = 0{,}52$) entre tentatives de connexion échouées et alertes IDS est statistiquement significative.

### 4. Confirmation via la $p$-value ($p = 0{,}027$)
La $p$-value calculée vaut $0{,}027 < \alpha = 0{,}05$ (calcul exact : $0{,}02696$), ce qui **confirme le rejet de $H_0$**. Pour le comité de direction IT : la probabilité d'observer une telle corrélation par pur hasard s'il n'existait aucun lien est seulement de $2{,}7\%$. Le signal est donc statistiquement crédible et justifie de corréler les règles d'alerte IDS aux échecs d'authentification (détection de *brute-force*).

---

## 📌 Exercice 3 – Ajustement par MCO et estimation de projet IT

Statistiques sommaires ($n = 5$) : $\overline{X} = 120$ PF, $\overline{Y} = 450$ j-h, $s_X^2 = 800$, $s_Y^2 = 6800$, $\text{Cov}(X,Y) = 2200$.

### 1. Pente $b_1$ et ordonnée à l'origine $b_0$
$$b_1 = \frac{\text{Cov}(X, Y)}{s_X^2} = \frac{2200}{800} = \mathbf{2{,}75}$$
$$b_0 = \overline{Y} - b_1 \overline{X} = 450 - 2{,}75 \times 120 = 450 - 330 = \mathbf{120}$$

### 2. Équation du modèle estimé
$$\hat{Y} = \mathbf{120 + 2{,}75 X}$$

### 3. Interprétation métier pour le Directeur de Projet IT
- **$b_1 = 2{,}75$ :** Chaque point de fonction supplémentaire dans le périmètre d'un projet requiert en moyenne **2,75 jours-homme** de charge de développement additionnelle.
- **$b_0 = 120$ :** Charge fixe incompressibles de base estimée à **120 jours-homme** (cadrage, mise en place de l'environnement, CI/CD, chefferie de projet) indépendante de la taille fonctionnelle *(à interpréter avec prudence si $X=0$ est loin des tailles de projets observées)*.

### 4. Estimation pour un projet de $X_0 = 150$ points de fonction
$$\hat{Y}(150) = 120 + 2{,}75 \times 150 = 120 + 412{,}5 = \mathbf{532{,}5\text{ jours-homme}}$$

---

## 📌 Exercice 4 – Performance d'un modèle d'optimisation SQL

Données ($n = 22$ requêtes) : $\text{SCT} = 12\,500$, $\text{SCR} = 2\,750$.

### 1. Somme des Carrés Expliquée (SCE)
$$\text{SCE} = \text{SCT} - \text{SCR} = 12\,500 - 2\,750 = \mathbf{9\,750}$$

### 2. Coefficient de détermination $R^2$
$$R^2 = \frac{\text{SCE}}{\text{SCT}} = \frac{9\,750}{12\,500} = \mathbf{0{,}78} \quad (78\%)$$

### 3. Interprétation métier pour l'équipe DBA
**78% de la variance totale** du temps d'exécution des requêtes complexes est expliquée linéairement par la taille de la table interrogée (en Go). Le modèle a donc un fort pouvoir explicatif.

### 4. Coefficient de corrélation de Pearson $r$
En régression simple, $R^2 = r^2 \implies |r| = \sqrt{0{,}78} \approx 0{,}8832$. Comme la pente $b_1$ est positive, $r$ est du même signe :
$$r = +\sqrt{0{,}78} \approx \mathbf{+0{,}8832}$$

### 5. Signification des 22% non expliqués ($1 - R^2 = 0{,}22$)
Ces 22% correspondent à la **variance résiduelle** liée à d'autres facteurs non pris en compte par la seule taille de la table : sélectivité des clauses `WHERE`, nombre de jointures, fragmentation des index, charge CPU/I/O concurrente du serveur SGBD, taux de *cache hit* en RAM, etc.

---

## 📌 Exercice 5 – Prédiction, IC/IP et limites d'un modèle Cloud

Modèle MCO ($n = 25$, plage observée $[10\text{ TO} \,;\, 80\text{ TO}]$) : $\hat{Y} = 1{,}5 + 0{,}08 X$ ($R^2 = 0{,}85$).
Pour $X_0 = 50$ TO, intervalles à 95% : $A = [5{,}15 \,;\, 5{,}85]$ et $B = [4{,}30 \,;\, 6{,}70]$.

### 1. Estimation ponctuelle pour $X_0 = 50$ TO
$$\hat{Y}_0 = 1{,}5 + 0{,}08 \times 50 = 1{,}5 + 4{,}0 = \mathbf{5{,}5\text{ k€ / mois}}$$

### 2. Identification IC vs IP et choix pour le responsable financier
- **(a) Identification :**
  - **Intervalle A ($[5{,}15 \,;\, 5{,}85]$, largeur $0{,}70$)** = **Intervalle de Confiance (IC)** du coût *moyen* $E[Y \mid X_0 = 50]$.
  - **Intervalle B ($[4{,}30 \,;\, 6{,}70]$, largeur $2{,}40$)** = **Intervalle de Prédiction (IP)** individuel.
  - *Justification :* L'IP intègre la variabilité résiduelle individuelle ($\sigma^2$) en plus de l'erreur d'estimation du modèle $(b_0, b_1)$, ce qui le rend **systématiquement plus large** que l'IC.
- **(b) Recommandation au responsable financier :** Lui transmettre l'**Intervalle B ($[4{,}30 \,;\, 6{,}70]$ k€)**, car il s'intéresse à la facture *exacte* d'un client particulier (une réalisation individuelle) et non à une moyenne statistique sur de nombreux clients.

### 3. Projet Big Data massif estimé à $X_0 = 500$ TO
- **(a) Prédiction théorique :** $\hat{Y}(500) = 1{,}5 + 0{,}08 \times 500 = \mathbf{41{,}5\text{ k€ / mois}}$.
- **(b) Mise en garde (Piège de l'extrapolation) :** Le modèle n'a été calibré et validé que sur la plage **$[10\text{ TO} \,;\, 80\text{ TO}]$**. Prédire à $500$ TO (plus de 6 fois la borne maximale observée) constitue une **extrapolation extrême et invalide**. À cette échelle, la tarification et l'architecture changent de régime (remises sur volume, changement de classe de stockage, coûts réseau inter-clusters, sharding, saturation ou effets de seuil non linéaires), rendant le chiffre de $41{,}5$ k€ totalement peu fiable.
