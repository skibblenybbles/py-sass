from ..utils import PRODUCTION
from Charset import Charset
from Imports import Imports
from Styles import Styles


class Stylesheet(Charset, Imports, Styles):
    
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
