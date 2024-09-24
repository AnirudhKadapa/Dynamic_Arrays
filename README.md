# Dynamic_Arrays

## Theoretical Complexity Analysis:

### Space Complexity:

Initially, we start with 2 elements in each array so space complexity is: O(1)
#### Strategy A:

Now, we increase the size to 10 and once we are full, we increase the size again until we completely fill out all the elements.
Total number of increments = n/10 (Where n is the size of the array)<br />
So, we can say that the array grows linearly in terms of n/10<br />
**Space Complexity: O(n)**
#### Strategy B:
Now, we increment our array size by double once the array is full<br />
n ➔ 2n ➔ 4n ➔ 8n ➔ … <br />
until our array is filled out with all the elements. So, the array still grows in terms of n <br />
**Space Complexity: O(n)**
#### Strategy C:
Now, we increase the size of the array in terms of Fibonacci order<br />
2 ➔ 3 ➔ 5 ➔ 8 ➔ ... <br />
The array still increases Linearly<br />
**Space Complexity: O(n)**

### Time Complexity:

#### Strategy A:
Since we are doing a binary search and insertion
For binary search the time complexity is O(logk) where k is the current length of the array
And for insertion the best case possibility is O(1) and worst case is O(k) then<br />
Binary search: O(log k)
Insertion: O(k)<br />
But since we are doing n insertions the time complexity of insertion is O(n) and the length of array varies from 2 to n then time complexity of binary search can be written as O(n)<br />
Now, worst case possibility of n binary searches and n insertion is O(nlog n)<br />
**Time Complexity: O(n log n)**

#### Strategy B:
Since we are doubling the array the time complexity still depends on the length of array <br />
2 ➔ 4 ➔ 8 ➔ ... ➔ n<br />
So the time complexity at worst case will still be O(n log n) as the insertion time is O(n) and binary search time complexity is O(log n)<br />
**Time Complexity: O(n log n)**

#### Strategy C:
Since we are copying all the elements into the new array which is current length  k which varies from 2 to n.<br />
The binary search time complexity still remains: O(log k)<br />
And insertion time is still O(k)<br />
So the array grows in the order of Fibonacci numbers so it is still linear order and it grows till the array if full till n elements
So the time complexity is O(n log n)<br />
**Time Complexity: O(n log n)**<br />
“The input size in this case depends on the number of elements in the text file given.”
