#!/usr/bin/env python3
"""
Point d'entrée de démonstration pour le Sujet 2 :
« Le parcours en profondeur (DFS) pour l'exploration et l'analyse de la structure d'un graphe »

Master IT — UE Théorie des Graphes (ASCENCIA KEYCE, Campus de Lomé)
Enseignant : Edem K. HOVI — Année académique 2026-2027
"""

from __future__ import annotations

import sys
import time

from applications import composantes_connexes, detecter_cycle_oriente, tri_topologique_dag
from benchmarks import (
    construire_chaine,
    construire_graphe_exemple,
    construire_pipeline_taches,
    construire_reseau_non_connexe,
    executer_mesure,
    generer_graphes_test,
)
from dfs import dfs_iteratif_pile, dfs_recursif


def afficher_exemple_gex() -> None:
    """Affiche le déroulement pas à pas et le classement des arcs sur G_ex."""
    g_ex = construire_graphe_exemple()
    res = dfs_iteratif_pile(g_ex, source_prioritaire="A", enregistrer_trace=True)

    print("\n[1] ILLUSTRATION SUR LE GRAPHE D'EXEMPLE G_ex (7 sommets, 10 arcs)")
    print("Ordre de découverte :", " -> ".join(res.ordre_visite))
    print("Ordre de fermeture  :", " -> ".join(res.ordre_fermeture))
    print(
        "Dates [d/f]         :",
        ", ".join(f"{s}[{res.decouverte[s]}/{res.fin[s]}]" for s in g_ex.sommets()),
    )
    print("Retours en arrière  :", res.nombre_retours_arriere)

    print("\nTrace pas à pas (DFS itératif / pile active) :")
    for etape in res.trace:
        print(
            f"  t={etape.instant:02d} | {etape.action:<15} | {etape.sommet} | "
            f"Pile={etape.pile_active} | {etape.detail}"
        )

    print("\nClassification des 10 arcs de G_ex :")
    for u, v, typ in res.arcs_classes:
        print(f"  ({u} -> {v}) : {typ.value}")

    cycle_ex = detecter_cycle_oriente(g_ex)
    print(f"Cycle détecté dans G_ex : {' -> '.join(cycle_ex) if cycle_ex else 'Aucun'}")


def afficher_pipeline_dag() -> None:
    """Affiche le tri topologique d'un pipeline valide puis la détection d'un cycle."""
    print("\n" + "-" * 78)
    print("[2] APPLICATION : ORDONNANCEMENT D'UN PIPELINE LOGICIEL (DAG vs CYCLE)")
    dag, libelles = construire_pipeline_taches()
    est_dag, ordre = tri_topologique_dag(dag)
    print(f"Vérification DAG valide : {est_dag}")
    print("Ordre d'exécution topologique obtenu :")
    for rang, tache in enumerate(ordre, start=1):
        print(f"  {rang}. {tache} — {libelles[tache]}")

    dag_fautif = dag.copier()
    dag_fautif.ajouter_arc("T7", "T2")
    est_dag_2, cycle_bloquant = tri_topologique_dag(dag_fautif)
    print(f"\nAprès ajout d'une dépendance fautive (T7 -> T2) -> DAG valide ? {est_dag_2}")
    print("Cycle bloquant identifié :", " -> ".join(cycle_bloquant))


def afficher_composantes_reseau() -> None:
    """Affiche l'extraction des composantes connexes sur un réseau de routeurs."""
    print("\n" + "-" * 78)
    print("[3] APPLICATION : COMPOSANTES CONNEXES D'UN RÉSEAU NON ORIENTÉ")
    reseau = construire_reseau_non_connexe()
    groupes = composantes_connexes(reseau)
    print(f"Nombre de sous-réseaux isolés détectés : {len(groupes)}")
    for numero, ilot in enumerate(groupes, start=1):
        print(f"  Composante {numero} : {ilot}")


def afficher_tests_formes() -> None:
    """Affiche les temps d'exécution et diagnostics sur 6 formes de graphes."""
    print("\n" + "-" * 78)
    print("[4] EXPÉRIMENTATION SUR 6 FORMES DE GRAPHES")
    print(f"{'Forme du graphe':<42} | {'|V|':>4} | {'|E|':>5} | {'Rec(ms)':>7} | {'It(ms)':>7} | {'Diagnostic'}")
    print("-" * 105)
    for nom, g in generer_graphes_test():
        m = executer_mesure(nom, g)
        print(
            f"{m['nom']:<42} | {m['V']:>4} | {m['E']:>5} | "
            f"{m['t_rec_ms']:>7.2f} | {m['t_it_ms']:>7.2f} | {m['diagnostic']}"
        )


def afficher_test_profondeur() -> None:
    """Compare récursif et itératif sur une chaîne linéaire de 2 000 sommets."""
    print("\n" + "-" * 78)
    print("[5] TEST DE PROFONDEUR EXTRÊME (chaîne linéaire |V| = 2 000)")
    chaine_profonde = construire_chaine(2000, "P")

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


def main() -> None:
    print("=" * 78)
    print("SUJET 2 — PARCOURS EN PROFONDEUR (DFS) & ANALYSE STRUCTURELLE")
    print("=" * 78)
    afficher_exemple_gex()
    afficher_pipeline_dag()
    afficher_composantes_reseau()
    afficher_tests_formes()
    afficher_test_profondeur()


if __name__ == "__main__":
    main()
