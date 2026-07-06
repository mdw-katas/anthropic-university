# CS 220 — Systems Programming in C and Unix

**Prerequisites:** CS 210
**Language:** C

## Course Description

Programming close to the operating system: manual memory management, file
descriptors, processes, signals, and the Unix toolset. C is the vehicle
because it hides nothing — every pointer bug is a lesson in how memory
actually works. This course is the bridge between architecture (CS 210) and
operating systems (CS 310).

## Learning Objectives

- Write correct C: pointers, arrays, strings, structs, dynamic allocation,
  and the discipline to avoid leaks and undefined behavior.
- Use the Unix system-call interface: open/read/write/close, fork/exec/wait,
  pipes, signals.
- Explain the layout of a process in memory: text, data, heap, stack.
- Build and debug with the standard toolchain: compiler stages, make, gdb,
  valgrind/sanitizers.
- Implement a nontrivial systems artifact (e.g., a small shell or a malloc)
  from scratch.

## Topic Outline

1. C fundamentals: types, operators, control flow, functions, compilation
   model (preprocessor, compiler, linker).
2. Pointers and arrays; pointer arithmetic; strings in C.
3. Dynamic memory: malloc/free, ownership discipline, common heap bugs.
4. Structs, unions, and building data structures in C.
5. The process address space; how the stack and heap actually behave.
6. Undefined behavior: what it is, why compilers exploit it, how to avoid it.
7. Files and file descriptors; buffered vs. unbuffered I/O.
8. Processes: fork, exec, wait; environment; exit codes.
9. Pipes, redirection, and signals; writing a small Unix shell.
10. Tooling: make, gdb, AddressSanitizer/valgrind, profiling basics.
