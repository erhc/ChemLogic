from abc import abstractmethod

from neuralogic.core import Template
from neuralogic.core.constructs.relation import BaseRelation, WeightedRelation
from neuralogic.core.constructs.rule import Rule


class ChemTemplate(Template):
    """
    Abstract class representing a template.

    Inherits from neuralogic.core.Template and adds functionality for template operations.
    """

    def __init__(self):
        super().__init__()

    def __add__(self, other):
        if isinstance(other, Template):
            self.add_rules(other.template)

        elif isinstance(other, list):
            self.add_rules(other)
        else:
            raise NotImplementedError(f"Cannot add `{type(self)}` and `{type(other)}`")
        self.flatten()
        return self

    # TODO: integrate this with adding logic to make it faster
    def flatten(self):
        template = []
        for rule in self.template:
            if isinstance(rule, BaseRelation | WeightedRelation | Rule):
                template.append(rule)
            elif isinstance(rule, Template):
                template.extend(rule.template)
        self.template = template

    @abstractmethod
    def create_template(self):
        pass
