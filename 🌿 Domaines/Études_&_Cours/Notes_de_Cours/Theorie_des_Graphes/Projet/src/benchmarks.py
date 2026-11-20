"""Jeux de données d'exemple, générateurs de graphes et mesures de temps pour DFS."""

from __future__ import annotations

import random
import time
from typing import Dict, List, Tuple

from applications import composantes_connexes
from dfs import dfs_iteratif_pile, dfs_recursif
from graphe import Graphe, TypeArc


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
    """Construit le DAG de 8 tâches dépendantes (pipeline logiciel)."""
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
    for tache in libelles:
        dag.ajouter_sommet(tache)
    for u, v in arcs:
        dag.ajouter_arc(u, v)
    return dag, libelles


def construire_reseau_non_connexe() -> Graphe:
    """Construit un réseau non orienté de 9 routeurs répartis en 3 groupes isolés."""
    reseau = Graphe(oriente=False)
    liens = [
        ("R1", "R2"), ("R2", "R3"), ("R3", "R4"), ("R1", "R4"),
        ("R5", "R6"), ("R6", "R7"),
        ("R8", "R9"),
    ]
    for u, v in liens:
        reseau.ajouter_arc(u, v)
    return reseau


def construire_chaine(nb_sommets: int, prefixe: str = "V") -> Graphe:
    """Construit une chaîne linéaire orientée de nb_sommets sommets."""
    chaine = Graphe(oriente=True)
    for i in range(nb_sommets - 1):
        chaine.ajouter_arc(f"{prefixe}{i:04d}", f"{prefixe}{i + 1:04d}")
    return chaine


def generer_graphes_test(graine: int = 42) -> List[Tuple[str, Graphe]]:
    """Génère 6 formes de graphes variées de façon reproductible (graine fixe)."""
    rng = random.Random(graine)
    jeux: List[Tuple[str, Graphe]] = []

    # 1. Chaîne linéaire orientée (n = 500)
    jeux.append(("Chaîne linéaire (orienté)", construire_chaine(500, "V")))

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

    # 3. Graphe complet dense orienté sans boucle (n = 200)
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
            non_connexe.ajouter_arc(f"S{base + i:03d}", f"S{base + i + 1:03d}")
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

    # 6. Graphe cyclique modéré (n = 500, m = 1200)
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


def executer_mesure(nom: str, graphe: Graphe) -> Dict[str, object]:
    """Mesure les temps d'exécution des deux versions de DFS sur un graphe."""
    t0 = time.perf_counter()
    dfs_recursif(graphe, trier_voisins=False, enregistrer_trace=False)
    t_rec_ms = (time.perf_counter() - t0) * 1000

    t1 = time.perf_counter()
    res_it = dfs_iteratif_pile(graphe, trier_voisins=False, enregistrer_trace=False)
    t_it_ms = (time.perf_counter() - t1) * 1000

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
