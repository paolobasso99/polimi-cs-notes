---
book_slug: smbud-systems-and-methods-for-big-and-unstructured-data
book_title: SMBUD - Systems and Methods for Big and Unstructured Data
chapter_slug: 11-hadoop
chapter_title: 11 Hadoop
created_at: '2021-12-31T14:36:21.000000Z'
id: 65
priority: 5
slug: hadoop-key-components
title: Hadoop key components
type: page
updated_at: '2022-01-01T12:59:30.000000Z'
---

# Hadoop key components

## Input Splitter
Is responsible for splitting your input into multiple
chunks (default is 64MB). These chunks are then used as input for your mappers
Splits on logical boundaries.

Typically, you can just use one of the built in splitters,
unless you are reading in a specially formatted file.

## Mapper
Reads in input pair <K,V> (a section as split by the input splitter)
Outputs a pair <K’, V’>

## Reducer
Accepts the Mapper output, and collects values on the key. All inputs with the same key must go to the same reducer!

Input is typically sorted, output is output exactly as is

## Partitioner (Shuffler)
Decides which pairs are sent to which reducer
Default is simply:
`Key.hashCode() % numOfReducers`

Custom partitioning is often required.

Important to choose well-balanced
partitioning functions.
If not, reduce tasks may delay completion time

## Combiner
An optional intermediate reducer.
Reduces output from each mapper,
reducing bandwidth and sorting.

Cannot change the type of its input and input types must be the same as output types.

## Output Committer
Is responsible for taking the reduce output,
and committing it to a file.

Typically, this committer needs a
corresponding input splitter (so that another
job can read the input).

Again, usually built-in committers are good
enough, unless you need to output a special
kind of file

## Master
Responsible for scheduling & managing jobs (handled by the framework, no user code is necessary).

If a task fails to report progress (such as reading input, writing
output, etc), crashes, the machine goes down, etc, it is assumed to
be stuck, and is killed, and the step is re-launched (with the same
input)