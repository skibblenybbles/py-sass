from ..utils import PRODUCTION
from Value import Value
from ActionFlag import ActionFlag


class Declarations(Value, ActionFlag):
    
    Lexer = None
    debug = None
    nested_selectors_parser = None
    
    ###########################################################################
    # constructor
    ###########################################################################
    
    def __init__(self, *args, **kwargs):
        super(Declarations, self).__init__(*args, **kwargs)
        
        # initialize the nested selector parser
        if self.Lexer is not None and self.debug is not None:
            from ..NestedSelectorsParser import NestedSelectorsParser
            self.nested_selectors_parser = NestedSelectorsParser(
                self.Lexer, 
                debug = self.debug,
            )
        else:
            raise RuntimeError(
                u"Constructor chain did not initialize the nested selectors " \
                u"parser correctly.",
            )
        
    
    
    ###########################################################################
    # declarations
    ###########################################################################
    
    # declarations
    # : declaration-opt SEMICOLON space-opt declarations
    # | SELECTORS space-opt declarations RBRACE space-opt declarations
    # | declaration-opt
    @PRODUCTION(
        "declarations : declaration-opt SEMICOLON space-opt declarations",
    )
    def p_declarations_list(self, t):
        # TODO - build AST
        pass
    
    
    @PRODUCTION(
        "declarations : SELECTORS space-opt declarations RBRACE space-opt declarations",
    )
    def p_declarations_ruleset(self, t):
        
        # parse the nested selector
        t[1] = self.nested_selectors_parser.parse(
            t[1].value,
            line = t[1].line,
            column = t[1].column,
        )
    
        # TODO - build AST
        pass
    
    
    @PRODUCTION(
        "declarations : declaration-opt",
    )
    def p_declarations_terminal(self, t):
        # TODO - build AST
        pass
    
    
    # declaration-opt
    # : declaration
    # | empty
    @PRODUCTION(
        "declaration-opt : declaration",
        "                | empty",
    )
    def p_declaration_opt(self, t):
        # TODO - build AST
        pass
    
    
    # declaration
    # : property COLON space-opt value flag-opt
    @PRODUCTION(
        "declaration : property COLON space-opt value flag-opt",
    )
    def p_declaration(self, t):
        # TODO - build AST
        pass
    
    
    # property
    # : IDENTIFIER space-opt
    @PRODUCTION(
        "property : IDENTIFIER space-opt",
    )
    def p_property(self, t):
        # TODO - build AST
        pass
    
    
    # flag-opt
    # : flag
    # | empty
    @PRODUCTION(
        "flag-opt : flag",
        "         | empty",
    )
    def p_flag_opt(self, t):
        # TODO - build AST
        pass


    # flag
    # : _before-flag BANG space-opt flag-type _after-flag
    @PRODUCTION(
        "flag : _before-flag BANG space-opt flag-type _after-flag",
    )
    def p_flag(self, t):
        # TODO - build AST
        pass
    
    
    # flag-type
    # : KEY_IMPORTANT
    @PRODUCTION(
        "flag-type : KEY_IMPORTANT space-opt",
    )
    def p_flag_type(self, t):
        # TODO - build AST
        pass
    
    
    ###########################################################################
    # error productions
    ###########################################################################

    # recover from a bad CSS property declaration right before the semicolon
    # or closing inside of a declarations block
    
    @PRODUCTION(
        "declarations : declaration-opt error",
    )
    def p_declarations_error(self, t):
        pass
