**Problem**
You have infinite cards for each number between  and  (inclusive of them). Your task is to select three integers such that after sorting them in ascending order, the difference between the adjacent number is less than or equal to two. Find the number of ways to choose three numbers and print them.

Note: The order of numbers does not matter.

**Input format**

The first line contains an integer  denoting the number of test cases.
For each test case, the first and only line contains an integer .
Output format

Print  lines, one for each test case, denoting the number of ways.

**Constraints**

    1 <= T <= 20000
    1 <= N <= 200000


Sample Input

    2
    1
    3
Sample Output

    1
    10

Time Limit: 1
Memory Limit: 256

Explanation

    For N=1 there is only one way:
    (1,1,1)
    
    For  N=3
    (1,1,1)
    (2,2,2)
    (3,3,3)
    (1,2,3)
    (1,1,3)
    (1,1,2)
    (1,2,2)
    (2,2,3)
    (1,3,3)
    (2,3,3)
    These are the 10 possible ways.
