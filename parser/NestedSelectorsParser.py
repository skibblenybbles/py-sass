from Parser import Parser
from productions import NestedSelectors


class NestedSelectorsParser(Parser, NestedSelectors):
    
    ###########################################################################
    # overrideable methods
    ###########################################################################
    
    def get_tokens(self):
        return self.lexer.selector_tokens
    
    def get_start(self):
        return "nested-selectors"
    
