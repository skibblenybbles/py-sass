###############################################################################
# PRODUCTION decorator, similar to the @TOKEN decorator for the lexer.
###############################################################################

def PRODUCTION(*args):
    
    def set_production(fn):
        # hack to overwrite the docstring with the given production
        fn.__doc__ = u"\n".join(args)
        return fn
        
    return set_production
