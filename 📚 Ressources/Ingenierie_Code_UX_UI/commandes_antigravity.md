---
parent: "[[My_Dev_Life]]"
---

Dans **Google Antigravity**, les « commandes » se répartissent en 3 catégories principales selon l'endroit où vous les utilisez :

---

### 1. 💬 Les Slash Commands (dans le Chat)

Ce sont les raccourcis que vous tapez avec un `/` dans le champ de discussion pour déclencher des flux de travail spécialisés :

| Commande        | Rôle & Utilité                                                                                                                                                                                                                                       |
|:--------------- |:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`/goal`**     | **Tâche longue et autonome** : Indique à l'agent de travailler de manière exhaustive sur un objectif complexe sans s'arrêter avant d'avoir entièrement terminé et vérifié le résultat (idéal pour les gros chantiers ou les refactorings de fond).   |
| **`/grill-me`** | **Session d'alignement & cadrage** : L'agent vous pose une série de questions précises et stimulantes pour challenger votre idée, clarifier vos besoins techniques et trancher les décisions d'architecture avant d'écrire la moindre ligne de code. |
| **`/schedule`** | **Planification & minuteries** : Permet de programmer une instruction pour plus tard (ex: *« vérifie le déploiement dans 10 minutes »*) ou de manière récurrente avec une expression cron (ex: *« génère un rapport chaque matin »*).                |
| **`/learn`**    | **Mémorisation & apprentissage** : Sauvegarde une règle ou une correction que vous venez d'apporter à l'agent dans sa mémoire persistante pour qu'il s'en souvienne dans toutes les futures conversations.                                           |
| **`/help`**     | **Aide** : Affiche la liste des commandes slash disponibles et leur description.                                                                                                                                                                     |
| **`/clear`**    | **Nettoyage** : Réinitialise le contexte de la conversation actuelle pour repartir sur une base propre.                                                                                                                                              |

---

### 2. ⌨️ Les Commandes Inline & Raccourcis (dans l'Éditeur / IDE)

Ces commandes s'utilisent directement au sein de vos fichiers de code :

* **`Ctrl + I` (ou `Cmd + I` sur macOS) — *Inline Edit*** :
  * **Sélection de code** : Permet de demander à l'agent de refactoriser, corriger un bug, ajouter des tests ou documenter uniquement le bloc sélectionné.
  * **Curseur vide** : Génère directement du nouveau code à l'endroit précis du curseur.
* **<kbd>Tab</kbd> — *Antigravity Tab / Autocomplete*** :
  * Propose des complétions multi-lignes prédictives.
  * Ajoute automatiquement les `import` manquants en haut de fichier.
  * Permet de sauter directement au prochain endroit pertinent dans le code (*Tab to Jump*).
* **Code Lenses & Quick Fixes** :
  * Liens cliquables directement au-dessus des classes ou fonctions (*"Explain"*, *"Add Tests"*, *"Refactor"*).
  * Correction automatique des erreurs de lint / compilation (*"Fix with Antigravity"*).

---

### 3. 🖥️ Les Commandes Terminal CLI (`agy`)

Si vous utilisez l'outil en ligne de commande :

* **`agy`** : Lance l'interface interactive TUI Antigravity directement dans votre terminal.
* **`agy --help`** : Affiche la liste de tous les drapeaux de configuration et sous-commandes disponibles.
* **`Ctrl + D Ctrl + D`** (ou `/exit`, `/quit`) : Quitte l'interface de terminal.

---

### 💡 Astuce complémentaire : Les `@ Mentions`

Dans le chat, vous pouvez taper **`@`** pour injecter directement du contexte :

* **`@nom_du_fichier`** : Attache un fichier spécifique au message.
* **`@conversation`** : Fait référence à une session précédente.
* **`@rules` / `@skills`** : Active explicitement une compétence ou une règle métier pour votre tâche.

Viewed AGENTS.md:24-33
