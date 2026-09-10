---
title: "MOC Stockly SaaS"
type: moc
project: Stockly
up: "[[Projet_Stockly]]"
created: 2026-09-07
---

# 🗺️ MOC — Stockly SaaS

> Hub de navigation dynamique pour le projet P0. Tout ce qui touche à Stockly remonte ici.

---

## Sessions de travail récentes

```dataview
TABLE file.mtime AS "Modifié", status AS "Statut"
FROM "🚀 Projets/Stockly_SaaS"
WHERE file.name != "MOC_Stockly"
SORT file.mtime DESC
LIMIT 10
```

---

## Prochaines actions & TODO

```dataview
TASK
FROM "🚀 Projets/Stockly_SaaS"
WHERE !completed
SORT file.mtime DESC
```

---

## Documents par type

```dataview
TABLE file.name AS "Fichier", type AS "Type"
FROM "🚀 Projets/Stockly_SaaS"
WHERE type != null
SORT type ASC
```

---

## Liens rapides

- [[Projet_Stockly]] — Fiche projet principale
- [[Centre_de_control]] — Tableau de bord global
- [[Boussole_de_Vie_&_Horizons]] — Vision à 3-5 ans

---

## Notes importantes
<!-- Décisions d'architecture, contraintes non-négociables -->

- Stack figée : Flutter / Supabase / SQLite (offline-first) — non négociable
- Architecture offline-first : le local prime sur le réseau
