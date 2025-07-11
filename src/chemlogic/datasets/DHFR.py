from chemlogic.datasets.Dataset import Dataset


class DHFR(Dataset):
    def __init__(self, param_size):
        atom_types = [f"atom_{i}" for i in range(7)]
        key_atoms = ["atom_0", "atom_5", "atom_3"]
        bond_types = ["b_4", "b_2", "b_3", "b_0", "b_1"]

        super().__init__(
            "dhfr",
            "atom_embed",
            "bond_embed",
            "bond",
            atom_types,
            key_atoms,
            bond_types,
            "b_2",
            "b_3",
            "b_4",
            ["b_2", "b_3", "b_4"],
            ["b_0"],
            "atom_1",
            "atom_3",
            "h",
            "atom_0",
            "atom_5",
            ["atom_2", "atom_4", "atom_6"],
            param_size,
        )
