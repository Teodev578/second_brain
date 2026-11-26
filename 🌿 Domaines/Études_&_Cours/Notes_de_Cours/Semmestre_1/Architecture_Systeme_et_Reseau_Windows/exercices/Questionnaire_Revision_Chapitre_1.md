---
type: sujet-corrigé
created: 2026-11-25
matiere: "Architecture Système et Réseau Windows"
chapitre: "01 - Architecture, Installation et Configuration de Windows Server"
enseignant: "M. Marney Elom MENSAH"
tags:
  - etudes
  - exercices
  - sujet-corrige
  - windows-server
  - revision
  - active-recall
parent: "[[MOC_Architecture_Systeme_et_Reseau_Windows]]"
---

# 📝 Questionnaire & Études de Cas de Révision — Chapitre 1

> ↖ [[MOC_Architecture_Systeme_et_Reseau_Windows|Hub du Module]] • [[01_Chapitre1_Architecture_Installation_Configuration_Windows_Server|📖 Fiche de Révision Chapitre 1]]
> **Mode d'emploi :** Répondre d'abord sans déplier les blocs `Corrigé`, puis vérifier chaque point et noter ses écarts.

---

## Partie 1 — 15 Questions de Connaissance (§1.13.1)

- [ ] **01. Quelle est la différence entre un serveur et un système d'exploitation serveur ?**
> [!success]- Corrigé Q01
> Un **serveur** est un système physique ou virtuel qui met des ressources à disposition (comptes, fichiers, IP, applications). Le **système d'exploitation serveur** fournit l'environnement logiciel qui pilote la machine (matériel, processus, réseau, sécurité) et permet la fourniture de ces services.

- [ ] **02. Pourquoi les entreprises centralisent-elles les identités et certaines ressources ?**
> [!success]- Corrigé Q02
> La centralisation simplifie l'administration (ne pas modifier chaque poste manuellement), garantit la cohérence des droits et politiques (stratégies de groupe) et facilite l'audit et la gouvernance des accès.

- [ ] **03. Quelle distinction faites-vous entre une édition Windows Server et une option d'installation ?**
> [!success]- Corrigé Q03
> L'**édition** (`Standard`, `Datacenter`, `Essentials`) concerne les fonctionnalités et les droits d'usage/virtualisation (licences). L'**option d'installation** (`Desktop Experience / GUI` ou `Server Core`) concerne la manière dont Windows est installé et administré (présence ou non d'un bureau graphique complet).

- [ ] **04. Pourquoi Server Core peut-il réduire la surface d'administration exposée ?**
> [!success]- Corrigé Q04
> Server Core comporte moins de composants graphiques locaux installés (moins de logiciels à maintenir et de vecteurs exposés), mais il doit toujours être configuré, durci et corrigé (il ne garantit pas la sécurité à lui seul).

- [ ] **05. Quel est le rôle du noyau Windows NT ?**
> [!success]- Corrigé Q05
> Le noyau gère les fonctions bas niveau : ordonnancement des processeurs (CPU), gestion de la mémoire virtuelle, interruptions et synchronisation, en reliant les applications aux ressources matérielles.

- [ ] **06. Que stocke le registre et pourquoi sa modification exige-t-elle de la prudence ?**
> [!success]- Corrigé Q06
> Le registre est une base hiérarchique stockant les paramètres système (`HKLM`) et applicatifs/utilisateur (`HKCU`). Une erreur de modification directe peut perturber le fonctionnement du système ou de services critiques : toute intervention doit rester exceptionnelle, documentée et précédée d'une sauvegarde.

- [ ] **07. Citez quatre rôles Windows Server et leur mission.**
> [!success]- Corrigé Q07
> Exemples issus du cours :
> - **AD DS :** stocker les objets d'annuaire, participer à l'authentification et à l'autorisation.
> - **DNS Server :** répondre aux requêtes de résolution de noms et localiser les services.
> - **DHCP Server :** distribuer automatiquement les paramètres IP aux clients.
> - **File and Storage Services :** exposer et gérer des ressources de stockage / partages.
> *(Autres rôles acceptés : **Hyper-V** pour héberger des VMs, **IIS** pour héberger des applications/services web.)*

- [ ] **08. Pourquoi faut-il prévoir une adresse IP stable pour un futur contrôleur de domaine ?**
> [!success]- Corrigé Q08
> Une IP fixe (statique) garantit un accès prévisible au contrôleur de domaine et au serveur DNS associé pour tous les clients et services du réseau (évite les ruptures de résolution ou d'authentification liées à un changement de bail DHCP).

- [ ] **09. Que signifie le préfixe `/24` sur `192.168.10.10/24` ?**
> [!success]- Corrigé Q09
> `/24` indique un préfixe de **24 bits** dédiés à la partie réseau, soit le masque **`255.255.255.0`** (les adresses `192.168.10.10` et `192.168.10.20` appartiennent donc au même sous-réseau `192.168.10.0/24`).

- [ ] **10. Quelle différence existe-t-il entre installer AD DS et promouvoir un DC ?**
> [!success]- Corrigé Q10
> **Installer le rôle AD DS** (`Install-WindowsFeature`) ajoute uniquement les fichiers et outils d'administration ; **promouvoir un DC** (`Install-ADDSForest` / assistant de promotion) configure une nouvelle forêt/domaine ou intègre un domaine existant en créant la base d'annuaire.

- [ ] **11. Pourquoi `nslookup ad.ascencia.test` peut-il échouer avant la séance 2 ?**
> [!success]- Corrigé Q11
> La zone DNS du domaine `ad.ascencia.test` n'existe pas encore avant la promotion du contrôleur de domaine : un échec de cette requête en séance 1 est donc normal et attendu.

- [ ] **12. Quelle différence faites-vous entre une panne ICMP et une panne TCP ?**
> [!success]- Corrigé Q12
> ICMP (`ping` / `Test-Connection`) et TCP (`Test-NetConnection -Port`) suivent des règles et services distincts : un ping refusé (souvent filtré par le pare-feu) n'implique pas que tous les ports TCP soient fermés ; inversement, un ping réussi au niveau IP ne prouve pas qu'un service applicatif écoute sur son port TCP.

- [ ] **13. Quelle commande affiche la configuration IP et DNS d'un serveur ?**
> [!success]- Corrigé Q13
> **`Get-NetIPConfiguration`** (complétée si nécessaire par `Get-DnsClientServerAddress` ou `ipconfig /all`).

- [ ] **14. À quoi sert `Get-WindowsFeature` et que vérifie son attribut `InstallState` ?**
> [!success]- Corrigé Q14
> `Get-WindowsFeature` liste les rôles et fonctionnalités Windows Server ainsi que leur état. L'attribut `InstallState = Installed` confirme que le composant est bien présent/installé sur le système.

- [ ] **15. Quelles preuves demanderiez-vous à un étudiant affirmant que le TP est réussi ?**
> [!success]- Corrigé Q15
> Des preuves concrètes : captures des deux VMs démarrées (GUI et Core, éditions/interfaces vérifiées), commandes réellement exécutées et sorties de configuration (`Get-NetIPConfiguration`, `Get-WindowsFeature`, `hostname`), preuve d'installation du rôle AD DS sans promotion prématurée, tests réseau sur réseau isolé cohérent, et compte rendu explicatif sans mots de passe en clair.

---

## Partie 2 — Mini-QCM d'Autoévaluation (§1.13.2)

1. **Un rôle Windows Server est :**
   - A. un outil visuel
   - B. un service principal d'infrastructure
   - C. une licence
2. **Server Core dispose :**
   - A. du bureau complet
   - B. d'aucune administration
   - C. de PowerShell et Sconfig
3. **Pour éviter un conflit d'adressage :**
   - A. les VMs partagent l'IP
   - B. chaque VM a une IP unique
   - C. on désactive DNS
4. **`192.168.10.20/24` est :**
   - A. sur le même sous-réseau que `192.168.10.10/24`
   - B. sur un autre sous-réseau
   - C. une adresse DNS publique
5. **`Install-WindowsFeature AD-Domain-Services` :**
   - A. crée directement le domaine
   - B. installe le rôle
   - C. désactive le pare-feu
6. **Avant promotion, le futur nom de domaine :**
   - A. doit nécessairement se résoudre
   - B. peut ne pas se résoudre
   - C. doit être public
7. **Une passerelle est requise :**
   - A. toujours
   - B. pour atteindre un autre réseau
   - C. seulement pour le nom de la VM
8. **`ncpa.cpl` sert à :**
   - A. gérer les interfaces réseau
   - B. créer les utilisateurs AD
   - C. configurer les GPO

> [!success]- Corrigé du Mini-QCM (1 à 8)
> - **1 = B** — Un rôle fournit un service principal d'infrastructure aux utilisateurs/applications.
> - **2 = C** — Server Core n'a pas de bureau complet mais s'administre via PowerShell, Sconfig et les outils distants.
> - **3 = B** — Une adresse IPv4 unique par interface empêche les conflits IP.
> - **4 = A** — Avec `/24` (`255.255.255.0`), les deux adresses appartiennent au sous-réseau `192.168.10.0/24`.
> - **5 = B** — Cette commande installe uniquement le rôle préparatoire sans promouvoir le serveur en DC.
> - **6 = B** — Tant que le DC n'est pas promu et sa zone DNS créée, le futur domaine peut ne pas se résoudre.
> - **7 = B** — Une passerelle par défaut ne sert qu'à joindre d'autres réseaux.
> - **8 = A** — `ncpa.cpl` ouvre le panneau des connexions/interfaces réseau sur Desktop Experience.

---

## Partie 3 — Exercice de Raisonnement Diagnostique (§1.12.2)

**Énoncé :** Vous avez installé deux VMs et attribué la même IP `192.168.10.10` aux deux interfaces. Le ping réussit de façon intermittente et une session à distance se connecte parfois au mauvais système.
1. Expliquer la cause probable.
2. Proposer une correction.
3. Citer deux commandes de validation.

> [!success]- Corrigé — Diagnostic du conflit IP
> 1. **Cause probable :** Conflit d'adresse IPv4 (`192.168.10.10` configurée simultanément sur les deux interfaces du même sous-réseau).
> 2. **Correction :** Attribuer l'adresse distincte **`192.168.10.20/24`** à `SRV-CORE-01` (en laissant `192.168.10.10/24` à `SRV-AD-01`).
> 3. **Commandes de validation :**
>    - Contrôler `Get-NetIPConfiguration` sur chacune des deux machines (vérifier l'unicité de l'IP).
>    - Vérifier la connectivité sur un service réellement disponible (ex. `Test-NetConnection -ComputerName 192.168.10.20 -Port 5985` ou `Test-Connection`).

---

## Partie 4 — 3 Études de Cas (§1.13.3 – §1.13.5)

### Étude de cas 1 — Choix d'architecture
Une PME souhaite déployer un service d'authentification, un serveur de fichiers et une application métier. Les administrateurs maîtrisent PowerShell, mais l'application métier exige une interface locale. Proposez une répartition des rôles entre un serveur Core et un serveur GUI, puis justifiez les choix en mentionnant la gestion des risques, la dépendance au DNS et les besoins de maintenance.

> [!success]- Corrigé — Étude de cas 1
> - **Répartition des rôles :**
>   - **Serveur Core (`Server Core`) :** hébergement des services d'infrastructure compatibles et administrables en PowerShell/à distance — **AD DS + DNS** (contrôleur de domaine) et éventuellement **File and Storage Services** (ou séparés sur deux serveurs distincts pour isoler les rôles).
>   - **Serveur GUI (`Desktop Experience`) :** hébergement dédié à l'**application métier** qui exige impérativement une interface graphique locale.
> - **Justifications :**
>   - **Séparation des rôles & gestion des risques :** isoler l'application métier (plus exposée aux changements applicatifs et dotée de composants graphiques) du contrôleur de domaine réduit l'impact d'une panne ou d'une compromission applicative sur l'annuaire AD. *Attention :* Server Core réduit le nombre de composants graphiques à maintenir, mais il ne garantit pas à lui seul la sécurité (durcissement, pare-feu, moindre privilège et sauvegardes restent obligatoires).
>   - **Dépendance au DNS :** le serveur applicatif GUI (et les postes clients) doivent pointer vers le **DNS interne** hébergeant la zone AD afin de localiser le contrôleur de domaine via les enregistrements `SRV` et authentifier les utilisateurs.
>   - **Maintenance :** l'équipe maîtrisant PowerShell peut automatiser les contrôles et l'administration à distance (RSAT/WinRM) sur Core, tout en conservant le GUI uniquement là où la contrainte métier l'impose (rappel : pas de conversion Core $\leftrightarrow$ GUI sans réinstallation sous Windows Server 2022/2025).

### Étude de cas 2 — Préparer le réseau
Un laboratoire comporte un réseau interne `192.168.10.0/24` et trois VMs. Vous devez définir leur nom, IP, masque, DNS cible et passerelle éventuelle. Présentez le plan sous forme de tableau puis expliquez pourquoi un client doit utiliser le DNS de l'annuaire une fois le domaine actif.

> [!success]- Corrigé — Étude de cas 2
> | Machine | Nom d'hôte | Adresse IP | Masque | DNS cible | Passerelle |
> | :--- | :--- | :--- | :--- | :--- | :--- |
> | VM 1 (GUI, futur AD/DNS) | `SRV-AD-01` | `192.168.10.10` | `255.255.255.0` (`/24`) | `192.168.10.10` (après config DNS) | *(Aucune — réseau interne isolé sans routeur)* |
> | VM 2 (Core) | `SRV-CORE-01` | `192.168.10.20` | `255.255.255.0` (`/24`) | `192.168.10.10` | *(Aucune)* |
> | VM 3 (Poste client) | `PC-IT-01` | `192.168.10.30` | `255.255.255.0` (`/24`) | `192.168.10.10` | *(Aucune)* |
>
> **Pourquoi ne pas mettre de passerelle :** dans un réseau interne isolé sans routeur réel (ou passerelle NAT effectivement présente et documentée), il ne faut pas renseigner de passerelle fictive ; toutes les VMs du même sous-réseau `192.168.10.0/24` communiquent directement.
>
> **Pourquoi le client doit utiliser le DNS de l'annuaire :** dans un domaine Active Directory, le poste client localise les contrôleurs de domaine et leurs services (authentification Kerberos, LDAP, GPO) grâce à des requêtes DNS portant sur les enregistrements **`SRV`** de la zone du domaine. Un DNS externe ne connaît pas le domaine interne `ad.ascencia.test` : la jonction et l'ouverture de session échoueraient même si la connectivité IP est bonne.

### Étude de cas 3 — Incident de mise en service
Le rôle AD DS apparaît « Installed », mais un étudiant affirme que le domaine `ad.ascencia.test` est déjà fonctionnel. Quels contrôles ou éléments devez-vous lui demander ? Pourquoi l'affirmation n'est-elle pas justifiée par le seul statut du rôle ?

> [!success]- Corrigé — Étude de cas 3
> - **Pourquoi l'affirmation est fausse :** le statut `InstallState = Installed` renvoyé par `Get-WindowsFeature` signifie uniquement que les binaires et outils du rôle AD DS ont été copiés sur le serveur (`Install-WindowsFeature`). Cela n'effectue **pas la promotion en contrôleur de domaine** (`Install-ADDSForest`) et ne crée ni forêt, ni domaine, ni annuaire fonctionnel.
> - **Contrôles et preuves à exiger pour prouver qu'un domaine est actif :**
>   1. Preuve d'une **promotion réussie** (journal/sortie de `Install-ADDSForest` ou existence effective de la forêt/domaine via `Get-ADDomain` / `Get-ADForest` une fois promu).
>   2. État des **services d'annuaire** fonctionnels (`Netlogon`, `NTDS`, `DNS`).
>   3. Existence et configuration de la **zone DNS** `ad.ascencia.test` avec ses enregistrements **`SRV`** et une résolution réussie (`Resolve-DnsName` / `nslookup`).
>   4. Contrôle d'intégrité (ex. `dcdiag` en séance ultérieure).

---

## Partie 5 — Travail Personnel PowerShell (§1.11.2)

**Consigne :** Adapter le script `Inventory-Lab.ps1` pour ajouter la sortie de `Get-Service -Name WinRM,W32Time` et expliquer les informations utiles pour le diagnostic. *(Ne jamais enregistrer de mots de passe dans le rapport.)*

> [!success]- Corrigé — Script complété & justification diagnostique
> ```powershell
> $repertoire = 'C:\Lab\Rapports'
> New-Item -Path $repertoire -ItemType Directory -Force | Out-Null
> $nom = $env:COMPUTERNAME
> $date = Get-Date -Format 'yyyyMMdd-HHmmss'
> $chemin = Join-Path $repertoire "inventaire-$nom-$date.txt"
>
> "Ordinateur : $nom" | Out-File $chemin -Encoding UTF8
> "Date : $(Get-Date)" | Out-File $chemin -Append
> Get-NetIPConfiguration | Out-String | Out-File $chemin -Append
> Get-WindowsFeature -Name AD-Domain-Services,DNS |
>     Format-Table Name,InstallState | Out-String |
>     Out-File $chemin -Append
> Get-Service -Name WinRM,W32Time |
>     Format-Table Name,Status,StartType | Out-String |
>     Out-File $chemin -Append
>
> Write-Host "Rapport enregistré : $chemin"
> ```
> **Utilité diagnostique des deux services :**
> - **`WinRM` :** vérifie si le service d'administration distante est bien `Running` (et son `StartType`). S'il est arrêté sur `SRV-CORE-01`, l'administration à distance via PowerShell/RSAT échoue même si la couche IP fonctionne.
> - **`W32Time` :** vérifie que le service de synchronisation horaire fonctionne. Une dérive d'horloge entre machines bloque plus tard l'authentification **Kerberos** dans Active Directory.

---

## 📋 Annexe — Fiche de Constat & Barème TP1 (/20)

### Fiche de constat de laboratoire (§1.10.6)

| Vérification | Résultat attendu | Résultat observé / preuve |
| :--- | :--- | :--- |
| **VM 1** | `SRV-AD-01` ; `192.168.10.10/24` | *(À renseigner pendant le TP)* |
| **VM 2** | `SRV-CORE-01` ; `192.168.10.20/24` | *(À renseigner pendant le TP)* |
| **Réseau virtuel** | Deux VMs sur le même réseau isolé | *(À renseigner pendant le TP)* |
| **Rôle AD DS** | Installé sur `SRV-AD-01`, pas encore de domaine | *(À renseigner pendant le TP)* |
| **Commandes** | Sorties `Get-NetIPConfiguration` et `Get-WindowsFeature` | *(À renseigner pendant le TP)* |
| **Sécurité** | Pas d'exposition non autorisée au réseau réel | *(À renseigner pendant le TP)* |

### Barème indicatif du TP1 (§1.13.6)

| Critère | Points | Preuves attendues |
| :--- | :---: | :--- |
| **Deux VMs opérationnelles** | 4 | GUI et Core démarrés ; édition et interface vérifiées |
| **Réseau et nommage** | 5 | Adresses uniques, masque, noms et tests documentés |
| **Installation du rôle AD DS** | 3 | `InstallState` cohérent, aucune promotion prématurée |
| **Vérifications et diagnostic** | 4 | Commandes, résultats réels, explication des limites |
| **Compte rendu et sécurité** | 4 | Procédure, captures pertinentes, incident et conclusion |
