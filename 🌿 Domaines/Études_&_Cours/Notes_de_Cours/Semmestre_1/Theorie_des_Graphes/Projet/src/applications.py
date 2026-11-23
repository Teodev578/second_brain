"""Applications de DFS : détection de cycles, tri topologique (DAG) et composantes connexes."""

from __future__ import annotations

from typing import Dict, Iterator, List, Optional, Tuple

from dfs import dfs_iteratif_pile
from graphe import Graphe, ResultatDFS, TypeArc


def _reconstruire_cycle(
    u: str,
    v: str,
    parents: Dict[str, Optional[str]],
) -> List[str]:
    """Reconstruit le circuit passant par l'arc arrière (u -> v) en remontant les parents."""
    chemin: List[str] = [u]
    courant: Optional[str] = u
    while courant is not None and courant != v:
        courant = parents[courant]
        if courant is not None:
            chemin.append(courant)
    chemin.reverse()
    chemin.append(v)
    return chemin


def extraire_cycle_oriente(resultat: ResultatDFS) -> Optional[List[str]]:
    """Extrait le premier circuit trouvé à partir d'un résultat DFS, ou None si acyclique."""
    for u, v, type_arc in resultat.arcs_classes:
        if type_arc == TypeArc.ARRIERE:
            return _reconstruire_cycle(u, v, resultat.parents)
    return None


def detecter_cycle_oriente(graphe: Graphe) -> Optional[List[str]]:
    """
    Détecte la présence d'un circuit dans un graphe orienté par recherche d'arc arrière.

    Retourne la liste des sommets formant le premier cycle trouvé (ex: ['B', 'D', 'E', 'B']),
    ou None si le graphe est un DAG.
    """
    resultat = dfs_iteratif_pile(graphe, enregistrer_trace=False)
    return extraire_cycle_oriente(resultat)


def tri_topologique_dag(graphe: Graphe) -> Tuple[bool, List[str]]:
    """
    Calcule le tri topologique d'un DAG en un seul parcours DFS.

    Retourne (True, ordre_topologique) par ordre décroissant des dates de fin f[u]
    si le graphe est acyclique, ou (False, cycle_detecte) s'il contient un circuit.
    """
    if not graphe.oriente:
        raise ValueError("Le tri topologique ne s'applique qu'aux graphes orientés.")

    resultat = dfs_iteratif_pile(graphe, enregistrer_trace=False)
    cycle = extraire_cycle_oriente(resultat)
    if cycle is not None:
        return False, cycle

    # L'ordre de fermeture donne f[u] croissant ; son inverse donne f[u] décroissant
    return True, list(reversed(resultat.ordre_fermeture))


def composantes_connexes(graphe: Graphe) -> List[List[str]]:
    """
    Trouve les composantes connexes d'un graphe non orienté par DFS itératif
    (pile explicite et itérateurs par sommet, d'après Sedgewick & Wayne).
    """
    if graphe.oriente:
        raise ValueError("La recherche de composantes connexes attend un graphe non orienté.")

    sommets = graphe.sommets()
    visites: set[str] = set()
    adj_iter: Dict[str, Iterator[str]] = {
        u: iter(sorted(graphe.adjacence[u])) for u in sommets
    }
    composantes: List[List[str]] = []

    for depart in sommets:
        if depart in visites:
            continue
        composante: List[str] = [depart]
        pile: List[str] = [depart]
        visites.add(depart)
        while pile:
            u = pile[-1]
            v = next(adj_iter[u], None)
            if v is not None:
                if v not in visites:
                    visites.add(v)
                    composante.append(v)
                    pile.append(v)
            else:
                pile.pop()
        composantes.append(sorted(composante))

    return composantes
