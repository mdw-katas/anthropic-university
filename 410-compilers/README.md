# CS 410 — Compiler Construction

**Prerequisites:** CS 340, CS 370
**Language:** OCaml, Go, or C — the vehicle matters less than the pipeline

## Course Description

Build a working compiler for a small language, front to back: lexing,
parsing, semantic analysis, intermediate representation, and code
generation. The capstone of the compilers-and-languages track. Few projects
teach as much per line of code — a compiler exercises data structures,
theory, architecture, and language design simultaneously.

## Learning Objectives

- Implement a lexer and a recursive-descent parser from a grammar
  (connecting CS 370's automata and grammars to running code).
- Build and traverse abstract syntax trees; implement a type checker.
- Translate an AST to an intermediate representation and generate real
  assembly (or bytecode) from it.
- Explain classic optimizations and what makes them sound.
- Read compiler output (and compiler error messages) with informed eyes for
  the rest of your career.

## Topic Outline

1. The compilation pipeline: phases and their contracts.
2. Lexical analysis: tokens, regular expressions to scanners.
3. Parsing I: grammars revisited, recursive descent, operator precedence.
4. Parsing II: LL vs. LR (survey), parser generators, error recovery.
5. Abstract syntax trees and symbol tables.
6. Semantic analysis: scope resolution and type checking.
7. Intermediate representations: three-address code, SSA (survey).
8. Runtime organization: stack frames, calling conventions, closures,
   objects.
9. Code generation: instruction selection, register allocation basics.
10. Optimization: constant folding, dead code elimination, inlining; what
    "undefined behavior" licenses.
11. Garbage collection from the implementer's side.
12. Project milestones culminating in a compiler for a small language.
