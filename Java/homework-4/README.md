# Homework 4 Programming (50 pts)

Please remember that to submit the assignment you must click Mark as Complete under the Education menu in the toolbar.

Please make sure to look at the written portion of this assignment, which is available on Courseworks.

## Problem 1 - A Process Scheduling System (and the DecreaseMin operation) (20 pts) 

Assume we are building a process scheduling system for an operating system. After a process has been added to the scheduler's priority queue, we might want to adjust its priority later (for example, a system administrator might want to decrease the priority of a process started by a user -- lower priority values mean the process gets more CPU time). 

Take a look at the file ```Process.java```, which implements an (extremely simplified) process. Each process contains a unique process ID and a priority. Two Process objects are equal if they have the same process ID, even if they have a different priority. The processes are comparable by their priority. This means that two Process instances may be equal according to their process ID, but one may be greater than the other, based on their priority. Take a look at the `equals`, `hashCode`, and `compareTo` methods in `Process.java` to understand how this is implemented. 

Next, take a look at the file `BinaryHeap.java` implements a Binary Heap. In the main method, we create a number of processes and add them to a heap. 

```
heap.insert(new Process("p1",20));
heap.insert(new Process("p2",40));
heap.insert(new Process("p3",30));
heap.insert(new Process("p4",10));
```

Finally we adjust the priority for process *p2*, forcing it to run next.

```
heap.insert(new Process("p2",5)); // decrease priority for p2
```

The heap array now looks like this: 
`[null, <p2,5>, <p4,10>, <p3,30>, <p2,40>, <p1,20>]`

Even though *p2* would be the next process to be run, we would still have a second copy of *p2* left on the heap. This is not what we want. 

Your task is to modify the class *BinaryHeap* so that, when `insert` is called with an object that is *equal* to one already in the heap, the old object should be replaced with the new one, and the position in the heap array should be adjusted. "Equal" in this case means that the objects are equal according to their `equals` and `hashCode` methods. However, the two objects might behave differently with respect to their `compareTo` methods, in which case the position of the position of the new item in the heap needs to change.
 

With the modified heap, using the same sequence of inserts as above, the heap array should look like this: 
`[null, <p2,5>, <p4,10>, <p3,30>, <p1,20>, null]`

Additional instructions:
* The insert operation should still take only O(log N) time (N is the size of the heap). This means that you cannot search the heap to check if an item is already present. 
* Use a Hash Map (java.util.HashMap), to record the current heap array position for each item in the heap. If an item is already present, insert the new object in place of the old one and then adjust the position for that item. Make sure to keep the Hash Map up-to-date on each heap operation.
* Do not change the signature of the BinaryHeap class or any of its methods. You can, of course, add methods and instance variables. 
* You should be able to adjust the priority of an item in either direction (making the priority value smaller or larger).


### Problem 2 - MergeSort (30 pts)
The Merge Sort implementation discussed in class uses recursion. In this problem, you will write a non-recursive (iterative) implementation of Merge Sort. Your algorithm should start with each pair of elements in the array and then sort larger and larger subarrays bottom-up. For instance, to sort `[1,9,4,2,8,7,3,5,0]` you do the following steps:

    input: [1,9,2,4,7,8,4,5,0]
    size 2: [1,9] [2,4] [7,8] [3,5] [0]
    size 4: [1,2,4,9] [3,5,7,8] [0]
    size 8: [1,2,3,4,5,7,8,9] [0]
    final: [0,1,2,3,4,5,7,8,9]

Note how these steps are different from the recursive merge sort.

You can use O(N) space (in addition to the input array) and your algorithm should have the same running time as recursive merge sort. Write the method `void mergeSort(Integer[] inputArray)` in the class `MergeSort` that sorts the array `inputArray` in place. You can use the the provided original merge method.  Finally, write a main method that creates at least two unsorted arrays (you can hardcode them), runs them through your merge sort algorithm and then prints the array back out. Make sure your method works for test cases where the input size is not a power of 2 (like in the example).