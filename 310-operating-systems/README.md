# CS 310 — Operating Systems

**Prerequisites:** CS 220
**Language:** C

## Course Description

The three pillars of every OS — virtualization, concurrency, and persistence.
How the kernel gives each process the illusion of its own CPU and memory, how
threads share safely (and how they fail to), and how file systems survive
crashes. This course explains the machinery your servers run on.

## Learning Objectives

- Explain how the OS virtualizes the CPU: processes, context switching,
  scheduling policies.
- Explain how the OS virtualizes memory: address translation, paging, TLBs,
  page replacement.
- Write correct concurrent code with locks, condition variables, and
  semaphores; identify races and deadlocks.
- Explain how file systems organize disks and how journaling makes them
  crash-consistent.
- Read a real kernel's design decisions critically.

## Topic Outline

1. OS overview: kernel vs. user mode, system calls, interrupts, traps.
2. Processes and context switching (revisited from the kernel's side).
3. CPU scheduling: FIFO, round robin, MLFQ, fair-share; latency vs.
   throughput tradeoffs.
4. Memory virtualization: address spaces, segmentation, paging.
5. TLBs, multi-level page tables, page faults, swapping and replacement
   policies.
6. Threads and the perils of shared state: race conditions, atomicity.
7. Locks: implementation (test-and-set, futexes), correctness, performance.
8. Condition variables, semaphores, classic concurrency problems
   (producer/consumer, readers/writers).
9. Deadlock: conditions, prevention, avoidance, detection.
10. Persistence: I/O devices, disks and SSDs, RAID.
11. File systems: inodes, directories, allocation; caching and buffering.
12. Crash consistency: fsck, journaling, log-structured file systems;
    a glance at virtualization and containers.
