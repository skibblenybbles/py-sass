import os, logging
from ply import yacc


# base class for all parsers

class Parser(object):
    
    ###########################################################################
    # internal state
    ###########################################################################
    
    # the lexer class to use for tokenizing the input
    Lexer = None
    
    # the Lexer instance
    lexer = None
    
    # the tokens from the Lexer
    tokens = None
    
    # the PLY yacc instance
    parser = None
    
    # the starting symbol
    start = None
    
    
    ###########################################################################
    # constructor and overrideable methods
    ###########################################################################
    
    def __init__(self, Lexer, line = 1, column = 1, debug = True, *args, **kwargs):
        super(Parser, self).__init__(*args, **kwargs)
        
        # instantiate the Lexer
        self.Lexer = Lexer
        self.lexer = self.Lexer(line = line, column = column)
        
        # debugging?
        self.debug = debug
        
        # get the tokens and start symbol from the overrideables
        self.tokens = self.get_tokens()
        self.start = self.get_start()
        
        # configure the output directory
        output_dir = os.path.join(os.path.dirname(__file__), "output/%s" % self.__class__.__name__)
        
        # set up a logging object?
        if debug:
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
            debuglog = logging.getLogger() if debug else None,
            debug = debug,
        )
    
    def get_tokens(self):
        return NotImplementedError
    
    def get_start(self):
        raise NotImplementedError
    
    
    ###########################################################################
    # public api
    ###########################################################################
    
    def parse(self, input):
        return self.parser.parse(input, lexer = self.lexer.lexer)

    
    ###########################################################################
    # unexpected token syntax errors
    ###########################################################################

    def p_error(self, t):
        print(u"Syntax error: unexpected token '%s' at Line %d, Column %d" % (
            t.value.value,
            t.value.line,
            t.value.column,
        ))
    


