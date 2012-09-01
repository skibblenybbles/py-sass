#!/usr/bin/env python

usage = \
"""
Usage: sass.py <css file>

Temporary usage for development. More coming soon!
"""

def print_usage():
    print usage
    sys.exit()

def parse(css):
    from lexer import Lexer
    from parser import Parser
    
    print Parser(Lexer()).parse(css)
    
    """
    lexer.input(css)
    token = lexer.token()
    while token is not None:
        print token
        token = lexer.token()
    """

if __name__ == "__main__":
    import os, sys
    
    if len(sys.argv) != 2:
        print_usage()
    
    filename = sys.argv[1]
    if not os.path.exists(filename):
        print_usage()
    
    f = open(sys.argv[1], "rb")
    css = f.read().decode("utf-8")
    f.close()
    
    parse(css)

