import json
import os

nodes = []
edges = []

def add_node(id_str, label, file_type, source_file, source_url=None, captured_at=None, author=None, contributor=None):
    nodes.append({
        "id": id_str,
        "label": label,
        "file_type": file_type,
        "source_file": source_file,
        "source_location": None,
        "source_url": source_url,
        "captured_at": captured_at,
        "author": author,
        "contributor": contributor
    })

def add_edge(source, target, relation, confidence, confidence_score, source_file):
    edges.append({
        "source": source,
        "target": target,
        "relation": relation,
        "confidence": confidence,
        "confidence_score": confidence_score,
        "source_file": source_file,
        "source_location": None,
        "weight": 1.0
    })

f1 = "/home/fabien/Documents/Agent/second_brain/📥 Inbox/MOC_Inbox.md"
add_node("00_inbox_moc_inbox", "MOC Inbox", "document", f1)
add_node("00_inbox_moc_inbox_dashboard", "Dashboard", "concept", f1)
add_edge("00_inbox_moc_inbox", "00_inbox_moc_inbox_dashboard", "references", "EXTRACTED", 1.0, f1)

f2 = "/home/fabien/Documents/Agent/second_brain/🚀 Projets/Certifications_Tech/Projet_Certifications.md"
add_node("01_projects_certifications_tech_projet_certifications", "Projet Certifications", "document", f2)

f3 = "/home/fabien/Documents/Agent/second_brain/🚀 Projets/MOC_Projets.md"
add_node("01_projects_moc_projets", "MOC Projets", "document", f3)

f4 = "/home/fabien/Documents/Agent/second_brain/🚀 Projets/Stockly_SaaS/Documentation/agents_fonctionnements.md"
add_node("01_projects_stockly_saas_documentation_agents_fonctionnements", "Agents Fonctionnements", "document", f4)

f5 = "/home/fabien/Documents/Agent/second_brain/🚀 Projets/Stockly_SaaS/Documentation/résumé_agent_ia.md"
add_node("01_projects_stockly_saas_documentation_r_sum__agent_ia", "Résumé Agent IA", "document", f5)

f6 = "/home/fabien/Documents/Agent/second_brain/🚀 Projets/Stockly_SaaS/Projet_Stockly.md"
add_node("01_projects_stockly_saas_projet_stockly", "Projet Stockly", "document", f6)

f7 = "/home/fabien/Documents/Agent/second_brain/🌿 Domaines/Système/MOC_Organisation.md"
add_node("02_areas_01_organisation___rituels_moc_organisation", "MOC Organisation", "document", f7)

f8 = "/home/fabien/Documents/Agent/second_brain/🌿 Domaines/Système/Organisation_&_Vision_Fabien.md"
add_node("02_areas_01_organisation___rituels_organisation___vision_fabien", "Organisation & Vision Fabien", "document", f8)

f9 = "/home/fabien/Documents/Agent/second_brain/🌿 Domaines/Système/README.md"
add_node("02_areas_01_organisation___rituels_readme", "Organisation README", "document", f9)

f10 = "/home/fabien/Documents/Agent/second_brain/🌿 Domaines/Système/Antidotes_Anti_Overthinking_&_BuJo.md"
add_node("02_areas_02_productivite___focus_antidotes_anti_overthinking___bujo", "Antidotes Anti-Overthinking", "document", f10)

f11 = "/home/fabien/Documents/Agent/second_brain/🌿 Domaines/Système/MOC_Productivite.md"
add_node("02_areas_02_productivite___focus_moc_productivite", "MOC Productivite", "document", f11)

f12 = "/home/fabien/Documents/Agent/second_brain/🌿 Domaines/Système/README.md"
add_node("02_areas_02_productivite___focus_readme", "Productivite README", "document", f12)

f13 = "/home/fabien/Documents/Agent/second_brain/🌿 Domaines/Finances/MOC_Finances.md"
add_node("02_areas_03_finances___patrimoine_moc_finances", "MOC Finances", "document", f13)

f14 = "/home/fabien/Documents/Agent/second_brain/🌿 Domaines/Finances/README.md"
add_node("02_areas_03_finances___patrimoine_readme", "Finances README", "document", f14)

f15 = "/home/fabien/Documents/Agent/second_brain/🌿 Domaines/Santé/Chronotype_&_Energie_Sommeil.md"
add_node("02_areas_04_sante___vitalite_chronotype___energie_sommeil", "Chronotype & Energie Sommeil", "document", f15)

f16 = "/home/fabien/Documents/Agent/second_brain/🌿 Domaines/Santé/MOC_Sante_Vitalite.md"
add_node("02_areas_04_sante___vitalite_moc_sante_vitalite", "MOC Sante Vitalite", "document", f16)

f17 = "/home/fabien/Documents/Agent/second_brain/🌿 Domaines/Vision/MOC_Mental_Equilibre.md"
add_node("02_areas_05_mental___equilibre_moc_mental_equilibre", "MOC Mental Equilibre", "document", f17)

f18 = "/home/fabien/Documents/Agent/second_brain/🌿 Domaines/Vision/Boussole_de_Vie_&_Horizons.md"
add_node("02_areas_06_vision___valeurs_boussole_de_vie___horizons", "Boussole de Vie & Horizons", "document", f18)

f19 = "/home/fabien/Documents/Agent/second_brain/🌿 Domaines/Vision/MOC_Vision_Objectifs.md"
add_node("02_areas_06_vision___valeurs_moc_vision_objectifs", "MOC Vision Objectifs", "document", f19)

f20 = "/home/fabien/Documents/Agent/second_brain/🌿 Domaines/Maison/MOC_Maison_Minimalisme.md"
add_node("02_areas_07_maison___environnement_moc_maison_minimalisme", "MOC Maison Minimalisme", "document", f20)

f21 = "/home/fabien/Documents/Agent/second_brain/🌿 Domaines/Maison/README.md"
add_node("02_areas_07_maison___environnement_readme", "Maison README", "document", f21)

out_data = {
    "nodes": nodes,
    "edges": edges,
    "hyperedges": [],
    "input_tokens": 0,
    "output_tokens": 0
}

os.makedirs("/home/fabien/Documents/Agent/second_brain/graphify-out", exist_ok=True)
with open("/home/fabien/Documents/Agent/second_brain/graphify-out/.graphify_chunk_01.json", "w") as f:
    json.dump(out_data, f)

print(json.dumps(out_data))
