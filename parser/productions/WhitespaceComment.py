from ..utils import PRODUCTION
from Empty import Empty


class WhitespaceComment(Empty):
    
    ###########################################################################
    # whitespace and comment productions
    ###########################################################################
    
    # space-opt
    # : space
    # | empty
    @PRODUCTION(
        "space-opt : space",
        "          | empty",
    )
    def p_space_opt(self, t):
        # TODO - build AST
        pass
    
    
    # space
    # : space-delimiter space
    # | space-delimiter
    @PRODUCTION(
        "space : space-delimiter space",
    )
    def p_space_list(self, t):
        # TODO - build AST
        pass
    
    @PRODUCTION(
        "space : space-delimiter",
    )
    def p_space_terminal(self, t):
        # TODO - build AST
        pass
    
    
    # space-delimiter
    # : whitespace
    # | blockcomment
    # | htmlcomment
    @PRODUCTION(
        "space-delimiter : whitespace",
        "                | blockcomment",
        "                | htmlcomment",
    )
    def p_space_delimiter(self, t):
        # TODO - build AST
        pass

    
    # whitespace
    # : SPACE
    @PRODUCTION(
        "whitespace : SPACE",
    )
    def p_whitespace(self, t):
        # TODO - build AST
        pass
        
    
    # blockcomment
    # : BLOCKCOMMENT
    @PRODUCTION(
        "blockcomment : BLOCKCOMMENT",
    )
    def p_blockcomment(self, t):
        # TODO - build AST
        pass
    
    
    # htmlcomment
    # : CDO
    # | CDC
    @PRODUCTION(
        "htmlcomment : CDO",
        "            | CDC",
    )
    def p_htmlcomment(self, t):
        # TODO - build AST
        pass
