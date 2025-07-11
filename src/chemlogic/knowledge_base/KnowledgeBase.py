## TODO: Knowledge base builder, choose which chemical rules or subgraph rules you want, then general rules, oxy, etc each one class. Later will modularize and extend to accept each individual.


from chemlogic.utils.ChemTemplate import ChemTemplate as Template


class KnowledgeBase(Template):
    required_keys = ["param_size", "layer_name"]

    def __init__(
        self,
        layer_name: str,
        param_size: tuple,
        node_embed: str = "",
        edge_embed: str = "",
        connection: str = "",
        single_bond: str = "",
        double_bond: str = "",
        triple_bond: str = "",
        aromatic_bond: str = "",
        aliphatic_bond: str = "",
        hydrogen: str = "",
        carbon: str = "",
        oxygen: str = "",
        nitrogen: str = "",
        sulfur: str = "",
        min_cycle_size: int = 3,  # cycles os size 2 do not make sense
        max_cycle_size: int = 8,
        atom_type: str = "",
        nbh_min_size: int = 3,
        nbh_max_size: int = 5,
        max_depth: int = 3,
        **kwargs,
    ):
        super().__init__()

        local_vars = locals()
        missing_keys = [key for key in self.required_keys if not local_vars.get(key)]

        if missing_keys:
            raise ValueError(
                f"Missing or empty required params: {', '.join(missing_keys)}"
            )

        if not isinstance(param_size, tuple):
            raise TypeError(
                f"Argument param_size must be tuple, {type(param_size)} not supported"
            )

        # General
        self.layer_name = layer_name
        self.param_size = param_size

        # Embeddings
        self.node_embed = node_embed
        self.edge_embed = edge_embed

        # Bonds
        self.connection = connection
        self.single_bond = single_bond
        self.double_bond = double_bond
        self.triple_bond = triple_bond
        self.aromatic_bond = aromatic_bond
        self.aliphatic_bond = aliphatic_bond

        # Atoms
        self.hydrogen = hydrogen
        self.carbon = carbon
        self.oxygen = oxygen
        self.nitrogen = nitrogen
        self.sulfur = sulfur
        self.atom_type = atom_type

        # Integers
        self.min_cycle_size = min_cycle_size
        self.max_cycle_size = max_cycle_size
        self.nbh_min_size = nbh_min_size
        self.nbh_max_size = nbh_max_size
        self.max_depth = max_depth

        self.create_template()
