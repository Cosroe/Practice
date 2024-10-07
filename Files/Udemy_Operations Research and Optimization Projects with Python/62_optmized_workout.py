import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from ortools.linear_solver import pywraplp

# Input Data
workouts = {
    'Workout': [
        'Treadmill Running/Walking', 'Elliptical Trainer', 'Rowing Machine', 'Stationary Bike',
        'Circuit Training', 'Jump Rope', 'Kettlebell Swings',
        'Bench Press', 'Squats', 'Deadlifts', 'Pull-Ups/Chin-Ups', 'Shoulder Press', 'Bent-Over Rows', 'Leg Press'
    ],
    'Calories Burned': [500, 400, 600, 300, 450, 700, 500, 0, 0, 0, 0, 0, 0, 0],
    'Time Required': [30, 30, 30, 30, 30, 15, 20, 30, 30, 30, 20, 30, 30, 30],
    'Type': ['Cardio', 'Cardio', 'Cardio', 'Cardio', 'Cardio', 'Cardio', 'Cardio', 'Strength', 'Strength', 'Strength', 'Strength', 'Strength', 'Strength', 'Strength']
}
df_workouts = pd.DataFrame(workouts)

# Streamlit App
st.title("Personalized Workout Plan Optimization")

# User Inputs
goal = st.selectbox('Fitness Goal', ['Weight Loss', 'Muscle Gain'])
available_time = st.slider('Available Time per Week (minutes)', 100, 600, 300)
physical_limitations = st.multiselect('Physical Limitations', ['None', 'Knee Issues', 'Back Issues', 'Shoulder Issues'])

# Optimization Model using OR-Tools
solver = pywraplp.Solver.CreateSolver('SCIP')

# Decision Variables
x = {}
for workout in df_workouts['Workout']:
    x[workout] = solver.IntVar(0, solver.infinity(), workout)

# Binary Variables for Variety Constraint
y = {}
for workout in df_workouts['Workout']:
    y[workout] = solver.BoolVar(workout + '_included')

# Objective Function
objective = solver.Objective()
if goal == 'Weight Loss':
    for w in df_workouts['Workout']:
        coefficient = float(df_workouts.loc[df_workouts['Workout'] == w, 'Calories Burned'].values[0])
        objective.SetCoefficient(x[w], coefficient)
elif goal == 'Muscle Gain':
    for w in df_workouts['Workout']:
        if df_workouts.loc[df_workouts['Workout'] == w, 'Type'].values[0] == 'Strength':
            coefficient = float(df_workouts.loc[df_workouts['Workout'] == w, 'Time Required'].values[0])
            objective.SetCoefficient(x[w], coefficient)
objective.SetMaximization()

# Constraints
solver.Add(sum(x[w] * float(df_workouts.loc[df_workouts['Workout'] == w, 'Time Required'].values[0]) for w in df_workouts['Workout']) <= available_time)

# Ensure a mix of workout types and at least 5 different exercises
if goal == 'Weight Loss':
    solver.Add(sum(x[w] for w in df_workouts['Workout'] if df_workouts.loc[df_workouts['Workout'] == w, 'Type'].values[0] == 'Cardio') >= 1)
    solver.Add(sum(x[w] for w in df_workouts['Workout'] if df_workouts.loc[df_workouts['Workout'] == w, 'Type'].values[0] == 'Strength') <= 1)
    solver.Add(sum(y[w] for w in df_workouts['Workout']) >= 5)
elif goal == 'Muscle Gain':
    solver.Add(sum(x[w] for w in df_workouts['Workout'] if df_workouts.loc[df_workouts['Workout'] == w, 'Type'].values[0] == 'Strength') >= 2)
    solver.Add(sum(x[w] for w in df_workouts['Workout'] if df_workouts.loc[df_workouts['Workout'] == w, 'Type'].values[0] == 'Cardio') >= 1)
    solver.Add(sum(y[w] for w in df_workouts['Workout']) >= 5)

# Link binary variables with decision variables
for w in df_workouts['Workout']:
    solver.Add(x[w] <= y[w] * available_time)
    solver.Add(x[w] >= y[w] * 0.1)

# Additional constraints for balanced workout plans
solver.Add(sum(x[w] for w in df_workouts['Workout'] if df_workouts.loc[df_workouts['Workout'] == w, 'Type'].values[0] == 'Cardio') <= 5)
solver.Add(sum(x[w] for w in df_workouts['Workout'] if df_workouts.loc[df_workouts['Workout'] == w, 'Type'].values[0] == 'Strength') <= 4)

# Physical limitations constraints
if 'Knee Issues' in physical_limitations:
    solver.Add(x['Treadmill Running/Walking'] == 0)
    solver.Add(x['Jump Rope'] == 0)
    solver.Add(x['Squats'] == 0)

if 'Back Issues' in physical_limitations:
    solver.Add(x['Deadlifts'] == 0)
    solver.Add(x['Bent-Over Rows'] == 0)

if 'Shoulder Issues' in physical_limitations:
    solver.Add(x['Shoulder Press'] == 0)
    solver.Add(x['Pull-Ups/Chin-Ups'] == 0)

# Solve the model
status = solver.Solve()

# Results
workout_plan = {w: x[w].solution_value() for w in df_workouts['Workout']}

st.header("Optimal Weekly Workout Plan")
st.write("Based on your inputs, here is your optimal weekly workout plan:")

workout_plan_df = pd.DataFrame(list(workout_plan.items()), columns=['Workout', 'Frequency'])
st.table(workout_plan_df)

# Visualization
fig, ax = plt.subplots()
ax.bar(workout_plan_df['Workout'], workout_plan_df['Frequency'], color='skyblue')
ax.set_xlabel('Workout')
ax.set_ylabel('Frequency')
ax.set_title('Optimal Weekly Workout Plan')
plt.xticks(rotation=45, ha='right')
st.pyplot(fig)
