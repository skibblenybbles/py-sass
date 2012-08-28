###############################################################################
# PRODUCTION decorator, similar to the @TOKEN decorator for the lexer.
###############################################################################

def PRODUCTION(production):
    
    def set_production(fn):
        # hack to overwrite the docstring with the given production
        if isinstance(production, (list, tuple)):
            p = u"\n".join(production)
        else:
            p = production
        fn.__doc__ = p
        return fn
        
    return set_production
