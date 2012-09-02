import os, logging
from ply import yacc
from utils import PRODUCTION

# TODO
# add support for awful MS expression() function for attributes


class Parser(object):
    
    ###########################################################################
    # internal state
    ###########################################################################
    
    # the Lexer to use for tokenizing the input
    lexer = None
    
    # the tokens from the Lexer
    tokens = None
    
    # the PLY yacc instance
    parser = None
    
    
    ###########################################################################
    # constructor
    ###########################################################################
    
    def __init__(self, lexer, *args, **kwargs):
        super(Parser, self).__init__(*args, **kwargs)
        
        # store the lexer and its tokens
        self.lexer = lexer
        self.tokens = lexer.tokens
        
        
        # set up a logging object
        output_dir = os.path.join(os.path.dirname(__file__), "output")
        logging.basicConfig(
            level = logging.DEBUG,
            filename = os.path.join(output_dir, "parser.out"),
            filemode = "w",
            format = u"%(message)s",
        )
        
        # create the yacc instance
        self.parser = yacc.yacc(
            module = self,
            outputdir = output_dir,
            debuglog = logging.getLogger(),
            debug = True,
        )
    
    
    ###########################################################################
    # public api
    ###########################################################################
    
    def parse(self, input):
        return self.parser.parse(input, lexer = self.lexer.lexer)

    
    ###########################################################################
    # starting symbol
    ###########################################################################

    start = "stylesheet"
    
    
    ###########################################################################
    # empty, whitespace and comment productions
    ###########################################################################
    
    # empty
    # : <empty>
    @PRODUCTION(
        "empty :",
    )
    def p_empty(self, t):
        pass
    
    
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

    
    ###########################################################################
    # sylesheet structure
    ###########################################################################
    
    # stylesheet
    # : charset-opt imports-opt styles-opt
    @PRODUCTION(
        "stylesheet : charset-opt imports-opt styles-opt",
    )
    def p_stylesheet(self, t):
        # TODO - build AST
        pass


    # charset-opt
    # : charset
    # | empty
    @PRODUCTION(
        "charset-opt : charset",
        "            | empty",
    )
    def p_charset_opt(self, t):
        # TODO - build AST
        pass
    
    
    # imports-opt
    # : imports
    # | empty
    @PRODUCTION(
        "imports-opt : imports",
        "            | empty",
    )
    def p_imports_opt(self, t):
        # TODO - build AST
        pass
        
    
    # styles-opt
    # : styles
    # | empty
    @PRODUCTION(
        "styles-opt : styles",
        "           | empty",
    )
    def p_styles_opt_styles(self, t):
        # TODO - build AST
        pass
    
    
    ###########################################################################
    # charset
    ###########################################################################
    
    # charset:
    # : SYM_CHARSET STRING space-opt SEMICOLON space-opt
    @PRODUCTION(
        "charset : SYM_CHARSET STRING space-opt SEMICOLON space-opt",
    )
    def p_charset(self, t):
        # TODO - build AST
        pass

    
    ###########################################################################
    # imports
    ###########################################################################
    
    
    # imports
    # : import imports
    # | import
    @PRODUCTION(
        "imports : import imports",
    )
    def p_imports_list(self, t):
        # TODO - build AST
        pass
    
    @PRODUCTION(
        "imports : import",
    )
    def p_imports_terminal(self, t):
        # TODO - build AST
        pass
    
    
    # import
    # : SYM_IMPORT space-opt _before-mediaquery import-src media-queries-opt _after-mediaquery SEMICOLON space-opt
    @PRODUCTION(
        "import : SYM_IMPORT space-opt _before-mediaquery import-src media-queries-opt _after-mediaquery SEMICOLON space-opt",
    )
    def p_import(self, t):
        # TODO - build AST
        pass
    
    
    # import-src
    # : value-string
    # | value-uri
    @PRODUCTION(
        "import-src : value-string",
        "           | value-uri",
    )
    def p_import_src(self, t):
        # TODO - build AST
        pass
    
    
    ###########################################################################
    # styles
    ###########################################################################
    
    # styles
    # : style styles
    # : style
    @PRODUCTION(
        "styles : style styles",
    )
    def p_styles_list(self, t):
        # TODO - build AST
        pass

    @PRODUCTION(
        "styles : style",
    )
    def p_styles_terminal(self, t):
        # TODO - build AST
        pass


    # style
    # : page
    # | media
    # | ruleset
    @PRODUCTION(
        "style : page",
        "      | media",
        "      | ruleset",
    )
    def p_style_page(self, t):
        # TODO - build AST
        pass
    
    
    ###########################################################################
    # page
    ###########################################################################
    
    # page
    # : SYM_PAGE space-opt pseudo-page LBRACE space-opt declarations RBRACE space-opt
    @PRODUCTION(
        "page : SYM_PAGE space-opt pseudo-page-opt LBRACE space-opt declarations RBRACE space-opt",
    )
    def p_page(self, t):
        # TODO - build AST
        pass


    # psuedo-page-opt
    # : pseudo-page
    # | empty
    @PRODUCTION(
        "pseudo-page-opt : pseudo-page",
        "                | empty",
    )
    def p_pseudo_page_opt(self, t):
        # TODO - build AST
        pass
    

    # pseudo-page
    # : COLON IDENTIFIER space-opt
    @PRODUCTION(
        "pseudo-page : COLON IDENTIFIER space-opt",
    )
    def p_pseudo_paget(self, t):
        # TODO - build AST
        pass
    
    
    ###########################################################################
    # media and media queries
    ###########################################################################
    
    # media
    # : _before-mediaquery SYM_MEDIA space-opt media-queries _after-mediaquery LBRACE space-opt styles-opt RBRACE space-opt
    @PRODUCTION(
        "media : _before-mediaquery SYM_MEDIA space-opt media-queries _after-mediaquery LBRACE space-opt styles-opt RBRACE space-opt",
    )
    def p_media(self, t):
        # TODO - build AST
        pass
    
    
    # media-queries-opt
    # : media-queries
    # | empty
    @PRODUCTION(
        "media-queries-opt : media-queries",
        "                  | empty",
    )
    def p_media_queries_opt(self, t):
        # TODO - build AST
        pass
        
    
    # media-queries
    # : media-query COMMA space-opt media-queries
    # | media-query
    @PRODUCTION(
        "media-queries : media-query COMMA space-opt media-queries",
    )
    def p_media_queries_list(self, t):
        # TODO - build AST
        pass
    
    @PRODUCTION(
        "media-queries : media-query",
    )
    def p_media_queries_terminal(self, t):
        # TODO - build AST
        pass
    
    
    # media-query
    # : media-limited-opt media-typed
    # | media-expressions
    @PRODUCTION(
        "media-query : media-limited-opt media-typed",
    )
    def p_media_query_typed(self, t):
        # TODO - build AST
        pass
    
    @PRODUCTION(
        "media-query : media-expressions",
    )
    def p_media_query_expressions(self, t):
        # TODO - build AST
        pass


    # media-limited-opt
    # : media-limited
    # | empty
    @PRODUCTION(
        "media-limited-opt : media-limited",
        "                  | empty",
    )
    def p_media_limited_opt(self, t):
        # TODO - build AST
        pass
    

    # media-limited
    # : KEY_ONLY space-opt
    # | KEY_NOT space-opt
    @PRODUCTION(
        "media-limited : KEY_ONLY space-opt",
        "              | KEY_NOT space-opt",
    )
    def p_media_limited(self, t):
        # TODO - build AST
        pass
    
    
    # media-typed
    # : media-type KEY_AND space-opt media-expressions
    # | media-type
    @PRODUCTION(
        "media-typed : media-type KEY_AND space-opt media-expressions",
    )
    def p_media_typed_type_expessions(self, t):
        # TODO - build AST
        pass
    
    @PRODUCTION(
        "media-typed : media-type",
    )
    def p_media_typed_type(self, t):
        # TODO - build AST
        pass
    
    
    # media-type
    # : IDENTIFIER space-opt
    @PRODUCTION(
        "media-type : IDENTIFIER space-opt",
    )
    def p_media_type(self, t):
        # TODO - build AST
        pass
    

    # media-expressions
    # : media-expression KEY_AND space-opt
    # | media-expression
    @PRODUCTION(
        "media-expressions : media-expression KEY_AND space-opt media-expressions",
    )
    def p_media_expressions_list(self, t):
        # TODO - build AST
        pass

    @PRODUCTION(
        "media-expressions : media-expression",
    )
    def p_media_expressions_terminal(self, t):
        # TODO - build AST
        pass
        
    
    # media-expression
    # | LPAREN space-opt media-featured media-value-opt RPAREN space-opt
    @PRODUCTION(
        "media-expression : LPAREN space-opt media-feature media-value-opt RPAREN space-opt",
    )
    def p_media_expression(self, t):
        # TODO - build AST
        pass
    

    # media-feature
    # : IDENTIFIER space-opt
    @PRODUCTION(
        "media-feature : IDENTIFIER space-opt",
    )
    def p_media_feature(self, t):
        # TODO - build AST
        pass

    
    # media-value-opt
    # : media-value
    # | empty
    @PRODUCTION(
        "media-value-opt : media-value",
        "                | empty",
    )
    def p_media_value_opt(self, t):
        # TODO - build AST
        pass
    
    
    # media-value
    # : COLON space-opt value
    @PRODUCTION(
        "media-value : COLON space-opt value",
    )
    def p_media_value(self, t):
        # TODO - build AST
        pass
    
    
    ###########################################################################
    # rulesets and selectors
    ###########################################################################
    
    # ruleset
    # : selectors LBRACE space-opt declarations RBRACE space-opt
    @PRODUCTION(
        "ruleset : selectors LBRACE space-opt declarations RBRACE space-opt",
    )
    def p_ruleset(self, t):
        # TODO - build AST
        pass
    
    
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
    # : type-selector selector-rules-opt
    # | selector-rules
    @PRODUCTION(
        "simple-selector : type-selector selector-rules-opt",
    )
    def p_simple_selector_type(self, t):
        # TODO - build AST
        pass

    @PRODUCTION(
        "simple-selector : selector-rules",
    )
    def p_simple_selector_rules(self, t):
        # TODO - build AST
        pass


    # type-selector
    # : element-selector
    # | all-selector
    @PRODUCTION(
        "type-selector : element-selector",
        "              | all-selector",
    )
    def p_type_selector(self, t):
        # TODO - build AST
        pass
    

    # element-selector
    # : namespace-prefix-opt element-name
    @PRODUCTION(
        "element-selector : namespace-prefix-opt element-name",
    )
    def p_element_selector(self, t):
        # TODO - build AST
        pass


    # all-selector
    # : namespace-prefix-opt OP_MUL
    @PRODUCTION(
        "all-selector : namespace-prefix-opt OP_MUL",
    )
    def p_all_selector(self, t):
        # TODO - build AST
        pass

    
    # namespace-prefix-opt 
    # : namespace-prefix
    # : empty
    @PRODUCTION(
        "namespace-prefix-opt : namespace-prefix",
        "                     | empty",
    )
    def p_namespace_prefix_opt(self, t):
        # TODO - build AST
        pass

    
    # namespace-prefix
    # : NAMESPACE_PREFIX
    @PRODUCTION(
        "namespace-prefix : NAMESPACE_PREFIX",
    )
    def p_namespace_prefix(self, t):
        # TODO - build AST
        pass


    # element-name
    # : IDENTIFIER
    @PRODUCTION(
        "element-name : IDENTIFIER",
    )
    def p_identifier(self, t):
        # TODO - build AST
        pass


    # selector-rules-opt
    # : selector-rules
    # | empty
    @PRODUCTION(
        "selector-rules-opt : selector-rules",
        "                   | empty",
    )
    def p_selector_rules_opt(self, t):
        # TODO - build AST
        pass
    
    
    # selector-rules
    # : selector-rule selector-rules
    # | selector-rule
    @PRODUCTION(
        "selector-rules : selector-rule selector-rules",
    )
    def p_selector_rules_list(self, t):
        # TODO - build AST
        pass

    @PRODUCTION(
        "selector-rules : selector-rule",
    )
    def p_selector_rules_terminal(self, t):
        # TODO - build AST
        pass


    # selector-rule
    # : HASH
    # | class
    # | attribute
    # | pseudo
    # | negation
    @PRODUCTION(
        "selector-rule : hash",
        "              | class",
        "              | attribute",
        "              | pseudo",
        "              | negation",
    )
    def p_selector_rule(self, t):
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
    # : LBRACKET space-opt namespace-prefix-opt IDENTIFIER space-opt attribute-match-opt RBRACKET
    @PRODUCTION(
        "attribute : LBRACKET space-opt namespace-prefix-opt IDENTIFIER space-opt attribute-match-opt RBRACKET",
    )
    def p_attribute(self, t):
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
    # : type-selector space-opt
    # | hash space-opt
    # | class space-opt
    # | attribute space-opt
    # | pseudo space-opt
    @PRODUCTION(
        "negation-argument : type-selector space-opt",
        "                  | hash space-opt",
        "                  | class space-opt",
        "                  | attribute space-opt",
        "                  | pseudo space-opt",
    )
    def p_negation_argument(self, t):
        # TODO - build AST
        pass
    
    
    ###########################################################################
    # declarations
    ###########################################################################
    
    # declarations
    # : declaration-opt SEMICOLON space-opt declarations
    # | declaration-opt
    @PRODUCTION(
        "declarations : declaration-opt SEMICOLON space-opt declarations",
    )
    def p_declarations_list(self, t):
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
    
    
    ###########################################################################
    # actions
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
    
    
    ###########################################################################
    # error productions
    #
    # these are carefully crafted error productions to handle common syntactical
    # problems in (S)CSS
    ###########################################################################

    # recover from a bad CSS property declaration right before the semicolon
    # or closing inside of a declarations block
    @PRODUCTION(
        "declarations : declaration-opt error",
    )
    def p_declarations_error(self, t):
        pass
    
    
    ###########################################################################
    # unexpected token syntax errors
    ###########################################################################

    def p_error(self, t):
        print(u"Syntax error: unexpected token '%s' at Line %d, Column %d" % (
            t.value.value,
            t.value.line,
            t.value.column,
        ))
    


