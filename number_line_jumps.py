'''
You are choreographing a circus show with various animals. For one act, you are given two kangaroos on a number line ready to jump in the positive direction (i.e, toward positive infinity).

The first kangaroo starts at location x1 and moves at a rate of v1 meters per jump.
The second kangaroo starts at location x2 and moves at a rate of v2 meters per jump.
You have to figure out a way to get both kangaroos at the same location at the same time as part of the show. If it is possible, return YES, otherwise return NO.

Example:
    x1 = 2
    v1 = 1
    x2 = 1
    v2 = 2
    After one jump, they are both at x = 3, (x1+v1=2+1,x2+v2=1+2 ), so the answer is YES.

Function Description

Complete the function kangaroo in the editor below.

kangaroo has the following parameter(s):

int x1, int v1: starting position and jump distance for kangaroo 1
int x2, int v2: starting position and jump distance for kangaroo 2
'''

x1, v1, x2, v2 = map(int, raw_input().split())
X = [x1, v1]
Y = [x2, v2]
back = min(X, Y)
fwd = max(X, Y)
dist = fwd[0] - back[0]

while back[0] < fwd[0]:
    back[0] += back[1]
    fwd[0] += fwd[1]
    if fwd[0] - back[0] >= dist:
        break

print ["NO", "YES"][back[0] == fwd[0]]

