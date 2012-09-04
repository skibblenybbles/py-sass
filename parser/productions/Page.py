from ..utils import PRODUCTION
from Declarations import Declarations
from ActionSelectors import ActionSelectors


class Page(Declarations, ActionSelectors):
    
    ###########################################################################
    # page
    ###########################################################################
    
    # page
    # : SYM_PAGE space-opt pseudo-page-opt _before-selectors LBRACE space-opt declarations _after-selectors RBRACE space-opt
    @PRODUCTION(
        "page : SYM_PAGE space-opt pseudo-page-opt _before-selectors LBRACE space-opt declarations _after-selectors RBRACE space-opt",
    )
    def p_page(self, t):
        # TODO - build AST
        pass


    # psuedo-page-opt
    # : pseudo-page
    # | empty
    @PRODUCTION(
        "pseudo-page-opt : pseudo-page",
        "                | empty",
    )
    def p_pseudo_page_opt(self, t):
        # TODO - build AST
        pass
    

    # pseudo-page
    # : COLON IDENTIFIER space-opt
    @PRODUCTION(
        "pseudo-page : COLON IDENTIFIER space-opt",
    )
    def p_pseudo_paget(self, t):
        # TODO - build AST
        pass
