# Time & space complexity comparison of the solutions to music library project

## **Initial data structures used**

| Data Structure   | Array (List) | Hash Table (Dictionary) | Pandas Dataframe |
| --------------   | :----------: | :---------------------: | :--------------: |
| Space complexity | O(n)         | O(n)                    | O(n)             | 
| Access (by index)| O(1)         | N/A                     | O(n)*            |
| Search           | O(n)         | O(1)                    | O(n)             |


* The index is lazily initialized and built (in O(n) time) the first time you try to access a row using that index. 
  So accessing a row for the first time using that index takes O(n) time.
All subsequent row access takes constant time ( O(1) ).
  

### Time complexity of solutions used in project 



