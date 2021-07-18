# GridWorld

Implement the GridWorld as describe in [Reinforcement Learning: An Introduction 2nd Edition](https://www.amazon.co.jp/exec/obidos/ASIN/0262039249/hatena-blog-22/)
Chapter 4 page 76.<br>
### Problem: <br>
Suppose we want to get to the top left corner or the bottom right corner of the Grid. <br> 
Set of action = {Up, Down, Left Right}<br>
Agent is randomly placed in the Grid.<br>
We want to see what is fastest way to get to the corner.<br>
Model in a way such that with each steps, the reward given is -1.

## 1. Policy Iteration
[1] Policy Evaluation<br> 
It is possible to solve for the value state function explicitly, but it is more computational more expensive.<br>
Here, we implement the iterative approach stated in the book as an approximation to the Policy based on the Bellman Equations (Recursive). <br>

[2] Policy Improvement


## 2. Value Iteration
[1] Using the Bellman Optimal Equations <br>
This does both Policy Evaluation and Improvement at the same time. 


All PseudoCode and Equations can also be found in the book.
Both are found in the Agent.py 
