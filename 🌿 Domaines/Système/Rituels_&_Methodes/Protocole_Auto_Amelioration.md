---
type: rituel-methode
created: 2026-09-13
updated: 2026-09-13
tags:
  - protocole
  - apprentissage
  - dual-loop
  - anais
parent: "[[MOC_Systeme_Execution]]"
---

# 🔄 Protocole de Consolidation Réflexive & Auto-Amélioration

> **Fondement théorique** : Inspiré du concept d'apprentissage en double boucle (*Double-Loop Learning* de Chris Argyris). La simple boucle ajuste l'action immédiate face à un problème ; la double boucle remonte jusqu'à la règle directrice sous-jacente pour la réécrire et empêcher structurellement la récurrence de la friction.

---

## ⏱️ Fréquence & Déclencheurs

- **Cadence nominale** : Chaque dimanche soir lors de la revue hebdomadaire (pilotée par **Anaïs**).
- **Déclencheur ponctuel** : Clôture d'une milestone majeure de développement sur Stockly SaaS ou incident d'exécution significatif.

---

## 🪜 Les 5 Étapes du Rétro-Mining

```text
1. MOISSONNAGE        2. ANALYSE CAUSE RACINE     3. REGISTRE HEURISTIQUE
(Daily Logs récents) ───► (Élimination du bruit) ────► (Registre_Apprentissages)
                                                              │
                                                              ▼
5. ÉLAGAGE & NETTOYAGE ◄── 4. PROPOSITION MUTATION ◄──────────┘
(Lutte anti-calcification)  (Dépôt dans Buffer_Mutations)
```

### Étape 1 : Moissonnage des Signaux Épisodiques
L'agent passe en revue les sections `## 📡 Signaux & Frictions` des Daily Logs des 7 derniers jours.
Il relève également les écarts flagrants entre les 3 tâches prioritaires planifiées et le bilan effectif.

### Étape 2 : Analyse de Cause Racine (Les 5 Pourquoi)
L'agent sépare l'aléa ponctuel de l'erreur structurelle. Il pose trois questions d'évaluation :
- *Ce blocage s'est-il produit plus d'une fois au cours du mois ?*
- *Le problème découle-t-il d'un manque d'information, d'une hypothèse fausse ou d'une règle inadaptée ?*
- *Une directive claire aurait-elle permis d'éviter cette friction ?*

### Étape 3 : Capitalisation dans le Registre
Si le signal est pertinent, il est formulé sous la forme canonique :
`[Date] Intitulé concis` $\rightarrow$ Friction $\rightarrow$ Cause racine $\rightarrow$ Heuristique.
Il est inscrit dans [[Registre_Apprentissages]] avec le statut `🔵 Observé` ou `🟡 En test`.

### Étape 4 : Soumission au Buffer de Mutations
Si l'heuristique exige de modifier un comportement agent ou un invariant de vie :
1. L'agent formule une proposition chirurgicale dans [[Buffer_Mutations]].
2. La proposition indique la cible exacte (`AGENTS.md`, routine d'un agent, template) et la formulation précise proposée.
3. L'agent attend la validation souveraine de Fabien.

### Étape 5 : Revue d'Élagage (Lutte Anti-Calcification)
Pour préserver la clarté et la vivacité cognitive des modèles, le fichier [[AGENTS]] ne doit jamais devenir une liste sans fin de micro-consignes.
- Toute nouvelle règle ajoutée dans `AGENTS.md` entraîne la vérification des règles existantes.
- Deux règles proches doivent être fusionnées en un principe d'ordre supérieur plus abstrait.
- Les règles devenues obsolètes ou naturelles sont retirées ou transférées dans la documentation spécifique.

---

> ↖ [[MOC_Systeme_Execution|Retour au Système & Exécution]] · [[Registre_Apprentissages|Voir le Registre]]
