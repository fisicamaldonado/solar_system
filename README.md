# Solar System (using log plots in python)

Welcome to the Solar System Visualization repository! In this project, we explore and visualize some important characteristics of our solar system using Python and Matplotlib.

## Introduction

The `solar_system` dictionary provided in this repository contains key information about the planets in our solar system. Each planet's information is stored as a list, including the mass, radius, gravity, rotation period, orbital period around the sun, and distance from the sun (in UA).

Understanding the vast differences in values among these characteristics can be challenging due to their wide range. To overcome this challenge, we leverage the power of logarithmic plots in our visualizations. By using a logarithmic scale on the y-axis, we can effectively represent the significant variations in mass and radius among the planets, making the comparisons more apparent and visually appealing.

## Requirements

To run the visualization scripts, you'll need the following:

- Python 3.x
- NumPy
- Matplotlib

## Visualization

We have provided two visualization functions to explore the data: `plotRadius()` and `plotMass()`. Here's a brief description of each:

### 1. `plotRadius(names, radius)`

This function creates a bar chart that compares the radii of the planets in our solar system. The radii are plotted on the y-axis, while the planet names are displayed on the x-axis. The bar chart is sorted in descending order, with the largest radius at the top. The y-axis scale is logarithmic for better visualization of the wide range of values.

### 2. `plotMass(names, mass)`

This function generates a bar chart to compare the masses of the planets in our solar system. The masses are shown on the y-axis, and the planet names are displayed on the x-axis. The bar chart is sorted in descending order, with the largest mass at the top. The y-axis scale is logarithmic to handle the significant differences in mass between the planets.

## Examples

Here are some example visualizations produced by the provided scripts:

1. Bar chart of planet radii:
![Planets Radius](images/planets_radius.png)

2. Bar chart of planet masses:
![Planets Masses](images/planets_masses.png)

Feel free to explore and modify the code to create your own visualizations!

## Usage

To use this project, follow these steps:

1. Clone the repository to your local machine.
2. Install the necessary dependencies (Python, NumPy, Matplotlib).
3. Run the `solar_system.py` script to execute the provided examples.

## License

Feel free to use. No need to credit but always appreciated.


