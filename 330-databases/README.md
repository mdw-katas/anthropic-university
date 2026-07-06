# CS 330 — Database Systems

**Prerequisites:** CS 201
**Language:** SQL; projects in your language of choice

## Course Description

Both sides of the database: using one well (data modeling, SQL, transactions)
and how one is built (storage engines, indexes, query processing, recovery).
The internals half is what separates this course from professional
experience — it explains *why* the database behaves the way it does.

## Learning Objectives

- Design relational schemas from requirements: ER modeling, normalization,
  and when to denormalize.
- Write sophisticated SQL: joins, aggregation, subqueries, window functions.
- Explain transactions precisely: ACID, isolation levels and their
  anomalies, locking vs. MVCC.
- Explain how B-tree indexes work and reason about query plans.
- Explain crash recovery (write-ahead logging) and the tradeoffs of NoSQL
  designs.

## Topic Outline

1. The relational model: relations, keys, integrity constraints.
2. SQL: queries, joins, aggregation, subqueries, window functions, DDL.
3. Data modeling: ER diagrams, translating models to schemas.
4. Normalization: functional dependencies, normal forms, and pragmatic
   denormalization.
5. Storage: pages, heap files, row vs. column layout.
6. Indexing: B+-trees in depth; hash indexes; covering indexes.
7. Query processing: join algorithms (nested loop, hash, merge), the
   optimizer, reading query plans.
8. Transactions: ACID, serializability, isolation levels and their
   anomalies (dirty/non-repeatable/phantom reads).
9. Concurrency control: two-phase locking, MVCC; deadlocks.
10. Recovery: write-ahead logging, checkpoints, ARIES concepts.
11. Beyond relational: key-value, document, and column stores; when the
    relational model is the wrong fit.
