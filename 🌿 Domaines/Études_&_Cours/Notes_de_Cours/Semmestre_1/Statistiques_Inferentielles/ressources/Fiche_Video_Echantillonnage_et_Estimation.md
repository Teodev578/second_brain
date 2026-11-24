---
type: fiche-video
created: 2026-11-24
matiere: "Statistiques Inférentielles"
chapitre: "Ressource Vidéo — Prérequis Proba/Stats, Échantillonnage & Estimation"
source: "https://youtu.be/CfEe3rZ-4ks"
chaine: "L'Économie-Gestion Simplement"
duree: "1h26m23s"
tags:
  - etudes
  - fiche-video
  - statistiques-inferentielles
  - prerequis-proba-stats
  - echantillonnage
  - estimation
  - intervalles-de-confiance
  - active-recall
parent: "[[MOC_Statistiques_Inferentielles]]"
---

# 🎬 Fiche Vidéo — Échantillonnage, Estimation & Prérequis Proba/Stats

> ↖ [[MOC_Statistiques_Inferentielles|Statistiques Inférentielles (M1 IT)]] • [[01_Echantillonnage_et_Estimations|Ch. 01]] • [[02_Intervalles_de_Confiance|Ch. 02]]
> **Source :** *ÉCHANTILLONNAGE et ESTIMATION : Statistiques inférentielles* — *L'Économie-Gestion Simplement* (17 janv. 2023, 1h26m23s, playlist *LOIS DE PROBABILITÉ et STATISTIQUES INFÉRENTIELLES*)
> **Liens :** [Voir la vidéo YouTube](https://youtu.be/CfEe3rZ-4ks) • [Sujet d'exercices (Google Drive)](https://drive.google.com/file/d/1KGOVQ923Aw3WvOKus5YBLa7lOZTuY7Cs/view?usp=share_link)

---

## 🎯 1. Les Acquis Indispensables : Statistiques Descriptives & Probabilités `[01:30–08:50]`

L'idée directrice de l'ouverture est opérationnelle : l'échantillonnage et l'estimation (statistiques inférentielles) ne sont pas une matière isolée, mais la **combinaison de deux socles prérequis** — les statistiques descriptives et les probabilités. Sans leur maîtrise préalable, on se noie dans les formules.

### 1.1 Statistiques descriptives à maîtriser `[02:00–04:24]`

La médiane n'est pas mobilisée dans ce périmètre ; trois grandeurs suffisent, car certains énoncés fournissent des données brutes ou groupées en classes qu'il faut d'abord résumer (comme dans l'exercice 5) :

- **Moyenne arithmétique :**
  $$\bar{x} = \frac{1}{N}\sum n_i x_i$$
  Pour une variable continue regroupée en classes $[a_i ; b_i[$, $x_i$ correspond au **centre de classe** $c_i = \frac{a_i + b_i}{2}$.
- **Variance :**
  $$V = \frac{1}{N}\sum n_i (x_i - \bar{x})^2$$
  *(Il existe également la forme développée de Koenig-Huygens : $V = \frac{1}{N}\sum n_i x_i^2 - \bar{x}^2$.)*
- **Écart-type :**
  $$\sigma = \sqrt{V}$$

### 1.2 Probabilités : Loi normale & Table de $\mathcal{N}(0,1)$ `[04:30–08:50]`

En probabilités, l'outil central de cette révision est la **loi normale** et son passage obligé par la **loi normale centrée réduite** (seule clé permettant de lire la table) :

$$Z = \frac{X - m}{\sigma} \sim \mathcal{N}(0, 1)$$

Deux compétences de lecture de table doivent être maîtrisées :
- **Lecture directe :** on connaît $a \ge 0$ (après centrage-réduction), on lit la probabilité cumulée $\Pi(a) = P(Z \le a)$ à l'intérieur de la table.
- **Lecture inversée :** on connaît la probabilité dans le corps de la table (issue du seuil de confiance), on retrouve la valeur critique $t$ en additionnant l'en-tête de ligne (dixièmes) et l'en-tête de colonne (centièmes) — ex. $0{,}975 \to 1{,}9 + 0{,}06 = 1{,}96$.

> [!NOTE] Notation $\Pi(a)$ dans la vidéo
> L'enseignant note $\Pi(a)$ (« Pi de $a$ ») la fonction de répartition de $\mathcal{N}(0,1)$, notée $\Phi(a)$ dans les manuels usuels et le polycopié M1. Elle n'a aucun lien avec le nombre $\pi \approx 3{,}14$.

#### Les 6 règles de calcul avec la table de $\mathcal{N}(0,1)$ (pour $a > 0$)

| Probabilité cherchée | Formule via $\Pi$ | Usage typique |
| :--- | :--- | :--- |
| $P(Z \le a)$ | $\Pi(a)$ | Lecture directe dans la table |
| $P(Z \ge a)$ | $1 - \Pi(a)$ | Passage au complémentaire |
| $P(Z \le -a)$ | $\Pi(-a) = 1 - \Pi(a)$ | Borne négative (symétrie de la courbe) |
| $P(Z \ge -a)$ | $1 - \Pi(-a) = \Pi(a)$ | Borne négative à droite *(corrigé à 47:43)* |
| $P(a \le Z \le b)$ | $\Pi(b) - \Pi(a)$ | Probabilité sur un intervalle quelconque |
| $P(-a \le Z \le +a)$ | $2\Pi(a) - 1$ | **Formule pivot des seuils de confiance** |

---

## 🔄 2. Échantillonnage vs Estimation : Sens de Raisonnement `[08:57–16:35]`

La distinction entre les deux volets repose sur ce qui est **connu** au départ et sur la direction de l'inférence :

| Axe | Échantillonnage | Estimation (*Statistiques inférentielles*) |
| :--- | :--- | :--- |
| **Point de départ (connu)** | **Population mère** ($m, \sigma, p$ donnés) | **Échantillon** ($m', \sigma', p'$ donnés ou calculés) |
| **Cible (inconnue)** | **Échantillon** (déduire $m'$, $\sigma_{\bar{X}}$ / $\sigma_F$ et calculer des probabilités dessus) | **Population mère** (estimer $m$, $\sigma$, $p$ ponctuellement ou par intervalle de confiance) |
| **Exemple de la vidéo** | Données nationales INSEE connues $\to$ étude locale sur un échantillon (ouverture d'un magasin à Dijon) | Sondages pré-électoraux sur un échantillon représentatif $\to$ projection sur l'ensemble des électeurs |

> [!TIP] Précision terminologique `[12:25]`
> Rigoureusement, on parle de **paramètres** pour la population mère et de **variables statistiques** (ou *statistiques*) pour l'échantillon — même si l'enseignant tolère à l'oral d'employer « paramètre » des deux côtés par commodité. Dans un énoncé cohérent, un paramètre manquant côté population doit toujours pouvoir être calculé ou estimé depuis l'échantillon (et réciproquement).

L'estimation se décline sous deux formes : l'**estimation ponctuelle** (une valeur unique) et l'**estimation par intervalle de confiance** (un encadrement continu associé à un niveau de confiance).

---

## 🧭 3. Méthode en 6 Cas Types & Calcul du Coefficient $t$ `[16:39–43:05]`

### 3.1 Réflexe de lecture & conditions de validité

Devant tout exercice, la première question est binaire : suis-je en présence d'une **moyenne** (valeur mesurée : notes, €, g, cm…) ou d'une **proportion** (pourcentage ou fréquence, toujours converti en valeur décimale : $20\% \to 0{,}20$) ?

Un **échantillon représentatif** au sens du cours vidéo suppose :
1. Un tirage **aléatoire simple** (chaque individu a la même probabilité d'être prélevé).
2. Un tirage **non exhaustif (avec remise)** (un individu peut figurer dans plusieurs échantillons possibles).
3. Une **grande taille d'échantillon ($n \ge 30$)**.
4. **En présence de proportions `[1:19:53]` :** $n \ge 30$, $np \ge 5$, $nq \ge 5$ (la vidéo cite aussi $npq \ge 5$).

- **Exception normalité :** si l'énoncé précise que la distribution dans la population suit déjà une loi normale, le recours à la loi normale reste valide même sans vérifier $n \ge 30$.
- **Tirage exhaustif (sans remise) `[35:30–37:05]` :** si l'effectif total $N$ de la population est fini et que le tirage s'effectue sans remise, il faut multiplier l'écart-type d'échantillonnage par le **coefficient d'exhaustivité** :
  $$\sqrt{\frac{N - n}{N - 1}}$$

### 3.2 Tableau récapitulatif des 6 cas de la vidéo

| Cas | Situation | Formules clés |
| :--- | :--- | :--- |
| **1. Échantillonnage — Moyenne** | $m, \sigma$ connus $\to$ proba sur $\overline{X}$ | $m' = m$, $\sigma_{\bar{X}} = \dfrac{\sigma}{\sqrt{n}}$, $\overline{X} \sim \mathcal{N}\!\left(m, \dfrac{\sigma}{\sqrt{n}}\right)$, $Z = \dfrac{\overline{X} - m}{\sigma/\sqrt{n}} \sim \mathcal{N}(0,1)$ |
| **2. Échantillonnage — Proportion** | $p$ connu $\to$ proba sur $F$ | $p' = p$, $\sigma_F = \sqrt{\dfrac{pq}{n}}$ ($q = 1-p$), $F \sim \mathcal{N}\!\left(p, \sqrt{\dfrac{pq}{n}}\right)$, $Z = \dfrac{F - p}{\sqrt{pq/n}} \sim \mathcal{N}(0,1)$ |
| **3. Estimation ponctuelle** | Estimer $m, p, \sigma$ depuis l'échantillon | $\hat{m} = m'$, $\hat{p} = p'$, $s = \sigma'\sqrt{\dfrac{n}{n-1}}$ *(tend vers $\sigma'$ quand $n$ grandit)* |
| **4. IC d'une moyenne ($\sigma$ connu)** | $\sigma$ population donné | $\left[m' - t\dfrac{\sigma}{\sqrt{n}} \;;\; m' + t\dfrac{\sigma}{\sqrt{n}}\right]$ |
| **5. IC d'une moyenne ($\sigma$ inconnu)** | $\sigma'$ échantillon donné/calculé ($n \ge 30$) | $\left[m' - t\dfrac{s}{\sqrt{n}} \;;\; m' + t\dfrac{s}{\sqrt{n}}\right]$ avec $s = \sigma'\sqrt{\dfrac{n}{n-1}}$ |
| **6. IC d'une proportion** | $p'$ observé sur l'échantillon | $\left[p' - t\sqrt{\dfrac{p'q'}{n}} \;;\; p' + t\sqrt{\dfrac{p'q'}{n}}\right]$ avec $q' = 1 - p'$ |

### 3.3 Intuition & recette mécanique pour trouver $t$ `[25:55–32:44 & 39:08–43:05]`

- **Sens concret de $t$ :** c'est le **nombre d'écarts-types** dont on s'écarte à gauche et à droite de la moyenne (analogie de l'horaire d'arrivée à 18h avec une marge de 1 écart-type = 10 min ou 2 écarts-types = 20 min). Plus la marge $t$ augmente, plus la confiance augmente, au prix d'un intervalle plus large.
- **Complémentarité confiance / risque :** $\text{Seuil de confiance} = 1 - \alpha \iff \text{Seuil de risque} = \alpha$ ($95\% \leftrightarrow 5\%$, $99\% \leftrightarrow 1\%$, $90\% \leftrightarrow 10\%$).
- **Recette en 3 étapes :**
  1. Convertir le seuil de confiance en valeur relative ($1 - \alpha$).
  2. Poser et résoudre :
     $$2\Pi(t) - 1 = 1 - \alpha \implies \Pi(t) = \frac{1 + (1 - \alpha)}{2} = 1 - \frac{\alpha}{2}$$
  3. Effectuer une **lecture inversée** dans la table de $\mathcal{N}(0,1)$ (si la valeur exacte n'apparaît pas, retenir la probabilité la plus proche).
- **Valeurs repères :**
  - Confiance $90\%$ ($\alpha = 10\%$) $\to \Pi(t) = 0{,}95 \to t = 1{,}645$
  - Confiance $95\%$ ($\alpha = 5\%$) $\to \Pi(t) = 0{,}975 \to t = 1{,}96$
  - Confiance $99\%$ ($\alpha = 1\%$) $\to \Pi(t) = 0{,}995$ (valeur la plus proche $0{,}99506$) $\to t = 2{,}58$

---

## 📝 4. Mémo des 6 Exercices Corrigés `[43:10–1:26:20]`

| N° & Repère | Cas | Données | Résolution & Résultat |
| :--- | :--- | :--- | :--- |
| **Ex. 1** `[43:10]` | Échantillonnage — Moyenne | Notes d'éco : $m = 11$, $\sigma = 3$, $n = 50$ (avec remise). Chercher $P(\overline{X} > 10)$. | $\sigma_{\bar{X}} = \frac{3}{\sqrt{50}} \approx 0{,}42$. $P(Z > -2{,}38) = \Pi(2{,}38) = 0{,}99134 \approx 99\%$. |
| **Ex. 2** `[49:18]` | Échantillonnage — Proportion | $p = 0{,}60$ (filles), $n = 50$ (avec remise). Chercher $P(F < 0{,}55)$. | $\sigma_F = \sqrt{\frac{0{,}6\times 0{,}4}{50}} \approx 0{,}07$. $P(Z < -0{,}71) = 1 - \Pi(0{,}71) = 1 - 0{,}76115 = 0{,}23885 \approx 24\%$. |
| **Ex. 3** `[54:50]` | Estimation ponctuelle | Camemberts ($\sim \mathcal{N}$), $n = 50$, $m' = 450\text{ g}$, $\sigma' = 40\text{ g}$. | $\hat{m} = 450\text{ g}$ ; $s = 40\sqrt{\frac{50}{49}} \approx 40{,}41\text{ g}$. |
| **Ex. 4** `[58:32]` | IC moyenne ($\sigma$ connu) | Camemberts ($\sim \mathcal{N}$), $\sigma = 30\text{ g}$, $n = 100$, $m' = 420\text{ g}$, confiance $95\%$. | $\frac{\sigma}{\sqrt{n}} = 3$, $t = 1{,}96$. $IC_{95\%} = [414{,}12\text{ g} \;;\; 425{,}88\text{ g}]$. |
| **Ex. 5** `[1:06:00]` | IC moyenne ($\sigma$ inconnu + stats descriptives) | CA de $n = 40$ entreprises en 5 classes $[0;4[$, $[4;8[$, $[8;12[$, $[12;16[$, $[16;20[$ M€ ($n_i = 4, 10, 12, 9, 5$ ; $c_i = 2, 6, 10, 14, 18$), confiance $99\%$. | $\sum n_i c_i = 404 \implies m' = 10{,}1\text{ M€}$, $\sigma' = 4{,}69\text{ M€}$, $s = 4{,}69\sqrt{\frac{40}{39}} \approx 4{,}75\text{ M€}$, $t = 2{,}58$. $IC_{99\%} = [8{,}16\text{ M€} \;;\; 12{,}04\text{ M€}]$. |
| **Ex. 6** `[1:19:20]` | IC proportion | Activité des femmes : $n = 100$, $p' = 0{,}45$, risque $5\%$ ($\to 95\%$). | $\sigma_F = \sqrt{\frac{0{,}45\times 0{,}55}{100}} \approx 0{,}05$, $t = 1{,}96$. $IC_{95\%} = [0{,}352 \;;\; 0{,}548] \approx [35\% \;;\; 55\%]$. |

---

## 🔗 5. Passerelle & Vigilances par Rapport au Cours M1 IT (K. E. HOVI)

### Correspondance des notations

| Concept | Notation Vidéo | Notation Cours M1 IT |
| :--- | :---: | :---: |
| Moyenne population / échantillon | $m$ / $m'$ | $\mu$ / $\overline{X}$ |
| Écart-type échantillon / corrigé | $\sigma'$ / $s$ | $\overline{S}$ / $S$ |
| Quantile normal centré réduit | $t$ | $z_{1-\alpha/2}$ *(en M1, $t$ est réservé à Student)* |
| Fonction de répartition $\mathcal{N}(0,1)$ | $\Pi(a)$ | $\Phi(a)$ |

> [!WARNING] Points de vigilance & corrections sur la vidéo
> 1. **Cas $n < 30$ avec $\sigma$ inconnu (Student absent de la vidéo) :** la vidéo utilise uniquement la loi normale car tous ses exemples ont $n \ge 30$. En M1 IT ([[02_Intervalles_de_Confiance]]), sous population normale avec $\sigma$ inconnu et $n < 30$, il faut impérativement remplacer la normale par la **loi de Student $t(n-1)$**.
> 2. **Imprécision dans l'analogie $t=1$ et $t=2$ (`[30:17–31:53]`) :** l'enseignant lit $\Pi(1) \approx 84{,}13\%$ et $\Pi(2) \approx 97{,}72\%$ (probabilités unilatérales $P(Z \le t)$) en parlant d'un intervalle symétrique autour de la moyenne. La probabilité bilatérale réelle sur $[-t, +t]$ vaut $2\Pi(t) - 1$, soit **$\approx 68{,}27\%$** pour $t=1$ et **$\approx 95{,}45\%$** pour $t=2$.
> 3. **Glissade orale d'interprétation (`[1:05:35]`) :** la vidéo dit « 95% de chances que la moyenne *de l'échantillon* soit comprise dans l'intervalle ». C'est faux : l'IC encadre le paramètre inconnu de la **population mère** ($\mu$), jamais la moyenne empirique qui sert déjà de centre à l'intervalle. Rigoureusement, 95% désigne la probabilité que l'intervalle aléatoire recouvre $\mu$.
> 4. **Dénominateur d'IC sur une proportion :** la vidéo utilise $\sqrt{p'q'/n}$ (approximation grand échantillon) ; le polycopié M1 privilégie $\sqrt{f(1-f)/(n-1)}$ et l'approximation rapide $f \pm 1/\sqrt{n}$ à 95%.
> 5. **Périmètre M1 non couvert par la vidéo :** propriétés formelles des estimateurs (biais, consistance, décomposition EQM, efficacité / borne de Cramér-Rao — [[01_Echantillonnage_et_Estimations]]), ainsi que les IC sur une variance ($\chi^2$) et un rapport de variances ($\mathcal{F}$ — [[02_Intervalles_de_Confiance]]).

---

## 🧠 6. Active Recall

- [ ] **Q1 : Quels sont les deux socles prérequis cités dans la vidéo et comment s'articulent-ils ?**
  - *Réponse flash :* Les statistiques descriptives (moyenne, centre de classe, variance, écart-type pour résumer une série empirique) et les probabilités (loi normale, centrage-réduction $Z = (X-m)/\sigma$ et lecture directe/inversée de la table $\Pi$ pour calculer probabilités d'échantillonnage et quantiles $t$).
- [ ] **Q2 : Comment distinguer immédiatement un exercice d'échantillonnage d'un exercice d'estimation ?**
  - *Réponse flash :* En échantillonnage, les paramètres de la population mère sont donnés et on calcule la loi / les probabilités sur un échantillon. En estimation, on observe un échantillon et on projette ses statistiques vers les paramètres inconnus de la population mère.
- [ ] **Q3 : Quelle équation mécanique permet de retrouver $t$ à partir d'un seuil de confiance $1-\alpha$, et pourquoi ?**
  - *Réponse flash :* $2\Pi(t) - 1 = 1 - \alpha \implies \Pi(t) = 1 - \frac{\alpha}{2}$, car l'intervalle est symétrique ($P(-t \le Z \le +t) = 2\Pi(t) - 1$) ; on retrouve ensuite $t$ par lecture inversée dans la table de $\mathcal{N}(0,1)$.
- [ ] **Q4 : À quelle condition la formule d'IC de la vidéo ($\sigma$ inconnu) ne suffit-elle plus en M1 IT ?**
  - *Réponse flash :* Lorsque $\sigma$ est inconnu et que l'échantillon est petit ($n < 30$, population normale) : il faut utiliser le quantile de Student $t_{1-\alpha/2}(n-1)$ à la place de la loi normale.
