import unittest

from neuralogic.core import Template

from chemlogic.knowledge_base.subgraph_patterns.CircularPatterns import CircularPatterns
from chemlogic.knowledge_base.subgraph_patterns.CollectivePatterns import (
    CollectivePatterns,
)
from chemlogic.knowledge_base.subgraph_patterns.CyclePattern import CyclePattern
from chemlogic.knowledge_base.subgraph_patterns.NeighborhoodPatterns import (
    NeighborhoodPatterns,
)
from chemlogic.knowledge_base.subgraph_patterns.PathPattern import PathPattern
from chemlogic.knowledge_base.subgraph_patterns.YShapePattern import YShapePattern


class TestSubgraphPatternModules(unittest.TestCase):
    def setUp(self):
        self.common_args = {
            "layer_name": "test_layer",
            "param_size": (4, 4),
            "node_embed": "node",
            "edge_embed": "edge",
            "connection": "connects",
        }

    # CircularPatterns
    def test_circular_instantiation(self):
        args = {
            **self.common_args,
            "single_bond": "sb",
            "double_bond": "db",
            "carbon": "C",
        }
        pattern = CircularPatterns(**args)
        self.assertIsInstance(pattern, Template)

    def test_circular_missing_required_param(self):
        required = CircularPatterns.required_keys
        for key in required:
            args = {
                **self.common_args,
                "single_bond": "sb",
                "double_bond": "db",
                "carbon": "C",
            }
            args.pop(key, None)
            with self.assertRaises((ValueError, TypeError)):
                CircularPatterns(**args)

    # CollectivePatterns
    def test_collective_instantiation(self):
        args = {
            **self.common_args,
            "aliphatic_bond": "sb",
            "carbon": "C",
            "max_depth": 3,
        }
        pattern = CollectivePatterns(**args)
        self.assertIsInstance(pattern, Template)

    def test_collective_missing_required_param(self):
        required = CollectivePatterns.required_keys
        for key in required:
            args = {
                **self.common_args,
                "aliphatic_bond": "sb",
                "carbon": "C",
                "max_depth": 3,
            }
            args.pop(key, None)
            with self.assertRaises((ValueError, TypeError)):
                CollectivePatterns(**args)

    # CyclePattern
    def test_cycle_instantiation(self):
        args = {
            **self.common_args,
            "min_cycle_size": 3,
            "max_cycle_size": 6,
        }
        pattern = CyclePattern(**args)
        self.assertIsInstance(pattern, Template)

    def test_cycle_invalid_min_cycle_size(self):
        args = {
            **self.common_args,
            "min_cycle_size": 2,
            "max_cycle_size": 6,
        }
        with self.assertRaises(ValueError):
            CyclePattern(**args)

    def test_cycle_invalid_max_cycle_size(self):
        args = {
            **self.common_args,
            "min_cycle_size": 3,
            "max_cycle_size": 3,
        }
        with self.assertRaises(ValueError):
            CyclePattern(**args)

    # NeighborhoodPatterns
    def test_neighborhood_instantiation(self):
        args = {
            **self.common_args,
            "atom_type": "atom",
            "carbon": "C",
            "nbh_min_size": 3,
            "nbh_max_size": 5,
        }
        pattern = NeighborhoodPatterns(**args)
        self.assertIsInstance(pattern, Template)

    def test_neighborhood_invalid_nbh_min_size(self):
        args = {
            **self.common_args,
            "atom_type": "atom",
            "carbon": "C",
            "nbh_min_size": 2,
            "nbh_max_size": 5,
        }
        with self.assertRaises(ValueError):
            NeighborhoodPatterns(**args)

    def test_neighborhood_invalid_nbh_max_size(self):
        args = {
            **self.common_args,
            "atom_type": "atom",
            "carbon": "C",
            "nbh_min_size": 4,
            "nbh_max_size": 3,
        }
        with self.assertRaises(ValueError):
            NeighborhoodPatterns(**args)

    # PathPattern
    def test_path_instantiation(self):
        args = {
            **self.common_args,
            "max_depth": 4,
        }
        pattern = PathPattern(**args)
        self.assertIsInstance(pattern, Template)

    def test_path_invalid_max_depth(self):
        args = {
            **self.common_args,
            "max_depth": 2,
        }
        with self.assertRaises(ValueError):
            PathPattern(**args)

    # YShapePattern
    def test_yshape_instantiation(self):
        args = {
            **self.common_args,
            "double_bond": "db",
        }
        pattern = YShapePattern(**args)
        self.assertIsInstance(pattern, Template)

    def test_yshape_missing_required_param(self):
        args = {**self.common_args}
        with self.assertRaises(ValueError):
            YShapePattern(**args)
