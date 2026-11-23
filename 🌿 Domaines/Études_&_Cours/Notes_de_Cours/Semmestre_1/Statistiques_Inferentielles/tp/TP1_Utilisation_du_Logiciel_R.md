---
type: note-cours
created: 2026-11-23
matiere: "Statistiques Inférentielles"
chapitre: "TP 1 - Utilisation du Logiciel R"
enseignant: "K. E. HOVI"
tags:
  - etudes
  - tp
  - r
  - statistiques-inferentielles
  - anova
  - kruskal-wallis
  - wilcoxon
  - friedman
parent: "[[MOC_Statistiques_Inferentielles]]"
---

# 💻 TP 1. Utilisation du Logiciel R

> **Matière :** [[MOC_Statistiques_Inferentielles|Statistiques Inférentielles (M1 IT)]] • **Support :** Travaux Pratiques n° 1 (p. 58–60) • **Statut :** Scripts R Complets & Résultats Vérifiés

---

## 📌 Exercice 1 – Temps de réponse à un test d'aptitude (Hommes vs Femmes)

### Jeu de données et script R complet
```r
hommes <- c(8.6, 10.9, 7.3, 9.2, 8.5, 9.2, 9.1, 8.9, 10.7, 8.2, 7.1, 9.4, 8.3, 9.7, 9.2)
femmes <- c(8.3, 7.2, 8.7, 6.7, 10.3, 6.8, 9.8, 8.9, 9.6, 8.6, 6.7, 7.5)

# Vérification préalable de la normalité (Shapiro-Wilk)
shapiro.test(hommes)
shapiro.test(femmes)

# 1. Test d'égalité des variances (Fisher-Snedecor)
var.test(hommes, femmes)

# 2. Test de comparaison des moyennes (Student avec variances égales)
t.test(hommes, femmes, var.equal = TRUE)
```

### Résultats numériques & Interprétation ($\alpha = 5\%$)
- **Statistiques descriptives :** Hommes ($n_1 = 15$, $\bar{x}_H = 8{,}9533$ min, $s_H^2 = 1{,}0927$, $s_H = 1{,}0453$) ; Femmes ($n_2 = 12$, $\bar{x}_F = 8{,}2583$ min, $s_F^2 = 1{,}6136$, $s_F = 1{,}2703$).
1. **Égalité des variances (`var.test`) :**
   - Hypothèses : $H_0 : \sigma_H^2 = \sigma_F^2$ vs $H_1 : \sigma_H^2 \ne \sigma_F^2$ (sous normalité des deux échantillons).
   - Statistique : $F_{\text{obs}} = \frac{1{,}0927}{1{,}6136} = \mathbf{0{,}6772}$ ($\text{ddl}_1 = 14$, $\text{ddl}_2 = 11$), **$p\text{-value} = 0{,}4860$**.
   - *Décision :* $p > 0{,}05 \implies$ **on ne rejette pas $H_0$**. Les variances peuvent être considérées comme identiques (homoscédasticité).
2. **Comparaison des performances moyennes (`t.test`) :**
   - Hypothèses : $H_0 : \mu_H = \mu_F$ vs $H_1 : \mu_H \ne \mu_F$.
   - Statistique (Student poolé, $\text{ddl} = 25$) : $t_{\text{obs}} = \mathbf{1{,}5608}$, **$p\text{-value} = 0{,}1311$** *(avec Welch par défaut sous R : $t = 1{,}5264$, $\nu = 21{,}25$, $p = 0{,}1417$)*.
   - *Décision :* $p > 0{,}05 \implies$ **on ne rejette pas $H_0$**. On ne peut pas affirmer qu'il existe une différence réelle de performance moyenne entre les hommes et les femmes au seuil de 5%.

---

## 📌 Exercice 2 – Régimes alimentaires (ANOVA et Kruskal-Wallis)

### Script R complet
```r
# Construction du tableau à 2 colonnes (format long)
taux_de_fer <- c(
  2.23, 1.14, 2.63, 1.00, 1.35, 2.01, 1.64, 1.13, 1.01, # A
  5.59, 0.96, 6.96, 1.23, 1.61, 2.94, 1.96, 3.68, 1.54, # B
  4.50, 3.92, 10.33, 8.23, 2.07, 4.90, 6.84, 6.42, 3.72,# C
  1.35, 1.06, 0.74, 0.96, 1.16, 2.08, 0.69, 0.68, 0.84, # D
  1.40, 1.51, 2.49, 1.74, 1.59, 1.36, 3.00, 4.81, 5.21  # E
)
type_de_regime <- as.factor(rep(c("A", "B", "C", "D", "E"), each = 9))
donnees <- data.frame(X = taux_de_fer, Y = type_de_regime)

# 1. Graphique combiné : 5 boîtes à moustaches + 5 ECDF
par(mfrow = c(1, 2))
boxplot(X ~ Y, data = donnees, col = rainbow(5),
        main = "Boîtes à moustaches par régime",
        xlab = "Régime", ylab = "Taux de fer")

couleurs <- c("black", "blue", "red", "darkgreen", "purple")
plot(ecdf(donnees$X[donnees$Y == "A"]), col = couleurs[1], xlim = range(taux_de_fer),
     main = "Fonctions de répartition empiriques", xlab = "Taux de fer", ylab = "F(x)")
for (i in 2:5) {
  lines(ecdf(donnees$X[donnees$Y == levels(donnees$Y)[i]]), col = couleurs[i])
}
legend("bottomright", legend = levels(donnees$Y), col = couleurs, lty = 1, bty = "n")

# 2a. Test paramétrique (ANOVA) et vérification des hypothèses
modele_aov <- aov(X ~ Y, data = donnees)
shapiro.test(residuals(modele_aov))  # Hypothèse de normalité des résidus
bartlett.test(X ~ Y, data = donnees) # Hypothèse d'homogénéité des variances
summary(modele_aov)

# 2b. Test non paramétrique (Kruskal-Wallis)
kruskal.test(X ~ Y, data = donnees)
```

### Résultats numériques & Conclusions
- **Moyennes par groupe ($n_j = 9, N = 45$) :** $\bar{x}_A = 1{,}5711$, $\bar{x}_B = 2{,}9411$, $\bar{x}_C = 5{,}6589$, $\bar{x}_D = 1{,}0622$, $\bar{x}_E = 2{,}5678$.
- **Hypothèses de l'ANOVA :** (1) indépendance des observations (assignation aléatoire), (2) normalité des données/résidus par groupe, (3) homogénéité des variances entre groupes (note : la dispersion du régime C et de D diffère sensiblement, rendant Kruskal-Wallis particulièrement pertinent).
- **Test paramétrique (`aov`) :** $\text{SC}_{\text{inter}} = 114{,}9229$ ($\text{ddl}=4$, $\text{CM}=28{,}7307$) ; $\text{SC}_{\text{intra}} = 109{,}4346$ ($\text{ddl}=40$, $\text{CM}=2{,}7359$) ; **$F = 10{,}5015$**, **$p\text{-value} = 6{,}53 \times 10^{-6}$**.
- **Test non paramétrique (`kruskal.test`) :** Sommes des rangs $R = [155{,}5;\; 229{,}5;\; 341{,}0;\; 78{,}0;\; 231{,}0]$, **$H = 24{,}6934$** (corrigé pour 2 ex-æquo ; $\text{ddl} = 4$), **$p\text{-value} = 5{,}80 \times 10^{-5}$**.
- **Conclusion :** Les deux tests convergent vers un **rejet très net de $H_0$** ($p < 0{,}001$) : le régime alimentaire influence significativement le taux de fer hépatique (régime C nettement plus élevé, régime D le plus bas).

---

## 📌 Exercice 3 – Données répétées et mesures longitudinales (10 patients, 5 jours)

### Script R complet
```r
mat <- matrix(c(
  124, 88, 130, 115, 92, 80, 101, 98, 132, 85,
  125, 75, 138, 108, 92, 78, 105, 97, 125, 86,
  117, 73, 133, 108, 92, 74, 101, 92, 124, 83,
  123, 69, 130, 102, 88, 70,  95, 93, 128, 84,
  119, 70, 127,  98, 88, 70,  95, 93, 125, 85
), nrow = 5, byrow = TRUE)
rownames(mat) <- paste0("Jour", 1:5)
colnames(mat) <- paste0("P", 1:10)

# Format long pour R
df3 <- data.frame(
  taux = as.vector(t(mat)),
  jour = factor(rep(paste0("J", 1:5), each = 10)),
  patient = factor(rep(paste0("P", 1:10), times = 5))
)

# 1. Graphique combiné : 5 ECDF + 5 boîtes à moustaches
par(mfrow = c(1, 2))
cols <- c("black", "blue", "darkgreen", "orange", "red")
plot(ecdf(mat[1, ]), col = cols[1], xlim = range(mat),
     main = "ECDF des 5 jours", xlab = "Taux (mg/L)", ylab = "F(x)")
for (j in 2:5) lines(ecdf(mat[j, ]), col = cols[j])
legend("bottomright", legend = paste0("J", 1:5), col = cols, lty = 1, bty = "n")
boxplot(taux ~ jour, data = df3, col = "lightblue",
        main = "Boîtes à moustaches par jour", xlab = "Jour", ylab = "Taux (mg/L)")

# 2. Analyse tenant compte des mesures répétées / appariées par patient
# Non paramétrique : Test de Friedman (extension de Wilcoxon pour k > 2 appariés)
friedman.test(taux ~ jour | patient, data = df3)

# Paramétrique : ANOVA à mesures répétées (patient en facteur intra-sujet / bloc)
summary(aov(taux ~ jour + Error(patient / jour), data = df3))
```

### Résultats numériques & Conclusion
- **Moyennes journalières :** J1 = $104{,}5$ ; J2 = $102{,}9$ ; J3 = $99{,}7$ ; J4 = $98{,}2$ ; J5 = $97{,}0$ mg/L (décroissance régulière).
- **Test de Friedman (`friedman.test`) :** Sommes des rangs intra-patient $R_j = [42{,}5;\; 42{,}0;\; 25{,}0;\; 21{,}5;\; 19{,}0]$, **$\chi^2_{\text{Friedman}} = 22{,}1818$** ($\text{ddl} = 4$), **$p\text{-value} = 0{,}000184$**.
- **ANOVA à mesures répétées :** $\text{SC}_{\text{jour}} = 399{,}32$ ($\text{ddl}=4$), $\text{SC}_{\text{patient}} = 19294{,}42$ ($\text{ddl}=9$), $\text{SC}_{\text{rés}} = 374{,}68$ ($\text{ddl}=36$), **$F = 9{,}5919$**, **$p\text{-value} = 2{,}19 \times 10^{-5}$**.
- **Conclusion :** Les deux méthodes (qui isolent la variabilité inter-patients très élevée) rejettent $H_0$ : il existe une **baisse statistiquement très significative** du taux du biomarqueur au cours des 5 jours.

---

## 📌 Exercice 4 – Homogénéité et distributions ordinales

### Script R complet
```r
# Tableau de contingence et vecteurs individuels codés (1=Mauvais .. 4=Excellent)
tab <- matrix(c(4, 6, 17, 15,
                10, 13, 16, 11), nrow = 2, byrow = TRUE)
rownames(tab) <- c("Traite", "Controle")
colnames(tab) <- c("Mauvais", "Moyen", "Bon", "Excellent")

traite   <- rep(1:4, times = c(4, 6, 17, 15))  # n1 = 42
controle <- rep(1:4, times = c(10, 13, 16, 11)) # n2 = 50

# 1. Superposition des ECDF
plot(ecdf(traite), col = "blue", xlim = c(1, 4), xaxt = "n",
     main = "ECDF : Groupe traité vs Contrôle",
     xlab = "Classement ordinal", ylab = "Fréquence cumulée")
axis(1, at = 1:4, labels = c("Mauvais", "Moyen", "Bon", "Excellent"))
lines(ecdf(controle), col = "red")
legend("topleft", legend = c("Traité (n=42)", "Contrôle (n=50)"),
       col = c("blue", "red"), lty = 1, bty = "n")

# 2a. Test du Chi-deux d'homogénéité (traite les classes comme nominales)
chisq.test(tab)

# 2b. Test de Mann-Whitney-Wilcoxon (exploite l'ordre des 4 classes)
wilcox.test(traite, controle)
```

### Résultats numériques & Nuance décisive
1. **Test du $\chi^2$ d'homogénéité (`chisq.test`) :** $\chi^2 = \mathbf{5{,}1393}$ ($\text{ddl} = 3$), **$p\text{-value} = 0{,}1619 > 0{,}05$**. En ignorant l'ordre naturel des modalités, le $\chi^2$ manque de puissance et ne rejette pas $H_0$.
2. **Test de Mann-Whitney (`wilcox.test`) :** $U_{\text{traité}} = \mathbf{1313{,}5}$ ($z = 2{,}1545$ avec correction des ex-æquo), **$p\text{-value} = 0{,}0312 < 0{,}05$**.
- **Conclusion :** En prenant en compte la structure **ordinale** des classes (la courbe ECDF du groupe traité est décalée vers la droite : $76{,}2\%$ de *Bon/Excellent* contre $54{,}0\%$ en contrôle), on **rejette l'hypothèse que le traitement est sans effet** au seuil de 5% ($p = 0{,}0312$).

---

## 📌 Exercice 5 – Analyse temporelle sur séries appariées (`dictee.xlsx`)

Le fichier externe `dictee.xlsx` contient, mot par mot (unités statistiques appariées), le pourcentage d'erreur enregistré en 1987, 2007 et 2015.

### Script R clé en main
```r
# 1. Importation (via readxl recommandé, sans dépendance Java)
library(readxl)
dictee <- read_excel("dictee.xlsx")
# Alternative demandée dans l'énoncé :
# library(xlsx); dictee <- read.xlsx("dictee.xlsx", sheetIndex = 1)

# Inspection et statistiques descriptives
str(dictee)
summary(dictee)
apply(dictee[, c("1987", "2007", "2015")], 2, sd, na.rm = TRUE)

# Graphiques descriptifs
boxplot(dictee[, c("1987", "2007", "2015")],
        col = c("lightgreen", "gold", "tomato"),
        main = "Évolution du % d'erreur par mot (CM2)", ylab = "% d'erreur")

# Passage au format long pour les tests sur séries appariées
# (Adapter les noms exacts des colonnes de dictee.xlsx si nécessaire)
df_long <- data.frame(
  erreur = c(dictee$`1987`, dictee$`2007`, dictee$`2015`),
  annee  = factor(rep(c("1987", "2007", "2015"), each = nrow(dictee))),
  mot    = factor(rep(seq_len(nrow(dictee)), times = 3))
)

# 2a. Approche non paramétrique (recommandée si % d'erreur non normaux)
friedman.test(erreur ~ annee | mot, data = df_long)
# Comparaisons post-hoc 2 à 2 appariées avec correction de Holm/Bonferroni
pairwise.wilcox.test(df_long$erreur, df_long$annee,
                     paired = TRUE, p.adjust.method = "bonferroni")

# 2b. Approche paramétrique (ANOVA à mesures répétées)
modele <- aov(erreur ~ annee + Error(mot / annee), data = df_long)
summary(modele)
pairwise.t.test(df_long$erreur, df_long$annee,
                paired = TRUE, p.adjust.method = "bonferroni")
```

### Grille d'interprétation attendue
- Si `friedman.test` (ou l'ANOVA répétée) donne $p < 0{,}05$, au moins une année diffère significativement des autres en taux d'erreur moyen/médian.
- Les tests post-hoc (`pairwise.wilcox.test` / `pairwise.t.test` appariés) permettent ensuite de dater l'évolution exacte (1987 vs 2007, 2007 vs 2015, 1987 vs 2015).

---

## 📌 Exercice 6 – Temps de réaction au volant (3 tests différents)

### Script R complet
```r
sans <- c(0.58, 0.54, 0.58, 0.72, 0.48, 0.70, 0.62, 0.55, 0.74, 0.63, 0.55, 0.49, 0.68, 0.57, 0.55)
avec <- c(0.73, 0.62, 0.66, 0.92, 0.68, 0.87, 0.77, 0.70, 0.88, 0.79, 0.72, 0.60, 0.78, 0.66, 0.68)

# 1. Superposition des deux ECDF
plot(ecdf(sans), col = "blue", xlim = range(c(sans, avec)),
     main = "ECDF du temps de réaction (Avec vs Sans alcool)",
     xlab = "Temps de réaction (s)", ylab = "F(x)")
lines(ecdf(avec), col = "red")
legend("bottomright", legend = c("Sans alcool", "Avec alcool"),
       col = c("blue", "red"), lty = 1, bty = "n")

# Vérification des hypothèses
diff <- avec - sans
shapiro.test(diff)          # Normalité des différences
shapiro.test(sans); shapiro.test(avec)
var.test(avec, sans)        # Homoscédasticité

# 2. Trois tests différents :
# Test 1 : Student apparié (paramétrique)
t.test(avec, sans, paired = TRUE)
# Test 2 : Rangs signés de Wilcoxon (non paramétrique apparié)
wilcox.test(avec, sans, paired = TRUE)
# Test 3 : Student indépendant (ou Mann-Whitney si non apparié)
t.test(avec, sans, var.equal = TRUE)
wilcox.test(avec, sans, paired = FALSE)
```

### Comparaison des 3 tests ($\alpha = 5\%$)

| Test utilisé | Hypothèses d'application requises | Statistique | $p$-value | Décision |
| :--- | :--- | :---: | :---: | :--- |
| **1. Student apparié** | Paires liées + normalité des différences $d_i$ | $t = 13{,}5561$ ($\text{ddl}=14$) | **$1{,}93 \times 10^{-9}$** | Rejet net de $H_0$ |
| **2. Wilcoxon apparié** | Paires liées + symétrie de la loi des $d_i$ (pas de normalité requise) | $W^+ = 120, W^- = 0$ | **$< 0{,}001$** ($6{,}4 \times 10^{-4}$) | Rejet net de $H_0$ |
| **3. Student indépendant** *(ou Mann-Whitney)* | Groupes indépendants + normalité & homoscédasticité *(ou rangs seuls pour MW)* | $t = 4{,}2758$ ($\text{ddl}=28$) *(MW : $U = 193{,}5$)* | **$0{,}00020$** *(MW : $0{,}00077$)* | Rejet net de $H_0$ |

Tous les tests concluent unanimement que **la consommation d'alcool augmente très significativement le temps de réaction** ($\bar{d} = +0{,}1387$ s en moyenne).

---

## 📌 Exercice 7 – Traitement anticholestérol (Shapiro-Wilk + choix du test)

### Script R complet
```r
avant <- c(0.10, 0.20, 0.15, 0.30, 0.34, 0.16, 0.09, 0.24, 0.17, 0.29)
apres <- c(0.80, 0.18, 0.12, 0.20, 0.30, 0.21, 0.12, 0.16, 0.17, 0.22)
diff  <- apres - avant

# 2. Justification préalable : test de normalité des différences (Shapiro-Wilk)
shapiro.test(diff)
boxplot(diff, main = "Différences (Après - Avant)", ylab = "g/L")

# 1. Test non paramétrique des rangs signés de Wilcoxon (apparié)
wilcox.test(apres, avant, paired = TRUE)
```

### Analyse des résultats ($\alpha = 5\%$)
1. **Choix du test via Shapiro-Wilk (Question 2) :**
   Les différences $d_i = \text{Après}_i - \text{Avant}_i$ valent :
   `+0.70, -0.02, -0.03, -0.10, -0.04, +0.05, +0.03, -0.08, 0.00, -0.07`.
   Le patient n° 1 présente un saut aberrant ($0{,}10 \to 0{,}80$, soit $+0{,}70$ g/L) alors que les 9 autres patients sont concentrés dans $[-0{,}10 \,;\, +0{,}05]$. Cette forte asymétrie rejette nettement la normalité au test de Shapiro-Wilk ($p < 0{,}05$). Comme $n = 10 < 30$ et que les différences ne sont pas normales, le test $t$ de Student apparié n'est **pas valide** : il faut impérativement choisir le **test des rangs signés de Wilcoxon**.
2. **Résultat du test de Wilcoxon apparié (Question 1) :**
   On retire la paire nulle ($d_9 = 0 \implies n = 9$). Rangs des $|d_i|$ : $W^+ = 16{,}5$, $W^- = 28{,}5$, d'où $W = \min(16{,}5;\; 28{,}5) = \mathbf{16{,}5}$.
   La $p$-value exacte vaut **$0{,}5156$** ($\gg 0{,}05$) *(et même un test $t$ apparié donnerait $t = 0{,}5914, p = 0{,}5688$)*.
   **Conclusion :** On **ne rejette pas $H_0$**. Les données ne permettent pas de démontrer un effet statistiquement significatif du traitement sur le taux de cholestérol après une semaine.
