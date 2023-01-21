#User function Template for python3

def getParent(n):
    
    if n&1 == 1:
        return n//2
    return n//2 - 1
    # 2*i+1 and 2*i+2

'''
heap = [0 for i in range(101)]  # our heap to be used
'''
#Function to insert a value in Heap.
def insertKey (x):
    
    
    global curr_size
    
    heap[curr_size] = x
    
    # print("Curr_size : ")
    # print(curr_size, end=" ")
    
    child = curr_size
    parent = getParent(curr_size)
    
    while parent >= 0:
        
        # print("Parent : {}".format(parent))
        
        if heap[parent] > heap[child]:
            
            heap[parent], heap[child] = heap[child], heap[parent]
            
        else:
             
            break
        
        child = parent
        parent = getParent(parent)
        
    curr_size += 1
    
    # print(heap)
        
    

#Function to delete a key at ith index.
def deleteKey (i):
    # print(heap)
    global curr_size
    
    if i >= curr_size:
        return -1
    
    
    heap[i], heap[curr_size-1] = heap[curr_size-1], heap[i]
    
    
    heap[curr_size-1] = 0
    curr_size -= 1
    
    # print("After swap : {}".format(heap))
    
    parent = i
    smallest = i
    
    while True:
        
        # print("Parent : {}".format(parent))
        
        l, r = 2*parent+1, 2*parent+2
        
        if l < curr_size and heap[smallest] > heap[l]: 
            smallest = l
            
        if r < curr_size and heap[smallest] > heap[r]: 
            smallest = r
            
        if smallest != parent:
            heap[smallest], heap[parent] = heap[parent], heap[smallest]
        else:
            break
        
        parent = smallest
        
    # print(heap)
            

#Function to extract minimum value in heap and then to store 
#next minimum value at first index.
def extractMin ():
    if curr_size == 0:
        return -1
        
    temp = heap[0]
    deleteKey(0)
    return temp



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

# Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

heap = []  # our heap to be used
curr_size = 0  # current size of heap

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int, input().strip().split()))
        # initialize every globals
        curr_size = 0
        heap = [0 for i in range(n)]
        i = 0
        while i < len(a):
            if a[i] == 1:
                insertKey(a[i + 1])
                i += 1
            elif a[i] == 2:
                deleteKey(a[i + 1])
                i += 1
            else:
                print(extractMin (), end=" ")
            i += 1
        # reinitialize every globals
        # curr_size = 0
        # heap = [0 for i in range(101)]
        print()
# } Driver Code Ends