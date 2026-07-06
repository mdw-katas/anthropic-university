# CS 340 — Programming Languages

**Prerequisites:** CS 201
**Language:** a functional language (OCaml, Standard ML, or Racket) plus
comparative examples

## Course Description

What a programming language *is*: syntax, semantics, and the design
dimensions along which languages differ — typing, evaluation, memory
management, paradigm. Centered on a functional language precisely because it
will be unfamiliar; learning it rewires how you see the languages you already
use. Includes building a small interpreter, which is the on-ramp to CS 410.

## Learning Objectives

- Program idiomatically in a functional language: immutability, algebraic
  data types, pattern matching, recursion over loops.
- Explain static vs. dynamic and strong vs. weak typing; read and apply
  type inference informally.
- Explain evaluation strategies (eager vs. lazy) and scoping rules
  (lexical vs. dynamic).
- Implement an interpreter for a small language (parser, evaluator,
  environments).
- Compare paradigms — procedural, OO, functional, logic — as design
  tradeoffs rather than tribal identities.

## Topic Outline

1. Why study languages; a map of the design space.
2. Functional programming I: expressions, recursion, immutability, lists.
3. Functional programming II: algebraic data types and pattern matching.
4. Higher-order functions, closures, currying.
5. Type systems: static/dynamic, inference, parametric polymorphism
   (generics); what type safety buys you.
6. Scope and binding: lexical vs. dynamic scope; environments.
7. Syntax and semantics: grammars, abstract syntax trees.
8. Building an interpreter for a small language.
9. Evaluation strategies: eager, lazy, streams.
10. Memory management across languages: manual, reference counting, tracing
    GC.
11. Paradigm tour: logic programming, concurrency-oriented design; modern
    hybrids (Rust's ownership, Go's simplicity as a stance).
