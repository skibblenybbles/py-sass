from ..utils import PRODUCTION


class ActionMediaquery(object):
    
    ###########################################################################
    # mediaquery actions
    ###########################################################################
    
    @PRODUCTION(
        "_before-mediaquery :",
    )
    def p_before_mediaquery(self, t):
        t.lexer.push_state("mediaquery")
    
    @PRODUCTION(
        "_after-mediaquery :",
    )
    def p_after_mediaquery(self, t):
        t.lexer.pop_state()