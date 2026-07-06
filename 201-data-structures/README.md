# CS 201 — Data Structures

**Prerequisites:** CS 102, MATH 120
**Language:** Python (with implementation-from-scratch emphasis)

## Course Description

The canonical data structures, implemented by hand: dynamic arrays, linked
lists, stacks, queues, hash tables, trees, heaps, and graphs. Every structure
is analyzed with big-O notation, and choosing the right structure for a
workload is the recurring exam question — in this course and in the rest of
your career.

## Learning Objectives

- Analyze time and space complexity with big-O, big-Ω, and big-Θ, including
  amortized analysis.
- Implement each core structure from scratch and explain its invariants.
- Choose structures based on workload: access patterns, mutation patterns,
  memory behavior.
- Understand how hash tables actually work: hash functions, collision
  strategies, resizing, and their failure modes.
- Understand tree balance: why it matters, and how BSTs, AVL or red-black
  trees, and B-trees maintain it.

## Topic Outline

1. Complexity analysis: big-O/Ω/Θ, best/worst/average case, amortized cost.
2. Arrays and dynamic arrays; the amortized analysis of append.
3. Linked lists (singly, doubly); stacks and queues.
4. Hash tables: hash functions, chaining vs. open addressing, load factor
   and resizing.
5. Binary trees and binary search trees; traversals.
6. Balanced trees: AVL and/or red-black; B-trees and why databases love
   them.
7. Priority queues and binary heaps; heapsort.
8. Graphs: representations (adjacency list/matrix), BFS, DFS.
9. Sorting survey: insertion, merge, quick; lower bounds for
   comparison-based sorting.
10. Choosing data structures: case studies from real systems (caches,
    indexes, schedulers).
