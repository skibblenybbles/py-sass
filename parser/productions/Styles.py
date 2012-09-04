from ..utils import PRODUCTION
from Page import Page
from Media import Media
from Ruleset import Ruleset


class Styles(Page, Media, Ruleset):
    
    ###########################################################################
    # styles
    ###########################################################################
    
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
    def p_style(self, t):
        # TODO - build AST
        pass
    
    