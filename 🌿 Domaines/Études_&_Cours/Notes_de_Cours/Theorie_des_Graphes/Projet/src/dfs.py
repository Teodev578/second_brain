"""Algorithmes de parcours en profondeur (DFS) récursif et itératif avec pile explicite."""

from __future__ import annotations

from typing import Dict, Iterator, List, Optional, Tuple

from graphe import Couleur, EtapeTrace, Graphe, ResultatDFS, TypeArc


def _preparer_sommets(graphe: Graphe, source_prioritaire: Optional[str]) -> List[str]:
    """Retourne les sommets triés, en plaçant source_prioritaire en tête si elle existe."""
    sommets = graphe.sommets()
    if source_prioritaire and source_prioritaire in graphe.adjacence:
        return [source_prioritaire] + [s for s in sommets if s != source_prioritaire]
    return sommets


def _classer_arc_visite(
    u: str,
    v: str,
    couleur: Dict[str, Couleur],
    decouverte: Dict[str, int],
) -> TypeArc:
    """Classe un arc (u -> v) vers un sommet déjà rencontré (GRIS ou NOIR)."""
    if couleur[v] == Couleur.GRIS:
        return TypeArc.ARRIERE
    return TypeArc.AVANT if decouverte[u] < decouverte[v] else TypeArc.CROISE


def _ajouter_etape(
    trace: List[EtapeTrace],
    actif: bool,
    instant: int,
    action: str,
    sommet: str,
    detail: str,
    pile_active: List[str],
) -> None:
    """Ajoute une étape dans la trace uniquement si la journalisation est active."""
    if actif:
        trace.append(
            EtapeTrace(
                instant=instant,
                action=action,
                sommet=sommet,
                detail=detail,
                pile_active=list(pile_active),
            )
        )


def dfs_recursif(
    graphe: Graphe,
    source_prioritaire: Optional[str] = None,
    trier_voisins: bool = True,
    enregistrer_trace: bool = True,
) -> ResultatDFS:
    """
    Exécute un parcours en profondeur récursif (Cormen et al. / support de cours).

    Calcule les dates de découverte d[u] et de fin f[u], construit les liens
    de parenté pi[u], classe chaque arc et compte les retours en arrière.
    """
    sommets = _preparer_sommets(graphe, source_prioritaire)
    couleur: Dict[str, Couleur] = {u: Couleur.BLANC for u in sommets}
    parents: Dict[str, Optional[str]] = {u: None for u in sommets}
    decouverte: Dict[str, int] = {}
    fin: Dict[str, int] = {}
    ordre_visite: List[str] = []
    ordre_fermeture: List[str] = []
    arcs_classes: List[Tuple[str, str, TypeArc]] = []
    trace: List[EtapeTrace] = []
    pile_active: List[str] = []
    temps = 0
    retours_arriere = 0

    def visiter(u: str) -> None:
        nonlocal temps, retours_arriere
        temps += 1
        decouverte[u] = temps
        couleur[u] = Couleur.GRIS
        ordre_visite.append(u)
        pile_active.append(u)
        _ajouter_etape(trace, enregistrer_trace, temps, "DECOUVERTE", u, f"d[{u}] = {temps}, passage en GRIS", pile_active)

        voisins = sorted(graphe.adjacence[u]) if trier_voisins else graphe.adjacence[u]
        for v in voisins:
            if couleur[v] == Couleur.BLANC:
                parents[v] = u
                arcs_classes.append((u, v, TypeArc.ARBRE))
                _ajouter_etape(trace, enregistrer_trace, temps, "CHOIX_BRANCHE", u, f"Arc ({u} -> {v}) [ARBRE] : descente vers {v}", pile_active)
                visiter(v)
                retours_arriere += 1
                _ajouter_etape(trace, enregistrer_trace, temps, "RETOUR_ARRIERE", u, f"Backtrack de {v} vers {u}", pile_active)
            else:
                type_arc = _classer_arc_visite(u, v, couleur, decouverte)
                arcs_classes.append((u, v, type_arc))
                etat = "cycle détecté" if type_arc == TypeArc.ARRIERE else f"{v} est déjà NOIR"
                _ajouter_etape(trace, enregistrer_trace, temps, "INSPECTION", u, f"Arc ({u} -> {v}) [{type_arc.value}] : {etat}", pile_active)

        temps += 1
        fin[u] = temps
        couleur[u] = Couleur.NOIR
        ordre_fermeture.append(u)
        _ajouter_etape(trace, enregistrer_trace, temps, "FIN", u, f"Fin des voisins de {u} -> f[{u}] = {temps}, passage en NOIR", pile_active)
        pile_active.pop()

    for s in sommets:
        if couleur[s] == Couleur.BLANC:
            visiter(s)

    return ResultatDFS(
        ordre_visite=ordre_visite,
        ordre_fermeture=ordre_fermeture,
        decouverte=decouverte,
        fin=fin,
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
    Exécute un parcours en profondeur itératif avec pile explicite (LIFO).

    Adaptation en Python de NonrecursiveDirectedDFS (Sedgewick & Wayne, Algorithms 4e éd., §4.2) :
    un itérateur par sommet (adj_iter) retient le prochain voisin à voir, tandis que la pile
    ne stocke que les sommets actifs. Enrichie avec les trois couleurs (BLANC, GRIS, NOIR),
    les parents pi[u] et les dates [d, f] (Cormen et al.) pour analyser la structure du graphe.
    """
    sommets = _preparer_sommets(graphe, source_prioritaire)
    couleur: Dict[str, Couleur] = {u: Couleur.BLANC for u in sommets}
    parents: Dict[str, Optional[str]] = {u: None for u in sommets}
    decouverte: Dict[str, int] = {}
    fin: Dict[str, int] = {}
    ordre_visite: List[str] = []
    ordre_fermeture: List[str] = []
    arcs_classes: List[Tuple[str, str, TypeArc]] = []
    trace: List[EtapeTrace] = []
    adj_iter: Dict[str, Iterator[str]] = {
        u: iter(sorted(graphe.adjacence[u]) if trier_voisins else graphe.adjacence[u])
        for u in sommets
    }
    pile: List[str] = []
    temps = 0
    retours_arriere = 0

    for depart in sommets:
        if couleur[depart] != Couleur.BLANC:
            continue

        temps += 1
        decouverte[depart] = temps
        couleur[depart] = Couleur.GRIS
        ordre_visite.append(depart)
        pile.append(depart)
        _ajouter_etape(trace, enregistrer_trace, temps, "EMPILE_RACINE", depart, f"d[{depart}] = {temps}, empilement sur LIFO", pile)

        while pile:
            u = pile[-1]
            v = next(adj_iter[u], None)

            if v is not None:
                if couleur[v] == Couleur.BLANC:
                    parents[v] = u
                    arcs_classes.append((u, v, TypeArc.ARBRE))
                    _ajouter_etape(trace, enregistrer_trace, temps, "CHOIX_BRANCHE", u, f"Arc ({u} -> {v}) [ARBRE] : empilement de {v}", pile)
                    temps += 1
                    decouverte[v] = temps
                    couleur[v] = Couleur.GRIS
                    ordre_visite.append(v)
                    pile.append(v)
                    _ajouter_etape(trace, enregistrer_trace, temps, "DECOUVERTE", v, f"d[{v}] = {temps}, passage en GRIS", pile)
                else:
                    type_arc = _classer_arc_visite(u, v, couleur, decouverte)
                    arcs_classes.append((u, v, type_arc))
                    _ajouter_etape(trace, enregistrer_trace, temps, "INSPECTION", u, f"Arc ({u} -> {v}) [{type_arc.value}]", pile)
            else:
                temps += 1
                fin[u] = temps
                couleur[u] = Couleur.NOIR
                ordre_fermeture.append(u)
                _ajouter_etape(trace, enregistrer_trace, temps, "DEPILE_FIN", u, f"f[{u}] = {temps}, dépilement (NOIR)", pile)
                pile.pop()
                if pile:
                    retours_arriere += 1
                    _ajouter_etape(trace, enregistrer_trace, temps, "RETOUR_ARRIERE", pile[-1], f"Backtrack de {u} vers {pile[-1]}", pile)

    return ResultatDFS(
        ordre_visite=ordre_visite,
        ordre_fermeture=ordre_fermeture,
        decouverte=decouverte,
        fin=fin,
        parents=parents,
        arcs_classes=arcs_classes,
        trace=trace,
        nombre_retours_arriere=retours_arriere,
    )
