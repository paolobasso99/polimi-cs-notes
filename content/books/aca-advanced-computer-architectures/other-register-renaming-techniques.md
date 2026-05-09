---
book_slug: aca-advanced-computer-architectures
book_title: ACA Advanced Computer Architectures
created_at: '2022-04-30T21:08:10.000000Z'
id: 142
priority: 12
slug: other-register-renaming-techniques
title: Other register renaming techniques
type: page
updated_at: '2022-05-03T12:58:23.000000Z'
---

# Other register renaming techniques

Tomasulo implements an **implicit register renaming**: the code is not changed and there is **dynamic loop unrolling**.

But there are other possible techniques for register renaming

## Compiler transformation: loop unrolling
The compiler unrolls a loop *n* number of times, where *n* is called **unrolling factor** and then procedes to rename the registers to avoid WAR and WAW hazards. Other optimizations are also possible.

Loop unrolling also decrease the instruction counts. For example, consider the code:
```assembly
LOOP: LD $FP0, 0 ($R1)
      LD $FP2, 0 ($R2)
      SUBD $FP4, $FP0, $FP2
      SD $FP4, 0 ($R1)
      ADDDUI $R1, $R1, 4
      ADDDUI $R2, $R2, 4
      BNE $R1, $R3, LOOP
```
If we use loop unrolling with factor 4:
```assembly
LOOP: LD $FP0, 0 ($R1) # iter 1
      LD $FP2, 0 ($R2)
      SUBD $FP4, $FP0, $FP2
      SD $FP4, 0 ($R1)
      LD $FP0, 0 ($R1) # iter 2
      LD $FP2, 0 ($R2)
      SUBD $FP4, $FP0, $FP2
      SD $FP4, 0 ($R1)
      ... # iter 3 and 4
      ADDDUI $R1, $R1, 16
      ADDDUI $R2, $R2, 16
      BNE $R1, $R3, LOOP
```
We have (4\*4)+3=19 instructions instead of 7\*4=28, this corresponds to a 32% decrease of the instruction count.

## Explicit register renaming
Using **physical register file that is larger than number of registers specified by the ISA** we allocate a new physical destination register for every instruction that writes a result.

Physical Registers are not exposed to the compiler because not specified by the ISA.

A **translation table** must keep track of which ISA register is located to which physical register.

This technique has some advantages:
1. Decouples the concept of renaming from scheduling: the pipeline can be whatever (MIPS, Tomasulo, Scoreboard, ...)
2. Allows data to be fetched from single register file: no need of reorder buffer.