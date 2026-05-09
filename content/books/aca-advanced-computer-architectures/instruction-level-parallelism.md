---
book_slug: aca-advanced-computer-architectures
book_title: ACA Advanced Computer Architectures
created_at: '2022-04-30T15:59:07.000000Z'
id: 138
priority: 9
slug: instruction-level-parallelism
title: Instruction level parallelism
type: page
updated_at: '2022-05-03T19:08:13.000000Z'
---

# Instruction level parallelism

## Multi-cycle pipelining
We make the following basic assumptions:
- **single-issue** processors: one instruction fetch per cycle
- **in order issue** of instructions
- **Execution stage may require multiple cycles** depending on the operation (i.e. multiply operations are longer than add/sub)
- **Memory stage might require multiple cycles** access time due to cache misses

### Commit type
If the processor is also **in order commit** of instructions then the precise exception model is preserved and WAR/WAW are avoided.

But the commit can be made **out of order**: we need to check the generation of WAR/WAW hazards.

## Multiple issue pipeline
To reach higher performance more parallelism must be used. Dependences must be solved and instructions must be re-ordered so as to achive the highest parallelism of instructions execution compatible with available resources.

In an ideal multiple-issue pipeline the ideal CPI is less than one: $CPI < 1$.

## Static and dynamic scheduling
There are two strategies to support ILP:
- **Static scheduling**: rely on compiler for identifying potential parallelism. Hazards due to data dependences stall the pipeline, no new instruction are fetched nor issued even if they are not data dependent.
- **Dynamic scheduling**: hardware locates parallelism. Hardware reorders instructions execution so as to reduce stalls, maintaining data flow and exception behaviour.

With dynamic scheduling we **allow data independent instructions behind a stall to proceed**. The hardware must rearrange dynamically the instruction execution to reduce stalls.

Dynamic scheduling implies:
- **in order issue**: instructions are fetched in program order
- Execution begins as soon as operands are aviable, possibly **out of order execution**. This will introduce **WAR and WAW hazards**.
- Out of order execution implies **out of order completion** unless there is a reorder buffer.

A problem with this approach is that we must preserve the **exception behavior** as in-order execution se the processor will ensure that no instruction can generate an exception until the processor knows that the instruction raising the exception will be executed. An exception is **imprecise** if the processor state when an exception is raised does not look exactly as if the instructions were executed in-order.

Imprecise exceptions can occur because:
- The pipeline may have already completed instructions that are later in program order than the instruction causing the exception
- The pipeline may have not yet completed some instructions that are earlier in program order than the instruction causing the exception

Generally, static scheduling techniques modify the code in a way that is
compliant only with the underlying architecture. This means that it may not be compatible or it
may have worse performance with another architecture. With dynamic scheduling, the task of
deciding which instructions to execute is done during the execution of the program and this
means that the same **code can be portable** on different dynamically scheduled processors with
comparable performance.

The main linimations of static scheduling are:
- Variable memory latency due to unpredictable cache misses
- Small amount of parallelism available within a basic block
- Code size increase and code portability