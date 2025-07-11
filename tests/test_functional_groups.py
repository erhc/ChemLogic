import unittest

from neuralogic.core import Template

from chemlogic.knowledge_base.functional_groups.GeneralFunctionalGroups import (
    GeneralFunctionalGroups,
)
from chemlogic.knowledge_base.functional_groups.Hydrocarbons import Hydrocarbons


class TestFunctionalGroupModules(unittest.TestCase):
    def setUp(self):
        self.common_args = {
            "layer_name": "fg_layer",
            "param_size": (4, 4),
            "node_embed": "node",
            "edge_embed": "edge",
            "connection": "connects",
            "single_bond": "sb",
            "double_bond": "db",
            "triple_bond": "tb",
            "aromatic_bond": "ar",
            "hydrogen": "H",
            "carbon": "C",
            "oxygen": "O",
        }

    # GeneralFunctionalGroups
    def test_general_functional_groups_instantiation(self):
        fg = GeneralFunctionalGroups(**self.common_args)
        self.assertIsInstance(fg, Template)
        self.assertEqual(fg.layer_name, "fg_layer")

    def test_general_functional_groups_missing_required_param(self):
        for key in GeneralFunctionalGroups.required_keys:
            args = {k: v for k, v in self.common_args.items() if k != key}
            with self.assertRaises((ValueError, TypeError)):
                GeneralFunctionalGroups(**args)

    def test_general_functional_groups_rule_structure(self):
        fg = GeneralFunctionalGroups(**self.common_args)
        rules_str = str(fg)
        expected_predicates = [
            "bond_message",
            "single_bonded",
            "double_bonded",
            "triple_bonded",
            "aromatic_bonded",
            "saturated",
            "halogen_group",
            "hydroxyl",
            "carbonyl_group",
            "general_groups",
        ]
        for name in expected_predicates:
            self.assertIn(f"fg_layer_{name}", rules_str)

    # Hydrocarbons
    def test_hydrocarbons_instantiation(self):
        args = {
            "layer_name": "hydro_layer",
            "param_size": (4, 4),
            "carbon": "C",
        }
        hc = Hydrocarbons(**args)
        self.assertIsInstance(hc, Template)
        self.assertEqual(hc.layer_name, "hydro_layer")

    def test_hydrocarbons_missing_required_param(self):
        for key in Hydrocarbons.required_keys:
            args = {
                "layer_name": "hydro_layer",
                "param_size": (4, 4),
                "carbon": "C",
            }
            args.pop(key, None)
            with self.assertRaises((ValueError, TypeError)):
                Hydrocarbons(**args)

    def test_hydrocarbons_rule_structure(self):
        args = {
            "layer_name": "hydro_layer",
            "param_size": (4, 4),
            "carbon": "C",
        }
        hc = Hydrocarbons(**args)
        rules_str = str(hc)
        expected_predicates = [
            "benzene_ring",
            "alkene_bond",
            "alkyne_bond",
            "hydrocarbon_groups",
        ]
        for name in expected_predicates:
            self.assertIn(f"hydro_layer_{name}", rules_str)
