#!/usr/bin/python
# -*- coding: utf-8 -*-
# {
 # Driver Code Starts
# Initial Template for Python 3

# } Driver Code Ends
# User function Template for python3

from queue import PriorityQueue


class Solution:

    def __init__(self):

        # Every index of prime stores zero or one
        # If prime[i] is zero means i is not a prime
        # If prime[i] is one means i is a prime

        self.prime = [0] * 10101

        ind = 2
        while ind < 10001:

            if self.prime[ind] == 0:

                i = ind + ind
                while i < 10001:
                    self.prime[i] = 1
                    i += ind
            ind += 1

    def shortestPath(self, num1, num2):
        if num1 > num2:
            return self.shortestPath(num2, num1)

        que = PriorityQueue()
        que.put((0, num1))

        mp = {}
        mp[num1] = 1

        while que.qsize() > 0:

            n = que.qsize()

            while n > 0:

                (lvl, temp) = que.get()

                if temp == num2:
                    return lvl

                lvl = lvl + 1

                for i in [1000, 100, 10, 1]:

                    dig = temp // i % 10

                    for j in range((1 if i == 1000 else 0), 10):

                        form = temp + (j - dig) * i

                        if form < 10000 and self.prime[form] == 0 \
                            and form not in mp.keys() and form != temp:

                            # print("{} {} {}".format(temp, form, lvl))

                            que.put((lvl, form))
                            mp[form] = 1

                n -= 1

        return -1


# {
 # Driver Code Starts.

if __name__ == '__main__':
    t = int(input())
    ob = Solution()
    for _ in range(t):
        (Num1, Num2) = map(int, input().split())
        print ob.shortestPath(Num1, Num2)

# } Driver Code Ends
