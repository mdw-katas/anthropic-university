# CS 420 — Distributed Systems

**Prerequisites:** CS 310, CS 320
**Language:** Go (the lingua franca of the field's lab work)

## Course Description

What happens when the answer must come from more than one machine:
partial failure, unreliable networks, replication, and consensus. The
theory (time, ordering, CAP, consistency models) and the practice
(building replicated, fault-tolerant services). Directly relevant to
professional backend work — this course explains the systems you already
operate.

## Learning Objectives

- Reason about partial failure: what can and cannot be known when a
  message goes unanswered.
- Explain logical time (Lamport clocks, vector clocks) and why "what
  happened first" is a hard question.
- Define consistency models precisely: linearizability, sequential and
  causal consistency, eventual consistency.
- Explain and implement consensus (Raft) and understand what Paxos-family
  protocols guarantee.
- Design replicated, partitioned systems and articulate their failure
  modes and tradeoffs (CAP, quorums).

## Topic Outline

1. Why distribution is different: partial failure, the two generals, the
   eight fallacies.
2. RPC and the illusion of local calls; exactly-once as a lie and
   idempotency as the truth.
3. Time and ordering: physical clocks, Lamport clocks, vector clocks.
4. Replication: primary-backup, chain replication, quorums.
5. Consistency models: linearizability through eventual consistency;
   CAP and PACELC.
6. Consensus I: the problem, FLP impossibility (survey).
7. Consensus II: Raft in depth; Paxos family (survey).
8. Replicated state machines; leases and leader election.
9. Partitioning/sharding; consistent hashing; rebalancing.
10. Distributed transactions: two-phase commit and its discontents;
    sagas.
11. Case studies: GFS/Spanner-style designs, Dynamo-style designs,
    Kafka-style logs.
12. Testing distributed systems: fault injection, Jepsen-style analysis.
