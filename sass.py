#!/usr/bin/env python

usage = \
"""
Usage: sass.py <css file>

Temporary usage for development. More coming soon!
"""


def print_usage(exit = True):
    print usage
    if exit:
        sys.exit()


def parse(css):
    from lexer import Lexer
    from parser import SCSSParser
    return SCSSParser(Lexer).parse(css)
    

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
    
    print parse(css)

