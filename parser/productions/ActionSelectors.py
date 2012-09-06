from ..utils import PRODUCTION


class ActionSelectors(object):
    
    ###########################################################################
    # selectors actions
    ###########################################################################
    
    @PRODUCTION(
        "_before-selectors :",
    )
    def p_before_selectors(self, t):
        #t.lexer.push_state("selectors")
        pass
    
    
    @PRODUCTION(
        "_after-selectors :",
    )
    def p_after_selectors(self, t):
        #t.lexer.pop_state()
        pass
