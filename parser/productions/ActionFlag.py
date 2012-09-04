from ..utils import PRODUCTION


class ActionFlag(object):
    
    ###########################################################################
    # flag actions
    ###########################################################################
    
    @PRODUCTION(
        "_before-flag :",
    )
    def p_before_flag(self, t):
        t.lexer.push_state("flag")

    @PRODUCTION(
        "_after-flag :",
    )
    def p_after_flag(self, t):
        t.lexer.pop_state()
