---
type: note-cours
created: 2026-11-23
matiere: "Architecture Système et Réseau Windows"
chapitre: "01 - Cadrage, Architecture du Lab, Adressage IP & Fondamentaux Windows"
enseignant: "M. Elom Marney-MENSAH"
tags:
  - etudes
  - cours
  - windows-server
  - reseau
  - adressage-ip
  - active-directory
  - dns
  - virtualisation
  - active-recall
parent: "[[MOC_Architecture_Systeme_et_Reseau_Windows]]"
---

# 📖 01. Cadrage, Architecture du Lab, Adressage IP & Fondamentaux Windows

> **Matière :** [[MOC_Architecture_Systeme_et_Reseau_Windows|Architecture Système et Réseau Windows (M1 IT)]] • **Enseignant :** M. Elom Marney-MENSAH • **Date :** 23 Novembre 2026 • **Statut :** Fiche de révision & d'assimilation terre à terre

---

## 📸 0. Photo du Tableau & Décodage Intégral

> ![[Tableau_Seance1_Cadrage_&_Lab.jpg]]

### Transcription ligne par ligne du tableau

| Zone du tableau | Texte original relevé | Signification & précision technique |
| :--- | :--- | :--- |
| **En-tête gauche** | *Cours : Architecture Syst. et Rés. Windows — Syllabus / Chap. 1* | Intitulé du module et démarrage du premier chapitre. |
| **En-tête droite** | *M. Elom Marney-MENSAH — RSSI / Chef Projets en Digitalisation d'ent/se — Formateur Spécialisé — Volume horaire : 20h* | Profil de l'enseignant (orientation sécurité & production d'entreprise) et durée du module. |
| **Prérequis (droite)** | *CCNA ou CCNP ; Adressage IP, Protocole TCP/IP, Modèle OSI, IPv4 / IPv6, Services Infrastructures* | Socle réseau exigé pour monter l'architecture Windows Server. |
| **Expérience & Écosystème (droite)** | *Expérience en Phy to Vi ; Virtualisation — vCenter, Xen (« Zen »), VMware ESXi 7, Proxmox VE 9* | Solutions d'hypervision d'entreprise (Type 1) et migration *Physical to Virtual* (P2V). |
| **Poste hôte (`PC/LPT`)** | *RAM ≤ 16 Go ; HD (SATA/SSD) = 100 Go* | Caractéristiques du PC portable pour héberger le lab *(viser ≥ 16 Go de RAM en pratique)*. |
| **Logiciel du lab** | *Log : VMware WRK (16 ou 17)* | Hyperviseur de bureau **VMware Workstation**. |
| **Nommage 1er Serveur** | `SRV-DMAD-MSTR01` *(Type matériel • Mode admin • Rôle • Filière)* | Serveur membre d'un Domaine hébergeant Active Directory (`AD`), filière Master 01. |
| **Nommage PC Client** | `PDT-ETU-M1IABD` / `M1RSI` *(Type matériel • User • Filière/Spé)* | Poste de travail étudiant de la filière M1 IABD ou M1 RSI. |
| **Paramètres IP (bas gauche)** | `@IP : 10.10.10.1/24` ; `MS : 255.255.255.0` ; `GTW : 10.10.10.1/24` ; `DNS 1 : 10.10.10.1/24` ; `DNS 2 : 8.8.8.8` | Plan d'adressage statique du 1er serveur *(sans saisir `/24` dans GTW/DNS sous Windows)*. |
| **Config matérielle VM** | `SRV` : RAM ≥ 4 Go, HD ≥ 15 Go, Display `Std`, Rés `Local Net` • `PC` : RAM 4 Go, HD 15–20 Go | Ressources allouées aux VMs *(prévoir 32–40 Go dynamiques si Windows Server avec interface graphique)*. |

---

## 💡 1. Lexique de Révision

> [!tip] Mémo rapide pour le cours & les TP
> | Terme / Sigle | Définition simple (en une phrase) |
> | :--- | :--- |
> | **`@IP` (Adresse IP)** | Numéro d'identification unique d'une machine pour communiquer sur un réseau. |
> | **`MS` (Masque de sous-réseau)** | Filtre (`255.255.255.0`) qui sépare l'identifiant du **réseau** et l'identifiant de la **machine**. |
> | **`/24` (Notation CIDR)** | Raccourci indiquant que les **24 premiers bits** (sur 32) de l'adresse IP identifient le réseau. |
> | **`GTW` (Gateway / Passerelle)** | Adresse IP du routeur par lequel sortent les paquets destinés à un **autre** réseau (ex. Internet). |
> | **`DNS 1 / DNS 2`** | Annuaire traduisant un nom (`SRV-DMAD-MSTR01`) en adresse IP (`10.10.10.1`). |
> | **`SRV` / `PDT`** | Codes de nommage normalisés : **Serveur** (`SRV`) et **Poste De Travail** (`PDT`). |
> | **`DM` (Domaine)** | Mode d'administration centralisée où un serveur commande l'authentification et les règles de tout le parc. |
> | **`AD` (Active Directory)** | Service d'annuaire Microsoft gérant utilisateurs, ordinateurs, mots de passe, droits et stratégies (GPO). |
> | **`Workgroup` vs `Domaine`** | En *Workgroup*, chaque PC est autonome (comptes locaux) ; en *Domaine*, tout est centralisé sur le serveur AD. |
> | **`Local Net` (Host-Only / LAN Segment)** | Réseau virtuel isolé reliant uniquement tes VMs entre elles sans toucher le Wi-Fi/LAN physique. |
> | **Hyperviseur Type 1 vs Type 2** | **Type 1** (ESXi, Proxmox) s'installe nu sur le serveur physique ; **Type 2** (Workstation) tourne sur un OS existant. |
> | **`P2V` (*Phy to Vi*)** | Opération consistant à cloner un vrai serveur physique pour en faire une machine virtuelle. |
> | **`OSI` vs `TCP/IP`** | Modèles en couches (7 pour OSI, 4 pour TCP/IP) découpant le voyage d'une donnée du câble jusqu'à l'application. |

---

## 🛠️ 2. Explications Terre à Terre & Exemples Pas-à-Pas

### A. Adressage IP & Masque de sous-réseau (`10.10.10.1/24` et `255.255.255.0`)

> [!note] Comprendre la logique (terre à terre)
> Imagine une adresse IP comme une **adresse postale** composée de deux informations collées ensemble :
> 1. Le **nom du quartier / de la rue** (la **partie Réseau**) ;
> 2. Le **numéro de la maison** dans cette rue (la **partie Hôte / Machine**).
>
> Deux personnes habitant la même rue se parlent directement en traversant le trottoir. Si tu veux parler à quelqu'un d'un autre quartier, tu dois prendre le bus au portail du quartier (**la Passerelle**).
> Le **masque de sous-réseau** est simplement la règle qui trace la frontière exacte entre « où s'arrête le nom de la rue » et « où commence le numéro de la maison ».

#### 1. D'où sort `255.255.255.0` quand on écrit `/24` ?
Une adresse IPv4 est toujours codée sur **32 bits** (32 cases contenant soit `1`, soit `0`), rangés en **4 paquets de 8 bits** appelés *octets* :

- `/24` signifie : « Les **24 premiers bits** appartiennent au réseau (on les met à **`1`**), et les **8 derniers bits** ($32 - 24 = 8$) appartiennent aux machines (on les met à **`0`**). »
- Traduction directe octet par octet :
  - Binaire du masque : `11111111 . 11111111 . 11111111 . 00000000`
  - Valeur d'un octet tout à `1` : $128 + 64 + 32 + 16 + 8 + 4 + 2 + 1 = \mathbf{255}$
  - Résultat en décimal : **`255.255.255.0`**

Retiens l'astuce immédiate : partout où le masque vaut **`255`**, le nombre correspondant dans l'IP est **verrouillé** (c'est le nom du réseau). Partout où il vaut **`0`**, le nombre est **libre** pour numéroter tes machines.

#### 2. Méthode en 4 étapes : comment tout trouver à partir de `10.10.10.1/24`

Prenons l'exemple exact du tableau : **`10.10.10.1/24`** (masque **`255.255.255.0`**).

1. **Étape 1 — Couper l'adresse selon le masque :**
   ```text
   Adresse IP :   10  .  10  .  10  .  1
   Masque     :  255  . 255  . 255  .  0
                 └───────┬───────┘   └─┬─┘
                   Partie RÉSEAU    Partie HÔTE
                 (verrouillée)      (libre : 8 bits)
   ```
2. **Étape 2 — Trouver l'Adresse du Réseau (nom de la rue) :**
   On met toute la partie hôte à **0** (le plus petit chiffre possible).
   $\implies$ Adresse réseau = **`10.10.10.0`** *(c'est l'étiquette du réseau, interdite sur une carte réseau).*
3. **Étape 3 — Trouver l'Adresse de Broadcast (diffusion générale) :**
   On met toute la partie hôte au **maximum** (`11111111` en binaire = `255`).
   $\implies$ Adresse de broadcast = **`10.10.10.255`** *(sert à crier un message à toutes les machines du réseau d'un coup, également interdite sur un PC).*
4. **Étape 4 — Trouver la plage utilisable et le nombre de machines :**
   On prend tout ce qui est strictement compris entre l'adresse réseau (`.0`) et le broadcast (`.255`) :
   - **Première IP utilisable :** `10.10.10.1` *(celle que le prof attribue au serveur !)*
   - **Dernière IP utilisable :** `10.10.10.254`
   - **Nombre total d'IP attribuables :** $2^{(32 - 24)} - 2 = 2^8 - 2 = 256 - 2 = \mathbf{254}$ machines *(on enlève toujours 2 : la première `.0` pour le réseau et la dernière `.255` pour le broadcast)*.

#### 3. Exemples comparatifs pour savoir calculer d'autres masques

Que se passe-t-il si le `/x` n'est pas un multiple de 8 ? On applique exactement la même règle binaire sur le dernier octet découpé (valeurs des 8 bits de gauche à droite : **`128 | 64 | 32 | 16 | 8 | 4 | 2 | 1`**) :

| Notation CIDR | Masque décimal | Bits hôtes ($32 - n$) | Nombre d'IP utilisables ($2^h - 2$) | Exemple de sous-réseau(x) pour `10.10.10.x` |
| :---: | :--- | :---: | :---: | :--- |
| **`/8`** | `255.0.0.0` | $24$ | $16\,777\,214$ | Réseau `10.0.0.0` $\to$ utilisables `10.0.0.1` à `10.255.255.254` |
| **`/16`** | `255.255.0.0` | $16$ | $65\,534$ | Réseau `10.10.0.0` $\to$ utilisables `10.10.0.1` à `10.10.255.254` |
| **`/24`** | `255.255.255.0` | $8$ | **$254$** | **Cas du TP :** `10.10.10.0` $\to$ `10.10.10.1` à `10.10.10.254` |
| **`/25`** | `255.255.255.128` | $7$ | $126$ | Coupe en 2 blocs de 128 : **`.1` à `.126`** (rés. `.0`, bcast `.127`) et **`.129` à `.254`** (rés. `.128`, bcast `.255`) |
| **`/26`** | `255.255.255.192` | $6$ | $62$ | Coupe en 4 blocs de 64 : `.1–.62`, `.65–.126`, `.129–.190`, `.193–.254` |

*(Comment trouver `128` ou `192` ? Pour `/25`, il y a 1 bit réseau dans le 4e octet $\to 128$ ; pour `/26`, il y en a 2 $\to 128 + 64 = 192$ ; et le « pas » d'un sous-réseau vaut toujours $256 - \text{octet du masque}$, soit $256 - 192 = 64$ !)*

#### 4. Comment savoir si deux machines peuvent se parler directement ?
On compare leur **partie Réseau** (ce qui correspond aux `255` du masque) :
- **Cas A (Direct) :** Serveur `10.10.10.1/24` et PC client `10.10.10.25/24` $\implies$ même partie réseau `10.10.10`. Ils sont dans le même sous-réseau et communiquent **directement via le switch virtuel** sans passer par un routeur.
- **Cas B (Routeur obligatoire) :** Serveur `10.10.10.1/24` et PC `10.10.20.25/24` $\implies$ le 3e octet diffère (`10` vs `20`) alors que le masque `/24` verrouille les 3 premiers octets. Ils ne sont **pas dans le même réseau** : sans passerelle (routeur), le `ping` échoue avec *Délai d'attente dépassé* ou *Hôte de destination inaccessible*.

---

### B. La Passerelle par défaut (`GTW : 10.10.10.1`)

> [!note] Comprendre la logique (terre à terre)
> La passerelle (*Gateway*) est la **porte de sortie du quartier**.
> - Tant que le PC `10.10.10.2` parle au serveur `10.10.10.1`, il n'utilise pas la passerelle.
> - Dès que le PC veut joindre `8.8.8.8` (Google, qui n'est pas dans `10.10.10.x`), il envoie le paquet à l'adresse de sa passerelle (`10.10.10.1`), en comptant sur elle pour savoir acheminer le trafic dehors.

- Dans un lab VMware isolé (`Local Net`), on met souvent l'IP du serveur lui-même (`10.10.10.1`) comme passerelle (en prévision d'un futur rôle *Routage et accès distant* sous Windows Server).
- **Piège pratique sur le tableau :** Le prof a noté `GTW : 10.10.10.1/24` et `DNS 1 : 10.10.10.1/24` par habitude de notation, mais sous Windows, **on ne saisit jamais `/24`** dans les champs Passerelle et DNS (les cases acceptent uniquement `10.10.10.1`). Le masque ne se renseigne que dans le champ dédié (`255.255.255.0`).

---

### C. Le DNS (`DNS 1 : 10.10.10.1`, `DNS 2 : 8.8.8.8`) et Active Directory

> [!note] Comprendre la logique (terre à terre)
> Le DNS est le **répertoire de contacts de ton téléphone**. Tu cliques sur « Maman », le téléphone compose `+228 90 ...`. Sur le réseau, tu tapes `google.com` ou `SRV-DMAD-MSTR01`, le DNS traduit en `142.250...` ou `10.10.10.1`.

Pourquoi le serveur (`10.10.10.1`) met-il **sa propre IP (`10.10.10.1`) en DNS 1** ?
1. **Règle d'or Windows Server :** Active Directory (AD) ne peut pas fonctionner sans DNS. Quand un PC client voudra rejoindre le domaine (ex. `m1it.local`), il demandera au DNS : *« Donne-moi l'adresse du contrôleur de domaine qui gère `m1it.local` »* (via des enregistrements spéciaux appelés enregistrements `SRV`, ex. `_ldap._tcp.dc._msdcs`).
2. Si le PC client n'interroge que `8.8.8.8` (Google), Google répondra qu'il ne connaît pas ton domaine local et **la jonction au domaine échouera systématiquement**.
3. **Et `DNS 2 : 8.8.8.8` alors ?** En TP, on l'ajoute parfois pour atteindre Internet si la VM a un accès NAT, mais **bonne pratique RSSI / production :** ne mets **que `10.10.10.1`** sur la carte réseau des PC et du serveur AD, et configure `8.8.8.8` comme **redirecteur (*Forwarder*)** à l'intérieur de la console DNS de Windows Server. Ainsi, ton serveur résout tout ce qui est interne, et transfère uniquement les noms Internet vers `8.8.8.8`.

---

### D. Décodage de la Convention de Nommage & Active Directory

```text
1er Serveur :   SRV  -  DM      AD   -  MSTR01
                 │       │       │        │
                 │       │       │        └─ Filière / N° (Master 01)
                 │       │       └────────── Rôle (Active Directory)
                 │       └────────────────── Mode d'administration (Domaine)
                 └────────────────────────── Type de matériel (Serveur)

PC Client   :   PDT  -  ETU  -  M1IABD   (ou M1RSI)
                 │       │        │
                 │       │        └───────── Filière / Spécialité
                 │       └────────────────── Type d'utilisateur (Étudiant)
                 └────────────────────────── Type de matériel (Poste De Travail)
```

| Critère | Mode **Workgroup** (Groupe de travail) | Mode **Domaine** (Active Directory) |
| :--- | :--- | :--- |
| **Où sont les comptes ?** | En local sur chaque PC (tu dois recréer ton compte sur chaque machine). | Centralisés sur le **Contrôleur de Domaine (`SRV-DMAD-...`)**. |
| **Sécurité & Règles** | Configurée PC par PC manuellement. | Déployée à tout le parc d'un clic via des **GPO** (mots de passe, blocage USB, mappages lecteurs). |
| **Départ d'un employé** | Il faut aller supprimer son compte sur chaque PC / serveur. | Le RSSI désactive **1 seul compte** dans l'AD $\implies$ accès coupé partout instantanément. |

---

### E. Architecture de Virtualisation & Configuration Exacte du Lab

```text
   HYPERVISEUR TYPE 2 (Ton Lab sur Laptop)       HYPERVISEUR TYPE 1 (Datacenter / Entreprise)
  ┌───────────────────────────────────────┐     ┌───────────────────────────────────────────┐
  │  [ VM Serveur ]       [ VM Client ]   │     │  [ VM Serveur 1 ]      [ VM Serveur 2 ]   │
  │    Windows Srv          Windows 10/11 │     │   (vCenter administre plusieurs ESXi)     │
  ├───────────────────────────────────────┤     ├───────────────────────────────────────────┤
  │    VMware Workstation (Logiciel)      │     │   VMware ESXi 7 / Proxmox VE 9 / Xen      │
  ├───────────────────────────────────────┤     ├───────────────────────────────────────────┤
  │    Ton OS hôte (Windows 11 / Linux)   │     │        (Aucun OS hôte intermédiaire)       │
  ├───────────────────────────────────────┤     ├───────────────────────────────────────────┤
  │  Matériel Laptop (RAM 16 Go, SSD)     │     │    Matériel Serveur Physique (Dell/HPE)   │
  └───────────────────────────────────────┘     └───────────────────────────────────────────┘
```

- **P2V (*Physical to Virtual*) :** Technique consistant à convertir un serveur physique vieillissant (avec son OS, ses logiciels et ses données déjà installés) en un fichier de machine virtuelle prêt à tourner sur ESXi ou Proxmox, sans devoir tout réinstaller de zéro.
- **Pourquoi choisir le mode réseau `Local Net` (*Host-Only* ou *LAN Segment*) ?** Pour enfermer les VMs dans une bulle réseau privée. Quand tu installeras plus tard un service **DHCP** sur ton serveur Windows, il ne risque pas de distribuer de fausses adresses IP aux vrais PC de la salle de classe ou de ta maison (ce qui couperait le réseau réel !).

#### Fiche de déploiement prête à copier dans VMware Workstation

| Paramètre VM / Réseau | **VM 1 : 1er Serveur** | **VM 2 : Poste Client** *(pour le TP)* |
| :--- | :--- | :--- |
| **Nom machine (Hostname)** | `SRV-DMAD-MSTR01` | `PDT-ETU-M1IABD` *(ou `M1RSI`)* |
| **RAM allouée** | `4 Go` (minimum `4096 Mo`) | `4 Go` (`4096 Mo`, ou `2 Go` si ton PC manque de RAM) |
| **Disque dur virtuel (HD)** | `≥ 15 Go` *(prévoir **40 Go** dynamique si GUI)* | `15 à 20 Go` *(prévoir **30–40 Go** pour Win 10/11)* |
| **Affichage (`Display`)** | Standard (`Std`) | Standard (`Std`) |
| **Carte réseau VMware** | `Local Net` (*LAN Segment* ou *Host-Only*) | **Même** `Local Net` que le serveur |
| **Adresse IP (`@IP`)** | `10.10.10.1` | `10.10.10.2` *(ou toute IP de `.2` à `.254`)* |
| **Masque (`MS`)** | `255.255.255.0` | `255.255.255.0` |
| **Passerelle (`GTW`)** | `10.10.10.1` | `10.10.10.1` |
| **DNS préféré (`DNS 1`)** | `10.10.10.1` *(ou `127.0.0.1` avant promo AD)* | **`10.10.10.1`** *(obligatoire pour trouver le domaine !)* |
| **DNS auxiliaire (`DNS 2`)** | `8.8.8.8` *(ou vide / en redirecteur DNS)* | *(laisser vide sur le client en domaine)* |

---

### F. Mémo des Prérequis Réseau (Modèle OSI & Dépannage Windows)

En cas de panne entre tes deux VMs, on remonte les couches du **modèle OSI** une par une (de la couche 1 vers la couche 7) :

| Couche OSI | Rôle concret | Ce qu'on vérifie en TP Windows | Commande Windows / PowerShell |
| :--- | :--- | :--- | :--- |
| **1. Physique** | Câble, carte réseau branchée | La carte réseau VMware est-elle « Connectée » (`Connected`) ? | Icône réseau / `Get-NetAdapter` |
| **2. Liaison** | Adresses MAC, switch local | Le PC client voit-il la table MAC de l'autre VM ? | `arp -a` |
| **3. Réseau** | Adresses **IP**, masques, routage | Les deux VMs ont-elles la bonne IP dans `10.10.10.0/24` ? Le ping passe ? *(Attention au pare-feu Windows !)* | `ipconfig /all`, `ping 10.10.10.1`, `tracert` |
| **4. Transport** | Ports **TCP / UDP** (ex. DNS 53, LDAP 389) | Le service écoute-t-il bien sur le port attendu ? | `Test-NetConnection 10.10.10.1 -Port 53` |
| **7. Application** | Services finaux (**DNS, HTTP, SMB, AD**) | Le serveur DNS répond-il bien à une requête de nom ? | `nslookup srv-dmad-mstr01` |

*(Note sur **IPv4 vs IPv6** : IPv4 utilise 32 bits comme `10.10.10.1`, mais ses ~4,3 milliards d'adresses publiques sont épuisées ; IPv6 utilise 128 bits en hexadécimal, ex. `fe80::...` visible dans `ipconfig`.)*

---

## 🧠 3. Batterie d'Active Recall (Questions d'Auto-Évaluation)

> *Masquer la section 2 et répondre directement à ces questions.*

- [ ] **Q1 : Pour l'adresse `10.10.10.1/24` écrite au tableau, quel est le masque en décimal, l'adresse réseau, l'adresse de broadcast et combien de machines peuvent recevoir une IP ?**
  - *Réponse flash :* Masque `255.255.255.0` ; adresse réseau `10.10.10.0` ; broadcast `10.10.10.255` ; $2^8 - 2 = \mathbf{254}$ machines utilisables (de `.1` à `.254`).
- [ ] **Q2 : Une machine configurée en `10.10.10.50/24` veut envoyer des données à `10.10.11.50/24`. Communiquent-elles directement ou passent-elles par la passerelle ? Pourquoi ?**
  - *Réponse flash :* Elles passent par la **passerelle**, car avec un masque `/24` (`255.255.255.0`), les trois premiers octets identifient le réseau : `10.10.10` $\ne$ `10.10.11`, ce sont donc deux réseaux distincts.
- [ ] **Q3 : Quelle IP configures-tu sur le PC client `PDT-ETU-M1IABD` pour qu'il puisse joindre le domaine géré par `SRV-DMAD-MSTR01`, et que mets-tu obligatoirement dans son champ `DNS 1` ?**
  - *Réponse flash :* IP entre `.2` et `.254` (ex. `10.10.10.2`), masque `255.255.255.0`, passerelle `10.10.10.1`, et **`DNS 1 = 10.10.10.1`** (l'IP du serveur AD/DNS, jamais `8.8.8.8` seul, sinon le client ne trouvera jamais le contrôleur de domaine).
- [ ] **Q4 : Décode `SRV-DMAD-MSTR01` segment par segment.**
  - *Réponse flash :* `SRV` = Serveur (type de matériel), `DM` = Domaine (mode d'administration), `AD` = Active Directory (rôle), `MSTR01` = Master 01 (filière).
- [ ] **Q5 : Quelle est la différence entre VMware Workstation (utilisé en classe) et VMware ESXi / Proxmox VE ?**
  - *Réponse flash :* Workstation est un hyperviseur de **Type 2** (installé par-dessus Windows/Linux sur ton PC). ESXi et Proxmox VE sont des hyperviseurs de **Type 1** (installés directement sur le matériel nu d'un serveur de datacenter).
- [ ] **Q6 : Pourquoi met-on les VMs du lab en réseau `Local Net` (*Host-Only* / *LAN Segment*) plutôt qu'en mode Pont (*Bridged*) sur le Wi-Fi de l'école ?**
  - *Réponse flash :* Pour isoler les VMs dans un réseau fermé afin qu'un futur serveur **DHCP** ou **DNS** monté en TP ne perturbe pas les autres ordinateurs connectés au réseau physique de l'école.
- [ ] **Q7 : Que signifie l'expression « Phy to Vi » (`P2V`) citée par M. Mensah dans les prérequis ?**
  - *Réponse flash :* *Physical to Virtual* : convertir un serveur physique existant (système, applis et données inclus) en une machine virtuelle hébergée sur un hyperviseur.
- [ ] **Q8 : Si `ping 10.10.10.1` fonctionne mais que `ping srv-dmad-mstr01` échoue, quelle couche / quel service est en cause ?**
  - *Réponse flash :* Le réseau IP (couche 3) fonctionne, c'est la **résolution de noms (DNS — couche 7)** qui est mal configurée.

---

## ⚡ 4. Prochaines Actions
- [ ] Récupérer le syllabus officiel / support de cours de M. Mensah dès sa diffusion et le déposer dans le dossier du module.
- [ ] Tester la création des deux VMs (`SRV-DMAD-MSTR01` et `PDT-ETU-M1IABD`) dans VMware Workstation avec le plan `10.10.10.0/24` sur réseau `Local Net`.
