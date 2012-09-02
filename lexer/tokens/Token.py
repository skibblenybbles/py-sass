###############################################################################
# Token class
#
# Tokens matched by the lexer will store a Token() instance as their values.
# Token-specific attributes will be added to the token, where appropriate,
# e.g. a HASH token will store the associated identifier in the "identifier"
# attribute.
###############################################################################

class Token(object):
    value = None
    type = None
    line = None
    column = None
    
    def __init__(self, lexer, token):
        self.value = token.value
        self.type = token.type
        self.line = lexer.line
        self.column = lexer.column
    
    def escape(self, value):
        return \
            value.replace(
                u"\n", u"\\n",
            ).replace(
                u"\r", u"\\r",
            ).replace(
                u"\t", u"\\t",
            ).replace(
                u"\f", u"\\f",
            )
    
    def __unicode__(self):
        return u"Value: \"%s\", Line: %d, Column: %d" % (
            self.escape(self.value),
            self.line,
            self.column,
        )    
    
    def __str__(self):
        return self.__unicode__().encode("ascii", "xmlcharrefreplace")

    def __repr__(self):
        return self.__unicode__()
