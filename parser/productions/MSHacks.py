from ..utils import PRODUCTION
from Value import Value


# TODO
# add support for awful MS expression() function for attributes


class MSHacks(Value):
    
    ###########################################################################
    # ): Microsoft CSS Extension Hacks :(
    #
    # boo - these are here for compatibility with the SASS parser
    ###########################################################################
    
    # property
    # : IDENTIFIER space-opt (already defined)
    # | ms-property-hack IDENTIFIER space-opt
    @PRODUCTION(
        "property : ms-property-hack IDENTIFIER space-opt",
    )
    def p_property_ms(self, t):
        # TODO - build AST
        pass
    
    
    # ms-property-hack
    # : OP_MUL
    @PRODUCTION(
        "ms-property-hack : OP_MUL",
    )
    def p_ms_property_hack(self, t):
        # TODO - build AST
        pass
    
    # value-term
    # : value-unary-op-opt value-numeric (already defined)
    # | value-nonnumeric (already defined)
    # | ms-value-hack
    @PRODUCTION(
        "value-term : ms-value-hack",
    )
    def p_value_term_hack(self, t):
        # TODO - build AST
        pass
    
    
    # ms-value-hack
    # : ms-scoped-function ms-function-arguments-opt RPAREN space-opt
    @PRODUCTION(
        "ms-value-hack : ms-scoped-function ms-arguments-opt RPAREN space-opt",
    )
    def p_ms_value_hack(self, t):
        # TODO - build AST
        pass
    
    
    # ms-scoped-function
    # : IDENTIFIER COLON ms-scoped-function
    # | IDENTIFIER DOT ms-scoped-function
    # | IDENTIFIER DOT FUNCTION space-opt
    @PRODUCTION(
        "ms-scoped-function : IDENTIFIER COLON ms-scoped-function",
        "                   | IDENTIFIER DOT ms-scoped-function",
    )
    def p_ms_scoped_function_list(self, t):
        # TODO - build AST
        pass
    
    @PRODUCTION(
        "ms-scoped-function : IDENTIFIER DOT FUNCTION space-opt",
    )
    def p_ms_scoped_function_terminal(self, t):
        # TODO - build AST
        pass
    
    
    # ms-arguments-opt
    # : ms-arguments
    # | empty
    @PRODUCTION(
        "ms-arguments-opt : ms-arguments",
        "                 | empty",
    )
    def p_ms_arguments_opt(self, t):
        # TODO - build AST
        pass
    
    
    # ms-arguments
    # : ms-argument COMMA space-opt ms-arguments
    # | ms-argument
    @PRODUCTION(
        "ms-arguments : ms-argument COMMA space-opt ms-arguments",
    )
    def p_ms_arguments_list(self, t):
        # TODO - build AST
        pass

    @PRODUCTION(
        "ms-arguments : ms-argument",
    )
    def p_ms_arguments_terminal(self, t):
        # TODO - build AST
        pass

    
    # ms-argument
    # : IDENTIFIER space-opt OP_EQUALS space-opt ms-value-term
    @PRODUCTION(
        "ms-argument : IDENTIFIER space-opt OP_EQUALS space-opt ms-value-term",
    )
    def p_ms_argument(self, t):
        # TODO - build AST
        pass

    
    # ms-value-term
    # : value-unary-op-opt ms-value-numeric
    # | ms-value-nonnumeric
    @PRODUCTION(
        "ms-value-term : value-unary-op-opt ms-value-numeric",
    )
    def p_ms_value_term_numeric(self, t):
        # TODO - build AST
        pass
    
    @PRODUCTION(
        "ms-value-term : ms-value-nonnumeric",
    )
    def p_ms_value_term_nonnumeric(self, t):
        # TODO - build AST
        pass
    
    
    # ms-value-numeric
    # : value-number
    @PRODUCTION(
        "ms-value-numeric : value-number",
    )
    def p_ms_value_numeric(self, t):
        # TODO - build AST
        pass
    
    
    # ms-value-nonnumeric
    # : value-string
    @PRODUCTION(
        "ms-value-nonnumeric : value-string",
    )
    def p_ms_value_nonnumeric(self, t):
        # TODO - build AST
        pass
