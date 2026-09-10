import json
import os

files = [
    "/home/fabien/Documents/Agent/second_brain/📥 Inbox/MOC_Inbox.md",
    "/home/fabien/Documents/Agent/second_brain/🚀 Projets/Certifications_Tech/Projet_Certifications.md",
    "/home/fabien/Documents/Agent/second_brain/🚀 Projets/MOC_Projets.md",
    "/home/fabien/Documents/Agent/second_brain/🚀 Projets/Stockly_SaaS/Documentation/agents_fonctionnements.md",
    "/home/fabien/Documents/Agent/second_brain/🚀 Projets/Stockly_SaaS/Documentation/résumé_agent_ia.md",
    "/home/fabien/Documents/Agent/second_brain/🚀 Projets/Stockly_SaaS/Projet_Stockly.md",
    "/home/fabien/Documents/Agent/second_brain/🌿 Domaines/Système/MOC_Organisation.md",
    "/home/fabien/Documents/Agent/second_brain/🌿 Domaines/Système/Organisation_&_Vision_Fabien.md",
    "/home/fabien/Documents/Agent/second_brain/🌿 Domaines/Système/README.md",
    "/home/fabien/Documents/Agent/second_brain/🌿 Domaines/Système/Antidotes_Anti_Overthinking_&_BuJo.md",
    "/home/fabien/Documents/Agent/second_brain/🌿 Domaines/Système/MOC_Productivite.md",
    "/home/fabien/Documents/Agent/second_brain/🌿 Domaines/Système/README.md",
    "/home/fabien/Documents/Agent/second_brain/🌿 Domaines/Finances/MOC_Finances.md",
    "/home/fabien/Documents/Agent/second_brain/🌿 Domaines/Finances/README.md",
    "/home/fabien/Documents/Agent/second_brain/🌿 Domaines/Santé/Chronotype_&_Energie_Sommeil.md",
    "/home/fabien/Documents/Agent/second_brain/🌿 Domaines/Santé/MOC_Sante_Vitalite.md",
    "/home/fabien/Documents/Agent/second_brain/🌿 Domaines/Vision/MOC_Mental_Equilibre.md",
    "/home/fabien/Documents/Agent/second_brain/🌿 Domaines/Vision/Boussole_de_Vie_&_Horizons.md",
    "/home/fabien/Documents/Agent/second_brain/🌿 Domaines/Vision/MOC_Vision_Objectifs.md",
    "/home/fabien/Documents/Agent/second_brain/🌿 Domaines/Maison/MOC_Maison_Minimalisme.md",
    "/home/fabien/Documents/Agent/second_brain/🌿 Domaines/Maison/README.md"
]

with open("all_files.txt", "w") as out:
    for f in files:
        out.write(f"--- FILE: {f} ---\n")
        try:
            with open(f, "r") as inf:
                out.write(inf.read())
        except Exception as e:
            out.write(f"ERROR: {e}")
        out.write("\n\n")

