# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']


# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

# test function by updating damages


def update_damages(data):
  updated_damages = []
  for value in data:
    if value == "Damages not recorded":
      updated_damages.append(value)
    elif "B" in value:
      updated_damages.append(float(value[:-1]) * conversion["B"])
    else:
      updated_damages.append(float(value[:-1]) * conversion["M"])
  return updated_damages

updated_damages = update_damages(damages)
#print(updated_damages)


# 2 
# Create a Table

# Create and view the hurricanes dictionary
def create_dict(names, months, years,max_sustained_winds, areas_affected, damages, deaths):
  hurricanes = {}
  for x in range(len(names)):
    hurricanes[names[x]] = {"Name": names[x], "Month": months[x], "Year": years[x],"Max Sustained Wind": max_sustained_winds[x], "Areas Affected": areas_affected[x], "Damage": updated_damages[x], "Deaths": deaths[x]}
  return hurricanes
   
hurricanes = create_dict(names, months, years,max_sustained_winds, areas_affected, damages, deaths)

#print(hurricanes)




 


# 3
# Organizing by Year

def canes_by_year(hurricanes):
  
  canes_by_year = {}
  for name in hurricanes:
    current_year = hurricanes[name]["Year"]
    current_cane = hurricanes[name]
    if current_year in canes_by_year:
      canes_by_year[current_year].append(current_cane)
    else:
      canes_by_year[current_year] = [current_cane]
  return canes_by_year

canes_by_year = canes_by_year(hurricanes)
#print(canes_by_year)
# create a new dictionary of hurricanes with year and key


# 4
# Counting Damaged Areas
def damaged_area_count(hurricanes):
  damaged_area_count = {}
  
  for hurricane in hurricanes:
    for area in hurricanes[hurricane]["Areas Affected"]:
      if area in damaged_area_count:
        
        damaged_area_count[area] += 1
      else:
        damaged_area_count[area] = 1
  return damaged_area_count

damaged_area_count = damaged_area_count(hurricanes)
#print(damaged_area_count)


# create dictionary of areas to store the number of hurricanes involved in


# 5 
# Calculating Maximum Hurricane Count
def max_cane_count(damaged_area_count):
  max_area = ''
  max_area_count = 0
  for area in damaged_area_count:
    if max_area_count < damaged_area_count[area]:
      max_area = area
      max_area_count = damaged_area_count[area]
  return max_area,  max_area_count

max_area, max_count = max_cane_count(damaged_area_count)
print(max_area, max_count)

# find most frequently affected area and the number of hurricanes involved in



# 6
# Calculating the Deadliest Hurricane
def most_deadly(hurricanes):
  name = ''
  num_deaths = 0
  for hurricane in hurricanes:
    if num_deaths < hurricanes[hurricane]['Deaths']:
      num_deaths = hurricanes[hurricane]['Deaths']
      name = hurricane
  return name, num_deaths

name, max_deaths = most_deadly(hurricanes)
print(name, max_deaths)
# find highest mortality hurricane and the number of deaths

# 7
# Rating Hurricanes by Mortality

def mortality(hurricanes):
  hurricanes_by_mortality = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for hurricane in hurricanes:
    deaths = hurricanes[hurricane]['Deaths']
    current_hurricane = hurricanes[hurricane]
    if deaths > 10000:
      hurricanes_by_mortality[5].append(current_hurricane)
    elif deaths > 1000:
      hurricanes_by_mortality[4].append(current_hurricane)
    elif deaths > 500:
      hurricanes_by_mortality[3].append(current_hurricane)
    elif deaths > 100:
      hurricanes_by_mortality[2].append(current_hurricane)
    elif deaths > 0:
      hurricanes_by_mortality[1].append(current_hurricane)
    else:
      hurricanes_by_mortality[0].append(current_hurricane)
  return hurricanes_by_mortality

hurricanes_by_mortality = mortality(hurricanes)
#print(hurricanes_by_mortality)
      
# categorize hurricanes in new dictionary with mortality severity as key


# 8 Calculating Hurricane Maximum Damage
def most_destructive(hurricanes):
  name = ''
  cost = 0
  for hurricane in hurricanes:
    if hurricanes[hurricane]['Damage'] == 'Damages not recorded':
      continue
    elif cost < int(hurricanes[hurricane]['Damage']):
      cost = int(hurricanes[hurricane]['Damage'])
      name = hurricane
  return name, cost

name, cost = most_destructive(hurricanes)
print(name, cost)
# find highest damage inducing hurricane and its total cost


# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}

def damages_scale(hurricanes):
  hurricanes_by_damage = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for hurricane in hurricanes:
    if hurricanes[hurricane]['Damage'] == "Damages not recorded":
      hurricanes_by_damage[0].append(hurricanes[hurricane])
    else:
      damage = int(hurricanes[hurricane]['Damage'])
      current_hurricane = hurricanes[hurricane]
      if damage > damage_scale[4]:
        hurricanes_by_damage[5].append(current_hurricane)
      elif damage > damage_scale[3]:
        hurricanes_by_damage[4].append(current_hurricane)
      elif damage > damage_scale[2]:
        hurricanes_by_damage[3].append(current_hurricane)
      elif damage > damage_scale[1]:
        hurricanes_by_damage[2].append(current_hurricane)
      elif damage > damage_scale[0]:
        hurricanes_by_damage[1].append(current_hurricane)
      else:
        hurricanes_by_damage[0].append(current_hurricane)
  return hurricanes_by_damage

hurricanes_by_damage = damages_scale(hurricanes)

print(hurricanes_by_damage)
  
# categorize hurricanes in new dictionary with damage severity as key
