---
type: moc
created: 2026-11-09
tags:
  - moc
  - etudes
  - cours
  - formation
parent: "[[Acceuil]]"
---

# 🎓 Études, Cours & Formations

> ↖ [[Acceuil|Retour au Dashboard]] • [[Centre_de_control|Centre de Contrôle]]

Bienvenue dans l'espace dédié au suivi académique, à la prise de notes de classe et à la gestion des cours. Cet espace centralise les contenus magistraux, les synthèses de révision active et l'emploi du temps pour articuler les exigences scolaires avec la routine quotidienne et les blocs de Deep Work.

---

## 🗓️ 1. Emploi du Temps & Rythme Hebdomadaire

- 📅 [[Emploi_du_Temps|Consulter et mettre à jour l'Emploi du Temps]]
- 🧠 *Rappel d'articulation rythmique :* Veiller à préserver le sas de décompression (sport à 17h) et le pic de clarté du soir (Deep Work Wolf 18h-22h) en fonction des créneaux de cours en présentiel ou à distance.

---

## 📚 2. Notes de Cours & Synthèses Actives

```dataview
TABLE file.folder AS "Matière / Dossier", date AS "Date", tags AS "Mots-clés"
FROM "🌿 Domaines/Études_&_Cours/Notes_de_Cours"
WHERE type = "cours" OR type = "note-cours"
SORT file.mtime DESC
```

### 🗂️ Matières & Domaines d'Étude
- *Les dossiers par matière viendront s'organiser ici au fil du semestre dans `Notes_de_Cours/`.*
- Modèle de capture recommandé : [[Template - Note de Cours|📝 Template de Prise de Note & Active Recall]]

---

## 🎯 3. Méthodologie & Révision Haute Efficacité

- [[Fiche_Video_Recommencer_Mes_Etudes|🎓 Ingénierie de la mémoire & Active Recall]] : substitution du résumé passif par des batteries de questions fermées et ouvertes.
- [[Fiche_Video_Reviser_le_Soir|📺 Réviser le soir après les cours]] : gestion de la fatigue cognitive et sanctuarisation de la borne horaire de fin.

---

## 📋 4. Prochains Devoirs & Échéances

```tasks
not done
path includes 🌿 Domaines/Études_&_Cours
sort by due
```
