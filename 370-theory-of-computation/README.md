# CS 370 — Theory of Computation

**Prerequisites:** MATH 120

## Course Description

The mathematical limits of computation: what machines can compute, what they
can't, and how hard the computable problems are. Finite automata, regular
and context-free languages, Turing machines, undecidability, and complexity
theory. This is where regular expressions, parsers, and the halting problem
get their rigorous foundations — and it feeds directly into CS 410.

## Learning Objectives

- Design finite automata (DFA/NFA) and regular expressions; prove languages
  regular or not (pumping lemma).
- Design context-free grammars and pushdown automata; understand why
  programming-language syntax lives here.
- Explain the Turing machine model and the Church-Turing thesis.
- Prove problems undecidable via the halting problem and reductions.
- Explain complexity classes P and NP, NP-completeness, and what the open
  P vs. NP question would mean either way.

## Topic Outline

1. Alphabets, strings, and languages; what a "problem" is, formally.
2. Deterministic finite automata; nondeterminism and NFA-to-DFA
   conversion.
3. Regular expressions and their equivalence to finite automata; what
   real-world "regex" adds beyond regularity.
4. Proving non-regularity: the pumping lemma; closure properties.
5. Context-free grammars: derivations, parse trees, ambiguity.
6. Pushdown automata; the limits of context-free languages.
7. Turing machines: the model, variants, and the Church-Turing thesis.
8. Decidability; the halting problem; proof by diagonalization.
9. Reductions: proving new problems undecidable; Rice's theorem (survey).
10. Complexity: time classes, P and NP, NP-completeness (Cook-Levin,
    reductions), and the frontier beyond.
