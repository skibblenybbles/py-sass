from ..utils import PRODUCTION


class Empty(object):
    
    ###########################################################################
    # empty production
    ###########################################################################
    
    # empty
    # : <empty>
    @PRODUCTION(
        "empty :",
    )
    def p_empty(self, t):
        pass
