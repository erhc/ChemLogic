import unittest

from chemlogic.datasets import (
    COX,
    DHFR,
    ER,
    MUTAG,
    PTC,
    PTCFM,
    PTCFR,
    PTCMM,
    CustomDataset,
    Dataset,
    get_available_datasets,
    get_dataset,
    get_dataset_len,
)


class TestDataset(unittest.TestCase):
    def test_valid_arguments(self):
        Dataset(
            dataset_name="cox",
            node_embed="a",
            edge_embed="a",
            connection="a",
            atom_types=["a"],
            key_atom_type=["a"],
            bond_types=["a"],
            single_bond="a",
            double_bond="a",
            triple_bond="a",
            aliphatic_bonds=["a"],
            aromatic_bonds=["a"],
            carbon="c",
            oxygen="o",
            hydrogen="h",
            nitrogen="n",
            sulfur="s",
            halogens=["f"],
            param_size=1,
        )

    def test_load_data_nonexisting_file(self):
        with self.assertRaises(FileNotFoundError) as context:
            Dataset(
                dataset_name="hello",
                node_embed="a",
                edge_embed="a",
                connection="a",
                atom_types=["a"],
                key_atom_type=["a"],
                bond_types=["a"],
                single_bond="a",
                double_bond="a",
                triple_bond="a",
                aliphatic_bonds=["a"],
                aromatic_bonds=["a"],
                carbon="c",
                oxygen="o",
                hydrogen="h",
                nitrogen="n",
                sulfur="s",
                halogens=["f"],
                param_size=1,
            )
            self.assertIn("does not exist", str(context.exception))

    def test_wrong_param_size(self):
        with self.assertRaises(ValueError) as context:
            Dataset(
                dataset_name="hello",
                node_embed="a",
                edge_embed="a",
                connection="a",
                atom_types=["a"],
                key_atom_type=["a"],
                bond_types=["a"],
                single_bond="a",
                double_bond="a",
                triple_bond="a",
                aliphatic_bonds=["a"],
                aromatic_bonds=["a"],
                carbon="c",
                oxygen="o",
                hydrogen="h",
                nitrogen="n",
                sulfur="s",
                halogens=["f"],
                param_size=-1,
            )
            self.assertIn("positive", str(context.exception))


class TestDatasetClasses(unittest.TestCase):
    def test_anti_sarscov2_activity(self):
        CustomDataset(
            examples=None,
            queries=None,
            param_size=1,
            dataset_name="anti_sarscov2_activity",
        )

    def test_blood_brain_barrier(self):
        CustomDataset(
            examples=None,
            queries=None,
            param_size=1,
            dataset_name="blood_brain_barrier",
        )

    def test_carcinogenous(self):
        CustomDataset(
            examples=None,
            queries=None,
            param_size=1,
            dataset_name="carcinogenous",
        )

    def test_cyp2c9_substrate(self):
        CustomDataset(
            examples=None,
            queries=None,
            param_size=1,
            dataset_name="cyp2c9_substrate",
        )

    def test_cyp2d6_substrate(self):
        CustomDataset(
            examples=None,
            queries=None,
            param_size=1,
            dataset_name="cyp2d6_substrate",
        )

    def test_cyp3a4_substrate(self):
        CustomDataset(
            examples=None,
            queries=None,
            param_size=1,
            dataset_name="cyp3a4_substrate",
        )

    def test_human_intestinal_absorption(self):
        CustomDataset(
            examples=None,
            queries=None,
            param_size=1,
            dataset_name="human_intestinal_absorption",
        )

    def test_oral_bioavailability(self):
        CustomDataset(
            examples=None,
            queries=None,
            param_size=1,
            dataset_name="oral_bioavailability",
        )

    def test_p_glycoprotein_inhibition(self):
        CustomDataset(
            examples=None,
            queries=None,
            param_size=1,
            dataset_name="p_glycoprotein_inhibition",
        )

    def test_pampa_permeability(self):
        CustomDataset(
            examples=None,
            queries=None,
            param_size=1,
            dataset_name="pampa_permeability",
        )

    def test_skin_reaction(self):
        CustomDataset(
            examples=None,
            queries=None,
            param_size=1,
            dataset_name="skin_reaction",
        )

    def test_nonexistent_custom(self):
        with self.assertRaises(FileNotFoundError):
            CustomDataset(
                examples="test",
                queries="test",
                param_size=1,
                dataset_name="test",
            )

    def test_cox(self):
        COX(param_size=1)

    def test_dhfr(self):
        DHFR(param_size=1)

    def test_er(self):
        ER(param_size=1)

    def test_mutag(self):
        MUTAG(param_size=1)

    def test_ptc(self):
        PTC(param_size=1)

    def test_ptcfm(self):
        PTCFM(param_size=1)

    def test_ptcfr(self):
        PTCFR(param_size=1)

    def test_ptcmm(self):
        PTCMM(param_size=1)


class TestDatasetLoader(unittest.TestCase):
    def test_get_available_datasets(self):
        datasets = get_available_datasets()
        self.assertIn("mutagen", datasets)
        self.assertIn("carcinogenous", datasets)

    def test_get_dataset_len(self):
        self.assertEqual(get_dataset_len("mutagen"), 183)
        self.assertEqual(get_dataset_len("nonexistent"), 0)

    def test_get_custom_dataset(self):
        dataset = get_dataset("carcinogenous", param_size=1)
        self.assertIsInstance(dataset, CustomDataset)

    def test_get_predefined_dataset(self):
        dataset = get_dataset("mutagen", param_size=1)
        self.assertIsInstance(dataset, MUTAG)

    def test_invalid_dataset_name(self):
        with self.assertRaises(ValueError):
            get_dataset("invalid_dataset", param_size=1)
