import re
from ply import lex
from tokens import Token
from tags import tags, deprecated_tags


class Lexer(object):
    
    ###########################################################################
    # internal state
    ###########################################################################
    
    # the PLY lex instance
    lexer = None
    
    # the current line
    line = 1
    
    # the current column
    column = 1
    
    
    ###########################################################################
    # constructor
    ###########################################################################
    
    def __init__(self, *args, **kwargs):
        super(Lexer, self).__init__(*args, **kwargs)
        
        # create the lexer instance
        self.lexer = lex.lex(module = self, reflags = re.IGNORECASE)
    
    
    ###########################################################################
    # public api
    ###########################################################################
    
    def set_position(self, line = None, column = None):
        if line is not None:
            self.line = line
        if column is not None:
            self.column = column
    
    
    ###########################################################################
    # partial regular expressions used to build tokens
    ###########################################################################
    
    partials = { }

    # whitespace
    partials['space']               = r'([ \t\r\n\f]+)'
    partials['optspace']            = r'(' + partials['space'] + '?)'
    partials['newline']             = r'(\n|\r\n|\r|\f)'

    # character sequences
    partials['hex']                 = r'[0-9a-f]'
    partials['nonascii']            = r'[\240-\377]'
    partials['unicode']             = r'(\\' + partials['hex'] + r'{1,6}(\r\n|[ \t\r\n\f])?)'
    partials['escape']              = r'(' + partials['unicode'] + r'|(\\[^\r\n\f0-9a-f]))'

    # names and identifiers
    partials['namestart']           = r'([_a-z]|' + partials['nonascii'] + r'|' + partials['escape'] + r')'
    partials['namechar']            = r'([-_a-z0-9]|' + partials['nonascii'] + r'|' + partials['escape'] + r')'
    partials['name']                = r'(' + partials['namechar'] + r'+)'
    partials['identifier']          = r'(-?' + partials['namestart'] + partials['namechar'] + r'*)'
    partials['namespace']           = r'(' + partials['identifier'] + r'|\*)'
    partials['namespacedelim']      = r'\|'
    
    # strings
    partials['stringdouble']        = r'(\"([^\n\r\f\\"]|\\' + partials['newline'] + r'|' + partials['escape'] + r')*\")'
    partials['stringsingle']        = r"(\'([^\n\r\f\\']|\\" + partials['newline'] + r'|' + partials['escape'] + r")*\')"
    partials['string']              = r'(' + partials['stringdouble'] + r'|' + partials['stringsingle'] + r')'
    partials['badstringdouble']     = r'(\"([^\n\r\f\\"]|\\' + partials['newline'] + r'|' + partials['escape'] + r')*\\?)'
    partials['badstringsingle']     = r"(\'([^\n\r\f\\']|\\" + partials['newline'] + r'|' + partials['escape'] + r")*\\?)"
    partials['badstring']           = r'(' + partials['badstringdouble'] + r'|' + partials['badstringsingle'] + r')'

    # comments
    partials['inlinecomment']       = r'((\/\/[^\n\r\f]*)' + partials['newline'] + r')'
    partials['blockcomment']        = r'(\/\*[^*]*\*+([^/*][^*]*\*+)*\/)'
    partials['badcommentstarless']  = r'(\/\*[^*]*\*+([^/*][^*]*\*+)*)'
    partials['badcommentslashless'] = r'(\/\*[^*]*(\*+[^/*][^*]*)*)'
    partials['badcomment']          = r'(' + partials['badcommentstarless'] + r'|' + partials['badcommentslashless'] + ')'

    # uris
    partials['baduri1']             = r'(url\(' + partials['optspace'] + r'([!#$%&*-\[\]-~]|' + partials['nonascii'] + r'|' + partials['escape'] + r')*' + partials['optspace'] + r')'
    partials['baduri2']             = r'(url\(' + partials['optspace'] + partials['string'] + partials['optspace'] + r')'
    partials['baduri3']             = r'(url\(' + partials['optspace'] + partials['badstring'] + r')'
    partials['baduri']              = r'(' + partials['baduri1'] + r'|' + partials['baduri2'] + r'|' + partials['baduri3'] + r')'

    # url
    partials['url']                 = r'(([!#$%&*-~]|' + partials['nonascii'] + r'|' + partials['escape'] + r')*)'

    # selectors
    partials['selectorchar']        = r'([^{};])'
    partials['selectors']           = r'((' + partials['selectorchar'] + r'|' + partials['inlinecomment'] + r'|' +  partials['blockcomment'] + ')+{)'
    
    # number
    partials['number']              = r'([0-9]+|[0-9]*\.[0-9]+)'
    
    # optional unicode-escaped characters used in keywords
    partials['A']                   = r'(a|\\0{0,4}(41|61)(\r\n|[ \t\r\n\f])?)'
    partials['B']                   = r'(b|\\0{0,4}(42|62)(\r\n|[ \t\r\n\f])?)'
    partials['C']                   = r'(c|\\0{0,4}(43|63)(\r\n|[ \t\r\n\f])?)'
    partials['D']                   = r'(d|\\0{0,4}(44|64)(\r\n|[ \t\r\n\f])?)'
    partials['E']                   = r'(e|\\0{0,4}(45|65)(\r\n|[ \t\r\n\f])?)'
    partials['F']                   = r'(f|\\0{0,4}(46|66)(\r\n|[ \t\r\n\f])?)'
    partials['G']                   = r'(g|\\0{0,4}(47|67)(\r\n|[ \t\r\n\f])?|\\g)'
    partials['H']                   = r'(h|\\0{0,4}(48|68)(\r\n|[ \t\r\n\f])?|\\h)'
    partials['I']                   = r'(i|\\0{0,4}(49|69)(\r\n|[ \t\r\n\f])?|\\i)'
    partials['J']                   = r'(j|\\0{0,4}(4a|6a)(\r\n|[ \t\r\n\f])?|\\j)'
    partials['K']                   = r'(k|\\0{0,4}(4b|6b)(\r\n|[ \t\r\n\f])?|\\k)'
    partials['L']                   = r'(l|\\0{0,4}(4c|6c)(\r\n|[ \t\r\n\f])?|\\l)'
    partials['M']                   = r'(m|\\0{0,4}(4d|6d)(\r\n|[ \t\r\n\f])?|\\m)'
    partials['N']                   = r'(n|\\0{0,4}(4e|6e)(\r\n|[ \t\r\n\f])?|\\n)'
    partials['O']                   = r'(o|\\0{0,4}(4f|6f)(\r\n|[ \t\r\n\f])?|\\o)'
    partials['P']                   = r'(p|\\0{0,4}(50|70)(\r\n|[ \t\r\n\f])?|\\p)'
    partials['Q']                   = r'(q|\\0{0,4}(51|71)(\r\n|[ \t\r\n\f])?|\\q)'
    partials['R']                   = r'(r|\\0{0,4}(52|72)(\r\n|[ \t\r\n\f])?|\\r)'
    partials['S']                   = r'(s|\\0{0,4}(53|73)(\r\n|[ \t\r\n\f])?|\\s)'
    partials['T']                   = r'(t|\\0{0,4}(54|74)(\r\n|[ \t\r\n\f])?|\\t)'
    partials['U']                   = r'(u|\\0{0,4}(55|75)(\r\n|[ \t\r\n\f])?|\\u)'
    partials['V']                   = r'(v|\\0{0,4}(56|76)(\r\n|[ \t\r\n\f])?|\\v)'
    partials['W']                   = r'(w|\\0{0,4}(57|77)(\r\n|[ \t\r\n\f])?|\\w)'
    partials['X']                   = r'(x|\\0{0,4}(58|78)(\r\n|[ \t\r\n\f])?|\\x)'
    partials['Y']                   = r'(y|\\0{0,4}(59|79)(\r\n|[ \t\r\n\f])?|\\y)'
    partials['Z']                   = r'(z|\\0{0,4}(5a|7a)(\r\n|[ \t\r\n\f])?|\\z)'


    ###########################################################################
    # create tokens, updating line and column numbers
    ###########################################################################
    
    rx_newline = re.compile(partials['newline'])
    def create_token(self, t, process_lines):
        """
        Create a Token from the given LexToken and update the line and 
        column values.
        """
        
        # store the original value from the lexer
        value = t.value
    
        # overwrite the value with a created token
        t.value = Token(self, t)
        
        # process line number?
        if process_lines:
            
            # find all of the newlines so we can update the line number
            matches = [m for m in self.rx_newline.finditer(value)]
            self.line += len(matches)
            
            # reset the column counter?
            if len(matches) > 0:
                m = matches[-1]
                self.column = len(value) - m.end() + 1
                
            else:
                self.column += len(value)
        
        else:
            # simply update the column counter
            self.column += len(value)
        
        # return the created token (in t.value)
        return t.value


    ###########################################################################
    # lexer states
    ###########################################################################

    states = (
    
        # mediaquery:
        # adds keywords "only", "and" and "not"
        ("mediaquery", "inclusive"),
    
        # flag:
        # adds keyword "important"
        ("flag", "inclusive"),
    )
    

    ###########################################################################
    # token names matched by the lexer
    ###########################################################################
    
    # tokens used by the SCSS parser
    tokens = ()
    

    ###########################################################################
    # ignored tokens
    ###########################################################################
    
    @lex.TOKEN(
        partials['inlinecomment']
    )
    def t_ignore_INLINECOMMENT(self, t):
        self.create_token(t, True)
        return None

    
    ###########################################################################
    # whitespace and comment tokens
    ###########################################################################

    # SPACE - whitespace
    tokens += ("SPACE",)

    @lex.TOKEN(
        partials['space'],
    )
    def t_SPACE(self, t):
        self.create_token(t, True)
        return t


    # CDO - HTML comment delimiter open: <!--
    tokens += ("CDO",)

    @lex.TOKEN(
        r'<!--',
    )
    def t_CDO(self, t):
        self.create_token(t, False)
        return t


    # CDC - HTML comment delimter close: -->
    tokens += ("CDC",)

    @lex.TOKEN(
        r'-->',
    )
    def t_CDC(self, t):
        self.create_token(t, False)
        return t


    # BLOCKCOMMENT - block comments: /* ... */
    tokens += ("BLOCKCOMMENT",)

    @lex.TOKEN(
        partials['blockcomment'],
    )
    def t_BLOCKCOMMENT(self, t):
        self.create_token(t, True)
        return t


    # BADCOMMENT - bad block comment syntax
    @lex.TOKEN(
        partials['badcomment'],
    )
    def t_BADCOMMENT(self, t):
        self.create_token(t, True)
        
        # TODO: yell about this!
        return None


    ###########################################################################
    # special selector tokens
    ###########################################################################

    # NOT_SELECTOR - :not( ... ) psuedo selector
    tokens += ("NOT_SELECTOR",)

    @lex.TOKEN(
        ':' + ''.join([partials[e] for e in "NOT"]) + r'\(',
    )
    def t_NOT_SELECTOR(self, t):
        self.create_token(t, True)
        return t


    ###########################################################################
    # directive tokens
    ###########################################################################

    # SYM_IMPORT - @import
    tokens += ("SYM_IMPORT",)
    
    @lex.TOKEN(
        r'@' + ''.join([partials[e] for e in "IMPORT"]),
    )
    def t_SYM_IMPORT(self, t):
        token = self.create_token(t, True)
        token.parsed = "@import"
        return t


    # SYM_PAGE - @page
    tokens += ("SYM_PAGE",)

    @lex.TOKEN(
        r'@' + ''.join([partials[e] for e in "PAGE"]),
    )
    def t_SYM_PAGE(self, t):
        token = self.create_token(t, True)
        token.parsed = "@page"
        return t


    # SYM_MEDIA - @media
    tokens += ("SYM_MEDIA",)

    @lex.TOKEN(
        r'@' + ''.join([partials[e] for e in "MEDIA"]),
    )
    def t_SYM_MEDIA(self, t):
        token = self.create_token(t, True)
        token.parsed = "@media"
        return t


    # SYM_CHARSET - "@charset "
    tokens += ("SYM_CHARSET",)

    @lex.TOKEN(
        r"@charset[ ]",
    )
    def t_SYM_CHARSET(self, t):
        token = self.create_token(t, False)
        token.parsed = "@charset"
        return t


    ###########################################################################
    # literal tokens
    ###########################################################################

    # STRING - single or double quote string
    tokens += ("STRING",)

    @lex.TOKEN(
        partials['string'],
    )
    def t_STRING(self, t):
        self.create_token(t, True)
        return t
    

    # BAD_STRING - bad string syntax
    @lex.TOKEN(
        partials['badstring'],
    )
    def t_BAD_STRING(self, t):
        self.create_token(t, True)
        
        # TODO: yell about this
        return None


    # HASH - hash literal: #this-is-a-hash
    tokens += ("HASH",)

    @lex.TOKEN(
        r'\#(?P<name>' + partials['name'] + ')',
    )
    def t_HASH(self, t):
        m = self.lexer.lexmatch
        token = self.create_token(t, True)
        token.name = m.group('name')
        return t


    # DIMENSION - number with arbitrary units
    # hybrid of CSS 2.1 and CSS 3 specs
    tokens += ("DIMENSION",)
 
    @lex.TOKEN(
        r'(?P<number>' + partials['number'] + r')(?P<units>' + partials['identifier'] + r')',
    )
    def t_DIMENSION(self, t):
        m = self.lexer.lexmatch
        token = self.create_token(t, True)
        token.number = m.group('number')
        try:
            token.number = int(token.number)
        except ValueError:
            try:
                token.number = float(token.number)
            except ValueError:
                # boo :(
                pass
        token.units = m.group('units')
        return t


    # PERCENTAGE - number with "%" units
    tokens += ("PERCENTAGE",)

    @lex.TOKEN(
        r'(?P<number>' + partials['number'] + r')%',
    )
    def t_PERCENTAGE(self, t):
        m = self.lexer.lexmatch
        token = self.create_token(t, False)
        token.number = m.group('number')
        try:
            token.number = int(token.number)
        except ValueError:
            try:
                token.number = float(token.number)
            except ValueError:
                # boo :(
                pass
        return t


    # NUMBER - number
    tokens += ("NUMBER",)

    @lex.TOKEN(
        partials['number'],
    )
    def t_NUMBER(self, t):
        m = self.lexer.lexmatch
        token = self.create_token(t, False)
        token.number = m.group()
        try:
            token.number = int(token.number)
        except ValueError:
            try:
                token.number = float(token.number)
            except ValueError:
                # boo :(
                pass
        return t


    # URI - url( ... )
    tokens += ("URI",)

    @lex.TOKEN(
        r'url\((?P<url>' + partials['string'] + r'|' + partials['url'] + r')\)',
    )
    def t_URI(self, t):
        m = self.lexer.lexmatch
        token = self.create_token(t, True)
        token.url = m.group('url')
        return t


    # BAD_URI - bad uri syntax
    @lex.TOKEN(
        partials['baduri'],
    )
    def t_BAD_URI(self, t):
        self.create_token(t, True)
        # TODO: yell about this
        
        return None


    ###########################################################################
    # function, prefixed identifiers and identifier tokens
    ###########################################################################

    # FUNCTION - identifier with following "("
    tokens += ("FUNCTION",)

    @lex.TOKEN(
        r'(?P<identifier>' + partials['identifier'] + ')\(',
    )
    def t_FUNCTION(self, t):
        m = self.lexer.lexmatch
        token = self.create_token(t, True)
        t.identifier = m.group('identifier')
        return t


    # PREFIXED_IDENTIFIER - optional namespace followed by a namespace
    # delimiter, prefixing an identifier
    tokens += ("PREFIXED_IDENTIFIER",)
    
    @lex.TOKEN(
        r'(?P<namespace>' + partials['namespace'] + r')?' + partials['namespacedelim'] + r'(?P<identifier>' + partials['identifier'] + r')'
    )
    def t_PREFIXED_IDENTIFIER(self, t):
        m = self.lexer.lexmatch
        token = self.create_token(t, True)
        t.namespace = m.group('namespace')
        t.identifier = m.group('identifier')
        return t
    
    
    # PREFIXED_ALL - optional namespace followed by a namespace
    # delimiter, prefixing '*"
    tokens += ("PREFIXED_ALL",)
    
    @lex.TOKEN(
        r'(?P<namespace>' + partials['namespace'] + r')?' + partials['namespacedelim'] + r'\*'
    )
    def t_PREFIXED_ALL(self, t):
        m = self.lexer.lexmatch
        token = self.create_token(t, True)
        t.namespace = m.group('namespace')
        return t
    
    
    # IDENTIFIER - identifier
    tokens += ("IDENTIFIER",)

    @lex.TOKEN(
        partials['identifier'],
    )
    def t_IDENTIFIER(self, t):
        # TODO: improve this check...
        if t.value in tags:
            
            #t.type = "ELEMENT"
            pass
            
        elif t.value in deprecated_tags:
            
            # TODO: yell about this
            # treat it as an identifier
            pass
        
        self.create_token(t, True)
        return t
    
    
    # TEMP!
    tokens += ("ELEMENT",)
    t_ELEMENT = t_IDENTIFIER

    
    
    ###########################################################################
    # mediaquery state tokens
    ###########################################################################
    
    # KEY_ONLY - "only" keyword
    # only available in "mediaquery" state
    tokens += ("KEY_ONLY",)

    @lex.TOKEN(
        r''.join([partials[e] for e in "ONLY"]),
    )
    def t_mediaquery_KEY_ONLY(self, t):
        token = self.create_token(t, True)
        token.parsed = "only"
        return t


    # KEY_AND - "and" keyword
    # only available in "mediaquery" state
    tokens += ("KEY_AND",)

    @lex.TOKEN(
        r''.join([partials[e] for e in "AND"]),
    )
    def t_mediaquery_KEY_AND(self, t):
        token = self.create_token(t, True)
        token.parsed = "and"
        return t
    

    # KEY_NOT - "not" keyword
    # only available in "mediaquery" state
    tokens += ("KEY_NOT",)

    @lex.TOKEN(
        r''.join([partials[e] for e in "NOT"]),
    )
    def t_mediaquery_KEY_NOT(self, t):
        token = self.create_token(t, True)
        token.parsed = "not"
        return t
    
    
    ###########################################################################
    # flag state tokens
    ###########################################################################
    
    # KEY_IMPORTANT - "important" keyword
    # only available in "flag" state
    tokens += ("KEY_IMPORTANT",)

    @lex.TOKEN(
        r''.join([partials[e] for e in "IMPORTANT"]),
    )
    def t_flag_KEY_IMPORTANT(self, t):
        token = self.create_token(t, True)
        token.parsed = "important"
        return t
    
    
    ###########################################################################
    # simple tokens (operators and grouping delimiters) matched by the lexer
    ###########################################################################

    simple_tokens = (
        ('~=', "OP_INCLUDES"),
        ('|=', "OP_DASHMATCH"),
        ('^=', "OP_PREFIXMATCH"),
        ('$=', "OP_SUFFIXMATCH"),
        ('*=', "OP_SUBSTRINGMATCH"),
        ('=', "OP_EQUALS"),
        ('-', "OP_MINUS"),
        ('+', "OP_PLUS"),
        ('*', "OP_MUL"),
        ('/', "OP_DIV"),
        ('>', "OP_GT"),
        ('~', "OP_TILDE"),
        (',', "COMMA"),
        ('.', "DOT"),
        (':', "COLON"),
        ('!', "BANG"),
        (';', "SEMICOLON"),
        ('(', "LPAREN"),
        (')', "RPAREN"),
        ('[', "LBRACKET"),
        (']', "RBRACKET"),
        ('{', "LBRACE"),
        ('}', "RBRACE"),
    )
    simple_tokens_xlt = dict(simple_tokens)
    
    tokens += tuple([b for a, b in simple_tokens])
    
    @lex.TOKEN(
        r'|'.join([re.escape(t) for t in [a for a, b in simple_tokens]])
    )
    def t_simple_token(self, t):
        t.type = self.simple_tokens_xlt.get(t.value)
        self.create_token(t, False)
        return t
        
    
    ###########################################################################
    # errors
    ###########################################################################
    
    def t_error(self, t):
        print(u"Illegal character '%s' at Line %d, Column %d" % (
            t.value[0], 
            self.line,
            self.column,
        ))
        self.column += 1
        self.lexer.skip(1)

