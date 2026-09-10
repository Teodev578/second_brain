---
type: arborescence
project: Charis-Web
created: 2026-08-29
updated: 2026-08-29
status: Draft
---

# 🌳 Arborescence — Portfolio OnePage (Charis-Web)

> **Page scrollable en une seule page** — Sections empilées verticalement.
> Source : [[UserFlow_4_Portfolio_OnePage|User Flow 4 — Portfolio OnePage]]

---

## Structure globale

```
🏠 ONEPAGE CHARIS-WEB
│
├── 🔝 1. HERO SECTION
│   ├── Titre : "Bienvenue à Charis Nation"
│   ├── Vidéo ou photo de fond (plein écran, overlay sombre)
│   ├── Sous-titre / tagline accrocheuse
│   └── CTA principal : 🎧 "Écouter nos enseignements"
│
├── 📜 2. VISION & MISSION
│   ├── Titre de section
│   ├── Texte court : mission de l'église (2-3 phrases max)
│   ├── Valeurs clés (3-4 icônes + labels)
│   │   ├── Ex : Foi
│   │   ├── Ex : Communion
│   │   ├── Ex : Service
│   │   └── Ex : Formation
│   └── CTA secondaire : "Découvrir notre histoire"
│
├── 👥 3. L'ÉQUIPE PASTORALE
│   ├── Titre de section
│   ├── Grille de photos (2-4 pastors)
│   │   ├── Photo circulaire
│   │   ├── Nom + titre
│   │   └── Bio courte (2 lignes max)
│   └── CTA : "En savoir plus sur l'équipe"
│
├── 🎧 4. EXTRAITS AUDIO (Player intégré)
│   ├── Titre de section ("Nos derniers enseignements")
│   ├── Player mini intégré
│   │   ├── Titre du message
│   │   ├── Nom de l'orateur
│   │   ├── Contrôles lecture (play/pause, seek)
│   │   └── Lien "Voir tout le catalogue"
│   ├── 2-3 extraits en vedette
│   └── CTA : "🎧 Explorer tous les enseignements"
│
├── 📅 5. PROCHAINS CULTES & ÉVÉNEMENTS
│   ├── Titre de section
│   ├── Cards événements (2-3 prochains)
│   │   ├── Date + heure
│   │   ├── Titre du culte/événement
│   │   ├── Orateur / responsable
│   │   └── Badge : "Culte" / "Événement" / "Formation"
│   └── CTA : "📅 Voir le calendrier complet"
│
├── 📍 6. LOCALISATION & HORAIRES
│   ├── Titre de section
│   ├── Adresse complète
│   ├── Carte intégrée (Google Maps ou OpenStreetMap)
│   ├── Horaires des cultes
│   │   ├── Dimanche : HHhMM — HHhMM
│   │   └── Mercredi (éventuel) : HHhMM — HHhMM
│   └── CTA : "📍 Itinéraire Google Maps"
│
├── 💛 7. DONS & SOUTIEN
│   ├── Titre de section
│   ├── Message court sur l'importance du don
│   ├── Méthodes de don
│   │   ├── Mobile Money (Moov / MTN / MoMo)
│   │   ├── Virement bancaire
│   │   └── En ligne (lien externe ou intégré)
│   └── CTA : "💛 Faire un don"
│
└── 🦶 8. FOOTER
    ├── Logo Charis Nation
    ├── Liens rapides (sections de la page)
    ├── Réseaux sociaux (Facebook, YouTube, WhatsApp)
    ├── Mention légale / copyright
    └── Contact : email + téléphone
```

---

## Notes de design

| Élément         | Recommandation                                                                       |
| --------------- | ------------------------------------------------------------------------------------ |
| **Navigation**  | Sticky header ou hamburger menu pour revenir à une section                           |
| **Scroll**      | Smooth scroll entre sections, indicateur de progression                              |
| **Mobile**      | Tout en colonne unique, touch-friendly (min 44px tap target)                         |
| **Audio**       | Sticky player en bas d'écran quand on écoute (persiste pendant le scroll)            || **Palette** | Orange `#fb5e17` (CTA), Violet `#6c288b` (structure), Or `#d4a017` (dégradés), Blanc crème `#fdf8f0` (fond) |
| **Typographie** | Serif pour les titres (ton solennel), Sans-serif pour le body (lisibilité)           |
| **Performance** | Lazy-load des images, audio en streaming (pas de téléchargement auto)                |

---

## Parcours utilisateur couverts

D'après les User Flows, cette one-page répond à **4 profils** :

1. **🔍 Le Visiteur** — Découvre l'église via Google/réseau social → Hero → Vision → Localisation
2. **⭐ Le Fidèle** — Revient pour écouter → Player sticky → Catalogue /enseignements
3. **🎧 Le Curieux** — Cherche du contenu audio → Section audio → Catalogue → Filtres
4. **💼 Le Portfolio** — Vue d'ensemble complète → Toutes les sections en scroll

---

*Dernière mise à jour : 29 août 2026*
