from ..utils import PRODUCTION
from WhitespaceComment import WhitespaceComment


class Charset(WhitespaceComment):
    
    ###########################################################################
    # charset
    ###########################################################################
    
    # charset-opt
    # : charset
    # | empty
    @PRODUCTION(
        "charset-opt : space-opt charset",
        "            | space-opt",
    )
    def p_charset_opt(self, t):
        # TODO - build AST
        pass
    
    
    # charset:
    # : SYM_CHARSET STRING space-opt SEMICOLON space-opt
    @PRODUCTION(
        "charset : SYM_CHARSET STRING space-opt SEMICOLON space-opt",
    )
    def p_charset(self, t):
        # TODO - build AST
        pass
