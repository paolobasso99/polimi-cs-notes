---
book_slug: aca-advanced-computer-architectures
book_title: ACA Advanced Computer Architectures
created_at: '2022-04-29T14:44:29.000000Z'
id: 131
priority: 1
slug: mips-architecture-and-pipeline
title: MIPS architecture and pipeline
type: page
updated_at: '2022-05-01T11:51:45.000000Z'
---

# MIPS architecture and pipeline

The MIPS processor is a **RISC (Reduced Instruction Set Computer)** which follows a **LOAD/STORE** architecture where the ALU operands come from the CPU general purposes registers and they cannot come directly from the memory: load data from the memory to the registers and store data from the registers to the memory.

## MIPS pipeline
The MIPS architecture has a 5 stages pipeline:
1. **Instruction Fetch (IF)**: Send the content of the **program counter (PC)** register to the **instruction memory** and fetch the current instruction. Then update the PC adding 4 (each instruction is 4 bytes long)
2. **Instruction Decode (ID)**: Decode the current instruction and read from the **register file** the value of the registers
3. **Execution (EX)**: The ALU operates on the operands prepared in the previous steps.
4. **Memory access (MEM)**: Load and store instructions require to access the memory.
5. **Write back (WB)**: Write to the register file.

### Optimized pipeline
Assume the register file read occurs in the second half of the clock cycle and the write in the first half.

To improve performance in case of branch hazards, we need to add more hardware resources to:
1. Compare registers to derive the Branch Outcome
2. Compute the Branch Target Address
3. Update the PC register

as soon as possible in the pipeline.

MIPS optimized processor anticipated the comparison of registers, computation of BTA and update of PC during ID stage.