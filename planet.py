import pandas as pd
df = pd.read_csv('planet_data.csv', index_col='eName')
df_all = df[['isPlanet', 'meanRadius', 'orbit_type', 'orbits']]
planetDict = dict()
moonDict = dict()

class planet():
    def __init__(self, name, radius=1):
        self.radius = radius
        self.name = name
        self.moon_list = []

class moon():
    def __init__(self, name, radius=1, planetc=None):
        self.planetc = planetc
        self.name = name
        self.radius = radius
    def update_planet(self):
        self.planetc.moon_list.append(self)

def print_largest(planet):
    largest = None
    for moon in planet.moon_list:
        if largest is None:
            largest = moon
        else:
            if largest.radius < moon.radius:
                largest = moon
    if largest is not None:
        print(f"The largest moon of {planet.name} is {largest.name}")

for index, row in df_all.iterrows():
    if row['isPlanet'] is True:
        planetDict[index] = planet(index, row[1])
        
for index, row in df_all.iterrows():
    if row['isPlanet'] is False:
        moonDict[index] = moon(index, row[1], planetDict[row[3]])

for key, val in moonDict.items():
    val.update_planet()

for key, val in planetDict.items():
    print('\n')
    print_largest(val)
    print(key,"Moons Are:", [moon.name for moon in val.moon_list])
    print('\n')



