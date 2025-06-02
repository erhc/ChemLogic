from chemlogic.datasets.Dataset import Dataset


class COX(Dataset):
    """
    # TODO write description
    """

    def __init__(self, param_size):
        atom_types = [f"atom_{i}" for i in range(7)]
        key_atoms = ["atom_1", "atom_4", "atom_3"]
        bond_types = ["b_4", "b_2", "b_3", "b_0", "b_1"]

        super().__init__(
            "cox",
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
            "atom_0",
            "atom_4",
            "h",
            "atom_1",
            "atom_3",
            ["atom_2", "atom_5", "atom_6"],
            param_size,
        )
