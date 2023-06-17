import numpy as np
import matplotlib.pyplot as plt

'''
In the next dict we have stored some important data from our Solar system.
Each planet's information is stored as a list, with the values representing:

1. Mass (in Earth masses)
2. Radius (in Earth radii)
3. Gravity (in m/s²)
4. Rotation period (in Earth hours)
5. Orbital period around the sun (in Earth days)
6. Semimajor axis: It is expressed in astronomical units (AU).
7. Eccentricity: Dimentionless value between 0 and 1.
8. Inclination: The inclination of the planet's axial tilt with respect to its orbital plane, measured in degrees.
9. Density: The estimated average density of the planet, measured in grams per cubic centimeter (g/cm³).
10. Atmospheric Composition: The composition of the planet's atmosphere, described as a string.
11. Number of Moons: The approximate number of moons orbiting the planet.

'''

solar_system = {
    'Mercury': [0.055, 0.383, 3.7, 58.6, 88, 0.39, 0.387, 0.205, 0.0, 5.427, 'N/A', 0],
    'Venus': [0.815, 0.949, 8.87, -243, 225, 0.72, 0.723, 0.007, 177.4, 5.243, 'Carbon Dioxide (96.5%), Nitrogen (3.5%)', 0],
    'Earth': [1.0, 1.0, 9.81, 1, 365.25, 1.0, 1.0, 0.017, 23.45, 5.515, 'Nitrogen (78.1%), Oxygen (20.9%)', 1],
    'Mars': [0.107, 0.532, 3.71, 1.03, 687, 1.52, 1.524, 0.094, 23.98, 3.933, 'Carbon Dioxide (95.3%), Nitrogen (2.7%)', 2],
    'Jupiter': [318, 11.209, 24.79, 0.41, 4332, 5.20, 5.203, 0.049, 3.08, 1.326, 'Hydrogen (90%), Helium (10%)', 79],
    'Saturn': [95, 9.449, 10.44, 0.43, 10759, 9.58, 9.582, 0.057, 26.73, 0.687, 'Hydrogen (96%), Helium (3%)', 82],
    'Uranus': [14.5, 4.007, 8.69, -0.72, 30688, 19.18, 19.182, 0.046, 97.92, 1.27, 'Hydrogen (83%), Helium (15%)', 27],
    'Neptune': [17.1, 3.883, 11.15, 0.67, 60182, 30.07, 30.070, 0.011, 28.8, 1.638, 'Hydrogen (80%), Helium (19%)', 14]
}


# Extract the masses and radii of the planets from the dictionary
mass = np.array(list(solar_system.values()))[:, 0]
radius = np.array(list(solar_system.values()))[:, 1]
names = np.array(list(solar_system.keys()))

def plotRadius(names, radius):
    '''
    Plot a bar chart of planet radii in the solar system.

    Args:
        names (numpy.ndarray): Array of planet names.
        radius (numpy.ndarray): Array of planet radii.

    Returns:
        None
    '''
    # Sort the lists of names and radii based on the radii
    names, radius = zip(*sorted(zip(names, radius), key=lambda x: x[1], reverse=True))

    # Create a bar plot sorted from largest to smallest radius
    plt.bar(range(len(names)), radius)

    # Configure the axes and labels
    plt.xlabel('Planets')
    plt.ylabel('Radius (Earth = 1)')
    plt.title('Planets Radius in Solar System (Logarithmic Scale)')
    plt.xticks(range(len(names)), names, rotation=45)
    
    plt.yscale('log')

    # Display the bar plot
    plt.show()

def plotMass(names, mass):
    '''
    Plot a bar chart of planet masses in the solar system.

    Args:
        names (numpy.ndarray): Array of planet names.
        mass (numpy.ndarray): Array of planet masses.

    Returns:
        None
    '''
    # Sort the lists of names and masses based on the masses
    names, mass = zip(*sorted(zip(names, mass), key=lambda x: x[1], reverse=True))

    # Create a bar plot sorted from largest to smallest mass
    plt.bar(range(len(names)), mass)

    # Configure the axes and labels
    plt.xlabel('Planets')
    plt.ylabel('Mass (Earth = 1)')
    plt.title('Planets Masses in Solar System (Logarithmic Scale)')
    plt.xticks(range(len(names)), names, rotation=45)
    
    plt.yscale('log')

    # Display the bar plot
    plt.show()


plotRadius(names,radius)
plotMass(names, mass)
