from neuralogic.core import R, V

from chemlogic.models.Model import Model


class GNN(Model):
    def __init__(self, *args, **kwargs):
        kwargs["model_name"] = "gnn"
        super().__init__(*args, **kwargs)

    # gnn_k(X) <=  gnn_k-1(X), gnn_k-1(Y), connection(X, Y, B), edge_embed(B)
    def build_layer(self, current_layer: str, previous_layer: str) -> list:
        return [
            (
                R.get(current_layer)(V.X)
                <= (
                    R.get(previous_layer)(V.X)[self.param_size],
                    R.get(previous_layer)(V.Y)[self.param_size],
                    R.get(self.connection)(
                        V.X, V.Y, V.B
                    ),  # should be first to ground faster?
                    R.get(self.edge_embed)(V.B),
                )
            )
        ]  # why not parametrized?
