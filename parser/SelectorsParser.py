from Parser import Parser
from productions import Selectors


class SelectorsParser(Parser, Selectors):
    
    ###########################################################################
    # overrideable methods
    ###########################################################################
    
    def get_tokens(self):
        return self.lexer.selector_tokens
    
    def get_start(self):
        return "selectors"
    
