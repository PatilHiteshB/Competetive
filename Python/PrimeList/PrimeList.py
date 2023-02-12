from typing import Optional

"""

Definition for singly Link List Node
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

You can also use the following for printing the link list.
printList(node)
"""

def isPrime(N):
    
    if N <= 1:
        return False
    
    if N in [2, 3]:
        return True
        
    ind = 2
    while ind < N**0.5 + 1:
        if N%ind == 0:
            return False
        ind = ind+1
        
    return True

class Solution:
    
    def closestPrime(self, N):
        
        if N == 1:
            return 2
        if N == 2:
            return 3
        
        
        pos = 1
        while isPrime(N+pos) != True:
            pos += 1
            
        neg = 1
        while isPrime(N-neg) != True:
            neg += 1
            
            
        return N+pos if pos < neg else N-neg
    
    def primeList(self, head : Optional['Node']) -> Optional['Node']:
        # code here
        
        if head == None:
            return head
            
        tmp = head
        
        while tmp != None:
            if isPrime(tmp.data) == True: pass
            else: tmp.data = self.closestPrime(tmp.data)
            tmp = tmp.next
            
        return head
        

