from Parser import Parser
from productions import Stylesheet, MSHacks


class SCSSParser(Parser, Stylesheet, MSHacks):
    
    ###########################################################################
    # overrideable methods
    ###########################################################################
    
    def get_tokens(self):
        return self.lexer.tokens
    
    def get_start(self):
        return "stylesheet"
    
