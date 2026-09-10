---
type: processus-design
project: Charis-Web
created: 2026-08-29
updated: 2026-08-29
status: En cours
ref_processus_general: "[[processus_design]]"
---

# 🎨 Processus Design — Charis-Web

> Application du [[processus_design|processus de design générique]] au projet Charis-Web.
> Cadre : Double Diamond adapté au contexte église / site vitrine + streaming audio.

---

## Phase 1 — Comprendre le problème (Discover)

### Le vrai problème à résoudre

Charis-Web n'est pas « un site pour une église ». C'est :

> **Un hub qui connecte les gens à l'enseignement de Charis Nation, où qu'ils soient, en moins de 3 clics.**

### Utilisateurs cibles

| Profil | Besoin principal | Contexte |
|--------|-----------------|----------|
| 🔍 **Le Visiteur** | Comprendre ce qu'est Charis Nation, trouver le lieu/horaires | Premier contact, Google, réseau social |
| ⭐ **Le Fidèle** | Reprendre l'écoute, explorer une série, prendre des notes | Régulier, connaît déjà l'église |
| 🎧 **Le Curieux** | Trouver et écouter un enseignement spécifique | Cherche du contenu audio, SEO |
| 💼 **Le Portfolio** | Vue d'ensemble complète du projet | Recruteur, client, collaborateur |

### Contraintes

- **Budget** : projet personnel, pas de budget hébergement premium
- **Contenu** : audio (messages/enseignements), photos équipe, événements
- **Technologies** : stack à définir (Next.js, tailwind CSS, supabase)
- **SEO** : le site doit être indexable (SSR ou SSG important)
- **Mobile-first** : 80%+ du trafic sera mobile (contexte Afrique)

---

## Phase 2 — Structurer l'information (Define)

### Arborescence

→ Voir : [[Arborescence_Portfolio_OnePage|Arborescence complète]]

### User Flows validés

| Flow | Statut | Fichier |
|------|--------|---------|
| Le Visiteur | ✅ Terminé | [[UserFlow_1_Visiteur]] |
| Le Fidèle | ✅ Terminé | [[UserFlow_2_Fidele]] |
| Le Curieux | ✅ Terminé | [[UserFlow_3_Curieux]] |
| Portfolio OnePage | ✅ Terminé | [[UserFlow_4_Portfolio_OnePage]] |

### Points d'attention UX

1. **Le Player Audio est le cœur du site** — Il doit être sticky, persistant, et fonctionner en arrière-plan
2. **La landing page = la one-page** — Pas de navigation complexe, tout est dans le scroll
3. **Les dons doivent être simples** — Mobile Money en 2 clics maximum
4. **La localisation doit être claire** — Carte + horaires visibles sans scroller longtemps

---

## Phase 3 — Explorer les idées visuelles (Ideate)

### Moodboard & Références

| Référence             | Pourquoi                                          | Lien                |
| --------------------- | ------------------------------------------------- | ------------------- |
| **Faith Church**      | One-page église, clean, player audio intégré      | faithchurch.com     |
| **Elevation Church**  | Design premium, vidéo hero, CTA clairs            | elevationchurch.org |
| **Apple Music**       | Player audio UX, sticky player, navigation fluide | music.apple.com     |
| **Awwwards — Church** | Variété de styles, inspiration layout             | awwwards.com        |

### Directions visuelles possibles

| Direction                       | Ambiance                                                 | Adaptée pour           |
| ------------------------------- | -------------------------------------------------------- | ---------------------- |
| **A. Minimaliste sombre**       | Fond noir/violet, or pour les accents, beaucoup d'espace | Player audio au centre |
| **B. Lumineuse et chaleureuse** | Fond clair, photos authentiques, tons chauds             | Communauté, proximité  |
| **C. Cinématographique**        | Vidéos pleine page, textes superposés, ambiance film     | Storytelling, émotion  |

### Palette de couleurs (validée depuis les affiches existantes)

| Rôle | Hex | Source |
|------|-----|--------|
| **Orange Charis** (CTA, accents) | `#fb5e17` | Affiches Tarr'i'Ye, Culte Prophétique |
| **Violet Charis** (nav, titres, footer) | `#6c288b` | Icônes sociales, accents violet |
| **Or / Doré** (dégradés, premium) | `#d4a017` | Dégradés typography, highlights |
| **Brun profond** (texte body) | `#3d1c02` | Texte des citations |
| **Blanc crème** (fond principal) | `#fdf8f0` | Fond des affiches |
| **Gris chaud** (fonds alternés) | `#f5f0eb` | Sections alternées |

→ Voir le moodboard complet : [[Moodboard_Charis_Web]]

---

## Phase 4 — Décider (Critères de validation)

### Checklist de bon design — Appliquée à Charis-Web

| Critère | Question concrète | Priorité |
|---------|-------------------|----------|
| **Clarté en 3 secondes** | En arrivant, comprend-on que c'est une église qui propose des enseignements audio ? | 🔴 Haute |
| **Hiérarchie visuelle** | Le regard va-t-il d'abord vers le CTA "Écouter" ? | 🔴 Haute |
| **Lisibilité mobile** | Le texte se lit-il sans zoom sur un écran 5" ? | 🔴 Haute |
| **Player accessibilité** | Le player est-il utilisable sans les mains (aria-labels, clavier) ? | 🟡 Moyenne |
| **Performance** | La page se charge-t-elle en < 3s sur une 3G ? | 🔴 Haute |
| **Dons en 2 clics** | Peut-on donner en moins de 10 secondes ? | 🟡 Moyenne |
| **Localisation immédiate** | L'adresse et la carte sont-elles visibles sans scroller 3 fois ? | 🟡 Moyenne |

### Méthodes de validation

1. **Test de comprehension 5 secondes** : Montrer la page à 5 personnes pendant 5 secondes → Qu'est-ce qu'ils retiennent ?
2. **Test sur mobile réel** : Tester sur un smartphone Android pas cher (contexte utilisateur réel)
3. **Lighthouse audit** : Score performance, accessibilité, SEO ≥ 90
4. **Test du non-expert** : Demander à quelqu'un qui ne connaît pas Charis de trouver le culte du dimanche

---

## Phase 5 — Prototyper et itérer (Deliver)

### Étapes de production

| Étape | Outil | Livrable | Statut |
|-------|-------|----------|--------|
| Recherche UX | Notion + Web | Notes de recherche | ✅ Terminé |
| User Flows | drawio | 4 diagrammes | ✅ Terminé |
| Arborescence | Markdown | Structure des pages | ✅ Terminé |
| Wireframes lo-fi | Figma | Maquettes fil-de-fer | 🔄 À faire |
| Moodboard | Figma/Pinterest | Direction visuelle | ⏳ À faire |
| Design UI | Figma | Maquettes haute fidélité | ⏳ À faire |
| Prototype interactif | Figma | Cliquable pour test | ⏳ À faire |
| Développement | Stack à définir | Site en production | ⏳ À faire |

### Boucle de feedback

```
Design → Feedback (Raphaël / équipe) → Ajustement → Re-test
```

**Règle** : Ne jamais passer à l'étape suivante sans validation de l'étape actuelle.

---

## Synthèse visuelle du processus

```
┌─────────────────────────────────────────────────────────────┐
│                    DOUBLE DIAMOND                           │
│                                                             │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │ DISCOVER │→ │  DEFINE  │→ │  IDEATE  │→ │  DELIVER │   │
│  │          │  │          │  │          │  │          │   │
│  │ Recherche│  │ User Flows│  │ Moodboard│  │ Wireframe│   │
│  │ Personas │  │ Arboresc.│  │ Palette  │  │ UI Design│   │
│  │ Contraintes│ │ Priorités│  │ Références│ │ Prototype│   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘   │
│       ✅            ✅           🔄            ⏳            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Prochaines actions

- [ ] Créer le moodboard Figma avec 3 directions visuelles
- [ ] Produire les wireframes lo-fi de la one-page (8 sections)
- [ ] Valider la direction visuelle avec Raphaël
- [ ] Tester la compréhension en 5 secondes sur mobile

---

*Dernière mise à jour : 29 août 2026*
