# Range Sum Trees

## Introduction

Segment Trees and Binary Indexed Trees are commonly used data structures to efficiently update and query sums of ranges of a array.

Both structure can achieve update and query in O(log(n)) time complexity. Original array can do update in O(1) and do query in O(n<sup>2</sup>) ;naive sum array can do update in O(n<sup>2</sup>) and do query in O(1). So Range sum trees are useful when the frequency of update and query are close.

### Segment Trees VS Binary Indexed Trees

Segment Trees are for ranges with arbitrary start index and BITs are for ranges start from index 0.


**In the implementation codes, I used bit manipulation for efficiency.**

