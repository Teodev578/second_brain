---
type: moodboard
project: Charis-Web
created: 2026-08-29
updated: 2026-08-29
status: Draft
palette_source: Affiches Charis Nation existantes
---

# 🎨 Moodboard — Charis-Web

> Basé sur l'identité visuelle réelle de Charis Nation (4 affiches analysées).

---

## Palette officielle

### Couleurs principales

| Rôle | Couleur | Hex | Usage web |
|------|---------|-----|-----------|
| **Orange Charis** | 🟠 | `#fb5e17` | CTA principal, accents, highlights, liens actifs |
| **Violet Charis** | 🟣 | `#6c288b` | Navigation, titres de section, footer, badges |
| **Or / Doré** | 🟡 | `#d4a017` | Dégradés avec l'orange, texte d'accroche premium |
| **Brun profond** | 🟤 | `#3d1c02` | Texte principal (plus lisible que le noir pur) |

### Couleurs secondaires

| Rôle | Couleur | Hex | Usage web |
|------|---------|-----|-----------|
| **Blanc crème** | ⬜ | `#fdf8f0` | Fond principal, espace négatif |
| **Gris chaud** | ⬜ | `#f5f0eb` | Fond de sections alternées |
| **Noir doux** | ⬛ | `#1a1a1a` | Texte body, contraste fort |
| **Or pâle** | 🟡 | `#f5d98a` | Highlights subtils, bordures |

### Dégradés signature

```css
/* Dégradé hero / sections premium */
.gradient-hero {
  background: linear-gradient(135deg, #fb5e17 0%, #d4a017 50%, #f5d98a 100%);
}

/* Dégradé violet → orange (accent) */
.gradient-accent {
  background: linear-gradient(90deg, #6c288b 0%, #fb5e17 100%);
}

/* Dégradé subtil pour fonds de cards */
.gradient-card {
  background: linear-gradient(180deg, #fdf8f0 0%, #f5f0eb 100%);
}
```

---

## Direction visuelle retenue : "Lumière Dorée"

> Reprend l'ambiance des affiches existantes : lumineux, chaleureux, premium accessible.

### Principes

1. **Fond clair par défaut** — blanc crème `#fdf8f0`, pas de fond noir massif
2. **Orange = action** — Tout CTA, bouton interactif, ou élément cliquable est orange
3. **Violet = structure** — Navigation, titres de sections, éléments d'identité
4. **Doré = émotion** — Dégradés, highlights spéciaux, moments premium
5. **Photographies réelles** — Pas d'illustrations génériques, toujours des visages humains
6. **Typographie gradient** — Les titres majeurs utilisent le dégradé orange→or (trait distinctif)

### Typographie

| Élément | Style | Police suggérée |
|---------|-------|-----------------|
| **Titres H1** | Serif Bold + Gradient orange→or | Playfair Display ou Cormorant Garamond |
| **Titres H2/H3** | Serif Regular, violet `#6c288b` | Même famille |
| **Body text** | Sans-serif, brun `#3d1c02` | Inter ou DM Sans |
| **Citations / Noms** | Script / Italic | Dancing Script ou Pacifico |
| **Boutons / Nav** | Sans-serif Bold, blanc sur violet | Inter Bold |

### Iconographie

- **Logo aigle** : toujours présent, version simplifiée pour le web (favicon + header)
- **Icônes sociales** : violet `#6c288b` sur fond blanc, ou blanc sur fond violet
- **Icônes fonctionnelles** : style outline, épaisseur 1.5px, couleur violet

---

## Moodboard web — Sections

### 1. Hero Section

```
┌─────────────────────────────────────────────────┐
│  [Logo aigle]          Navigation (violet)      │
│                                                 │
│        ✦ BIENVENUE À CHARIS NATION ✦           │
│    ─────────────────────────────────            │
│   "Une communauté de foi, de puissance          │
│            et d'excellence"                     │
│                                                 │
│      [🎧 Écouter nos enseignements]  ← CTA     │
│         (bouton orange arrondi)                 │
│                                                 │
│  Fond : photo église/personnes avec overlay     │
│  dégradé orange→or subtil en bas                │
└─────────────────────────────────────────────────┘
```

### 2. Section Audio / Enseignements

```
┌─────────────────────────────────────────────────┐
│  NOS DERNIERS ENSEIGNEMENTS                     │
│  (titre violet, underline orange)               │
│                                                 │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐         │
│  │ ▶️      │  │ ▶️      │  │ ▶️      │         │
│  │ [photo] │  │ [photo] │  │ [photo] │         │
│  │ Message │  │ Message │  │ Message │         │
│  │ Rev. X  │  │ Rev. Y  │  │ Rev. Z  │         │
│  │ 45 min  │  │ 32 min  │  │ 58 min  │         │
│  └─────────┘  └─────────┘  └─────────┘         │
│                                                 │
│  [🎧 Voir tout le catalogue]  ← CTA violet     │
└─────────────────────────────────────────────────┘
```

### 3. Section Équipe

```
┌─────────────────────────────────────────────────┐
│         L'ÉQUIPE PASTORALE                      │
│  (titre violet, texte centré)                   │
│                                                 │
│      [Photo circulaire]    [Photo circulaire]   │
│       Rev. Israël           Pasteur X           │
│       Watchman                                 │
│       Fondateur                                 │
│       "Un mot de la bio..."                     │
│                                                 │
│  Fond : blanc crème, pas de bordure             │
│  Séparateur : ligne fine dorée                  │
└─────────────────────────────────────────────────┘
```

### 4. Section Événements

```
┌─────────────────────────────────────────────────┐
│    PROCHAINS ÉVÉNEMENTS                         │
│                                                 │
│  ┌──────────────────────────┐                   │
│  │ [Photo event gradient]   │                   │
│  │                          │                   │
│  │  CULTE PROPHÉTIQUE       │ ← badge violet   │
│  │  Dimanche 12 Juillet     │                   │
│  │  09:00 GMT               │                   │
│  │  Auditorium Charis Nation│                   │
│  │                          │                   │
│  │  [📅 Ajouter au agenda]  │ ← CTA outline    │
│  └──────────────────────────┘                   │
└─────────────────────────────────────────────────┘
```

### 5. Footer

```
┌─────────────────────────────────────────────────┐
│  Fond violet #6c288b                            │
│                                                 │
│  [Logo aigle blanc]   CHARIS NATION             │
│                        House of Excellence      │
│                                                 │
│  📍 Audito...    📞 +228 71...   📧 email      │
│                                                 │
│  [f] [Telegram] [TikTok] [YouTube]              │
│   ← icônes blanches sur violet                  │
│                                                 │
│  © 2026 Charis Nation. Tous droits réservés.    │
└─────────────────────────────────────────────────┘
```

---

## Ce qui change par rapport au moodboard précédent

| Avant (generic) | Maintenant (basé sur affiches) |
|-----------------|-------------------------------|
| Fond sombre `#1A0A21` par défaut | Fond clair `#fdf8f0` par défaut |
| Violet `#572269` comme primary | Orange `#fb5e17` comme primary (action) |
| Or `#FBC906` comme accent | Violet `#6c288b` comme structure |
| Pas de dégradé signature | Dégradé orange→or sur les titres |
| Typo generic | Serif pour titres, Sans-serif pour body |
| Pas de référence aux affiches | Cohérence totale avec les supports existants |

---

## Références visuelles

| Source | Pourquoi |
|--------|----------|
| Affiches Charis Nation existantes | Identité officielle, palette validée |
| Elevation Church (site) | One-page église, sections audio, player |
| YouVersion Bible App | Section audio/écoute, clean, mobile-first |
| Apple Music (web) | Player sticky, navigation fluide |
| Faith Church (site) | Layout events, localisation intégrée |

---

## Prochaines étapes

- [ ] Créer le fichier Figma avec la palette officielle
- [ ] Décliner les composants (boutons, cards, navigation) dans les couleurs Charis
- [ ] Prototyper la hero section avec le dégradé signature
- [ ] Valider avec l'équipe Charis Nation

---

*Moodboard basé sur l'analyse de 4 affiches Charis Nation — 29 août 2026*
