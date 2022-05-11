# BinomialAlgorithmComparisons
This project compares the effectiveness of different algorithm strategies; recursive, dynamic programming, and memoization using the binomial equation. By generating a random list of tuples to put into the binomial equation, and running each list through each type of binomial problem, I was able to construct a graph that shows the time it took to solve each equation attempt.

Below is the attempt to graph all of this data using the results of all three algorithms. The x axis is the specific problem id number, ranging from 1-500 in which each algorithm was given the same two numbers and asked to find a solution. The y axis is the number of seconds it took for the given problem to be solved. 

![Initial Comparison](https://github.com/jk1834/BinomialAlgorithmComparisons/blob/main/captures/binomialcapture1.jpg)

As you can see, the green dots overwhelm the graph completely. This is because the green dots are representative of the basic recursion algorithm. With those removed, it becomes clearer that the other two approaches are much faster.

![Culled Comparison](https://github.com/jk1834/BinomialAlgorithmComparisons/blob/main/captures/binomialcapture2.jpg)

While this shows how the comparison is more even when dealing with the dynamic programming approach and the memoization approach, 500 data points is a lot to comprehend, and the graph still looks a little muddy. To remedy this, the following results were put into a table, shows here.

![Table Comparison](https://github.com/jk1834/BinomialAlgorithmComparisons/blob/main/captures/binomialtable.jpg)

As you can see, the dynamic programming approach is much faster than the memoization approach, on average. For more details in the code I used, and a more detailed report, refer to the BinomialReport.pdf and binomial.py files. All of the resulting data was pushed into BinomialData.xls.
