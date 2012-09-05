from ..utils import PRODUCTION
from WhitespaceComment import WhitespaceComment


class Value(WhitespaceComment):
    
    ###########################################################################
    # value
    ###########################################################################
    
    # value
    # : value-term value-op-opt value
    # | value-term
    @PRODUCTION(
        "value : value-term value-op-opt value",
    )
    def p_value_list(self, t):
        # TODO - build AST
        pass


    @PRODUCTION(
        "value : value-term",
    )
    def p_value_terminal(self, t):
        # TODO - build AST
        pass
    
    
    # value-op-opt
    # : value-op
    # | empty
    @PRODUCTION(
        "value-op-opt : value-op",
        "             | empty",
    )
    def p_value_op_opt(self, t):
        # TODO - build AST
        pass
    

    # value-op
    # : OP_DIV space-opt
    # | COMMA space-opt
    @PRODUCTION(
        "value-op : OP_DIV space-opt",
        "         | COMMA space-opt",
    )
    def p_value_op(self, t):
        # TODO - build AST
        pass
    
    
    # value-term
    # : value-unary-op-opt value-numeric
    # | value-nonnumeric
    @PRODUCTION(
        "value-term : value-unary-op-opt value-numeric",
    )
    def p_value_term_numeric(self, t):
        # TODO - build AST
        pass


    @PRODUCTION(
        "value-term : value-nonnumeric",
    )
    def p_value_term_nonnumeric(self, t):
        # TODO - build AST
        pass
    
    
    # value-unary-op-opt
    # : value-unary-op
    # | empty
    @PRODUCTION(
        "value-unary-op-opt : value-unary-op",
        "                   | empty",
    )
    def p_value_unary_op_opt(self, t):
        # TODO - build AST
        pass
    
    
    # value-unary-op
    # : OP_MINUS space-opt
    # | OP_PLUS space-opt
    @PRODUCTION(
        "value-unary-op : OP_MINUS space-opt",
        "               | OP_PLUS space-opt",
    )
    def p_value_unary_op(self, t):
        # TODO - build AST
        pass
    
    
    # value-numeric
    # : value-number
    # | value-percentage
    # | value-dimension

    @PRODUCTION(
        "value-numeric : value-number",
        "              | value-percentage",
        "              | value-dimension",
    )
    def p_value_numeric(self, t):
        # TODO - build AST
        pass
    
    
    # value-nonnumeric
    # : value-string
    # | value-uri
    # | value-identifier
    # | value-hexcolor
    # | value-function
    @PRODUCTION(
        "value-nonnumeric : value-string",
        "                 | value-uri",
        "                 | value-identifier",
        "                 | value-hexcolor",
        "                 | value-function",
    )
    def p_value_nonnumeric(self, t):
        # TODO - build AST
        pass

    
    # value-number
    # : NUMBER space-opt
    @PRODUCTION(
        "value-number : NUMBER space-opt",
    )
    def p_value_number(self, t):
        # TODO - build AST
        pass
    
    
    # value-percentage
    # : PERCENTAGE space-opt
    @PRODUCTION(
        "value-percentage : PERCENTAGE space-opt",
    )
    def p_value_percentage(self, t):
        # TODO - build AST
        pass
    
    
    # value-dimension
    # : DIMENSION space-opt
    @PRODUCTION(
        "value-dimension : DIMENSION space-opt",
    )
    def p_value_dimension(self, t):
        # TODO - build AST
        pass
        

    # value-string
    # : STRING space-opt
    @PRODUCTION(
        "value-string : STRING space-opt",
    )
    def p_value_string(self, t):
        # TODO - build AST
        pass
    
    
    # value-uri
    # : URI space-opt
    @PRODUCTION(
        "value-uri : URI space-opt",
    )
    def p_value_uri(self, t):
        # TODO - build AST
        pass
    
    
    # value-identifier
    # : IDENTIFIER space-opt
    @PRODUCTION(
        "value-identifier : IDENTIFIER space-opt",
    )
    def p_value_identfier(self, t):
        # TODO - build AST
        pass
    

    # value-hexcolor
    # : HASH space-opt
    @PRODUCTION(
        "value-hexcolor : HASH space-opt",
    )
    def p_value_hexcolor(self, t):
        # TODO - build AST
        pass


    # value-function
    # : FUNCTION space-opt value RPAREN space-opt
    @PRODUCTION(
        "value-function : FUNCTION space-opt value RPAREN space-opt",
    )
    def p_value_function(self, t):
        # TODO - build AST
        pass
