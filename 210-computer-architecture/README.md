# CS 210 — Computer Organization and Architecture

**Prerequisites:** CS 102
**Language:** C and assembly (x86-64 or RISC-V)

## Course Description

How a computer actually executes your program: from transistors and gates up
through machine code, the memory hierarchy, and the processor pipeline. This
is the "how the machine works" course — the foundation for systems
programming, operating systems, and every performance conversation you'll
ever have.

## Learning Objectives

- Represent data in binary: integers (two's complement), floating point
  (IEEE 754), characters; explain overflow and float-precision bugs from
  first principles.
- Read and write simple assembly; trace how a compiled C function uses
  registers and the stack.
- Explain the fetch-decode-execute cycle and how pipelining, branch
  prediction, and superscalar execution speed it up.
- Explain the memory hierarchy — registers, caches, RAM, disk — and predict
  cache behavior of simple code.
- Connect high-level code to its cost: why some loops are 10x faster than
  equivalent ones.

## Topic Outline

1. Digital logic: gates, combinational circuits, flip-flops, a simple ALU.
2. Data representation: bits, two's complement, IEEE 754 floating point,
   endianness.
3. Instruction set architecture: registers, instructions, addressing modes.
4. Assembly language: arithmetic, control flow, the calling convention and
   stack frames.
5. How C maps to the machine: pointers, arrays, structs in memory.
6. The processor: single-cycle datapath, pipelining, hazards, branch
   prediction.
7. The memory hierarchy: SRAM/DRAM, cache organization (lines, sets,
   associativity), locality.
8. Virtual memory preview: address translation (developed fully in CS 310).
9. I/O and buses; how devices talk to the CPU.
10. Measuring performance: latency vs. throughput, Amdahl's law.
