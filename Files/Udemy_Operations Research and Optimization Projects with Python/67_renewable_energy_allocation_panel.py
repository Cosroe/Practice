import pandas as pd
import panel as pn
from bokeh.plotting import figure
from bokeh.layouts import column
from pulp import LpMaximize, LpProblem, LpVariable, lpSum, value

# Panel extension
pn.extension()

# Function to perform optimization and return results
def optimize_energy_allocation(solar, wind, hydro):
    # Define the problem
    prob = LpProblem("Renewable_Energy_Allocation", LpMaximize)

    # Define decision variables
    energy_sources = ['solar', 'wind', 'hydro']
    energy = LpVariable.dicts("Energy", energy_sources, 0, None)

    # Define parameters
    costs = {'solar': 50, 'wind': 40, 'hydro': 30}
    production_limits = {'solar': 100, 'wind': 120, 'hydro': 80}
    demand = 250  # Total demand

    # Define the objective function
    prob += lpSum([energy[i] * (100 - costs[i]) for i in energy_sources]), "Total_Profit"

    # Add constraints
    prob += lpSum([energy[i] for i in energy_sources]) == demand, "Total_Demand"
    for i in energy_sources:
        prob += energy[i] <= production_limits[i], f"Production_Limit_{i}"

    # Solve the problem
    prob.solve()

    # Extract results
    results = {v.name: v.varValue for v in prob.variables()}
    total_cost = value(lpSum([energy[i] * costs[i] for i in energy_sources]))

    return results, total_cost

# Interactive widgets
solar_slider = pn.widgets.FloatSlider(name='Solar Energy Allocation', start=0, end=100, step=1, value=50)
wind_slider = pn.widgets.FloatSlider(name='Wind Energy Allocation', start=0, end=100, step=1, value=50)
hydro_slider = pn.widgets.FloatSlider(name='Hydro Energy Allocation', start=0, end=100, step=1, value=50)

# Callback function to update the plot and text
@pn.depends(solar_slider.param.value, wind_slider.param.value, hydro_slider.param.value)
def update_dashboard(solar, wind, hydro):
    allocations = {'solar': solar, 'wind': wind, 'hydro': hydro}
    total_alloc = solar + wind + hydro

    # Optimization
    results, total_cost = optimize_energy_allocation(solar, wind, hydro)

    # Data for plotting
    df = pd.DataFrame(list(allocations.items()), columns=['Source', 'Allocation'])

    # Bokeh plot
    plot = figure(x_range=df['Source'], height=250, title="Energy Allocation",
                  toolbar_location=None, tools="")
    plot.vbar(x=df['Source'], top=df['Allocation'], width=0.9)

    # Results text
    result_text = f"Total Cost: {total_cost:.2f}\nAllocations: {results}"

    return pn.Column(plot, pn.pane.Markdown(result_text))

# Layout
dashboard = pn.Column(
    solar_slider,
    wind_slider,
    hydro_slider,
    update_dashboard
)

# Serve the dashboard
dashboard.servable()
