---
book_slug: aca-advanced-computer-architectures
book_title: ACA Advanced Computer Architectures
created_at: '2022-04-30T17:33:32.000000Z'
id: 140
priority: 10
slug: scoreboard
title: Scoreboard
type: page
updated_at: '2022-05-02T18:08:25.000000Z'
---

# Scoreboard

In the scoreboard architecture we **divide the ID stage**:
1. **Issue**: decode instructions, check for structural hazards
2. **Read operands (RR)**: wait until there are no data hazards, then read operands

Another characteristic of the scoreboard is that there are **no forwarding paths**.

Instructions executed whenever not dependent on previous instructions and there are no hazards. This implies **in-order issue** but **out-of-order read-operands**, so **out-of-order execution and completion**.

We distinguish when an instruction **begins** execution and it **completes** execution: between the two times, the instruction is **in execution**.

### Handling WAR and WAW
Since we have out of order completition there may be WAW and WAR hazards. They need to be solved:
- **Solution for WAR**: Stall write back until registers have been read and read registers only during Read Operands stage.
- **Solution for WAW**: Detect hazard and stall issue of new instruction until the other instruction completes.

### Hazard detection and resolution
Hazard detection and resolution is centralized in the scoreboard: every instruction goes through the Scoreboard, where a record of data dependences is constructed.

The Scoreboard then determines when the instruction can read its operand and begin execution. If the scoreboard decides the instruction cannot execute immediately, it monitors every change and decides when the instruction can execute.

The scoreboard controls when the instruction can write its result into destination register.

## Four Stages of Scoreboard Control
##### 1) Issue
**Decode instruction and check for structural hazards & WAW hazards**. Instructions issued in program order (for hazard checking).

If a functional unit for the instruction is free and no other active instruction has the same destination register (no WAW), the scoreboard issues the instruction to the functional unit and updates its internal data structure.

If a structural hazard or a WAW hazard exists, then the instruction issue stalls, and no further instructions will issue until these hazards are cleared.

#### 2) Read Operands
**Wait until there are no RAW hazards, then read operands. Check for structural hazards in reading RF.**

A source operand is available if:
- No earlier issued active instruction will write it; or
- A functional unit is writing its value in a register

When the source operands are available, the scoreboard tells the functional unit to proceed to read the operands from the registers and begin execution. **RAW hazards are solved dynamically in this step**. Out-of-order reading of operands then instructions are sent into execution out-of-order.

#### 3) Execution
**The functional unit begins execution upon receiving operands. When the result is ready, it notifies the
scoreboard that it has completed execution.**

#### 4) Write result
**Check for WAR hazards and finish execution**

Once the scoreboard is aware that the functional unit has completed execution, the scoreboard checks for WAR hazards.
- If none, it writes results.
- If WAR, then it stalls the completing instruction.

## Scoreboard Structure
In the scoreboard we need to save:
1. **Instruction status**
2. **Functional Unit status**:
	- Busy: Indicates whether the unit is busy or not
	- Op: The operation to perform in the unit (+,-, etc.)
	- Fi: Destination register
	- Fj, Fk: Source register numbers
	- Qj, Qk: Functional units producing source registers Fj, Fk
	- Rj, Rk: Flags indicating when Fj, Fk are ready. Flags are set to NO after operands are read.
3. **Register result status.**: Indicates which functional unit will write each register. Blank if no pending instructions will write that register.

## Optimized scoreboard
The optimized scoreboard has the check from WAW postponed to the Write-Back stage and the introduction of forwarding paths.