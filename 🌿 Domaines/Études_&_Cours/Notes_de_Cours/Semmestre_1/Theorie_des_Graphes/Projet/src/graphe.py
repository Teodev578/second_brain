"""Structures de données de base pour l'étude du parcours en profondeur (DFS)."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional, Tuple


class Couleur(str, Enum):
    """États d'un sommet durant un parcours en profondeur."""

    BLANC = "BLANC"  # Sommet non encore découvert
    GRIS = "GRIS"    # Sommet ouvert, parcours des voisins en cours (sur la pile)
    NOIR = "NOIR"    # Sommet terminé (tous ses voisins sont traités)


class TypeArc(str, Enum):
    """Catégories d'arcs rencontrées lors d'un parcours DFS."""

    ARBRE = "ARBRE"      # Découverte d'un sommet BLANC
    ARRIERE = "ARRIERE"  # Lien vers un ancêtre GRIS (prouve un cycle)
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
        """Ajoute un arc (source -> destination), ou une arête si le graphe est non orienté."""
        self.ajouter_sommet(source)
        self.ajouter_sommet(destination)
        if destination not in self.adjacence[source]:
            self.adjacence[source].append(destination)
        if not self.oriente and source not in self.adjacence[destination]:
            self.adjacence[destination].append(source)

    def sommets(self) -> List[str]:
        """Retourne les sommets triés par ordre alphabétique."""
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
    """Enregistrement d'une étape du parcours pour l'affichage détaillé."""

    instant: int
    action: str
    sommet: str
    detail: str
    pile_active: List[str]


@dataclass
class ResultatDFS:
    """Résultat complet d'un parcours en profondeur (ordres, dates, parents, arcs)."""

    ordre_visite: List[str]
    ordre_fermeture: List[str]
    decouverte: Dict[str, int]
    fin: Dict[str, int]
    parents: Dict[str, Optional[str]]
    arcs_classes: List[Tuple[str, str, TypeArc]]
    trace: List[EtapeTrace]
    nombre_retours_arriere: int
