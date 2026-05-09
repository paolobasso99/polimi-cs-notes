---
book_slug: aca-advanced-computer-architectures
book_title: ACA Advanced Computer Architectures
created_at: '2022-04-30T15:40:06.000000Z'
id: 137
priority: 8
slug: dependences
title: Dependences
type: page
updated_at: '2022-04-30T15:58:02.000000Z'
---

# Dependences

## Dependences
In an assembly code there may be varius dependences between instructions. The dependences are a **property of the code**, while **hazards may arise from these dependeces depending on the pipeline architecture**.

There are three types of dependences:
### 1) Data Dependencies (or True Data Dependencies)
Occurs when an instruction *j* read a registry or memory location written by a previus instruction *i* (can generate RAW).
```assembly
i: r3 <- r1 op r2
j: r4 <- r3 op r5
```
### 2) Name Dependencies
Occurs when two instructions use the same register or memory location but there is no flow of data between the instructions. Name dependencies are not true data dependencies, since there is no value being trasmitted between instructions. There are two type of name dependencies:
1. **Anti-dependences**: when the instruction *j* writes a register or memory location that a previus instruction *i* reads (can generate WAR). The instruction ordering must be perserved to ensure thath the instruction *i* reads the correct value.
```assembly
i: r3 <- r1 op r2
j: r1 <- r4 op r5
```
2. **Output dependences**: when the instructions *i* and *j* writes the same register or memory location (can generate WAW). The instruction ordering must be perserved to ensure thath the value finally written corresponds to the one written by *j*.
```assembly
i: r3 <- r1 op r2
j: r3 <- r4 op r5
```

If we change the name (register or memory location) ued in the instructions with **register renaming** the instructions would not conflict anymore. For example:
- Anti-dependences:
```assembly
i: r3 <- r1 op r2
j: r1 <- r4 op r5 => r4 <- r4 op r5
```
- Output dependences:
```assembly
i: r3 <- r1 op r2
j: r3 <- r4 op r5 => r6 <- r4 op r5 
 ```
The ranaming is easier to do if there are more registers aviable in the ISA and in can be done both statically at compile time or dynamically by the hardware.

### 3) Control Dependencies
A contro dependence determines the orderin of instructions and it is preserved by two properties:
- Instruction execution in **program order** to ensure that instructions that occurs before a branch is executed before the branch
- Detection of control hazards to ensure that an instruction (that is control-dependent on a branch) is not executed until the branch direction is known.