from chemlogic.datasets.Dataset import Dataset


class PTCMM(Dataset):
    def __init__(self, param_size):
        atom_types = [f"atom_{i}" for i in range(20)]
        key_atoms = ["atom_1", "atom_2", "atom_3", "atom_7"]
        bond_types = ["b_1", "b_2", "b_3", "b_0"]

        super().__init__(
            "ptc_mm",
            "atom_embed",
            "bond_embed",
            "bond",
            atom_types,
            key_atoms,
            bond_types,
            "b_2",
            "b_1",
            "b_0",
            ["b_0", "b_1", "b_2"],
            ["b_3"],
            "atom_5",
            "atom_2",
            "h",
            "atom_3",
            "atom_7",
            ["atom_9", "atom_6", "atom_8", "atom_15"],
            param_size,
        )
