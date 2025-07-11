from neuralogic.utils.data import Mutagenesis

from chemlogic.datasets.Dataset import Dataset


# TODO: try the MUTAG from TUD datasets (different bond types and implicit hydrogens)
class MUTAG(Dataset):
    def __init__(self, param_size):
        atom_types = ["c", "o", "br", "i", "f", "h", "n", "cl"]
        key_atoms = ["o", "s", "n"]
        bond_types = ["b_1", "b_2", "b_3", "b_4", "b_5", "b_7"]

        super().__init__(
            "mutag",
            "atom_embed",
            "bond_embed",
            "bond",
            atom_types,
            key_atoms,
            bond_types,
            "b_1",
            "b_2",
            "b_3",
            ["b_1", "b_2", "b_3"],
            ["b_4", "b_5", "b_6", "b_7"],
            "c",
            "o",
            "h",
            "n",
            "s",
            ["f", "cl", "br", "i"],
            param_size,
        )

    def load_data(self):
        _, dataset = Mutagenesis()
        return dataset
