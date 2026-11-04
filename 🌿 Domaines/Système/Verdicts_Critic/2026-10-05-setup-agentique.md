---
type: critic-verdict
date: 2026-10-05
tags: [critic, setup-agentique, stockly]
---

# Verdict — Architecture du setup agentique (persona_team)

**Idée reformulée :** 20 personas, Second Cerveau Obsidian, catalogue de skills et règles globales/locales, pour réduire le doute d'action et protéger le créneau de deep work de Fabien (Stockly, échéance 31/12/2026).

## Plaidoirie (résumé)
Prothèse cognitive pour un créneau court (18h-22h) : protocoles texte, sans runtime lourd, Star Topology contre l'emballement. Avoue ne pas pouvoir prouver que le coût de maintenance reste inférieur au temps gagné.

## Réquisitoire (résumé)
Le système nourrit le doute d'action qu'il prétend guérir : chaîne /index obligatoire contre « geste direct, minimal, imparfait », horaires contradictoires, logs vides, aucune mesure. Risque : le système devient le projet. Ratio « 50 fois » exagéré (349 notes couvrent toute la vie).

## Comptes (résumé)
Aucun revenu ni coût documenté ; seul payeur possible : un client Stockly. Seuil de rentabilité non calculable faute d'heures de construction/maintenance mesurées.

## Vérifications du juge
- Finances/ : budget personnel de ~59 000-67 000 F CFA/mois (≈ 90-100 €) : un abonnement à 20 $/mois n'est pas négligeable. Aucun revenu.
- Clients/ : deux prospects, Expert Logistique Dior (P1, échange à planifier 15/09) et Architecte BTP (P3, relance 28/09). Aucun prix, aucun pilote signé.
- Meta/ : aucun chiffre de coût ni de temps (GATES, scripts, templates).
- Projet_Stockly.md : « 14h-17h / 15h-18h ou session de soirée » ; incohérent avec le profil (18h-22h) et avec AGENTS.md (14h-17h).

## Verdict : CORRIGER D'ABORD

**Raisonnement.** Le système a un coût de maintenance inconnu et une hypothèse de valeur jamais mesurée. Mais l'abandonner détruirait un actif déjà construit, et le risque est limité (fichiers Markdown, coût direct faible). Les défauts décisifs sont corrigeables en une session : trois sources donnent trois créneaux différents, dont AGENTS.md, chargé à chaque session, qui désigne faussement le créneau à protéger ; la chaîne /index obligatoire contredit la règle du profil contre l'analyse préalable excessive. Construire davantage (personas, notes) avant ces corrections aggraverait le risque central. L'incertitude porte sur l'effet réel du setup : seule une mesure de 2-4 semaines le tranchera.

**Plus gros risque.** Le système devient le projet : les soirées 18h-22h passent à entretenir personas et notes pendant que Stockly (7 fichiers) stagne, ce qui nourrit la culpabilité puis davantage de méta-travail. Déclencheur : une semaine sans livraison Stockly mais avec des modifications du setup.

**Test de dix minutes.** Ouvrir l'historique git ou la liste des fichiers modifiés (date de modification) et compter, sur les 4 dernières semaines, les fichiers de second_brain/ et de personas modifiés contre ceux de Stockly (code et notes).
- Confirme (le setup absorbe l'effort, correction urgente) : plus de la moitié des modifications touchent le setup, ou aucune modification Stockly récente.
- Infirme (le verdict peut passer à CONSTRUIRE) : l'essentiel du travail récent est sur Stockly et le setup n'a bougé qu'à la marge.

**Correction exacte avant de relancer le critic.**
1. Fixer un seul créneau (18h-22h selon le profil) et l'aligner dans AGENTS.md (= CLAUDE.md), Projet_Stockly.md, Dave (retirer « jamais de décisions après 17h ») et Inès (retirer « dîner 19h »).
2. Rendre la chaîne /index optionnelle ou allégée (une tâche minuscule = geste direct, sans chaîne complète).
3. Ouvrir un journal de livraisons Stockly (date, durée, livré oui/non) et le tenir 4 semaines, avec chronométrage du temps passé sur le setup. Ne créer aucune nouvelle persona ni note de méta pendant cette période.
4. Dédupliquer AGENTS.md/CLAUDE.md (lien symbolique) et les skills affichés en double.

Résultat du test :

Prochaine action : lancer le comptage des modifications git/mtime sur 4 semaines (setup vs Stockly), puis aligner le créneau 18h-22h dans AGENTS.md.
