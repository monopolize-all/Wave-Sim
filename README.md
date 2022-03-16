# Wave-Sim
A python application to display wave equations. Made using Python 3 and tkinter.


# Running the program

To run the program, first clone this repository to a local directory.

Then run main.py either from the terminal or by double clicking main.py file.

```
python3 main.py
```

OR
```
python main.py
```


# How to simulate a wave?

1) Select an equation type (1D or 2D)
2) Enter an expression for the equation type you chose.

  If you chose a 1D equation, then enter an expression for y in terms of variables.
  There are two standard variables; x (position in x coordinate) and t (time elapsed).
  Eg: y = 100 * (2 + sin(2*t+0.02*x))
  You can't use y as a variable here.

  Similarly, if you chose a 2D equation, enter an expression for y and x in terms of variables. (Parametrized form)
  There is one standard variable; t (time elapsed)
  Eg: x = 200 + 100 * cos(t)
      y = 200 + 100 * sin(t)
  You can't use x and y as a variable here.

  When the program detects a new variable in the expression, it adds a slider for the same.
  The variable x for 1D equation shows no slider.
  The variable t for for both 1D and 2D equations show's two sliders;
    a) Time flow rate - How fast time flows
    b) Graph refresh rate - How frequently the graph updates. Increase this value if your device hangs while showing the equation.
  You can change the extreme values for the sliders via the provided textboxes.
  
  The graph for the equation will be displayed on screen automatically if a valid expression is detected. 
  
(PS: Use * for multiplication)


# Examples

https://user-images.githubusercontent.com/19649720/158644055-1f6c9962-7f42-4ed9-8f79-d30850a991c7.mov



https://user-images.githubusercontent.com/19649720/158644257-78917371-0849-4ab5-ada5-51030dc1a2c2.mov



https://user-images.githubusercontent.com/19649720/158644275-f7a318ab-fea9-43df-abee-a0700ec02c0a.mov

