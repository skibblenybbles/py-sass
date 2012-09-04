from ..utils import PRODUCTION
from Selectors import Selectors
from Declarations import Declarations
from ActionSelectors import ActionSelectors


class Ruleset(Selectors, Declarations, ActionSelectors):
    
    # ruleset
    # : selectors LBRACE space-opt declarations RBRACE space-opt
    @PRODUCTION(
        "ruleset : selectors _before-selectors LBRACE space-opt declarations _after-selectors RBRACE space-opt",
    )
    def p_ruleset(self, t):
        # TODO - build AST
        pass
