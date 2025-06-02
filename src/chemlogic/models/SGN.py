from neuralogic.core import R, V

from chemlogic.models.Model import Model


class SGN(Model):
    def __init__(self, *args, **kwargs):
        kwargs["model_name"] = "sgn"

        self.max_depth = kwargs.pop("max_depth", 3)
        if not isinstance(self.max_depth, int) or self.max_depth < 1:
            raise TypeError("`max_depth` must be a positive integer.")

        super().__init__(*args, **kwargs)

    # Creating SGN sets up to max depth
    def build_layer(self, current_layer: str, previous_layer: str) -> list:
        template = []

        # First order SGN aggregates node embeddings sharing an edge, ensuring higher orders are connected
        template += [
            R.get(f"{current_layer}_order_1")(V.X, V.Y)
            <= (
                R.get(self.connection)(V.X, V.Y, V.B),
                R.get(self.edge_embed)(V.B)[self.param_size],
                R.get(previous_layer)(V.X)[self.param_size],
                R.get(previous_layer)(V.Y)[self.param_size],
            )
        ]

        # Constructing orders
        for i in range(2, self.max_depth + 1):
            template += [
                R.get(f"{current_layer}_order_{i}")(V.X, V.Y)
                <= (
                    R.get(f"{current_layer}_order_{i - 1}")(V.X, V.Y)[self.param_size],
                    R.get(f"{current_layer}_order_{i - 1}")(V.Y, V.Z)[self.param_size],
                )
            ]

        # Extracting Subgraph messages to nodes
        template += [
            R.get(current_layer)(V.X)
            <= (R.get(f"{current_layer}_order_{self.max_depth}")(V.X, V.Y)),
            R.get(current_layer)(V.Y)
            <= (R.get(f"{current_layer}_order_{self.max_depth}")(V.X, V.Y)),
        ]
        return template
