from neuralogic.core import R, V

from chemlogic.models.Model import Model


class RGCN(Model):
    def __init__(self, *args, **kwargs):
        kwargs["model_name"] = "rgcn"

        # Extract and validate edge_types
        # TODO: maybe make this simpler
        if "edge_types" not in kwargs:
            raise KeyError("Missing required keyword argument: `edge_types`")

        self.edge_types = kwargs.pop("edge_types")
        if not isinstance(self.edge_types, list):
            raise TypeError("`edge_types` must be a list of predicates.")
        if len(self.edge_types) < 2:
            raise ValueError(
                "`edge_types` must contain at least two types. "
                "RGCN with one edge type is equivalent to a standard GNN."
            )

        super().__init__(*args, **kwargs)

    # rgcn_k(X) <=  rgcn_k-1(X), rgcn_k-1(Y), connection(X, Y, B), edge_embed(B), edge_type(B) for all edge types
    def build_layer(self, current_layer: str, previous_layer: str) -> list:
        return [
            (
                R.get(current_layer)(V.X)
                <= (
                    R.get(previous_layer)(V.X)[self.param_size],
                    R.get(previous_layer)(V.Y)[self.param_size],
                    R.get(self.connection)(V.X, V.Y, V.B),
                    # R.get(edge_embed)(V.B), # maybe doesnt make sense to have this, as the information is encoded below
                    R.get(t)(V.B),
                )
            )
            for t in self.edge_types
        ]
