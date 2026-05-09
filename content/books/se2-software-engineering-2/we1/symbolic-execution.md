---
book_slug: se2-software-engineering-2
book_title: SE2 - Software Engineering 2
chapter_slug: we1
chapter_title: WE1
created_at: '2022-02-04T16:44:18.000000Z'
id: 100
priority: 2
slug: symbolic-execution
title: Symbolic Execution
type: page
updated_at: '2022-02-06T14:59:58.000000Z'
---

# Symbolic Execution

A **Symbolic state** is made by the tuple: **<path-condition, symbolic bindings>**.

A simple example of a symbolic execution:
```c
read(a); read(b);
x = a + b;
write(x);
```
We assign `A` to `a` and `B` to `b`, the printed result will be: `A+B`.

When we have more than one path the execution is *performed on a single specific path*.
For example for the code:
```c
read (y, a);
x = y + 2;
if x > a
  a = a + 2;
else
  y = x + 3;
x = x + a + y;
```
And the execution path `<1, 2, 3, 5, 6, 7>` which is the used path if `Y + 2 ≤ A` we get the following execution result: `{a=A, y=Y+5, x=2Y+A+7}`.

### Find the path conditions example
Using symbolic execution, identify the path condition that allows the
program to follow the path 1 2 3 4 5 8 9 2 3 4 6 7 8 9 2 10 11:
```c
0  int foo() {
1    x = input();
2    while (x > 0) {
3        y = 2 * x;
4      if (x > 10)
5        y = x - 1;
6      else
7        x = x + 2;
8      x = x - 1;
9    }
10   x = x - 1;
11   return x;
12 }
```
Then:
| Step | Definitions           | Path Conditions               |
| ---- | --------------------- | ----------------------------- |
| 1    | x=X                   |                               |
| 2    |                       |                               |
| 3    | y=2X                  | X>0                           |
| 4    |                       |                               |
| 5    | y=X-1                 | X>0, X>10                     |
| 8    | x=X-1                 |                               |
| 9    |                       |                               |
| 2    |                       | X>0, X>10, X-1>0              |
| 3    | y=2(X-1)              |                               |
| 4    |                       |                               |
| 6    |                       | X>0, X>10, X>1, X-1<=10       |
| 7    | x = X - 1 + 2 = X + 1 |                               |
| 8    | x = X + 1 - 1 = X     |                               |
| 9    |                       |                               |
| 2    |                       |                               |
| 10   | x = X - 1             | X>0, X>10, X>1, X-1<=10, X<=0 |
| 11   |                       |                               |

The path condition for the given path is then
`X>10` and `X<=11` and `X<=0`. This is clearly an **inconsistent condition**, the given path is impossible.

## Past exam exercises
### 2021 06 24 Q2 (5 points) Even/Odd
```c
0 int funct(int x, int y)
1     if(x > 0 && y > 0) {
2         if (y % 2 == 0)
3             return -1;
4         while (x*y % 2 == 0)
5             x = x / 2;
6         while ((x+y) % 2 == 0)
7             x = x - 1;
8     }
9 return x+y;
```
#### Point 1: Find path conditions
Symbolically execute the program covering the following paths, highlighting the path condition
associated with each path:
1. 0, 1, 2, 4, 5, 4, 5, 4, 6, 7, 6, 7, 6, 8, 9
2. 0, 1, 2, 4, 6, 8, 9

**SOLUTION**

The execution of the first path:

| Step | Definitions | Path Conditions                                              |
| ---- | ----------- | ------------------------------------------------------------ |
| 0    | x=X, y=Y    |                                                              |
| 1    |             |                                                              |
| 2    |             | X>0, Y>0                                                     |
| 4    |             | X>0, Y>0, Y odd                                              |
| 5    | x=X/2       | X>0, Y>0, Y odd, X even                                      |
| 4    |             |                                                              |
| 5    | x=X/4       | X>0, Y>0, Y odd, X even, X/2 even                            |
| 4    |             |                                                              |
| 6    |             | X>0, Y>0, Y odd, X even, X/2 even, X/4 odd                   |
| 7    | x=X/4 - 1   | X>0, Y>0, Y odd, X even, X/2 even, X/4 odd, Y+X/4 even       |
| 6    |             |                                                              |
| 7    | x=X/4 - 2   | X>0, Y>0, Y odd, X even, X/2 even, X/4 odd, Y+X/4 even, Y+X/4 -1 even |
| 6    |             |                                                              |
| 8    |             | X>0, Y>0, Y odd, X even, X/2 even, X/4 odd, Y+X/4 even, Y+X/4 -1 even, Y+X/4-2 odd |
| 9    |             |                                                              |

The path is taken if `X>0, Y>0, Y odd, X even, X/2 even, X/4 odd, Y+X/4 even, Y+X/4 -1 even, Y+X/4-2 odd` which is **impossible** because if both X and Y are greater than 0 than `Y+X/4` and `Y+X/4 -1` cannot be even at the same time.

The execution of the second path:
| Step | Definitions | Path Conditions                  |
| ---- | ----------- | -------------------------------- |
| 0    | x=X, y=Y    |                                  |
| 1    |             |                                  |
| 2    |             | X>0, Y>0                         |
| 4    |             | X>0, Y>0, Y  odd                 |
| 6    |             | X>0, Y>0, Y  odd, X odd          |
| 8    |             | X>0, Y>0, Y  odd, X odd, X+Y odd |
| 9    |             |                                  |

The path is taken if `X>0, Y>0, Y  odd, X odd, X+Y odd` which is **impossible** because if X and Y are both odd positive number then X+Y is even

#### Point 2: All instructions reachable?
Are all instructions in the code reachable through some path, even one not listed in the text, or not?
Motivate your answer.

**SOLUTION**

Even thought the two described paths are not feasible all instructions are reachable: based on the analysis of path 0, 1, 2, 4, 5, 4, 5, 4, 6, 7, 6, 7, 6, 8, 9, which
is unfeasible, we can conclude, instead, that it is possible to jump out of the second loop following the
path: 0, 1, 2, 4, 5, 4, 5, 4, 6, 7, 6, 8, 9. This one allows all instructions except the one at line 3 to be
covered. In turn, instruction 3 can be covered by path 0, 1, 2, 3, for which it is enough that x and y are
both positive, and y is even.

### 2021 01 13 Q2 (3 points) Mixed def-use and symbolic execution
```c
0  int func (int x) {
1      int k, i, y;
2      int res = 0;
3      if (x < 1)
4          return res;
5      if (x % 2 != 0)
6          return res;
7      y = x;
8      i = 0;
9      while (i <= 10 && y % 4 != 0)
10         y = y*y;
11         i = i + 1;
12     }
13     if (i > 5)
14 	       res = k;
15     else
16         res = res + 1;
17     return res;
```

#### Point A: identify pairs and highlight unusual
Identify the def-use pairs for program func and say whether they highlight anything unusual.

**SOLUTION**

| Variable | Def-Use pairs |
| - | - |
| x | <0,3>, <0,5>, <0,7> |
| k | <\?,14> |
| i | <8,9>, <8,11>, <8,13><br><11, 9>, <11, 11>, <11, 13> |
| y | <7, 9>, <7, 10><br><10, 9>, <10,10> |
| res | <2,4>, <2,6>, <2,16>, <14,17>, <16,17> |

Variable k is used in line 14 but it is never initialized.

#### Point B: symbolic execution
Use symbolic execution to determine the feasibility (and, in case, the path condition) of the following path: 0, 1, 2, 3, 5, 7, 8, 9, 10, 11, 12, 9, 10, 11, 12, 9, 13, 15, 16, 17

**SOLUTION**

| Step | Definitions | Path Conditions                                              |
| ---- | ----------- | ------------------------------------------------------------ |
| 0    | x=X         |                                                              |
| 1    |             |                                                              |
| 2    | res=0       |                                                              |
| 3    |             |                                                              |
| 5    | X=2K        | X >= 1                                                       |
| 7    | y=X         | X >= 1                                                       |
| 8    | i=0         |                                                              |
| 9    |             |                                                              |
| 10   |             | X >= 1, X not divisible by 4 (not exists P s.t. 2K = 4P)     |
| 11   | y=X^2=4K^2  |                                                              |
| 12   | i = 1       |                                                              |
| 9    |             |                                                              |
| 10   |             | X >= 1, X not divisible by 4, X^2 not divisible by 4 (not exists P s.t. 4\*K\*K = 4P)  |

The last condition is not feasible, since it is enough to consider `K*K = P` to violate the condition. The path is not feasible.

#### Point C: mix def-use and symbolic execution
For any possibly erroneous situation highlighted by the def-use analysis, use symbolic execution to argue whether or not the problem can indeed manifest itself.

**SOLUTION**

We saw that variable k is used in line 14 but it is never initialized. This situation is impossible to occur since the loop can get executed at most 1 time and for this reason `i<=5` so the path is not taken.

### 2021 09 03 Q3 (4 points) Enter in the loop at most once
Consider the following function:
```c
0  int proc (int x, int y) {
1      int n;
2      if (x == y)
3          return 1;
4      else {
5          if (x > y) {
6              y = x*2;
7              n = 0;
8          }
9          else n=1;
10         while (x<y) {
11             n = n + 1;
12             x = x +2;
13         }
14 	       return n; }
15 }
```
Considering positive values for variables x and y, answer to the following question: identify the paths in the program that **enter in the loop at most once per path**. Derive the path conditions corresponding to the execution of all the identified paths showing how to get to the result you propose.

**SOLUTION**

The paths that enter the loop zero times are:
1. 0 1 2 3
2. 0 1 2 3 4 5 **6 7 8** 10 13 14
3. 0 1 2 3 4 5 **9** 10 13 14

There are two paths that enter the loop one time:
1. 0 1 2 3 4 5 **6 7 8** 10 11 12 13 10 14
2. 0 1 2 3 4 5 **9** 10 11 12 13 10 14

**0 1 2 3**
|Step|Definitions and conditions|
|-|-|
|0| x=X, y=Y|
|1| |
|2| X==Y|
|3| X==Y|

Path condition is `X==Y`

**0 1 2 3 4 5 6 7 8 10 13 14**
|Step|Definitions and conditions|
|-|-|
|0| x=X, y=Y|
|1| |
|2| X!=Y|
|3|| 
|4|| 
|5| X>Y|
|6| y=2X|
|7| n=0|
|8||
|10| X>=2X|
|14|

Path is not possible because for positive values `X>=2X` is never satisfied.

**0 1 2 3 4 5 9 10 13 14**
|Step|Definitions and conditions|
|-|-|
|0| x=X, y=Y|
|1 ||
|2| X!=Y|
|3|| 
|4|| 
|5| X<=Y|
|9| n=1|
|10| X>=Y This implies that X==Y which is a contradiction to X!=Y so the path is impossible.|

**0 1 2 3 4 5 6 7 8 10 11 12 13 10 14**
|Step|Definitions and conditions|
|-|-|
|0| x=X, y=Y|
|1||
|2| X!=Y|
|3|| 
|4|| 
|5| X>Y|
|6| y=2X|
|7| n=0|
|8| |
|10| X<2X|
|11| n=1|
|12| x=X+2|
|13||
|10| X+2 >= 2\*X (possible if X<=2)|
|14|| 

This path is possible and it is taken if `X>Y` (we are considering only positive x and y) and `X<=2`.

**0 1 2 3 4 5 9 10 11 12 13 10 14**
|Step|Definitions and conditions|
|-|-|
|0| x=X, y=Y|
|1| |
|2| X!=Y|
|3| |
|4| |
|5| X<=Y|
|9| n=1|
|10| X\<Y|
|11| n=2|
|12| x=X+2|
|13| |
|10| X+2 >= Y|
|14|| 

This path is possible and it is taken if `Y-2 <= X < Y`.

### 2020 06 17 Q2.b (3 points)
```c
0  mycode (int S[], int Slength) {
1      int h, x, p, res = 0;
2      if (S == null)
3          return 23;
4      x = Slength;
5      if (x == 0)
6          return -5;
7      h = 0;
8      while (h < Slength) {
9          p = S[h] - S[x-(h+1)];
10         if (p != 0)
11             return 14;
12         h = h + 1;
13     }
14 	   return -5; }
```

For each of the following paths: symbolically execute the program covering it, highlight the path condition associated with it, and define a test case that realises the path.
1. 0, 1, 2, 4, 5, 7, 8, 9, 10, 12, 13, 8, 14
2. 0, 1, 2, 4, 5, 7, 8, 9, 10, 12, 13, 8, 9, 10, 12, 13, 8, 14

**SOLUTION**

**0, 1, 2, 4, 5, 7, 8, 9, 10, 12, 13, 8, 14**
|Step|Definitions and conditions|
|-|-|
|0|s=S, Slength=SLENGTH|
|1|res=0|
|2|S != null|
|4|x=SLENGTH|
|5|SLENGTH != 0|
|7|h=0|
|8|SLENGTH > 0|
|9|p=S\[0\]-S\[SLENGTH-1\]|
|10|S\[0\] == S\[SLENGTH-1\]|
|12|h=1|
|13||
|8|SLENGTH <= 1|
|14||

This path is taken if `S != null`, `SLENGTH = 1`. A test case could be `mycode([5], 1)`.

**0, 1, 2, 4, 5, 7, 8, 9, 10, 12, 13, 8, 9, 10, 12, 13, 8, 14**
|Step|Definitions and conditions|
|-|-|
|0|s=S, Slength=SLENGTH|
|1|res=0|
|2|S != null|
|4|x=SLENGTH|
|5|SLENGTH != 0|
|7|h=0|
|8|SLENGTH > 0|
|9|p=S\[0\]-S\[SLENGTH-1\]|
|10|S\[0\] == S\[SLENGTH-1\]|
|12|h=1|
|13||
|8|SLENGTH > 1|
|9|p=S\[1\]-S\[SLENGTH-2\]|
|10|S\[1\] == S\[SLENGTH-2\]|
|12|h=2|
|13||
|8|SLENGTH <= 2|
|14||

This path is taken if `S != null`, `SLENGTH = 2` and `S[0] == S[1]`. A test case could be `mycode([5,5], 1)`.