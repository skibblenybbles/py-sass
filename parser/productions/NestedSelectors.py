from ..utils import PRODUCTION
from Selectors import Selectors


class NestedSelectors(Selectors):
    
    ###########################################################################
    # nested selectors
    ###########################################################################
    
    # nested-selectors
    # : selectors LBRACE
    @PRODUCTION(
        "nested-selectors : selectors LBRACE",
    )
    def p_nested_selectors(self, t):
        # TODO - build AST
        pass
