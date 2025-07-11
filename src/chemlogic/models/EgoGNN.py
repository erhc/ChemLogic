from neuralogic.core import R, V

from chemlogic.models.Model import Model


class EgoGNN(Model):
    def __init__(self, *args, **kwargs):
        kwargs["model_name"] = "ego"
        super().__init__(*args, **kwargs)

    def build_layer(self, current_layer: str, previous_layer: str) -> list:
        template = []
        template += [
            R.get(current_layer + "_multigraph")(V.X)
            <= (
                R.get(self.connection)(V.X, V.Y, V.B),
                R.get(self.edge_embed)(V.B)[self.param_size],
                R.get(previous_layer)(V.Y)[self.param_size],
            )
        ]

        template += [
            R.get(current_layer)(V.X)
            <= (
                R.get(self.connection)(V.X, V.Y, V.B),
                R.get(current_layer + "_multigraph")(V.Y)[self.param_size],
            )
        ]
        return template
