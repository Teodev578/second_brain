#!/usr/bin/env python3
"""Tests unitaires de parité, d'applications structurelles et de tenue en profondeur."""

from __future__ import annotations

import unittest

from applications import composantes_connexes, detecter_cycle_oriente, tri_topologique_dag
from benchmarks import (
    construire_chaine,
    construire_graphe_exemple,
    construire_pipeline_taches,
    construire_reseau_non_connexe,
    generer_graphes_test,
)
from dfs import dfs_iteratif_pile, dfs_recursif
from graphe import Graphe


class TestParcoursDFS(unittest.TestCase):
    """Vérifie le fonctionnement des deux versions de DFS et de leurs applications."""

    def test_parite_recursif_iteratif_sur_gex(self) -> None:
        g_ex = construire_graphe_exemple()
        res_rec = dfs_recursif(g_ex, source_prioritaire="A", enregistrer_trace=True)
        res_it = dfs_iteratif_pile(g_ex, source_prioritaire="A", enregistrer_trace=True)

        self.assertEqual(res_rec.ordre_visite, res_it.ordre_visite)
        self.assertEqual(res_rec.ordre_fermeture, res_it.ordre_fermeture)
        self.assertEqual(res_rec.decouverte, res_it.decouverte)
        self.assertEqual(res_rec.fin, res_it.fin)
        self.assertEqual(res_rec.parents, res_it.parents)
        self.assertEqual(res_rec.arcs_classes, res_it.arcs_classes)
        self.assertEqual(res_rec.nombre_retours_arriere, res_it.nombre_retours_arriere)

        self.assertEqual(res_it.ordre_visite, ["A", "B", "D", "E", "G", "C", "F"])
        self.assertEqual(res_it.ordre_fermeture, ["E", "G", "D", "B", "F", "C", "A"])
        self.assertEqual(
            {s: (res_it.decouverte[s], res_it.fin[s]) for s in g_ex.sommets()},
            {
                "A": (1, 14),
                "B": (2, 9),
                "C": (10, 13),
                "D": (3, 8),
                "E": (4, 5),
                "F": (11, 12),
                "G": (6, 7),
            },
        )
        self.assertEqual(res_it.nombre_retours_arriere, 6)
        self.assertEqual(detecter_cycle_oriente(g_ex), ["B", "D", "E", "B"])

    def test_tri_topologique_dag_et_cycle(self) -> None:
        dag, _ = construire_pipeline_taches()
        est_dag, ordre = tri_topologique_dag(dag)
        self.assertTrue(est_dag)
        self.assertEqual(len(ordre), 8)
        for u, voisins in dag.adjacence.items():
            for v in voisins:
                self.assertLess(ordre.index(u), ordre.index(v))

        dag_fautif = dag.copier()
        dag_fautif.ajouter_arc("T7", "T2")
        est_dag_2, cycle = tri_topologique_dag(dag_fautif)
        self.assertFalse(est_dag_2)
        self.assertEqual(cycle, ["T2", "T4", "T6", "T7", "T2"])

        with self.assertRaises(ValueError):
            tri_topologique_dag(Graphe(oriente=False))

    def test_composantes_connexes(self) -> None:
        reseau = construire_reseau_non_connexe()
        groupes = composantes_connexes(reseau)
        self.assertEqual(
            groupes,
            [
                ["R1", "R2", "R3", "R4"],
                ["R5", "R6", "R7"],
                ["R8", "R9"],
            ],
        )

        with self.assertRaises(ValueError):
            composantes_connexes(Graphe(oriente=True))

    def test_parite_sur_six_formes(self) -> None:
        for nom, g in generer_graphes_test():
            with self.subTest(graphe=nom):
                res_rec = dfs_recursif(g, trier_voisins=False, enregistrer_trace=False)
                res_it = dfs_iteratif_pile(g, trier_voisins=False, enregistrer_trace=False)
                self.assertEqual(res_rec.ordre_visite, res_it.ordre_visite)
                self.assertEqual(res_rec.ordre_fermeture, res_it.ordre_fermeture)
                self.assertEqual(res_rec.decouverte, res_it.decouverte)
                self.assertEqual(res_rec.fin, res_it.fin)
                self.assertEqual(res_rec.arcs_classes, res_it.arcs_classes)
                self.assertEqual(res_rec.nombre_retours_arriere, res_it.nombre_retours_arriere)

    def test_profondeur_extreme_chaine_2000(self) -> None:
        chaine = construire_chaine(2000, "P")
        with self.assertRaises(RecursionError):
            dfs_recursif(chaine, trier_voisins=False, enregistrer_trace=False)

        res_it = dfs_iteratif_pile(chaine, trier_voisins=False, enregistrer_trace=False)
        self.assertEqual(len(res_it.ordre_visite), 2000)
        self.assertEqual(res_it.nombre_retours_arriere, 1999)


if __name__ == "__main__":
    unittest.main()
