---
parent: "[[My_Dev_Life]]"
---

La création et l'utilisation d'un **sous-agent** dépendent du contexte dans lequel vous souhaitez l'implémenter :

---

### 1. Dans le Chat Antigravity (Délégation directe)

Dans l'interface Antigravity, l'agent principal peut créer et orchestrer des sous-agents pour paralléliser ou isoler des tâches (recherche documentaire, exploration de code, tâches de navigation web avec un sous-agent de navigateur, etc.).

* **Comment faire :** Il suffit d'instruire l'agent dans votre prompt :
  
  > *"Lance des sous-agents en parallèle pour analyser les fichiers du module auth et les routes API associées."*
* Vous pouvez également utiliser des commandes comme `/goal` pour des tâches complexes nécessitant des délégations autonomes.

---

### 2. Créer un rôle / persona de sous-agent réutilisable (Customizations / Skills)

Pour doter Antigravity d'un comportement d'agent spécialisé (ex: *Auditeur de sécurité*, *Réviseur de code*, etc.), vous pouvez créer un **Skill / Persona** dans votre projet :

1. Créez le dossier dans `.agents/skills/` (ou `.agent/skills/`) :
   
   ```
   .agents/skills/mon-sous-agent/SKILL.md
   ```

2. Remplissez le fichier `SKILL.md` avec le frontmatter et les instructions du rôle :
   
   ```markdown
   ---
   name: security-reviewer
   description: Sous-agent expert en audit de sécurité et détection de vulnérabilités. À activer lors de l'analyse de code sensible ou d'endpoints d'authentification.
   ---
   
   # Rôle : Security Reviewer
   
   Vous agissez en tant qu'expert en sécurité logicielle.
   
   ## Directives
   - Analyser systématiquement les entrées utilisateur non assainies.
   - Vérifier la gestion des tokens, des permissions et des clés API.
   - Fournir un rapport structuré des vulnérabilités avec criticité (Faible, Moyenne, Haute, Critique).
   ```

*(Le projet dispose également du framework **BMAD** avec des personas intégrés comme `bmad-agent-architect`, `bmad-agent-dev`, `bmad-agent-pm` ou `bmad-party-mode`).*

---

### 3. Via le SDK Python (`google-antigravity`)

Si vous développez des scripts ou des applications autonomes en Python avec le SDK Antigravity, vous pouvez activer la capacité de sous-agents ou orchestrer plusieurs agents :

#### Option A : Délégation native via `CapabilitiesConfig`

```python
import asyncio
from google.antigravity import Agent, LocalAgentConfig, types

async def main():
    # Activer la capacité des sous-agents
    config = LocalAgentConfig(
        system_instructions="Vous êtes un orchestrateur de projet.",
        capabilities=types.CapabilitiesConfig(
            enable_subagents=True,  # Activé par défaut
        )
    )

    async with Agent(config) as agent:
        response = await agent.chat(
            "Utilise un sous-agent pour auditer les dépendances et un autre pour résumer l'architecture."
        )
        print(await response.text())

if __name__ == "__main__":
    asyncio.run(main())
```

#### Option B : Orchestration explicite de plusieurs agents dédiés

```python
import asyncio
from google.antigravity import Agent, LocalAgentConfig

async def main():
    config_chercheur = LocalAgentConfig(
        system_instructions="Vous êtes un sous-agent dédié à la recherche technique."
    )
    config_redacteur = LocalAgentConfig(
        system_instructions="Vous êtes un sous-agent dédié à la rédaction de documentation."
    )

    async with Agent(config_chercheur) as chercheur, Agent(config_redacteur) as redacteur:
        # Étape 1 : Le chercheur extrait les infos
        recherche = await chercheur.chat("Quels sont les points clés de l'architecture ?")
        notes = await recherche.text()

        # Étape 2 : Le rédacteur formate le rapport final
        rapport = await redacteur.chat(f"Rédige un README clair basé sur ces notes :\n{notes}")
        print(await rapport.text())

if __name__ == "__main__":
    asyncio.run(main())
```

---

Souhaitez-vous concevoir un sous-agent pour un cas d'usage particulier (compétence spécifique, tâche de code automatisée, ou script Python) ?


