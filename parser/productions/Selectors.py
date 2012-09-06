from ..utils import PRODUCTION
from WhitespaceComment import WhitespaceComment


class Selectors(WhitespaceComment):
    
    ###########################################################################
    # selectors
    ###########################################################################
    
    
    # TEMP!
    
    
    
    
    # selectors
    # : selector COMMA space-opt selectors
    # | selector
    @PRODUCTION(
        "selectors : selector COMMA space-opt selectors",
    )
    def p_selectors_list(self, t):
        # TODO - build AST
        pass

    @PRODUCTION(
        "selectors : selector",
    )
    def p_selectors_terminal(self, t):
        # TODO - build AST
        pass
    
    
    # selector
    # : simple-selector combinator selector
    # | simple-selector space-opt
    @PRODUCTION(
        "selector : simple-selector combinator selector",
    )
    def p_selector_list(self, t):
        # TODO - build AST
        pass

    @PRODUCTION(
        "selector : simple-selector space-opt",
    )
    def p_selector_terminal(self, t):
        # TODO - build AST
        pass

    
    # simple-selector
    # : element-selector selector-filters-opt
    # | selector-filters
    @PRODUCTION(
        "simple-selector : element-selector selector-filters-opt",
    )
    def p_simple_selector_type(self, t):
        # TODO - build AST
        pass

    @PRODUCTION(
        "simple-selector : selector-filters",
    )
    def p_simple_selector_filters(self, t):
        # TODO - build AST
        pass


    # element-selector
    # : IDENTIFER
    # | OP_MUL
    # | PREFIXED_IDENTIFIER
    # | PREFIXED_ALL
    @PRODUCTION(
        "element-selector : IDENTIFIER",
        "element-selector : OP_MUL",
        "                 | PREFIXED_IDENTIFIER",
        "                 | PREFIXED_ALL",
    )
    def p_element_selector(self, t):
        # TODO - build AST
        pass
    
    
    # selector-filters-opt
    # : selector-filters
    # | empty
    @PRODUCTION(
        "selector-filters-opt : selector-filters",
        "                     | empty",
    )
    def p_selector_filters_opt(self, t):
        # TODO - build AST
        pass
    
    
    # selector-filters
    # : selector-filter selector-filters
    # | selector-filter
    @PRODUCTION(
        "selector-filters : selector-filter selector-filters",
    )
    def p_selector_filters_list(self, t):
        # TODO - build AST
        pass

    @PRODUCTION(
        "selector-filters : selector-filter",
    )
    def p_selector_filters_terminal(self, t):
        # TODO - build AST
        pass


    # selector-filter
    # : HASH
    # | class
    # | attribute
    # | pseudo
    # | negation
    @PRODUCTION(
        "selector-filter : hash",
        "                | class",
        "                | attribute",
        "                | pseudo",
        "                | negation",
    )
    def p_selector_filter(self, t):
        # TODO - build AST
        pass
    
    
    # combinator
    # : space-opt combinator-op space-opt
    # : space-opt OP_PLUS space-opt
    # | space-opt OP_GT space-opt
    # | space-opt OP_TILDE space-opt
    # | space
    @PRODUCTION(
        "combinator : space-opt combinator-op",
    )
    def p_combinator_combinator_op(self, t):
        # TODO - build AST
        pass

    @PRODUCTION(
        "combinator : space",
    )
    def p_combinator_space(self, t):
        # TODO - build AST
        pass

    
    # combinator-op
    # : OP_PLUS space-opt
    # | OP_GT space-opt
    # | OP_TILDE space-opt
    @PRODUCTION(
        "combinator-op : OP_PLUS space-opt",
        "              | OP_GT space-opt",
        "              | OP_TILDE space-opt",
    )
    def p_combinator_op(self, t):
        # TODO - build AST
        pass
    
    
    # hash
    # : HASH
    @PRODUCTION(
        "hash : HASH",
    )
    def p_hash(self, t):
        # TODO - build AST
        pass
    
    
    # class
    # : DOT IDENTIFIER
    @PRODUCTION(
        "class : DOT IDENTIFIER",
    )
    def p_class(self, t):
        # TODO - build AST
        pass
    
    
    # attribute
    # : LBRACKET space-opt attribute-name attribute-match-opt RBRACKET
    @PRODUCTION(
        "attribute : LBRACKET space-opt attribute-name attribute-match-opt RBRACKET",
    )
    def p_attribute(self, t):
        # TODO - build AST
        pass
    
    
    # attribute-name
    # : IDENTIFIER space-opt
    # | PREFIXED_IDENTIFIER space-opt
    @PRODUCTION(
        "attribute-name : ELEMENT space-opt",
        "               | IDENTIFIER space-opt",
        "               | PREFIXED_IDENTIFIER space-opt",
    )
    def p_attribute_name(self, t):
        # TODO - build AST
        pass
    
    
    # attribute-match-opt
    # : attribute-match
    # | empty
    @PRODUCTION(
        "attribute-match-opt : attribute-match",
        "                    | empty",
    )
    def p_attribute_match_opt(self, t):
        # TODO - build AST
        pass

    
    # attribute-match
    # : attribute-op attribute-value
    @PRODUCTION(
        "attribute-match : attribute-op attribute-value",
    )
    def p_attribute_match(self, t):
        # TODO - build AST
        pass

    
    # attribute-op
    # : OP_PREFIXMATCH space-opt
    # | OP_SUFFIXMATCH space-opt
    # | OP_SUBSTRINGMATCH space-opt
    # | OP_INCLUDES space-opt
    # | OP_DASHMATCH space-opt
    # | OP_EQUALS space-opt
    @PRODUCTION(
        "attribute-op : OP_PREFIXMATCH space-opt",
        "             | OP_SUFFIXMATCH space-opt",
        "             | OP_SUBSTRINGMATCH space-opt",
        "             | OP_INCLUDES space-opt",
        "             | OP_DASHMATCH space-opt",
        "             | OP_EQUALS space-opt",
    )
    def p_attribute_op(self, t):
        # TODO - build AST
        pass
    
    
    # attribute-value
    # : IDENTIFIER space-opt
    # | STRING space-opt
    @PRODUCTION(
        "attribute-value : IDENTIFIER space-opt",
        "                | STRING space-opt",
    )
    def p_attribute_value(self, t):
        # TODO - build AST
        pass
    
    
    # pseudo
    # : COLON pseudo-selector
    # | COLON COLON pseudo-selector
    @PRODUCTION(
        "pseudo : COLON pseudo-selector",
    )
    def p_pseudo_colon(self, t):
        # TODO - build AST
        pass
    
    @PRODUCTION(
        "pseudo : COLON COLON pseudo-selector",
    )
    def p_pseudo_colon_colon(self, t):
        # TODO - build AST
        pass
    

    # pseudo-selector
    # : IDENTIFIER
    # | pseudo-function
    @PRODUCTION(
        "pseudo-selector : IDENTIFIER",
    )
    def p_pseudo_selector_identifier(self, t):
        # TODO - build AST
        pass
    
    @PRODUCTION(
        "pseudo-selector : pseudo-function",
    )
    def p_pseudo_selector_pseudo_function(self, t):
        # TODO - build AST
        pass
    

    # pseudo-function
    # : FUNCTION space-opt pseudo-expression RPAREN
    @PRODUCTION(
        "pseudo-function : FUNCTION space-opt pseudo-expression RPAREN",
    )
    def p_pseudo_function(self, t):
        # TODO - build AST
        pass
    
    
    # pseudo-expression
    # : pseudo-term pseudo-expression
    # | pseudo-term
    @PRODUCTION(
        "pseudo-expression : pseudo-term pseudo-expression",
    )
    def p_pseudo_expression_list(self, t):
        # TODO - build AST
        pass

    @PRODUCTION(
        "pseudo-expression : pseudo-term",
    )
    def p_pseudo_expression_terminal(self, t):
        # TODO - build AST
        pass
    

    # pseudo-term
    # : OP_PLUS space-opt
    # | OP_MINUS space-opt
    # | DIMENSION space-opt
    # | NUMBER space-opt
    # | STRING space-opt
    # | IDENTIFIER space-opt
    @PRODUCTION(
        "pseudo-term : OP_PLUS space-opt",
        "            | OP_MINUS space-opt",
        "            | DIMENSION space-opt",
        "            | NUMBER space-opt",
        "            | STRING space-opt",
        "            | IDENTIFIER space-opt",
    )
    def p_pseudo_term(self, t):
        # TODO - build AST
        pass
    

    # negation
    # : NOT_SELECTOR space-opt negation-arg RPAREN
    @PRODUCTION(
        "negation : NOT_SELECTOR space-opt negation-argument RPAREN",
    )
    def p_negation(self, t):
        # TODO - build AST
        pass


    # negation-argument
    # : element-selector space-opt
    # | hash space-opt
    # | class space-opt
    # | attribute space-opt
    # | pseudo space-opt
    @PRODUCTION(
        "negation-argument : element-selector space-opt",
        "                  | hash space-opt",
        "                  | class space-opt",
        "                  | attribute space-opt",
        "                  | pseudo space-opt",
    )
    def p_negation_argument(self, t):
        # TODO - build AST
        pass
    