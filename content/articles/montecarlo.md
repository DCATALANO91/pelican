Title: Monte Carlo Ant Simulation
Date: 2020-11-20 8:37PM
Author: Dean
Tags: Python, Monte Carlo, Markov Chain
Category: Python

##Monte Carlo Ant Simulation

In this project, we will utilize the Monte Carlo method to simulate an ant moving around a 3x3 board, which we will then record where the ant lands on it's 1000th step. The Monte Carlo Method was invented by Stanislaw Ulam and uses randomly repeated sampling to predict statistical results.

Let's start by discussing the caveats to our project:

- The ant can begin at any random position on the 3x3 board

- The ant cannot move diagonally

- We will complete 1000 steps and record only the final landing space

- The simulation will run 100000 times, giving us 100000 data points

- The results will be converted to a decimal probability and written to a csv file

We'll start by importing random amd pandas. Random will be used to randomize our starting point and steps, while pandas will be used to store out data points in a dataframe.

```python
import random
import pandas as pd
```

Now we need to declare a few global variables. A list will be used to store the results of each simulation, a dictionary to write the results to which will be converted to a dataframe, and another dictionary that stores our valid moves based on the current position of the ant.

```python
results = []
my_dict = {}
markov_dict = {1:[2,4],2:[1,3,5],3:[2,6],4:[1,5,7],5:[2,4,6,8],6:[3,5,9],7:[4,8],8:[5,7,9],9:[6,8]}
```

Now we can begin coding our movement simulation. Keep in mind that this simulation needs run 100000 times, each iteration starts at a random spot and moves 1000 times. We can achieve this with a nested for loop.

```python
# begin first for loop, from 0 to 100000 exclusive
for sim in range(0,100000):
	# store a random integer between 1 and 9 as x, this is the starting point
    x = random.randint(1,9)
	# second for loop uses the current value of x to obtain a new random valid value from our markov_dict
    for step in range(0,1000):
        x = random.choice(markov_dict[x])
	# once the for loop is finished moving our ant 1000 times, we append the last move (x) to our results list	
    results.append(x)
```

Next, we count each instance of 1 - 9 and divide the result by 100000 to give us a decimal representation, before writting how many time each number appears in our list to a dictionary.

```python
for rec in range(1,10):
    my_dict[rec] = results.count(rec)/100000
```

Finally, we'll write the dictionary to a dataframe then export the results to a csv file.

```python
df = pd.DataFrame([my_dict])
df.to_csv(r'F:\PythonProjects\steps.csv', index=False)
```

Once the code runs, you should end up with a csv file that looks like this:

![Image](https://i.imgur.com/fzWbseT.jpg "CSV output")
---