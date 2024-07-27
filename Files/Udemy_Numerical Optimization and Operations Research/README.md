# Optimization Course

Welcome to the Optimization and Operations Research course material!

Here you will find the code used throughout the course as exercises and solved examples

Enjoy your models!


[Configure your project](#configure-your-project) | [Exercises](#exercises) | [Solutions](#solutions) | [Contact](#contact)


## Configure your project

To configure your Python environment for the course, I suggest using virtual environments. They can be used to control the version of your packages and make sure your project is consistent. I suggest naming the virtual environment as `venv`, which is a convention for Python development, often ignored on default `.gitgnore` files.

### Windows

To configure your Python `venv`, run:

```bash
python -m venv venv
```

Which should call the module `venv` from Python (by including the `-m` argument) and create a virtual environment of the same name.

To activate it, run:

```bash
venv\Scripts\activate
```

And then install the project requirements using:

```bash
pip install -r requirements.txt
```

### Linux and MacOS

To configure your Python `venv`, run:

```bash
python3 -m venv venv
```

Or to choose a specific Python version different from default, run:

```bash
python3.X -m venv venv
```

In which "X" corresponds to the minor installation version.

This should call the module `venv` from Python (by including the `-m` argument) and create a virtual environment of the same name.

To activate it, run:

```bash
source venv/bin/activate
```

And then install the project requirements using:

```bash
pip install -r requirements.txt
```

### Select Interpreter for VS Code

VS Code should automatically detect the Python interpreter from the virtual environment when you create it. In case it doesn't occur, you can select it manually:

Open the Command Palette (Ctrl+Shift+P or Cmd+Shift+P on macOS).
Type Python: Select Interpreter.
Choose the interpreter that is located inside your project's `venv` directory.


## Exercises

- [Knapsack Problem](./exercises/01%20-%20Introduction/knapsack.ipynb)
- [Product mix with Pyomo](./exercises/02%20-%20Linear%20Programming/product-mix/product-mix-pyomo.ipynb) and with [Scipy](./exercises/02%20-%20Linear%20Programming/product-mix/product-mix-scipy.ipynb)
- [Transportation problem](./exercises/02%20-%20Linear%20Programming/transportation/transportation.ipynb)
- [Dynamic Lot Size](./exercises/03%20-%20Lot%20Sizing/dynamic_lot_size.ipynb)
- [Job-shop with time-indexed model](./exercises/04%20-%20Sequencing/jssp_time_indexed.ipynb)
- [Job-shop with disjunctive model](./exercises/04%20-%20Sequencing/jssp_disj.ipynb)
- [Traveling Salesman MTZ](./exercises/04%20-%20Sequencing/tsp_mtz.ipynb)
- [Facility Dispersion Model](./exercises/05%20-%20Dispersion/facility_dispersion.ipynb)
- [Traveling Salesman with recursive subtour elimination DFJ](./exercises/06%20-%20Routing/tsp_dfj.ipynb)
- [CVRP MIP](./exercises/06%20-%20Routing/cvrp_mip.ipynb)
- [CVRP OR-Tools](./exercises/06%20-%20Routing/cvrp_heur.ipynb)


## Solutions

- [Knapsack Problem](./solutions/01%20-%20Introduction/knapsack.ipynb)
- [Product mix with Pyomo](./solutions/02%20-%20Linear%20Programming/product-mix/product-mix-pyomo.ipynb) and with [Scipy](./solutions/02%20-%20Linear%20Programming/product-mix/product-mix-scipy.ipynb)
- [Transportation problem](./solutions/02%20-%20Linear%20Programming/transportation/transportation.ipynb)
- [Dynamic Lot Size](./solutions/03%20-%20Lot%20Sizing/dynamic_lot_size.ipynb)
- [Job-shop with time-indexed model](./solutions/04%20-%20Sequencing/jssp_time_indexed.ipynb)
- [Job-shop with disjunctive model](./solutions/04%20-%20Sequencing/jssp_disj.ipynb)
- [Traveling Salesman MTZ](./solutions/04%20-%20Sequencing/tsp_mtz.ipynb)
- [Facility Dispersion Model](./solutions/05%20-%20Dispersion/facility_dispersion.ipynb)
- [Traveling Salesman with recursive subtour elimination DFJ](./solutions/06%20-%20Routing/tsp_dfj.ipynb)
- [Traaveling Salesman with OR-Tools and custom heuristics](./solutions/06%20-%20Routing/tsp_heur.ipynb)
- [CVRP MIP](./solutions/06%20-%20Routing/cvrp_mip.ipynb)
- [CVRP OR-Tools](./solutions/06%20-%20Routing/cvrp_heur.ipynb)


## Contact

You can reach out to me at bruscalia12@gmail.com
