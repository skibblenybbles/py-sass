py-sass
=======

A pure Python implementation of the SASS language for extending CSS3's capabilities.

## Why?

I haven't had to write any serious parsers or compilers since college. This is mostly a fun exercise for me 
to brush up on some dusty parts of my comp sci chops. If I find enough time to finish this project, it might
serve as a nice alternative to SASS' Ruby implementation.

### State of the Project

I've built a basic CSS3 lexer and parser using
<a href="https://github.com/dabeaz/ply" target="_blank">David M. Beazley's Python port of Lex and Yacc.</a>
I've added grammar extensions to parse some of the IE-specific hacks that commonly appear in modern CSS,
i.e. `\*display: inline`, `filter:progid:Something.Awful.From.Microsoft(param = value)`, etc.

My big next steps are:
* Flesh out grammar extension IE hacks for `expression()` property values. This involves implementing a subset of 
JavaScript in CSS. Ick.
* Refactor into decent OO.
* Extend the grammar with SASS' additions. Yum.
* Build a useful abstract syntax tree from the parsed grammar.
* Implement all of SASS' awesome CSS-transformation tools.
