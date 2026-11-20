#!/usr/bin/env python3
"""
Implémentation de référence pour le Sujet 2 :
« Le parcours en profondeur (DFS) pour l'exploration et l'analyse de la structure d'un graphe »

Master IT — UE Théorie des Graphes (ASCENCIA KEYCE, Campus de Lomé)
Enseignant : Edem K. HOVI — Année académique 2026-2027

Fonctionnalités implémentées (bibliothèque standard Python uniquement) :
1. Représentation de graphes orientés et non orientés par listes d'adjacence.
2. DFS récursif avec coloration tricolore (BLANC, GRIS, NOIR), estampilles [d/f],
   journalisation détaillée (visites, choix de branche, backtracking) et
   classification des 4 types d'arcs (ARBRE, ARRIERE, AVANT, CROISE).
3. DFS itératif avec pile explicite (LIFO) reproduisant la trace et résistant aux
   grandes profondeurs sans dépassement de la pile d'appels.
4. Applications structurelles :
   - Détection de cycle dans un graphe orienté (avec reconstruction du circuit).
   - Identification des composantes connexes dans un graphe non orienté.
   - Tri topologique d'un DAG appliqué à l'ordonnancement de tâches dépendantes.
5. Campagne expérimentale sur 6 topologies de graphes et test de tenue en profondeur.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
import random
import sys
import time
from typing import Dict, List, Optional, Tuple


class Couleur(str, Enum):
    """États d'un sommet durant un parcours en profondeur."""

    BLANC = "BLANC"  # Sommet non encore découvert
    GRIS = "GRIS"    # Sommet découvert, exploration des voisins en cours (actif sur la pile)
    NOIR = "NOIR"    # Sommet totalement exploré (fermé)


class TypeArc(str, Enum):
    """Classification standard des arcs lors d'un parcours DFS."""

    ARBRE = "ARBRE"      # Découverte d'un sommet BLANC
    ARRIERE = "ARRIERE"  # Lien vers un ancêtre GRIS (caractérise un cycle)
    AVANT = "AVANT"      # Lien vers un descendant NOIR déjà fermé
    CROISE = "CROISE"    # Lien vers un sommet NOIR d'une autre branche


@dataclass
class Graphe:
    """Représentation d'un graphe par listes d'adjacence."""

    oriente: bool = True
    adjacence: Dict[str, List[str]] = field(default_factory=dict)

    def ajouter_sommet(self, sommet: str) -> None:
        """Ajoute un sommet isolé s'il n'existe pas encore."""
        if sommet not in self.adjacence:
            self.adjacence[sommet] = []

    def ajouter_arc(self, source: str, destination: str) -> None:
        """Ajoute un arc (source -> destination), ou une arête si non orienté."""
        self.ajouter_sommet(source)
        self.ajouter_sommet(destination)
        if destination not in self.adjacence[source]:
            self.adjacence[source].append(destination)
        if not self.oriente and source not in self.adjacence[destination]:
            self.adjacence[destination].append(source)

    def sommets(self) -> List[str]:
        """Retourne les sommets triés pour un ordre d'exploration déterministe."""
        return sorted(self.adjacence.keys())

    def nombre_sommets(self) -> int:
        return len(self.adjacence)

    def nombre_arcs(self) -> int:
        total = sum(len(voisins) for voisins in self.adjacence.values())
        return total if self.oriente else total // 2

    def copier(self) -> "Graphe":
        """Retourne une copie indépendante du graphe."""
        copie = Graphe(oriente=self.oriente)
        for u, voisins in self.adjacence.items():
            copie.adjacence[u] = list(voisins)
        return copie


@dataclass
class EtapeTrace:
    """Enregistrement d'une étape élémentaire du parcours pour l'illustration."""

    instant: int
    action: str
    sommet: str
    detail: str
    pile_active: List[str]


@dataclass
class ResultatDFS:
    """Ensemble des structures produites par un parcours en profondeur."""

    ordre_visite: List[str]
    ordre_cloture: List[str]
    decouverte: Dict[str, int]
    cloture: Dict[str, int]
    parents: Dict[str, Optional[str]]
    arcs_classes: List[Tuple[str, str, TypeArc]]
    trace: List[EtapeTrace]
    nombre_retours_arriere: int


def dfs_recursif(
    graphe: Graphe,
    source_prioritaire: Optional[str] = None,
    trier_voisins: bool = True,
    enregistrer_trace: bool = True,
) -> ResultatDFS:
    """
    Exécute un parcours en profondeur récursif complet sur le graphe.

    Calcule les dates de découverte d[u] et de clôture f[u], construit les
    liens de parenté pi[u], classe chaque arc et journalise les retours en arrière.
    """
    sommets = graphe.sommets()
    if source_prioritaire and source_prioritaire in graphe.adjacence:
        sommets = [source_prioritaire] + [s for s in sommets if s != source_prioritaire]

    couleur: Dict[str, Couleur] = {u: Couleur.BLANC for u in sommets}
    parents: Dict[str, Optional[str]] = {u: None for u in sommets}
    decouverte: Dict[str, int] = {}
    cloture: Dict[str, int] = {}
    ordre_visite: List[str] = []
    ordre_cloture: List[str] = []
    arcs_classes: List[Tuple[str, str, TypeArc]] = []
    trace: List[EtapeTrace] = []
    pile_active: List[str] = []
    temps = 0
    retours_arriere = 0

    def noter(action: str, sommet: str, detail: str) -> None:
        if enregistrer_trace:
            trace.append(
                EtapeTrace(
                    instant=temps,
                    action=action,
                    sommet=sommet,
                    detail=detail,
                    pile_active=list(pile_active),
                )
            )

    def visiter(u: str) -> None:
        nonlocal temps, retours_arriere
        temps += 1
        decouverte[u] = temps
        couleur[u] = Couleur.GRIS
        ordre_visite.append(u)
        pile_active.append(u)
        noter("DECOUVERTE", u, f"d[{u}] = {temps}, passage en GRIS")

        voisins = sorted(graphe.adjacence[u]) if trier_voisins else graphe.adjacence[u]
        for v in voisins:
            if couleur[v] == Couleur.BLANC:
                parents[v] = u
                arcs_classes.append((u, v, TypeArc.ARBRE))
                noter("CHOIX_BRANCHE", u, f"Arc ({u} -> {v}) [ARBRE] : descente vers {v}")
                visiter(v)
                retours_arriere += 1
                noter("RETOUR_ARRIERE", u, f"Backtrack de {v} vers {u}")
            elif couleur[v] == Couleur.GRIS:
                arcs_classes.append((u, v, TypeArc.ARRIERE))
                noter("INSPECTION", u, f"Arc ({u} -> {v}) [ARRIERE] : {v} est GRIS (cycle détecté)")
            else:
                # Distinction entre arc avant et arc croisé via le théorème des intervalles
                if decouverte[u] < decouverte[v]:
                    type_arc = TypeArc.AVANT
                else:
                    type_arc = TypeArc.CROISE
                arcs_classes.append((u, v, type_arc))
                noter("INSPECTION", u, f"Arc ({u} -> {v}) [{type_arc.value}] : {v} est déjà NOIR")

        temps += 1
        cloture[u] = temps
        couleur[u] = Couleur.NOIR
        ordre_cloture.append(u)
        noter("CLOTURE", u, f"Fin des voisins de {u} -> f[{u}] = {temps}, passage en NOIR")
        pile_active.pop()

    for s in sommets:
        if couleur[s] == Couleur.BLANC:
            visiter(s)

    return ResultatDFS(
        ordre_visite=ordre_visite,
        ordre_cloture=ordre_cloture,
        decouverte=decouverte,
        cloture=cloture,
        parents=parents,
        arcs_classes=arcs_classes,
        trace=trace,
        nombre_retours_arriere=retours_arriere,
    )


def dfs_iteratif_pile(
    graphe: Graphe,
    source_prioritaire: Optional[str] = None,
    trier_voisins: bool = True,
    enregistrer_trace: bool = True,
) -> ResultatDFS:
    """
    Exécute un parcours en profondeur itératif à l'aide d'une pile explicite (LIFO).

    Chaque entrée de la pile mémorise un couple (sommet, indice_prochain_voisin),
    reproduisant fidèlement la pile d'appels tout en évitant tout débordement
    de récursion sur les graphes profonds.
    """
    sommets = graphe.sommets()
    if source_prioritaire and source_prioritaire in graphe.adjacence:
        sommets = [source_prioritaire] + [s for s in sommets if s != source_prioritaire]

    couleur: Dict[str, Couleur] = {u: Couleur.BLANC for u in sommets}
    parents: Dict[str, Optional[str]] = {u: None for u in sommets}
    decouverte: Dict[str, int] = {}
    cloture: Dict[str, int] = {}
    ordre_visite: List[str] = []
    ordre_cloture: List[str] = []
    arcs_classes: List[Tuple[str, str, TypeArc]] = []
    trace: List[EtapeTrace] = []
    listes_voisins: Dict[str, List[str]] = {
        u: (sorted(graphe.adjacence[u]) if trier_voisins else list(graphe.adjacence[u]))
        for u in sommets
    }

    temps = 0
    retours_arriere = 0
    # Pile LIFO explicite : [sommet, index_voisin_courant]
    pile: List[List[object]] = []

    def noter(action: str, sommet: str, detail: str) -> None:
        if enregistrer_trace:
            pile_sommets = [str(cadre[0]) for cadre in pile]
            trace.append(
                EtapeTrace(
                    instant=temps,
                    action=action,
                    sommet=sommet,
                    detail=detail,
                    pile_active=pile_sommets,
                )
            )

    for depart in sommets:
        if couleur[depart] != Couleur.BLANC:
            continue

        temps += 1
        decouverte[depart] = temps
        couleur[depart] = Couleur.GRIS
        ordre_visite.append(depart)
        pile.append([depart, 0])
        noter("EMPILE_RACINE", depart, f"d[{depart}] = {temps}, empilement sur LIFO")

        while pile:
            u = str(pile[-1][0])
            idx = int(pile[-1][1])
            voisins = listes_voisins[u]

            if idx < len(voisins):
                v = voisins[idx]
                pile[-1][1] = idx + 1

                if couleur[v] == Couleur.BLANC:
                    parents[v] = u
                    arcs_classes.append((u, v, TypeArc.ARBRE))
                    noter("CHOIX_BRANCHE", u, f"Arc ({u} -> {v}) [ARBRE] : empilement de {v}")
                    temps += 1
                    decouverte[v] = temps
                    couleur[v] = Couleur.GRIS
                    ordre_visite.append(v)
                    pile.append([v, 0])
                    noter("DECOUVERTE", v, f"d[{v}] = {temps}, passage en GRIS")
                elif couleur[v] == Couleur.GRIS:
                    arcs_classes.append((u, v, TypeArc.ARRIERE))
                    noter("INSPECTION", u, f"Arc ({u} -> {v}) [ARRIERE] : cycle potentiel")
                else:
                    type_arc = TypeArc.AVANT if decouverte[u] < decouverte[v] else TypeArc.CROISE
                    arcs_classes.append((u, v, type_arc))
                    noter("INSPECTION", u, f"Arc ({u} -> {v}) [{type_arc.value}] : {v} déjà NOIR")
            else:
                temps += 1
                cloture[u] = temps
                couleur[u] = Couleur.NOIR
                ordre_cloture.append(u)
                noter("DEPILE_CLOTURE", u, f"f[{u}] = {temps}, dépilement (NOIR)")
                pile.pop()
                if pile:
                    retours_arriere += 1
                    parent_actif = str(pile[-1][0])
                    noter("RETOUR_ARRIERE", parent_actif, f"Backtrack de {u} vers {parent_actif}")

    return ResultatDFS(
        ordre_visite=ordre_visite,
        ordre_cloture=ordre_cloture,
        decouverte=decouverte,
        cloture=cloture,
        parents=parents,
        arcs_classes=arcs_classes,
        trace=trace,
        nombre_retours_arriere=retours_arriere,
    )


def detecter_cycle_oriente(graphe: Graphe) -> Optional[List[str]]:
    """
    Détecte la présence d'un circuit dans un graphe orienté par recherche d'arc arrière.

    Retourne la liste des sommets formant le premier cycle trouvé (ex: ['B', 'D', 'E', 'B']),
    ou None si le graphe est un DAG (acyclique).
    """
    resultat = dfs_iteratif_pile(graphe, enregistrer_trace=False)
    for u, v, type_arc in resultat.arcs_classes:
        if type_arc == TypeArc.ARRIERE:
            # v est ancêtre de u dans la forêt DFS : on remonte les parents de u jusqu'à v
            chemin: List[str] = [u]
            courant = u
            while courant != v and courant is not None:
                courant = resultat.parents[courant]  # type: ignore[assignment]
                if courant is not None:
                    chemin.append(courant)
            chemin.reverse()
            chemin.append(v)
            return chemin
    return None


def composantes_connexes(graphe: Graphe) -> List[List[str]]:
    """
    Identifie toutes les composantes connexes d'un graphe non orienté par DFS itératif.
    """
    if graphe.oriente:
        raise ValueError("La recherche de composantes connexes attend un graphe non orienté.")

    visites: set[str] = set()
    composantes: List[List[str]] = []

    for depart in graphe.sommets():
        if depart in visites:
            continue
        composante: List[str] = []
        pile: List[str] = [depart]
        visites.add(depart)
        while pile:
            u = pile.pop()
            composante.append(u)
            for v in sorted(graphe.adjacence[u], reverse=True):
                if v not in visites:
                    visites.add(v)
                    pile.append(v)
        composantes.append(sorted(composante))

    return composantes


def tri_topologique_dag(graphe: Graphe) -> Tuple[bool, List[str]]:
    """
    Calcule un tri topologique par ordre décroissant des dates de clôture f[u] du DFS.

    Retourne (True, ordre_topologique) si le graphe est acyclique (DAG),
    ou (False, cycle_detecte) s'il contient au moins un circuit.
    """
    if not graphe.oriente:
        raise ValueError("Le tri topologique ne s'applique qu'aux graphes orientés.")

    cycle = detecter_cycle_oriente(graphe)
    if cycle is not None:
        return False, cycle

    resultat = dfs_iteratif_pile(graphe, enregistrer_trace=False)
    # L'ordre de clôture liste f[u] croissant : son inversion donne f[u] décroissant
    ordre_topologique = list(reversed(resultat.ordre_cloture))
    return True, ordre_topologique


# ---------------------------------------------------------------------------
# Jeux de données et scénarios de démonstration / expérimentation
# ---------------------------------------------------------------------------

def construire_graphe_exemple() -> Graphe:
    """Construit le graphe d'étude G_ex à 7 sommets et 10 arcs."""
    g = Graphe(oriente=True)
    arcs = [
        ("A", "B"), ("A", "C"), ("A", "G"),
        ("B", "D"), ("B", "E"),
        ("C", "F"),
        ("D", "E"), ("D", "G"),
        ("E", "B"),
        ("F", "E"),
    ]
    for u, v in arcs:
        g.ajouter_arc(u, v)
    return g


def construire_pipeline_taches() -> Tuple[Graphe, Dict[str, str]]:
    """Construit un DAG de 8 tâches dépendantes (pipeline logiciel CI/CD)."""
    libelles = {
        "T1": "Configuration environnement & variables",
        "T2": "Installation des dépendances",
        "T3": "Génération du schéma BDD & migrations",
        "T4": "Compilation du backend API",
        "T5": "Compilation du frontend Web",
        "T6": "Tests unitaires et d'intégration",
        "T7": "Construction de l'image Docker",
        "T8": "Déploiement en pré-production",
    }
    arcs = [
        ("T1", "T2"), ("T1", "T3"),
        ("T2", "T4"), ("T2", "T5"),
        ("T3", "T4"), ("T3", "T6"),
        ("T4", "T6"), ("T4", "T7"),
        ("T5", "T7"),
        ("T6", "T7"),
        ("T7", "T8"),
    ]
    dag = Graphe(oriente=True)
    for t in libelles:
        dag.ajouter_sommet(t)
    for u, v in arcs:
        dag.ajouter_arc(u, v)
    return dag, libelles


def construire_reseau_non_connexe() -> Graphe:
    """Construit un réseau non orienté de 9 routeurs répartis en 3 îlots isolés."""
    reseau = Graphe(oriente=False)
    liens = [
        ("R1", "R2"), ("R2", "R3"), ("R3", "R4"), ("R1", "R4"),
        ("R5", "R6"), ("R6", "R7"),
        ("R8", "R9"),
    ]
    for u, v in liens:
        reseau.ajouter_arc(u, v)
    return reseau


def generer_graphes_experimentaux(graine: int = 42) -> List[Tuple[str, Graphe]]:
    """Génère 6 topologies variées pour évaluer le comportement de DFS."""
    rng = random.Random(graine)
    jeux: List[Tuple[str, Graphe]] = []

    # 1. Chaîne linéaire orientée (n = 500)
    chaine = Graphe(oriente=True)
    for i in range(499):
        chaine.ajouter_arc(f"V{i:04d}", f"V{i+1:04d}")
    jeux.append(("Chaîne linéaire (orienté)", chaine))

    # 2. Arbre binaire complet orienté (n = 511)
    arbre = Graphe(oriente=True)
    for i in range(511):
        gauche = 2 * i + 1
        droite = 2 * i + 2
        if gauche < 511:
            arbre.ajouter_arc(f"N{i:03d}", f"N{gauche:03d}")
        if droite < 511:
            arbre.ajouter_arc(f"N{i:03d}", f"N{droite:03d}")
    jeux.append(("Arbre binaire complet (orienté)", arbre))

    # 3. Graphe dense complet orienté sans boucle (n = 200)
    dense = Graphe(oriente=True)
    sommets_dense = [f"D{i:03d}" for i in range(200)]
    for u in sommets_dense:
        dense.adjacence[u] = [v for v in sommets_dense if v != u]
    jeux.append(("Graphe complet dense (orienté)", dense))

    # 4. Graphe non connexe (non orienté, 5 îlots de 100 sommets)
    non_connexe = Graphe(oriente=False)
    for bloc in range(5):
        base = bloc * 100
        for i in range(99):
            non_connexe.ajouter_arc(f"S{base+i:03d}", f"S{base+i+1:03d}")
        for _ in range(50):
            a = rng.randint(base, base + 99)
            b = rng.randint(base, base + 99)
            if a != b:
                non_connexe.ajouter_arc(f"S{a:03d}", f"S{b:03d}")
    jeux.append(("Graphe non connexe (non orienté, 5 îlots)", non_connexe))

    # 5. DAG structuré par couches (n = 500, m = 1500)
    dag = Graphe(oriente=True)
    for i in range(500):
        dag.ajouter_sommet(f"G{i:03d}")
    arcs_ajoutes = 0
    while arcs_ajoutes < 1500:
        u = rng.randint(0, 498)
        v = rng.randint(u + 1, 499)
        src, dst = f"G{u:03d}", f"G{v:03d}"
        if dst not in dag.adjacence[src]:
            dag.ajouter_arc(src, dst)
            arcs_ajoutes += 1
    jeux.append(("DAG aléatoire (orienté)", dag))

    # 6. Graphe cyclique dense modéré (n = 500, m = 1200)
    cyclique = Graphe(oriente=True)
    for i in range(500):
        cyclique.ajouter_arc(f"C{i:03d}", f"C{(i + 1) % 500:03d}")
    arcs_ajoutes = 500
    while arcs_ajoutes < 1200:
        u = rng.randint(0, 499)
        v = rng.randint(0, 499)
        if u != v:
            src, dst = f"C{u:03d}", f"C{v:03d}"
            if dst not in cyclique.adjacence[src]:
                cyclique.ajouter_arc(src, dst)
                arcs_ajoutes += 1
    jeux.append(("Graphe cyclique (orienté)", cyclique))

    return jeux


def executer_benchmark(nom: str, graphe: Graphe) -> Dict[str, object]:
    """Mesure les temps et propriétés structurelles d'un graphe donné."""
    t0 = time.perf_counter()
    res_rec = dfs_recursif(graphe, trier_voisins=False, enregistrer_trace=False)
    t_rec_ms = (time.perf_counter() - t0) * 1000

    t1 = time.perf_counter()
    res_it = dfs_iteratif_pile(graphe, trier_voisins=False, enregistrer_trace=False)
    t_it_ms = (time.perf_counter() - t1) * 1000

    assert res_rec.ordre_visite == res_it.ordre_visite, "Incohérence récursif vs itératif"

    nb_arriere = sum(1 for _, _, t in res_it.arcs_classes if t == TypeArc.ARRIERE)
    if graphe.oriente:
        diagnostic = f"Cycle détecté ({nb_arriere} arc(s) arrière)" if nb_arriere > 0 else "Acyclique (DAG)"
    else:
        nb_comp = len(composantes_connexes(graphe))
        diagnostic = f"{nb_comp} composante(s) connexe(s)"

    return {
        "nom": nom,
        "V": graphe.nombre_sommets(),
        "E": graphe.nombre_arcs(),
        "t_rec_ms": t_rec_ms,
        "t_it_ms": t_it_ms,
        "retours": res_it.nombre_retours_arriere,
        "diagnostic": diagnostic,
    }


def main() -> None:
    print("=" * 78)
    print("SUJET 2 — PARCOURS EN PROFONDEUR (DFS) & ANALYSE STRUCTURELLE")
    print("=" * 78)

    # 1. Illustration sur le graphe d'exemple G_ex
    g_ex = construire_graphe_exemple()
    res_rec = dfs_recursif(g_ex, source_prioritaire="A", enregistrer_trace=True)
    res_it = dfs_iteratif_pile(g_ex, source_prioritaire="A", enregistrer_trace=True)

    assert res_rec.ordre_visite == res_it.ordre_visite
    assert res_rec.decouverte == res_it.decouverte
    assert res_rec.cloture == res_it.cloture
    assert res_rec.arcs_classes == res_it.arcs_classes

    print("\n[1] ILLUSTRATION SUR LE GRAPHE D'EXEMPLE G_ex (7 sommets, 10 arcs)")
    print("Ordre de découverte :", " -> ".join(res_rec.ordre_visite))
    print("Ordre de clôture    :", " -> ".join(res_rec.ordre_cloture))
    print("Estampilles [d/f]   :", ", ".join(
        f"{s}[{res_rec.decouverte[s]}/{res_rec.cloture[s]}]" for s in g_ex.sommets()
    ))
    print("Retours en arrière  :", res_rec.nombre_retours_arriere)

    print("\nTrace pas à pas (DFS récursif / pile active) :")
    for etape in res_rec.trace:
        print(
            f"  t={etape.instant:02d} | {etape.action:<15} | {etape.sommet} | "
            f"Pile={etape.pile_active} | {etape.detail}"
        )

    print("\nClassification des 10 arcs de G_ex :")
    for u, v, typ in res_rec.arcs_classes:
        print(f"  ({u} -> {v}) : {typ.value}")

    cycle_ex = detecter_cycle_oriente(g_ex)
    print(f"Cycle détecté dans G_ex : {' -> '.join(cycle_ex) if cycle_ex else 'Aucun'}")

    # 2. Application : Ordonnancement d'un pipeline de tâches dépendantes
    print("\n" + "-" * 78)
    print("[2] APPLICATION : ORDONNANCEMENT D'UN PIPELINE LOGICIEL (DAG vs CYCLE)")
    dag, libelles = construire_pipeline_taches()
    est_dag, ordre = tri_topologique_dag(dag)
    print(f"Vérification DAG valide : {est_dag}")
    print("Ordre d'exécution topologique obtenu :")
    for rang, tache in enumerate(ordre, start=1):
        print(f"  {rang}. {tache} — {libelles[tache]}")

    # Injection d'une dépendance circulaire (T7 dépend de T2, or on ajoute T7 -> T2)
    dag_corrompu = dag.copier()
    dag_corrompu.ajouter_arc("T7", "T2")
    est_dag_2, resultat_2 = tri_topologique_dag(dag_corrompu)
    print(f"\nAprès ajout d'une dépendance fautive (T7 -> T2) -> DAG valide ? {est_dag_2}")
    print("Cycle bloquant identifié :", " -> ".join(resultat_2))

    # 3. Application complémentaire : Composantes connexes d'un réseau
    print("\n" + "-" * 78)
    print("[3] APPLICATION : COMPOSANTES CONNEXES D'UN RÉSEAU NON ORIENTÉ")
    reseau = construire_reseau_non_connexe()
    comp = composantes_connexes(reseau)
    print(f"Nombre de sous-réseaux isolés détectés : {len(comp)}")
    for idx, ilot in enumerate(comp, start=1):
        print(f"  Composante {idx} : {ilot}")

    # 4. Campagne expérimentale sur 6 topologies de graphes
    print("\n" + "-" * 78)
    print("[4] EXPÉRIMENTATION SUR 6 TOPOLOGIES DE GRAPHES")
    print(f"{'Topologie':<42} | {'|V|':>4} | {'|E|':>5} | {'Rec(ms)':>7} | {'It(ms)':>7} | {'Diagnostic'}")
    print("-" * 105)
    for nom, g in generer_graphes_experimentaux():
        m = executer_benchmark(nom, g)
        print(
            f"{m['nom']:<42} | {m['V']:>4} | {m['E']:>5} | "
            f"{m['t_rec_ms']:>7.2f} | {m['t_it_ms']:>7.2f} | {m['diagnostic']}"
        )

    # 5. Test de robustesse à la profondeur (chaîne de 2 000 sommets)
    print("\n" + "-" * 78)
    print("[5] TEST DE PROFONDEUR EXTRÊME (chaîne linéaire |V| = 2 000)")
    chaine_profonde = Graphe(oriente=True)
    for i in range(1999):
        chaine_profonde.ajouter_arc(f"P{i:04d}", f"P{i+1:04d}")

    print(f"Limite de récursion Python active : {sys.getrecursionlimit()}")
    try:
        dfs_recursif(chaine_profonde, trier_voisins=False, enregistrer_trace=False)
        print("DFS récursif : terminé sans erreur")
    except RecursionError:
        print("DFS récursif : ÉCHEC (RecursionError — dépassement de la pile d'appels)")

    t_prof = time.perf_counter()
    res_prof = dfs_iteratif_pile(chaine_profonde, trier_voisins=False, enregistrer_trace=False)
    duree_prof = (time.perf_counter() - t_prof) * 1000
    print(
        f"DFS itératif (pile LIFO) : SUCCÈS en {duree_prof:.2f} ms "
        f"({len(res_prof.ordre_visite)} sommets visités, {res_prof.nombre_retours_arriere} retours arrière)"
    )


if __name__ == "__main__":
    main()
