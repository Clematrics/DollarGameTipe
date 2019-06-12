# DollarGameTipe

This is my work done for the TIPE in CPGE. It is about the dollar game.

The `report` folder contains the tex source of the report (in french), one dependancy file to compile it, and the precompiled pdf. It presents the rules of the game, its stake, which is finding a minimal sequence of moves to solve the game, and my work.

The `dollar_game` folder contains the source of the program used to study the dollar game and to play around with.

# Screenshots

![The peterson graph, a give move made on the vertex 5](https://github.com/Clematrics/DollarGameTipe/blob/master/screenshot_1.png)

![The algorithm only_borrow is solving a more complex graph](https://github.com/Clematrics/DollarGameTipe/blob/master/screenshot_2.png)

![The graph solved by the algorithm. The sequence was minimized](https://github.com/Clematrics/DollarGameTipe/blob/master/screenshot_3.png)

![A random graph automatically generated](https://github.com/Clematrics/DollarGameTipe/blob/master/screenshot_4.png)

![The same random graph, but rearranged, solved and the sequence minimized](https://github.com/Clematrics/DollarGameTipe/blob/master/screenshot_5.png)

# How to use the program

You can either load a custom graph from a `.json` file in the `dollar_game` folder (some are provided as examples), or generate a random graph when the program launches.

For example, to load the custom graph `graph_peterson`, the beginning of `dollar_game.pyde` should look like this :

```python
  custom_graph = True
  custom_graph_name = "graph_peterson"
  random_graph_size = 15
  random_graph_degree = 4
```

To generate a random graph, set `custom_graph` to `False`. Here 15 represents the number of vertices of the graph, and 4 the maximum degree of the graph.

To play the game, left click on a vertex to do a give move, or right click to do a borrow move. You can also drag vertices to adjust their position. When solved, the square in the bottom right corner becomes green. The red number on a vertex represent its number, while the white number is the dollar amount it has.

The program includes some algorithms which will try to solve the game. You can select the algorithm by using the `b` and `n` keys. Then press the `Manual` button to switch to the `Automatic` mode.

You can also reset a graph (it won't reset the position of the vertices however), save its current state (if you click it multiple time, it will not overwrite the previous saves), and finally minimize the sequence you or an algorithm found.

On the left is the list of moves you or the algorithm made. A `<-> 6` means that the vertex `6` made a give move, while `>-< 10` means that the vertex `10` made a borrow move.

A benchmarking mode was added to test performances of an algorithm. Select an algorithm first using the `b` and `n` keys, then press `t` to start the benchmark. To stop it, just press `t` again. The benchmark will use randomly generated graphs with the parameters given at the beginning of the `dollar_age.pyde` file. You can also ajust the number of graphs you want the algorithm to test by changing the `benchmark_count` variable. If an algorithm could not solve a graph, you can adjust `benchmark_moves_attempts`, which hold the number of moves it will try before giving up and going to the next graph.
You can then consult the result of the benchmark by pressing `y`. It will create a file `results.csv` and output values to it,  like the maximum number of moves for a graph, the average, the number of moves after minimizing the sequence, and so on.

# Requirements

For the program to launch, you will need [Processing](https://processing.org/) and its module PyProcessing, available to download inside the software.
To open the project, just open `dollar_game.pyde` with Processing, then click on the launch button.