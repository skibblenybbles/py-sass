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
    # whitespace, comments and empty productions
    ###########################################################################

    #######################################
    # space-opt
    # : space
    # | empty

    @PRODUCTION(
        "space-opt : space"
    )
    def p_space_opt_space(self, t):
        # TODO - build AST
        pass


    @PRODUCTION(
        "space-opt : empty"
    )
    def p_space_opt_empty(self, t):
        # TODO - build AST
        pass


    #######################################
    # space
    # : whitespace space
    # | blockcomment space
    # | htmlcomment space
    # | whitespace
    # | blockcomment
    # | htmlcomment

    @PRODUCTION(
        "space : whitespace space"
    )
    def p_space_whitespace_space(self, t):
        # TODO - build AST
        pass
    

    @PRODUCTION(
        "space : blockcomment space"
    )
    def p_space_blockcomment_space(self, t):
        # TODO - build AST
        pass


    @PRODUCTION(
        "space : htmlcomment space"
    )
    def p_space_htmlcomment_space(self, t):
        # TODO - build AST
        pass


    @PRODUCTION(
        "space : whitespace"
    )
    def p_space_whitespace(self, t):
        # TODO - build AST
        pass
    

    @PRODUCTION(
        "space : blockcomment"
    )
    def p_space_blockcomment(self, t):
        # TODO - build AST
        pass
    

    @PRODUCTION(
        "space : htmlcomment"
    )
    def p_space_htmlcomment(self, t):
        # TODO - build AST
        pass


    #######################################
    # whitespace
    # : SPACE

    @PRODUCTION(
        "whitespace : SPACE"
    )
    def p_whitespace(self, t):
        # TODO - build AST
        pass


    #######################################
    # blockcomment
    # : BLOCKCOMMENT

    @PRODUCTION(
        "blockcomment : BLOCKCOMMENT"
    )
    def p_blockcomment(self, t):
        # TODO - build AST
        pass


    #######################################
    # htmlcomment
    # : CDO
    # | CDC

    @PRODUCTION(
        "htmlcomment : CDO"
    )
    def p_htmlcomment_cdo(self, t):
        # TODO - build AST
        pass


    @PRODUCTION(
        "htmlcomment : CDC"
    )
    def p_htmlcomment_cdc(self, t):
        # TODO - build AST
        pass


    #######################################
    # empty
    # : <empty>

    @PRODUCTION(
        "empty :"
    )
    def p_empty(self, t):
        pass


    ###########################################################################
    # TODO
    ###########################################################################

    # stylesheet
    # : charset-opt space-opt imports-opt styles-opt

    @PRODUCTION(
        "stylesheet : charset-opt space-opt imports-opt styles-opt"
    )
    def p_stylesheet(self, t):
        # TODO - build AST
        pass


    # charset-opt
    # : charset
    # | empty

    @PRODUCTION(
        "charset-opt : charset"
    )
    def p_charset_opt_charset(self, t):
        # TODO - build AST
        pass


    @PRODUCTION(
        "charset-opt : empty"
    )
    def p_charset_opt_empty(self, t):
        # TODO - build AST
        pass


    # charset:
    # : SYM_CHARSET STRING space-opt SEMICOLON

    @PRODUCTION((
        "charset : SYM_CHARSET STRING space-opt SEMICOLON",
    ))
    def p_charset(self, t):
        # TODO - build AST
        pass


    # imports-opt
    # : imports
    # | empty

    @PRODUCTION(
        "imports-opt : imports"
    )
    def p_imports_opt_imports(self, t):
        # TODO - build AST
        pass


    @PRODUCTION(
        "imports-opt : empty"
    )
    def p_imports_opt_empty(self, t):
        # TODO - build AST
        pass


    # imports
    # : import imports
    # | import

    @PRODUCTION(
        "imports : import imports"
    )
    def p_imports_import_imports(self, t):
        # TODO - build AST
        pass


    @PRODUCTION(
        "imports : import"
    )
    def p_imports_import(self, t):
        # TODO - build AST
        pass


    # import
    # : SYM_IMPORT space-opt STRING space-opt media-queries-opt SEMICOLON space-opt
    # | SYM_IMPORT space-opt URI space-opt media-queries-opt SEMICOLON space-opt

    @PRODUCTION(
        "import : SYM_IMPORT space-opt STRING space-opt media-queries-opt SEMICOLON space-opt"
    )
    def p_import_string(self, t):
        # TODO - build AST
        pass


    @PRODUCTION(
        "import : SYM_IMPORT space-opt URI space-opt media-queries-opt SEMICOLON space-opt"
    )
    def p_import_uri(self, t):
        # TODO - build AST
        pass


    # media-queries-opt
    # : media-queries
    # | empty

    @PRODUCTION(
        "media-queries-opt : media-queries"
    )
    def p_media_queries_opt_media_queries(self, t):
        # TODO - build AST
        pass


    @PRODUCTION(
        "media-queries-opt : empty"
    )
    def p_media_queries_opt_empty(self, t):
        # TODO - build AST
        pass


    # media-queries
    # : media-query COMMA space-opt media-queries
    # | media-query

    @PRODUCTION(
        "media-queries : media-query COMMA space-opt media-queries"
    )
    def p_media_queries_media_query_media_queries(self, t):
        # TODO - build AST
        pass


    @PRODUCTION(
        "media-queries : media-query"
    )
    def p_media_queries_media_query(self, t):
        # TODO - build AST
        pass


    # media-query
    # : KEY_ONLY space-opt media-query-typed
    # | KEY_NOT space-opt media-query-typed
    # | media-query-typed
    # | media-query-expressions

    @PRODUCTION(
        "media-query : KEY_ONLY space-opt media-query-typed"
    )
    def p_media_query_only(self, t):
        # TODO - build AST
        pass


    @PRODUCTION(
        "media-query : KEY_NOT space-opt media-query-typed"
    )
    def p_media_query_not(self, t):
        # TODO - build AST
        pass


    @PRODUCTION(
        "media-query : media-query-typed"
    )
    def p_media_query_typed(self, t):
        # TODO - build AST
        pass


    @PRODUCTION(
        "media-query : media-query-expression"
    )
    def p_media_query_expression(self, t):
        # TODO - build AST
        pass


    # media-query-typed
    # : media-type KEY_AND space-opt media-query-expressions
    # | media-type

    @PRODUCTION(
        "media-query-typed : media-type KEY_AND space-opt media-query-expressions"
    )
    def p_media_query_typed_type_expessions(self, t):
        # TODO - build AST
        pass


    @PRODUCTION(
        "media-query-typed : media-type"
    )
    def p_media_query_typed_type(self, t):
        # TODO - build AST
        pass


    # media-type
    # : IDENTIFIER space-opt

    @PRODUCTION(
        "media-type : IDENTIFIER space-opt"
    )
    def p_media_type(self, t):
        # TODO - build AST
        pass


    # media-query-expressions
    # : media-query-expression KEY_AND space-opt media-query-expressions
    # | media-query-expression

    @PRODUCTION(
        "media-query-expressions : media-query-expression KEY_AND space-opt media-query-expressions"
    )
    def p_media_query_expressions_media_query_expressions_media_query_expressions(self, t):
        # TODO - build AST
        pass


    @PRODUCTION(
        "media-query-expressions : media-query-expression"
    )
    def p_media_query_expressions_media_query_expression(self, t):
        # TODO - build AST
        pass


    # media-query-expression
    # | LPAREN space-opt media-feature COLON space-opt declaration-expression RPAREN space-opt
    # : LPAREN space-opt media-feature RPAREN space-opt

    @PRODUCTION(
        "media-query-expression : LPAREN space-opt media-feature COLON space-opt declaration-expression RPAREN space-opt"
    )
    def p_media_query_expression_features_expression(self, t):
        # TODO - build AST
        pass


    @PRODUCTION(
        "media-query-expression : LPAREN space-opt media-feature RPAREN space-opt"
    )
    def p_media_query_expression_features(self, t):
        # TODO - build AST
        pass


    # media-feature
    # : IDENTIFIER space-opt

    @PRODUCTION(
        "media-feature : IDENTIFIER space-opt"
    )
    def p_media_feature(self, t):
        # TODO - build AST
        pass


    # styles-opt
    # : styles
    # | empty

    @PRODUCTION(
        "styles-opt : styles"
    )
    def p_styles_opt_styles(self, t):
        # TODO - build AST
        pass


    @PRODUCTION(
        "styles-opt : empty"
    )
    def p_styles_opt_empty(self, t):
        # TODO - build AST
        pass


    # styles
    # : style styles
    # : style

    @PRODUCTION(
        "styles : style styles"
    )
    def p_styles_style_styles(self, t):
        # TODO - build AST
        pass


    @PRODUCTION(
        "styles : style"
    )
    def p_styles_style(self, t):
        # TODO - build AST
        pass


    # style
    # : page
    # | media
    # | ruleset

    @PRODUCTION(
        "style : page"
    )
    def p_style_page(self, t):
        # TODO - build AST
        pass


    @PRODUCTION(
        "style : media"
    )
    def p_style_media(self, t):
        # TODO - build AST
        pass


    @PRODUCTION(
        "style : ruleset"
    )
    def p_style_ruleset(self, t):
        # TODO - build AST
        pass


    # page
    # : SYM_PAGE space-opt pseudo-page LBRACE space-opt declarations RBRACE space-opt

    @PRODUCTION(
        "page : SYM_PAGE space-opt pseudo-page-opt LBRACE space-opt declarations RBRACE space-opt"
    )
    def p_page(self, t):
        # TODO - build AST
        pass


    # psuedo-page-opt
    # : pseudo-page
    # | empty

    @PRODUCTION(
        "pseudo-page-opt : pseudo-page"
    )
    def p_pseudo_page_opt_pseudo_page(self, t):
        # TODO - build AST
        pass


    @PRODUCTION(
        "pseudo-page-opt : empty"
    )
    def p_pseudo_page_opt_empty(self, t):
        # TODO - build AST
        pass


    # pseudo-page
    # : COLON IDENTIFIER space-opt

    @PRODUCTION(
        "pseudo-page : COLON IDENTIFIER space-opt"
    )
    def p_pseudo_paget(self, t):
        # TODO - build AST
        pass


    # media
    # : SYM_MEDIA space-opt _before-media-queries media-queries _after-media-queries LBRACE space-opt styles-opt RBRACE space-opt

    @PRODUCTION(
        "media : SYM_MEDIA space-opt _before-media-queries media-queries _after-media-queries LBRACE space-opt styles-opt RBRACE space-opt"
    )
    def p_media(self, t):
        # TODO - build AST
        pass


    @PRODUCTION(
        "_before-media-queries :"
    )
    def p_before_media_queries(self, t):
        t.lexer.push_state("mediaquery")


    @PRODUCTION(
        "_after-media-queries :"
    )
    def p_after_media_queries(self, t):
        t.lexer.pop_state()



    # ruleset
    # : selectors LBRACE space-opt declarations RBRACE space-opt

    @PRODUCTION(
        "ruleset : selectors LBRACE space-opt declarations RBRACE space-opt"
    )
    def p_ruleset(self, t):
        # TODO - build AST
        pass


    # selectors
    # : selector COMMA space-opt selectors
    # | selector

    @PRODUCTION(
        "selectors : selector COMMA space-opt selectors"
    )
    def p_selectors_selector_selectors(self, t):
        # TODO - build AST
        pass


    @PRODUCTION(
        "selectors : selector"
    )
    def p_selectors_selector(self, t):
        # TODO - build AST
        pass


    # selector
    # : simple-selector combinator selector
    # | simple-selector space-opt

    @PRODUCTION(
        "selector : simple-selector combinator selector"
    )
    def p_selector_simple_selector_combinator_selector(self, t):
        # TODO - build AST
        pass


    @PRODUCTION(
        "selector : simple-selector space-opt"
    )
    def p_selector_simple_selector(self, t):
        # TODO - build AST
        pass


    # simple-selector
    # : type-selector selector-rules-opt
    # | selector-rules

    @PRODUCTION(
        "simple-selector : type-selector selector-rules-opt"
    )
    def p_simple_selector_type_selector_selector_rules_opt(self, t):
        # TODO - build AST
        pass


    @PRODUCTION(
        "simple-selector : selector-rules"
    )
    def p_simple_selector_selector_rules(self, t):
        # TODO - build AST
        pass


    # type-selector
    # : element-selector
    # | all-selector

    @PRODUCTION(
        "type-selector : element-selector"
    )
    def p_type_selector_element_selector(self, t):
        # TODO - build AST
        pass


    @PRODUCTION(
        "type-selector : all-selector"
    )
    def p_type_selector_all_selector(self, t):
        # TODO - build AST
        pass


    # element-selector
    # : namespace-prefix-opt element-name

    @PRODUCTION(
        "element-selector : namespace-prefix-opt element-name"
    )
    def p_element_selector(self, t):
        # TODO - build AST
        pass


    # all-selector
    # : namespace-prefix-opt OP_MUL

    @PRODUCTION(
        "all-selector : namespace-prefix-opt OP_MUL"
    )
    def p_all_selector(self, t):
        # TODO - build AST
        pass


    # namespace-prefix-opt 
    # : namespace-prefix
    # : empty

    @PRODUCTION(
        "namespace-prefix-opt : namespace-prefix"
    )
    def p_namespace_prefix_opt_namespace_prefix(self, t):
        # TODO - build AST
        pass


    @PRODUCTION(
        "namespace-prefix-opt : empty"
    )
    def p_namespace_prefix_opt_empty(self, t):
        # TODO - build AST
        pass


    # namespace-prefix
    # : NAMESPACE_PREFIX

    @PRODUCTION(
        "namespace-prefix : NAMESPACE_PREFIX"
    )
    def p_namespace_prefix(self, t):
        # TODO - build AST
        pass


    # element-name
    # : IDENTIFIER

    @PRODUCTION(
        "element-name : IDENTIFIER"
    )
    def p_identifier(self, t):
        # TODO - build AST
        pass


    # selector-rules-opt
    # : selector-rules
    # | empty

    @PRODUCTION(
        "selector-rules-opt : selector-rules"
    )
    def p_selector_rules_opt_selector_rules(self, t):
        # TODO - build AST
        pass


    @PRODUCTION(
        "selector-rules-opt : empty"
    )
    def p_selector_rules_opt_empty(self, t):
        # TODO - build AST
        pass


    # selector-rules
    # : selector-rule selector-rules
    # | selector-rule

    @PRODUCTION(
        "selector-rules : selector-rule selector-rules"
    )
    def p_selector_rules_selector_rule_selector_rules(self, t):
        # TODO - build AST
        pass


    @PRODUCTION(
        "selector-rules : selector-rule"
    )
    def p_selector_rules_selector_rule(self, t):
        # TODO - build AST
        pass


    # selector-rule
    # : HASH
    # | class
    # | attribute
    # | pseudo
    # | negation


    @PRODUCTION(
        "selector-rule : HASH"
    )
    def p_selector_rule_hash(self, t):
        # TODO - build AST
        pass


    @PRODUCTION(
        "selector-rule : class"
    )
    def p_selector_rule_class(self, t):
        # TODO - build AST
        pass


    @PRODUCTION(
        "selector-rule : attribute"
    )
    def p_selector_rule_attribute(self, t):
        # TODO - build AST
        pass


    @PRODUCTION(
        "selector-rule : pseudo"
    )
    def p_selector_rule_pseudo(self, t):
        # TODO - build AST
        pass


    @PRODUCTION(
        "selector-rule : negation"
    )
    def p_selector_rule_negation(self, t):
        # TODO - build AST
        pass


    # combinator
    # : space-opt OP_PLUS space-opt
    # | space-opt OP_GT space-opt
    # | space-opt OP_TILDE space-opt
    # | space


    @PRODUCTION(
        "combinator : space-opt OP_PLUS space-opt"
    )
    def p_combinator_plus(self, t):
        # TODO - build AST
        pass


    @PRODUCTION(
        "combinator : space-opt OP_GT space-opt"
    )
    def p_combinator_gt(self, t):
        # TODO - build AST
        pass


    @PRODUCTION(
        "combinator : space-opt OP_TILDE space-opt"
    )
    def p_combinator_tilde(self, t):
        # TODO - build AST
        pass


    @PRODUCTION(
        "combinator : space"
    )
    def p_combinator_space(self, t):
        # TODO - build AST
        pass


    # class
    # : DOT IDENTIFIER

    @PRODUCTION(
        "class : DOT IDENTIFIER"
    )
    def p_class(self, t):
        # TODO - build AST
        pass


    # attribute
    # : LBRACKET space-opt namespace-prefix-opt IDENTIFIER space-opt attribute-rule-opt RBRACKET

    @PRODUCTION(
        "attribute : LBRACKET space-opt namespace-prefix-opt IDENTIFIER space-opt attribute-rule-opt RBRACKET"
    )
    def p_attribute(self, t):
        # TODO - build AST
        pass


    # attribute-rule-opt
    # : attribute-rule
    # | empty

    @PRODUCTION(
        "attribute-rule-opt : attribute-rule"
    )
    def p_attribute_rule_opt_attribute_rule(self, t):
        # TODO - build AST
        pass


    @PRODUCTION(
        "attribute-rule-opt : empty"
    )
    def p_attribute_rule_opt_empty(self, t):
        # TODO - build AST
        pass


    # attribute-rule
    # : attribute-op attribute-value

    @PRODUCTION(
        "attribute-rule : attribute-op attribute-value"
    )
    def p_attribute_rule(self, t):
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
        "attribute-op : OP_PREFIXMATCH space-opt"
    )
    def p_attribute_op_prefixmatch(self, t):
        # TODO - build AST
        pass


    @PRODUCTION(
        "attribute-op : OP_SUFFIXMATCH space-opt"
    )
    def p_attribute_op_suffixmatch(self, t):
        # TODO - build AST
        pass


    @PRODUCTION(
        "attribute-op : OP_SUBSTRINGMATCH space-opt"
    )
    def p_attribute_substringmatch(self, t):
        # TODO - build AST
        pass
    

    @PRODUCTION(
        "attribute-op : OP_INCLUDES space-opt"
    )
    def p_attribute_op_includes(self, t):
        # TODO - build AST
        pass
    

    @PRODUCTION(
        "attribute-op : OP_DASHMATCH space-opt"
    )
    def p_attribute_op_dashmatch(self, t):
        # TODO - build AST
        pass
    


    @PRODUCTION(
        "attribute-op : OP_EQUALS space-opt"
    )
    def p_attribute_op_equals(self, t):
        # TODO - build AST
        pass
    

    # attribute-value
    # : IDENTIFIER space-opt
    # | STRING space-opt

    @PRODUCTION(
        "attribute-value : IDENTIFIER space-opt"
    )
    def p_attribute_value_identifier(self, t):
        # TODO - build AST
        pass
    

    @PRODUCTION(
        "attribute-value : STRING space-opt"
    )
    def p_attribute_value_string(self, t):
        # TODO - build AST
        pass
    

    # pseudo
    # : COLON pseudo-selector
    # | COLON COLON pseudo-selector

    @PRODUCTION(
        "pseudo : COLON pseudo-selector"
    )
    def p_pseudo_colon(self, t):
        # TODO - build AST
        pass
    

    @PRODUCTION(
        "pseudo : COLON COLON pseudo-selector"
    )
    def p_pseudo_colon_colon(self, t):
        # TODO - build AST
        pass
    

    # pseudo-selector
    # : IDENTIFIER
    # | pseudo-function

    @PRODUCTION(
        "pseudo-selector : IDENTIFIER"
    )
    def p_pseudo_selector_identifier(self, t):
        # TODO - build AST
        pass
    

    @PRODUCTION(
        "pseudo-selector : pseudo-function"
    )
    def p_pseudo_selector_pseudo_function(self, t):
        # TODO - build AST
        pass
    

    # pseudo-function
    # : FUNCTION space-opt pseudo-expression RPAREN

    @PRODUCTION(
        "pseudo-function : FUNCTION space-opt pseudo-expression RPAREN"
    )
    def p_pseudo_function(self, t):
        # TODO - build AST
        pass
    

    # pseudo-expression
    # : pseudo-term pseudo-expression
    # | pseudo-term

    @PRODUCTION(
        "pseudo-expression : pseudo-term pseudo-expression"
    )
    def p_pseudo_expression_term_expression(self, t):
        # TODO - build AST
        pass
    

    @PRODUCTION(
        "pseudo-expression : pseudo-term"
    )
    def p_pseudo_expression_term(self, t):
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
        "pseudo-term : OP_PLUS space-opt"
    )
    def p_pseudo_term_plus(self, t):
        # TODO - build AST
        pass
    

    @PRODUCTION(
        "pseudo-term : OP_MINUS space-opt"
    )
    def p_pseudo_term_minus(self, t):
        # TODO - build AST
        pass
    

    @PRODUCTION(
        "pseudo-term : DIMENSION space-opt"
    )
    def p_pseudo_term_dimension(self, t):
        # TODO - build AST
        pass
    

    @PRODUCTION(
        "pseudo-term : NUMBER space-opt"
    )
    def p_pseudo_term_number(self, t):
        # TODO - build AST
        pass
    

    @PRODUCTION(
        "pseudo-term : STRING space-opt"
    )
    def p_pseudo_term_string(self, t):
        # TODO - build AST
        pass
    

    @PRODUCTION(
        "pseudo-term : IDENTIFIER space-opt"
    )
    def p_pseudo_term_identifier(self, t):
        # TODO - build AST
        pass
    

    # negation
    # : NOT_SELECTOR space-opt negation-arg RPAREN

    @PRODUCTION(
        "negation : NOT_SELECTOR space-opt negation-argument RPAREN"
    )
    def p_negation(self, t):
        # TODO - build AST
        pass


    # negation-argument
    # : type-selector space-opt
    # | HASH space-opt
    # | class space-opt
    # | attribute space-opt
    # | pseudo space-opt

    @PRODUCTION(
        "negation-argument : type-selector space-opt"
    )
    def p_negation_argument_type_selector(self, t):
        # TODO - build AST
        pass
    

    @PRODUCTION(
        "negation-argument : HASH space-opt"
    )
    def p_negation_argument_hash(self, t):
        # TODO - build AST
        pass


    @PRODUCTION(
        "negation-argument : class space-opt"
    )
    def p_negation_argument_class(self, t):
        # TODO - build AST
        pass
    

    @PRODUCTION(
        "negation-argument : attribute space-opt"
    )
    def p_negation_argument_attribute(self, t):
        # TODO - build AST
        pass
    

    @PRODUCTION(
        "negation-argument : pseudo space-opt"
    )
    def p_negation_argument_pseudo(self, t):
        # TODO - build AST
        pass
    

    # declarations
    # : declaration-opt SEMICOLON space-opt declarations
    # | declaration-opt


    @PRODUCTION(
        "declarations : declaration-opt SEMICOLON space-opt declarations"
    )
    def p_declarations_declaration_opt_declarations(self, t):
        # TODO - build AST
        pass


    @PRODUCTION(
        "declarations : declaration-opt"
    )
    def p_declarations_declaration_opt(self, t):
        # TODO - build AST
        pass


    # declaration-opt
    # : declaration
    # | empty

    @PRODUCTION(
        "declaration-opt : declaration"
    )
    def p_declaration_opt_declaration(self, t):
        # TODO - build AST
        pass


    @PRODUCTION(
        "declaration-opt : empty"
    )
    def p_declaration_opt_empty(self, t):
        # TODO - build AST
        pass


    # declaration
    # : property COLON space-opt declaration-expression important-opt

    @PRODUCTION(
        "declaration : property COLON space-opt declaration-expression important-opt"
    )
    def p_declaration(self, t):
        # TODO - build AST
        pass


    # property
    # : IDENTIFIER space-opt

    @PRODUCTION(
        "property : IDENTIFIER space-opt"
    )
    def p_property(self, t):
        # TODO - build AST
        pass
    

    # important-opt
    # : important
    # | empty

    @PRODUCTION(
        "important-opt : _before-important important _after-important"
    )
    def p_important_opt_important(self, t):
        # TODO - build AST
        pass


    @PRODUCTION(
        "important-opt : empty"
    )
    def p_important_opt_empty(self, t):
        # TODO - build AST
        pass


    @PRODUCTION(
        "_before-important :"
    )
    def p_before_important(self, t):
        t.lexer.push_state("flag")


    @PRODUCTION(
        "_after-important :"
    )
    def p_after_important(self, t):
        t.lexer.pop_state()


    # important
    # : BANG space-opt KEY_IMPORTANT space-opt

    @PRODUCTION(
        "important : BANG space-opt KEY_IMPORTANT space-opt"
    )
    def p_important(self, t):
        # TODO - build AST
        pass


    # declaration-expression
    # : declaration-term declaration-op-opt declaration-expression
    # | declaration-term

    @PRODUCTION(
        "declaration-expression : declaration-term declaration-op-opt declaration-expression"
    )
    def p_declaration_expression_term_expression(self, t):
        # TODO - build AST
        pass


    @PRODUCTION(
        "declaration-expression : declaration-term"
    )
    def p_declaration_expression_term(self, t):
        # TODO - build AST
        pass


    # declaration-op-opt
    # : declaration-op
    # | empty

    @PRODUCTION(
        "declaration-op-opt : declaration-op"
    )
    def p_declaration_op_opt_op(self, t):
        # TODO - build AST
        pass


    @PRODUCTION(
        "declaration-op-opt : empty"
    )
    def p_declaration_op_opt_empty(self, t):
        # TODO - build AST
        pass


    # declaration-op
    # : OP_DIV space-opt
    # | COMMA space-opt

    @PRODUCTION(
        "declaration-op : OP_DIV space-opt"
    )
    def p_declaration_op_div(self, t):
        # TODO - build AST
        pass


    @PRODUCTION(
        "declaration-op : COMMA space-opt"
    )
    def p_declaration_op_comma(self, t):
        # TODO - build AST
        pass


    # declaration-term
    # : declaration-unary-op-opt declaration-numeric
    # | declaration-nonnumeric

    @PRODUCTION(
        "declaration-term : declaration-unary-op-opt declaration-numeric"
    )
    def p_declaration_term_numeric(self, t):
        # TODO - build AST
        pass


    @PRODUCTION(
        "declaration-term : declaration-nonnumeric"
    )
    def p_declaration_term_nonnumeric(self, t):
        # TODO - build AST
        pass


    # declaration-unary-op-opt
    # : declaration-unary-op
    # | empty

    @PRODUCTION(
        "declaration-unary-op-opt : declaration-unary-op"
    )
    def p_declaration_unary_op_opt_op(self, t):
        # TODO - build AST
        pass


    @PRODUCTION(
        "declaration-unary-op-opt : empty"
    )
    def p_declaration_unary_op_empty(self, t):
        # TODO - build AST
        pass


    # declaration-unary-op
    # : OP_MINUS space-opt
    # | OP_PLUS space-opt

    @PRODUCTION(
        "declaration-unary-op : OP_MINUS space-opt"
    )
    def p_declaration_unary_op_minus(self, t):
        # TODO - build AST
        pass


    @PRODUCTION(
        "declaration-unary-op : OP_PLUS space-opt"
    )
    def p_declaration_unary_op_plus(self, t):
        # TODO - build AST
        pass


    # declaration-numeric
    # : NUMBER space-opt
    # | PERCENTAGE space-opt
    # | DIMENSION space-opt

    @PRODUCTION(
        "declaration-numeric : NUMBER space-opt"
    )
    def p_declaration_numeric_number(self, t):
        # TODO - build AST
        pass


    @PRODUCTION(
        "declaration-numeric : PERCENTAGE space-opt"
    )
    def p_declaration_numeric_percentage(self, t):
        # TODO - build AST
        pass


    @PRODUCTION(
        "declaration-numeric : DIMENSION space-opt"
    )
    def p_declaration_numeric_dimension(self, t):
        # TODO - build AST
        pass


    # declaration-nonnumeric
    # : STRING space-opt
    # | URI space-opt
    # | IDENTIFIER space-opt 
    # | declaration-hexcolor
    # | declaration-function

    @PRODUCTION(
        "declaration-nonnumeric : STRING space-opt"
    )
    def p_declaration_nonnumeric_string(self, t):
        # TODO - build AST
        pass


    @PRODUCTION(
        "declaration-nonnumeric : URI space-opt"
    )
    def p_declaration_nonnumeric_uri(self, t):
        # TODO - build AST
        pass


    @PRODUCTION(
        "declaration-nonnumeric : IDENTIFIER space-opt"
    )
    def p_declaration_nonnumeric_identifier(self, t):
        # TODO - build AST
        pass


    @PRODUCTION(
        "declaration-nonnumeric : declaration-hexcolor"
    )
    def p_declaration_nonnumeric_hexcolor(self, t):
        # TODO - build AST
        pass


    @PRODUCTION(
        "declaration-nonnumeric : declaration-function"
    )
    def p_declaration_nonnumeric_function(self, t):
        # TODO - build AST
        pass


    # declaration-hexcolor
    # : HASH space-opt

    @PRODUCTION(
        "declaration-hexcolor : HASH space-opt"
    )
    def p_declaration_hexcolor(self, t):
        # TODO - build AST
        pass


    # declaration-function
    # : FUNCTION space-opt declaration-expression RPAREN space-opt

    @PRODUCTION(
        "declaration-function : FUNCTION space-opt declaration-expression RPAREN space-opt"
    )
    def p_declaration_function(self, t):
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
        "property : ms-property-hack IDENTIFIER space-opt"
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


    # declaration-term
    # : declaration-unary-op-opt declaration-numeric (already defined)
    # | declaration-nonnumeric (already defined)
    # | ms-declaration-hack

    @PRODUCTION(
        "declaration-term : ms-declaration-hack"
    )
    def p_declaration_term_ms_declaration_hack(self, t):
        # TODO - build AST
        pass


    # ms-declaration-hack
    # : ms-declaration-function ms-declaration-arguments-opt RPAREN space-opt

    @PRODUCTION(
        "ms-declaration-hack : ms-declaration-function ms-declaration-arguments-opt RPAREN space-opt"
    )
    def p_ms_declaration_hack(self, t):
        # TODO - build AST
        pass


    # ms-declaration-function
    # : IDENTIFIER COLON ms-declaration-function
    # | IDENTIFIER DOT ms-declaration-function
    # | IDENTIFIER DOT FUNCTION space-opt

    @PRODUCTION(
        "ms-declaration-function : IDENTIFIER COLON ms-declaration-function"
    )
    def p_ms_declaration_function_colon(self, t):
        # TODO - build AST
        pass


    @PRODUCTION(
        "ms-declaration-function : IDENTIFIER DOT ms-declaration-function"
    )
    def p_ms_declaration_function_dot(self, t):
        # TODO - build AST
        pass


    @PRODUCTION(
        "ms-declaration-function : IDENTIFIER DOT FUNCTION space-opt"
    )
    def p_ms_declaration_function_function(self, t):
        # TODO - build AST
        pass


    # ms-declaration-arguments-opt
    # : ms-declaration-arguments
    # | empty

    @PRODUCTION(
        "ms-declaration-arguments-opt : ms-declaration-arguments"
    )
    def p_ms_declaration_arguments_opt_arguments(self, t):
        # TODO - build AST
        pass


    @PRODUCTION(
        "ms-declaration-arguments-opt : empty"
    )
    def p_ms_declaration_arguments_opt_empty(self, t):
        # TODO - build AST
        pass


    # ms-declaration-arguments
    # : ms-declaration-argument COMMA space-opt ms-declaration-arguments

    @PRODUCTION(
        "ms-declaration-arguments : ms-declaration-argument COMMA space-opt ms-declaration-arguments"
    )
    def p_ms_declaration_arguments_argument_arguments(self, t):
        # TODO - build AST
        pass


    @PRODUCTION(
        "ms-declaration-arguments : ms-declaration-argument"
    )
    def p_ms_declaration_arguments_argument(self, t):
        # TODO - build AST
        pass


    # ms-declaration-argument
    # : IDENTIFIER space-opt OP_EQUALS space-opt ms-declaration-argument-value

    @PRODUCTION(
        "ms-declaration-argument : IDENTIFIER space-opt OP_EQUALS space-opt ms-declaration-argument-value",
    )
    def p_ms_declaration_argument(self, t):
        # TODO - build AST
        pass


    # ms-declaration-argument-value
    # : STRING space-opt
    # | NUMBER space-opt

    @PRODUCTION(
        "ms-declaration-argument-value : STRING space-opt"
    )
    def p_ms_declaration_argument_value_string(self, t):
        # TODO - build AST
        pass


    @PRODUCTION(
        "ms-declaration-argument-value : NUMBER space-opt"
    )
    def p_ms_declaration_argument_value_number(self, t):
        # TODO - build AST
        pass


    ###########################################################################
    # error productions
    #
    # these are carefully crafted error productions to handle common syntactical
    # problems in (S)CSS
    ###########################################################################

    # recover from a bad CSS property declaration right before the semicolon
    # or closing inside of a declarations block
    @PRODUCTION(
        "declarations : declaration-opt error"
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


    ###########################################################################
    # starting symbol
    ###########################################################################

    start = "stylesheet"


