---
parent: "[[Projet_Stockly]]"
---

Bonne question — voici comment ça fonctionne réellement :

---

## Ce qu'Antigravity charge **automatiquement**

### ✅ Les `rules/` — toujours chargées

Les fichiers dans `.agents/rules/` marqués `trigger: always_on` sont **injectés dans mon contexte à chaque conversation**. Je les lis comme des instructions permanentes, sans que tu aies à rien faire.

```yaml
# always_on = je les applique automatiquement
trigger: always_on   → database, reasoner, api-patterns, ui-consistency, qa-verifier
```

### ✅ Les `rules/` `on_demand` — chargées si pertinentes

Les agents `on_demand` sont dans mes règles globales — je les **applique activement quand la tâche correspond**, même sans que tu les nommes explicitement.

```yaml
trigger: on_demand   → flutter-expert, supabase-guardian, testing, documentation, performance, finalize
```

---

## Ce qu'il faut **déclencher manuellement**

| Ce que tu veux             | Comment l'invoquer                      |
| -------------------------- | --------------------------------------- |
| Vérification complète      | *"Fais une vérification complète"*      |
| Vérifier un fichier précis | *"Vérifie vente_service.dart"*          |
| Avant un commit            | *"Finalise avant commit"*               |
| Débuguer un bug            | *"Débogue ce problème : [erreur]"*      |
| Générer un test            | *"Écris les tests pour ArticleService"* |

---

## Ce que les Skills font

Les **skills** (dans `.agent/skills/`) sont des **cheat sheets chargées à la demande**. Antigravity les lit quand une tâche correspond à leur domaine — mais là aussi il faut souvent être explicite :

```
"Aide-moi à brainstormer une feature"   → skill bmad-brainstorming
"Revue de code"                         → skill bmad-code-review
"Crée un test d'intégration"            → skill flutter-add-integration-test
```

---

## En pratique pour Stockly

> **Ce qui marche sans rien faire :**
> Quand tu me donnes un fichier `.dart` à modifier, j'applique automatiquement `flutter-expert`, `api-patterns`, et `ui-consistency` dans ma façon de coder.

> **Ce qui nécessite un prompt explicite :**
> Le rapport QA formel (`qa-verifier`), les tests (`testing`), la finalisation avant commit (`finalize`).

---

**Conseil** : garde le cheat sheet [`AGENTS.md`](file:///home/fabien/Documents/Projets/Pro/project_mugen/bright_morning_app_flutter/.agents/AGENTS.md) ouvert — c'est ta référence rapide pour savoir quoi dire.
