---
type: note-cours
created: 2026-11-25
matiere: "Architecture Système et Réseau Windows"
chapitre: "01 - Architecture, Installation et Configuration de Windows Server"
enseignant: "M. Marney Elom MENSAH"
tags:
  - etudes
  - cours
  - windows-server
  - active-directory
  - powershell
  - reseau
  - revision
  - active-recall
parent: "[[MOC_Architecture_Systeme_et_Reseau_Windows]]"
---

# 📖 Chapitre 1 — Architecture, Installation et Configuration de Windows Server

> ↖ [[MOC_Architecture_Systeme_et_Reseau_Windows|Hub du Module]] • [[01_Cadrage_Lab_Adressage_IP_&_Fondamentaux_Windows|Notes du Tableau (Séance 1)]] • [[Questionnaire_Revision_Chapitre_1|📝 Questionnaire & Exercices de Révision]]
> **Matière :** Architecture Systèmes et Windows (Master 1 – IT, ASCENCIA KEYCE) • **Enseignant :** M. Marney Elom MENSAH • **Environnement de référence :** Windows Server 2022

---

## 💡 0. Glossaire & Mémo Rapide (§1.16)

> [!tip] Les 15 termes essentiels à maîtriser
> | Terme | Définition à retenir |
> | :--- | :--- |
> | **`AD DS`** | *Active Directory Domain Services* : service d'annuaire stockant les objets du domaine et assurant l'authentification/autorisation. |
> | **`ACL`** | *Access Control List* : liste de contrôle d'accès attribuant les permissions sur une ressource (NTFS/partages). |
> | **`DC`** | *Domain Controller* (Contrôleur de domaine) : serveur promu exécutant les fonctions d'annuaire AD DS. |
> | **`Desktop Experience`** | Option d'installation Windows Server incluant le bureau graphique complet (`GUI`), Server Manager et les consoles locales. |
> | **`DNS`** | Service de résolution de noms et de localisation des services (indispensable à AD via les enregistrements `SRV`). |
> | **`GUI`** | *Graphical User Interface* : interface utilisateur graphique. |
> | **`Hyperviseur`** | Logiciel/couche permettant d'exécuter plusieurs machines virtuelles isolées sur un hôte physique. |
> | **`IP statique`** | Adresse IP configurée de façon fixe sur une interface réseau (obligatoire pour un futur DC/DNS). |
> | **`MMC`** | *Microsoft Management Console* : infrastructure hébergeant les composants d'administration (*snap-ins* `.msc`). |
> | **`NAT`** | *Network Address Translation* : traduction d'adresses réseau fournie par l'hyperviseur pour sortir vers l'extérieur. |
> | **`PowerShell`** | Shell et langage d'administration orienté objets (pipeline d'objets et non de simple texte). |
> | **`RSAT`** | *Remote Server Administration Tools* : outils d'administration distante de serveurs. |
> | **`Server Core`** | Option d'installation Windows Server sans bureau graphique complet (administrée via Sconfig, PowerShell et outils distants). |
> | **`VM`** | Machine virtuelle exécutée sur un hyperviseur. |
> | **`WinRM`** | *Windows Remote Management* : service de gestion distante Windows (port `5985 TCP` en HTTP). |

---

## 🏛️ 1. Rôle de Windows Server & Architecture Client–Serveur (§1.1)

### A. Serveur, système d'exploitation serveur et service
- **Serveur :** système physique ou virtuel mettant des ressources à disposition d'autres équipements appelés **clients** (comptes, dossiers partagés, adresses IP, authentification, applications, bases de données).
- **Système d'exploitation serveur :** couche logicielle qui assure la gestion du matériel, des processus, du réseau, de la sécurité et des fonctions nécessaires à la fourniture de ces services.
- **Windows Server :** élément structurant d'une architecture d'entreprise (et non un simple poste Windows enrichi) : il doit être **nommé, sécurisé, documenté, supervisé et sauvegardé**.

> [!important] Idée essentielle
> Un serveur Windows ne tire pas sa valeur de sa seule puissance matérielle, mais des **services partagés**, de l'**administration cohérente** et de la **gouvernance des accès** qu'il apporte.

### B. Architecture client–serveur et centralisation

| Fonction | Rôle côté serveur | Exemple d'usage |
| :--- | :--- | :--- |
| **Identité** | Contrôler les comptes et l'authentification | Ouverture de session sur un poste du domaine |
| **Nommage** | Résoudre des noms et localiser des services | Trouver le contrôleur de domaine par DNS |
| **Adressage** | Distribuer les configurations IP autorisées | Attribuer une adresse à un poste par DHCP |
| **Fichiers** | Publier des dossiers avec des permissions | Accès au partage du service RH |
| **Administration** | Appliquer des paramètres à plusieurs postes | Politique de mot de passe ou de pare-feu (GPO) |
| **Virtualisation** | Exécuter plusieurs systèmes isolés sur un hôte | Héberger plusieurs VMs sur un hyperviseur |

### C. Les 6 principes de conception d'une infrastructure professionnelle
1. **Disponibilité :** service accessible au besoin (supervision, prévention des défaillances, rétablissement).
2. **Confidentialité :** accès strictement limité aux personnes autorisées.
3. **Intégrité :** configurations et données exactes, traçables et protégées contre toute modification non autorisée.
4. **Maintenabilité :** nommage cohérent, documentation et automatisation pour réduire l'erreur humaine.
5. **Évolutivité :** ajout d'utilisateurs, services ou sites sans tout reconstruire.
6. **Résilience :** stratégie de sauvegarde, plan de restauration et redondance pensés *avant* l'incident.

---

## 📦 2. Éditions Windows Server et Options d'Installation (§1.2)

Il s'agit de **deux décisions indépendantes** :
- L'**édition** définit les droits d'usage, de virtualisation et certaines fonctionnalités.
- L'**option d'installation** définit la présence ou l'absence d'interface graphique complète.

### A. Comparatif des éditions

| Édition | Positionnement pédagogique | Points d'attention |
| :--- | :--- | :--- |
| **Standard** | Serveurs d'entreprise et virtualisation modérée | Les droits de virtualisation dépendent des licences couvrant les cœurs de l'hôte et des conditions Microsoft (ne pas interpréter « 2 VMs » comme une limite matérielle universelle). |
| **Datacenter** | Hôtes à forte densité de virtualisation et services de datacenter | Droits de virtualisation étendus conditionnés aux licences correspondantes et au respect des termes d'usage. |
| **Essentials** | Offre destinée à certains contextes de petites organisations selon la version | Vérifier la disponibilité, les limites et les modalités propres à la version considérée. |

### B. Desktop Experience (GUI) vs Server Core

| Critère | Desktop Experience (GUI) | Server Core |
| :--- | :--- | :--- |
| **Interface** | Bureau, menus, consoles locales, Server Manager | Pas de bureau graphique complet |
| **Administration** | Interface graphique et PowerShell | `Sconfig`, PowerShell et outils distants (RSAT) |
| **Surface d'attaque** | Composants graphiques supplémentaires | Moins de composants locaux à maintenir/corriger |
| **Formation** | Approche intuitive pour découvrir les consoles | Entraînement à l'automatisation |
| **Cas d'usage** | Applications ou logiciels métier exigeant une GUI | Services d'infrastructure compatibles (DNS, AD DS, fichiers) gérés à distance |
| **Changement ultérieur** | Passage vers Core **non prévu sans réinstallation** | Passage vers GUI **non prévu sans réinstallation** |

> [!warning] Idées reçues à éviter
> - Il n'existe **pas de gain uniforme de « 40 % de ressources »** valable partout pour Server Core : le gain dépend du rôle, de la charge, des mises à jour et des composants installés.
> - Server Core **ne garantit pas à lui seul la sécurité** : il réduit les composants graphiques, mais doit toujours être configuré, durci et maintenu à jour.
> - En Windows Server 2022/2025, le basculement GUI $\leftrightarrow$ Core après installation n'est **pas pris en charge** : le choix initial est structurant.

### C. Démarche de décision en 5 étapes
1. Recenser les applications, rôles et contraintes de compatibilité.
2. Vérifier les exigences d'administration, d'exploitation et de support.
3. Choisir l'**édition** selon l'échelle et les droits de licence.
4. Choisir **GUI ou Core** selon les fonctionnalités requises et les compétences disponibles.
5. Documenter le choix, les risques et la stratégie de maintenance.

---

## ⚙️ 3. Architecture Interne & Composants Critiques (§1.3)

1. **Noyau Windows NT :** gère l'ordonnancement des processeurs, la mémoire virtuelle, les interruptions et la synchronisation, en reliant les applications au matériel. Une panne matérielle, un pilote défectueux ou une pression mémoire peut donc affecter plusieurs services simultanément.
2. **Services et processus Windows :** programmes en arrière-plan dotés d'un nom, d'un état, d'un type de démarrage et parfois de dépendances. *Ne jamais désactiver un service simplement parce que son nom est inconnu.*

| Service / composant | Fonction | À observer |
| :--- | :--- | :--- |
| **`W32Time`** | Synchronisation de l'horloge | État, source de temps, dérive (critique pour Kerberos) |
| **`WinRM`** | Administration distante | Statut, écoute et règles de pare-feu |
| **`DNS`** | Service de noms (si rôle installé) | Résolution, zones, journaux |
| **`Netlogon`** | Fonctions de domaine sur un DC | À interpréter *après* promotion |
| **`Event Log`** | Collecte des événements Windows | Journaux Système / Application / Sécurité |

3. **Registre Windows :** base hiérarchique de paramètres :
   - `HKLM` (*HKEY_LOCAL_MACHINE*) : paramètres locaux de la machine.
   - `HKCU` (*HKEY_CURRENT_USER*) : vue des paramètres de l'utilisateur courant.
   - Modification directe exceptionnelle, documentée et précédée d'une sauvegarde.
4. **Système de fichiers NTFS & sécurité :** permissions, journalisation et **ACL** décrivant quels comptes/groupes peuvent lire, modifier ou exécuter une ressource (éviter d'attribuer des droits à « Tout le monde » par facilité).
5. **Journaux et observabilité :** Observateur d'événements et `Get-WinEvent`. Un événement n'est pas une cause en soi : il faut recouper horodatages, niveau, source et changements récents.

```powershell
# Services critiques et registre en lecture seule
Get-Service -Name W32Time,WinRM
Get-Service | Where-Object Status -eq "Running" | Select-Object -First 10 Name,Status
Get-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion" | Select-Object ProductName,CurrentBuild
Get-WinEvent -LogName System -MaxEvents 8 | Select-Object TimeCreated,Id,LevelDisplayName,ProviderName
```

---

## 🧩 4. Rôles Serveur, Fonctionnalités & Préparation AD DS / DNS (§1.4)

- **Rôle serveur :** ensemble de composants fournissant un service principal aux utilisateurs ou applications.
- **Fonctionnalité :** composant complémentaire facilitant l'administration ou ajoutant une capacité transverse.

| Élément | Type | Mission principale |
| :--- | :--- | :--- |
| **Active Directory Domain Services (AD DS)** | Rôle | Stocker les objets d'annuaire, participer à l'authentification et à l'autorisation |
| **DNS Server** | Rôle | Répondre aux requêtes de résolution de noms |
| **DHCP Server** | Rôle | Fournir automatiquement des paramètres IP aux clients |
| **File and Storage Services** | Rôle / services | Exposer et gérer des ressources de stockage |
| **Hyper-V** | Rôle | Héberger des machines virtuelles compatibles |
| **IIS** | Rôle | Héberger des applications et services web |
| **RSAT / outils AD PowerShell** | Fonctionnalités / outils | Administrer des rôles localement ou à distance |
| **Failover Clustering** | Fonctionnalité | Créer une infrastructure de cluster de basculement |

### Distinction critique : Installer AD DS ≠ Promouvoir un DC
- **Installer le rôle AD DS** (`Install-WindowsFeature -Name AD-Domain-Services`) : prépare uniquement les fichiers binaires et les outils. **Ne crée ni forêt ni domaine fonctionnel** (c'est l'objectif maximal de la séance 1).
- **Promouvoir en contrôleur de domaine** (`Install-ADDSForest`, étudié en séance 2) : construit ou rejoint l'annuaire et active le domaine.

### Pourquoi le DNS est déterminant pour AD DS
Les clients localisent les contrôleurs de domaine par des requêtes DNS contenant des enregistrements de service (**`SRV`**). Une erreur DNS bloque l'ouverture de session même si le ping IP répond.

> [!warning] Point critique : quatre états DNS distincts à ne jamais confondre
> 1. Rôle DNS **installé** (`InstallState = Installed`).
> 2. Service DNS **démarré**.
> 3. Zone DNS **configurée**.
> 4. **Résolution du domaine réussie** (ex. `nslookup ad.ascencia.test` n'est **pas exigible** avant la promotion du DC en séance 2).

---

## 🌐 5. Virtualisation, Topologie & Préparation Réseau (§1.5–1.6)

### A. Modes réseau d'une machine virtuelle

| Mode | Principe | Risque / utilisation pédagogique |
| :--- | :--- | :--- |
| **Réseau interne / Host-only** | Communication entre VMs (et parfois l'hôte), sans accès au LAN réel | **Mode conseillé** pour isoler le TP ; pas de passerelle sans routeur |
| **NAT** | Sortie par traduction d'adresses via l'hyperviseur | Utile pour mises à jour si maîtrisé |
| **Pont / Bridged** | VM directement visible sur le réseau physique | **À éviter** pour les TP AD/DHCP hors autorisation (risque de conflit et de distribution DHCP pirate) |

### B. Topologie & plan d'adressage de référence du support

```text
RÉSEAU DE LABORATOIRE ISOLÉ — 192.168.10.0/24 (Masque 255.255.255.0)
┌────────────────────┐      ┌────────────────────┐      ┌────────────────────┐
│     SRV-AD-01      │      │    SRV-CORE-01     │      │  PC-IT-01 (option) │
│ Windows Server GUI │      │ Windows Server Core│      │     Windows 11     │
│  192.168.10.10/24  │      │  192.168.10.20/24  │      │  192.168.10.30/24  │
└─────────┬──────────┘      └─────────┬──────────┘      └─────────┬──────────┘
          │                           │                           │
          └───────────────────────────┼───────────────────────────┘
                                      │
                             [ Commutateur SW-LAB ]
              (Sans passerelle si aucun routeur NAT n'est présent)
```

| Machine | Nom d'hôte | Adresse IPv4 | DNS client avant / après promotion |
| :--- | :--- | :--- | :--- |
| **VM 1 (GUI)** | `SRV-AD-01` | `192.168.10.10/24` | `192.168.10.10` une fois DNS configuré (résolution AD non disponible avant promotion) |
| **VM 2 (Core)** | `SRV-CORE-01` | `192.168.10.20/24` | `192.168.10.10` lorsque le DNS interne fonctionne |
| **Poste test (option)** | `PC-IT-01` | `192.168.10.30/24` | `192.168.10.10` après installation/configuration DNS |

- **Domaine prévu (séance 2) :** `ad.ascencia.test` (nom fictif réservé au labo).
- **Convention de nommage :** `SRV-ROLE-NN` (court, unique, descriptif ; réduit les erreurs d'inventaire et d'incident).
- **Passerelle par défaut :** sert uniquement à joindre d'autres réseaux. Dans un réseau interne isolé sans routeur réel, **on ne renseigne pas de passerelle fictive**.
- **Erreur classique à éviter :** reprendre `192.168.10.10` sur les deux serveurs $\implies$ **conflit IP**.

> [!note] Articulation avec les notes du tableau oral
> Lors du cours oral ([[01_Cadrage_Lab_Adressage_IP_&_Fondamentaux_Windows|fiche tableau]]), l'enseignant avait illustré un autre exemple de plan (`10.10.10.1/24`, `SRV-DMAD-MSTR01`, `PDT-ETU-M1IABD`). Pour le polycopié officiel et les exercices/TP du Chapitre 1, la référence est **`192.168.10.0/24`** (`SRV-AD-01`, `SRV-CORE-01`, `ad.ascencia.test`).

### C. Principaux ports et protocoles à connaître

| Service | Port(s) courants | Utilité |
| :--- | :--- | :--- |
| **DNS** | `53 TCP/UDP` | Résolution de noms et transferts de zone |
| **DHCPv4** | `67/68 UDP` | Échanges client/serveur d'adressage |
| **Kerberos** | `88 TCP/UDP` | Authentification de domaine |
| **NTP / W32Time** | `123 UDP` | Synchronisation de l'heure |
| **LDAP** | `389 TCP/UDP` | Accès annuaire / opérations associées |
| **LDAPS** | `636 TCP` | LDAP protégé par TLS (avec certificat valide) |
| **RPC Endpoint Mapper** | `135 TCP` | Découverte de services RPC (+ ports dynamiques) |
| **SMB** | `445 TCP` | Accès aux dossiers et ressources partagées |
| **WinRM HTTP** | `5985 TCP` | Administration distante |
| **RDP** | `3389 TCP/UDP` | Session distante (si autorisée et activée) |

---

## 🛠️ 6. Outils Graphiques, Consoles MMC & PowerShell (§1.7–1.8)

### A. Consoles MMC & Sconfig
La **MMC** héberge des composants (*snap-ins*). **Attention :** lancer une console est un simple raccourci ; cela n'installe pas le rôle correspondant.

| Commande / console | Usage principal | Disponibilité |
| :--- | :--- | :--- |
| `ncpa.cpl` | Interfaces réseau | Sur installation GUI |
| `services.msc` | Gestion des services | Console graphique |
| `eventvwr.msc` | Observation des événements | Console graphique |
| `compmgmt.msc` | Administration locale de l'ordinateur | Console graphique |
| `dsa.msc` | Utilisateurs et ordinateurs Active Directory | Après installation outils AD |
| `dnsmgmt.msc` | Console DNS | Après installation outils DNS |
| `gpmc.msc` | Gestion des GPO | Après installation outils GPMC |

Sur **Server Core**, l'outil **`Sconfig`** fournit un menu texte pour la configuration initiale (nom, IP, mises à jour, gestion distante), complété par **PowerShell** et **RSAT** via **WinRM** (à n'activer que dans un périmètre autorisé).

### B. Approche « PowerShell-first »
PowerShell manipule des **objets** via le pipeline (`|`), ce qui assure reproductibilité et traçabilité. Les commandes suivent la convention **`Verb-Noun`** (`Get-Service`, `Install-WindowsFeature`).

| Commande | Rôle pédagogique |
| :--- | :--- |
| `Get-ComputerInfo` | Inventorier la version système et les paramètres |
| `Get-NetAdapter` | Identifier les interfaces réseau et leur alias réel |
| `Get-NetIPConfiguration` | Afficher IP, DNS et passerelle |
| `Get-WindowsFeature` | Lister les rôles/fonctionnalités et leur `InstallState` |
| `Install-WindowsFeature` | Ajouter un rôle ou une fonctionnalité |
| `Get-Service` | Contrôler l'état des services |
| `Get-WinEvent` | Inspecter les journaux récents |
| `Test-NetConnection` | Tester une route, un ping ou un port TCP (`-Port`) |
| `Rename-Computer` | Renommer l'ordinateur (avec `-Restart`) |
| `Get-Help` | Obtenir l'aide et les exemples de syntaxe |

**Règles d'exécution sécurisée :** exécuter en administrateur uniquement si nécessaire ; toujours vérifier le nom exact de l'interface (`"Ethernet"` n'est qu'un exemple) ; inventorier avant de modifier ; journaliser les valeurs initiales ; ne jamais laisser de mot de passe en clair.

---

## 🧪 7. Synthèse TP1, Automatisation & Diagnostic (§1.9–1.12)

### A. Commandes clés du TP1 (SRV-AD-01 & SRV-CORE-01)

```powershell
# 1. Inventaire lecture seule avant toute modification (TP A)
Get-NetAdapter | Format-Table Name,InterfaceDescription,Status,ifIndex
Get-NetIPConfiguration
Get-NetRoute -AddressFamily IPv4 | Select-Object DestinationPrefix,NextHop,RouteMetric

# 2. Configuration IP/DNS/Nom sur SRV-AD-01 (TP B) — adapter .20 et "SRV-CORE-01" pour Core (TP C)
New-NetIPAddress -InterfaceAlias "Ethernet" -IPAddress "192.168.10.10" -PrefixLength 24
Set-DnsClientServerAddress -InterfaceAlias "Ethernet" -ServerAddresses "192.168.10.10"
Rename-Computer -NewName "SRV-AD-01" -Restart

# 3. Installation du rôle AD DS sans promotion sur SRV-AD-01 uniquement (TP D)
Install-WindowsFeature -Name AD-Domain-Services -IncludeManagementTools
Get-WindowsFeature -Name AD-Domain-Services,DNS | Select-Object Name,InstallState

# 4. Vérifications finales (TP E)
Test-Connection -ComputerName 192.168.10.20 -Count 2
Test-NetConnection -ComputerName 192.168.10.10 -Port 5985
```

> [!note] Précaution de déploiement
> Ne jamais cloner une VM déjà intégrée à un domaine sans procédure adaptée (Sysprep/SID) ; ne pas exécuter `Install-ADDSForest` en séance 1.

### B. Script d'inventaire `Inventory-Lab.ps1` (§1.11)
Permet de collecter à l'identique l'état de plusieurs serveurs sans rien modifier (`New-Item -Force`, `$env:COMPUTERNAME`, `Get-Date`, `Join-Path`, `Out-File -Append`, `Get-NetIPConfiguration`, `Get-WindowsFeature`).

### C. Méthode de diagnostic en 4 couches (§1.12)
Toujours partir des faits observables dans l'ordre :
**(1) Machine et carte réseau** $\to$ **(2) Adresse IP et routes** $\to$ **(3) Service visé** $\to$ **(4) Configuration applicative**.

| Symptôme | Hypothèses à vérifier | Contrôles prioritaires |
| :--- | :--- | :--- |
| **Les deux VMs ne communiquent pas** | Réseaux virtuels différents, carte désactivée, ICMP filtré | `Get-NetAdapter`, `Get-NetIPAddress`, réseau hyperviseur, pare-feu |
| **Conflit d'adresse IP** | Même IPv4 sur plusieurs interfaces | Plan IP, `Get-NetIPConfiguration` sur chaque VM |
| **Nom de domaine non résolu** | Zone DNS non créée ou client mal configuré | État service DNS, IP DNS client, existence de la zone |
| **Server Core difficile à administrer** | Alias réseau inconnu ou WinRM non configuré | `Sconfig`, `Get-NetAdapter`, `Get-Service WinRM` |
| **Rôle absent** | Installation échouée ou rôle non sélectionné | `Get-WindowsFeature`, journaux d'installation |
| **Nom serveur ancien après changement** | Redémarrage non effectué | `hostname`, `Rename-Computer`, redémarrage |

> [!tip] Panne ICMP vs Panne TCP
> L'échec d'un `ping` (**ICMP**) ne prouve pas une coupure réseau totale (le pare-feu peut filtrer ICMP), et un `ping` réussi ne prouve pas qu'un service applicatif écoute sur son port **TCP** (`Test-NetConnection -Port`).

---

## ✅ 8. Checklist de Fin de Chapitre & Transition (§1.15)

- [ ] Expliquer le rôle de Windows Server dans une infrastructure client–serveur.
- [ ] Distinguer édition (`Standard`/`Datacenter`) et mode (`GUI`/`Core`) sans les confondre.
- [ ] Reconnaître les composants internes et rôles utiles à la mise en service.
- [ ] Préparer deux VMs avec des noms et adresses IP distincts.
- [ ] Documenter un état réseau et l'interpréter.
- [ ] Installer AD DS sans le promouvoir prématurément.
- [ ] Réaliser des contrôles PowerShell et expliquer un incident simple (4 couches).
- [ ] Rédiger un compte rendu factuel avec preuves et limites.

**Transition vers la Séance 2 :** `SRV-AD-01` sera promu contrôleur de domaine pour créer la forêt/domaine `ad.ascencia.test`, structurer les OU, utilisateurs et groupes, puis intégrer les ressources.

---

## ⚡ 9. Prochaine Action : Passer aux Questionnaires
👉 Ouvre [[Questionnaire_Revision_Chapitre_1|📝 Questionnaire & Études de Cas — Chapitre 1]] pour tester tes connaissances sur les 15 questions, le Mini-QCM, le cas de conflit IP et les 3 études de cas.
