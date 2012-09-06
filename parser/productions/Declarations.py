from ..utils import PRODUCTION
from Value import Value
from ActionFlag import ActionFlag


class Declarations(Value, ActionFlag):
    
    ###########################################################################
    # declarations
    ###########################################################################
    
    # declarations
    # : native-declarations
    # | ???
    @PRODUCTION(
        "declarations : native-declarations",
    )
    def p_declarations_native(self, t):
        # TODO - build AST
        pass
    
    
    # seems to work...
    @PRODUCTION(
        "declarations : property COLON space-opt LBRACE space-opt declarations RBRACE space-opt declarations",
    )
    def p_declarations_family(self, t):
        # TODO - build AST
        pass
    
    
    # TEMP!
    # works so long as selectors don't try to match an IDENTIFIER token
    @PRODUCTION(
        "declarations : selector-filters combinator simple-selector space-opt LBRACE space-opt declarations RBRACE space-opt declarations",
    )
    def p_declarations_nested(self, t):
        # TODO - build AST
        pass
    
    
    # native-declarations
    # : declaration-opt SEMICOLON space-opt declarations
    # | declaration-opt
    
    @PRODUCTION(
        "native-declarations : declaration-opt SEMICOLON space-opt declarations",
    )
    def p_native_declarations_list(self, t):
        # TODO - build AST
        pass
    
    @PRODUCTION(
        "native-declarations : declaration-opt",
    )
    def p_native_delcarations_terminal(self, t):
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
    
    # @PRODUCTION(
    #         "declarations : declaration-opt error",
    #     )
    #     def p_declarations_error(self, t):
    #         pass
    