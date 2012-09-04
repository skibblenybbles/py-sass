py-sass
=======

A pure Python implementation of SASS for an enhanced CSS3 development experience.

## Why?

I haven't had to write any serious parsers or compilers since college. This is mostly a fun exercise for me 
to brush up on some dusty parts of my comp sci chops. If I find enough time to finish this project, it might
serve as a nice alternative to SASS' Ruby implementation.

### State of the Project

I've built a basic CSS3 lexer and parser using
<a href="https://github.com/dabeaz/ply" target="_blank">PLY, David M. Beazley's Python port of Lex and Yacc.</a>
I've added grammar extensions to parse some of the IE-specific hacks that commonly appear in modern CSS,
i.e. `*display: inline`, `filter:progid:Something.Awful.From.Microsoft(param = value)`, etc.

I've found that the SCSS language is not LALR-parseable. Nested selector rulesets inside of
style declaration blocks are the culprit. For example, in this code:

<pre><code>
nav {
    font-size: 1.1em;
    a:hover {
        color: #e22;
    }
}
</code></pre>

an LALR parser cannot decide whether `a:hover` is a property declaration, like the `font-size: 1.1em` line above it,
or the start of a new selector and ruleset. This is a limitation for LALR parsers, and I would argue that modifying 
SCSS' grammar would make the language a more viable standard. I've fleshed out a basic hack to work around this
problem to meet my goal of implementing SASS' current functionality in Python, but it would be better to modify the
grammar and eliminate the need for hacks.

My big next steps are:
* Flesh out grammar extension IE hacks for `expression()` property values. This involves implementing a subset of 
JavaScript in CSS. Ick.
* <del>Refactor into decent OO.</del>
* Extend the grammar with SASS' additions. Yum.
* Build a useful abstract syntax tree from the parsed grammar.
* Implement all of SASS' awesome CSS-transformation tools.
