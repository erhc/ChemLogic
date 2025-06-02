from chemlogic.datasets.Dataset import Dataset


class PTCFM(Dataset):
    def __init__(self, param_size):
        atom_types = [f"atom_{i}" for i in range(18)]
        key_atoms = ["atom_1", "atom_4", "atom_3", "atom_6"]
        bond_types = ["b_1", "b_2", "b_3", "b_0"]

        super().__init__(
            "ptc_fm",
            "atom_embed",
            "bond_embed",
            "bond",
            atom_types,
            key_atoms,
            bond_types,
            "b_1",
            "b_1",
            "b_0",
            ["b_0", "b_1", "b_2"],
            ["b_3"],
            "atom_2",
            "atom_3",
            "h",
            "atom_4",
            "atom_6",
            ["atom_9", "atom_5", "atom_7", "atom_13"],
            param_size,
        )
