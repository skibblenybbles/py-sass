from ..utils import PRODUCTION
from Value import Value
from ActionMediaquery import ActionMediaquery


class Media(Value, ActionMediaquery):
    
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
