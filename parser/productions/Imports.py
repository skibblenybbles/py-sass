from ..utils import PRODUCTION
from Media import Media


class Imports(Media):
    
    ###########################################################################
    # imports
    ###########################################################################
    
    # imports-opt
    # : imports
    # | empty
    @PRODUCTION(
        "imports-opt : imports",
        "            | empty",
    )
    def p_imports_opt(self, t):
        # TODO - build AST
        pass
    
    
    # imports
    # : import imports
    # | import
    @PRODUCTION(
        "imports : import imports",
    )
    def p_imports_list(self, t):
        # TODO - build AST
        pass
    
    @PRODUCTION(
        "imports : import",
    )
    def p_imports_terminal(self, t):
        # TODO - build AST
        pass
    
    
    # import
    # : SYM_IMPORT space-opt _before-mediaquery import-src media-queries-opt _after-mediaquery SEMICOLON space-opt
    @PRODUCTION(
        "import : SYM_IMPORT space-opt _before-mediaquery import-src media-queries-opt _after-mediaquery SEMICOLON space-opt",
    )
    def p_import(self, t):
        # TODO - build AST
        pass
    
    
    # import-src
    # : STRING space-opt
    # | URI space-opt
    @PRODUCTION(
        "import-src : STRING space-opt",
        "           | URI space-opt",
    )
    def p_import_src(self, t):
        # TODO - build AST
        pass
