---
book_slug: aca-advanced-computer-architectures
book_title: ACA Advanced Computer Architectures
created_at: '2022-04-29T15:22:26.000000Z'
id: 134
priority: 3
slug: exception-handling
title: Exception handling
type: page
updated_at: '2022-05-01T11:51:45.000000Z'
---

# Exception handling

The following type of exceptions, interrupts and faults are considered:
- I/O device request;
- Invoking OS system call from a user program;
- Tracing instruction execution;
- Integer arithmetic overflow/underflow;
- Floating point arithmetic anomaly;
- Page fault;
- Misaligned memory access;
- Memory protection violation;
- Hardware / power failure.

**Interrupt**: an event that requires the attention of the processor. It can be **asynchronous** if it is an external event or **synchronous** if it is internal (exceptions).

### Classes of exceptions
- **Synchronous vs asynchronous**: asynchronous events are caused by devices external to the CPU and memory and can be handled after the completion of the current instruction (easier to handle)
- **User requested vs coerced**: user requested (such as I/O events) are predictable while coerced are caused by some HW event not under control of the user program; hard to implement because they are unpredictable.
- **User maskable vs user nonmaskable**: The mask simply controls whether the HW responds to the exception or not
- **Within vs between instructions**: Exceptions that occur within instructions are usually synchronous since the instruction triggers the exception. The instruction must be stopped and restarted. Asynchronous that occur between instructions arise from catastrophic situations such as HW malfunctions and always cause program termination.
- **Resume vs terminate**: whether the program’s execution continues after the interrupt/exception

#### Handling asynchronous interrupts
When the processor decides to process the interrupt:
- It stops the current program at instruction *i*, completing all the instructions up to *i‐1* (precise interrupt)
- It saves the PC of instruction *i* in a special register Exception Program Counter: **PC ‐> EPC**
- It disables interrupts and transfers control to a designated interrupt handler running in the kernel mode: **Int. Vector Address ‐> PC**

To allow nested interrupts, we need to save PC before enabling interrupts.

#### Handling synchronous interrupts
In general, the instruction *i* cannot be completed and needs to be restarted after the exception has been handled. In the pipeline this would require undoing the effect of one or more partially executed instructions.

### Exception handling in the MIPS pipeline
Exceptions may occur at different stages in pipeline so the exception may be raised **out of order**. A way to keep the order of exceptions is to hold exception flags in pipeline until commit point so raise all exceptions in the MEM stage.