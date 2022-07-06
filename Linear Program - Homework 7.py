#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import pulp and pandas
from pulp import *
import pandas as pd

#I first imported the pulp and pandas packages


# In[2]:


#read file
diet = pd.read_csv(r"C:\Users\molly\OneDrive\Documents\GaT\Modeling\Week 7\diet.csv")
diet

#then imported the file from my local machine


# In[3]:


#remove last 3 rows
diet_data = diet[:64]
minimum_requirement = diet[65:66]
maximum_requirement = diet[66:67]

print(diet_data)
print(minimum_requirement)
print(maximum_requirement)

#I then seperated the data into 3 different tables.  the dataset that I will use called diet data, 
#the minimum requirement section and the maximum requirement section


# In[4]:


#create values
food_name = list(diet_data.Foods)
price_per_serving = dict(zip(food_name,diet_data['Price/ Serving']))
calories = dict(zip(food_name,diet_data['Calories']))
serving_size = dict(zip(food_name,diet_data['Serving Size']))
cholesterol = dict(zip(food_name,diet_data['Cholesterol mg']))
carbs = dict(zip(food_name,diet_data['Carbohydrates g']))
sodium = dict(zip(food_name,diet_data['Sodium mg']))
fat = dict(zip(food_name,diet_data['Total_Fat g']))
fiber = dict(zip(food_name,diet_data['Dietary_Fiber g']))
protein = dict(zip(food_name,diet_data['Protein g']))
vitamin_a = dict(zip(food_name,diet_data['Vit_A IU']))
vitamin_c = dict(zip(food_name,diet_data['Vit_C IU']))
calcium = dict(zip(food_name,diet_data['Calcium mg']))
iron = dict(zip(food_name,diet_data['Iron mg']))

# I then created directories of my data with each seperate food item


# In[5]:


prob = LpProblem('Diet_Problem', LpMinimize)
food_vars = LpVariable.dicts("Food",food_name,lowBound=0,cat='Continuous')
prob += lpSum([price_per_serving[i]*food_vars[i] for i in food_name])

# I then created food vars to store my referenced variabled and created my objective function, stating that I want
# to minimize the cost per serving


# In[6]:


# constraints

#calories
prob += lpSum([food_vars[x]*calories[x] for x in food_name]) >= minimum_requirement['Calories'], "Calories Min"
prob += lpSum([food_vars[x]*calories[x] for x in food_name]) <= maximum_requirement['Calories'], "Calories Max"

#cholesterol
prob += lpSum([food_vars[x]*cholesterol[x] for x in food_name]) >= minimum_requirement['Cholesterol mg'], "Cholesterol Min"
prob += lpSum([food_vars[x]*cholesterol[x] for x in food_name]) <= maximum_requirement['Cholesterol mg'], "Cholesterol Max"

#fat
prob += lpSum([food_vars[x]*fat[x] for x in food_name]) >= minimum_requirement['Total_Fat g'], "Fat Min"
prob += lpSum([food_vars[x]*fat[x] for x in food_name]) <= maximum_requirement['Total_Fat g'], "Fat Max"

#sodium
prob += lpSum([food_vars[x]*sodium[x] for x in food_name]) >= minimum_requirement['Sodium mg'], "Sodium Min"
prob += lpSum([food_vars[x]*sodium[x] for x in food_name]) <= maximum_requirement['Sodium mg'], "Sodium Max"

#carbs
prob += lpSum([food_vars[x]*carbs[x] for x in food_name]) >= minimum_requirement['Carbohydrates g'], "Carbs Min"
prob += lpSum([food_vars[x]*carbs[x] for x in food_name]) <= maximum_requirement['Carbohydrates g'], "Carbs Max"

#fiber
prob += lpSum([food_vars[x]*fiber[x] for x in food_name]) >= minimum_requirement['Dietary_Fiber g'], "Fiber Min"
prob += lpSum([food_vars[x]*fiber[x] for x in food_name]) <= maximum_requirement['Dietary_Fiber g'], "Fiber Max"

#protein
prob += lpSum([food_vars[x]*protein[x] for x in food_name]) >= minimum_requirement['Protein g'], "Protein Min"
prob += lpSum([food_vars[x]*protein[x] for x in food_name]) <= maximum_requirement['Protein g'], "Protein Max"

#vitamin_a
prob += lpSum([food_vars[x]*vitamin_a[x] for x in food_name]) >= minimum_requirement['Vit_A IU'], "VitaminA Min"
prob += lpSum([food_vars[x]*vitamin_a[x] for x in food_name]) <= maximum_requirement['Vit_A IU'], "VitaminA Max"

#vitamin_c
prob += lpSum([food_vars[x]*vitamin_c[x] for x in food_name]) >= minimum_requirement['Vit_C IU'], "VitaminC Min"
prob += lpSum([food_vars[x]*vitamin_c[x] for x in food_name]) <= maximum_requirement['Vit_C IU'], "VitaminC Max"

#calcium
prob += lpSum([food_vars[x]*calcium[x] for x in food_name]) >= minimum_requirement['Calcium mg'], "Calcium Min"
prob += lpSum([food_vars[x]*calcium[x] for x in food_name]) <= maximum_requirement['Calcium mg'], "Calcium Max"

#iron
prob += lpSum([food_vars[x]*iron[x] for x in food_name]) >= minimum_requirement['Iron mg'], "Iron Min"
prob += lpSum([food_vars[x]*iron[x] for x in food_name]) <= maximum_requirement['Iron mg'], "Iron Max"


#I then added in all of my constraints to the function where each nutritional measurement is required to be between
# the minimum and maximum requirement stated within the dataset. 


# In[7]:


prob.solve()
prob. solver
LpStatus[prob.status]

print('Total Dollars Cost', prob.objective.value())

for var in prob.variables():
    if (var.value()) > 0:     
        print((var.name,var.value())) 

# finally I outputted my data, showing the results to match the homework instructions.  I dont think anyone wants to eat
# 52 servings of celery so I will continue to refine my linear program


# In[8]:


food_chosen = LpVariable.dicts("Chosen",food_name,0,1,cat='Binary')

for f in food_name:
    prob += food_vars[f] >= .1 * food_chosen[f]
#making sure that there is greater than .1 of a serving choosen    
    
prob += food_chosen['Frozen Broccoli'] + food_chosen['Celery, Raw'] <= 1
#making sure that if broccoli or celery is choosen there can only be one of them choosen

prob += food_chosen['Tofu'] + food_chosen['Roasted Chicken'] + food_chosen['Scrambled Eggs'] + food_chosen['Bologna,Turkey'] + food_chosen['Frankfurter, Beef'] + food_chosen['Ham,Sliced,Extralean'] +  food_chosen['Hamburger W/Toppings'] + food_chosen['Hotdog, Plain'] + food_chosen['Pork'] + food_chosen['White Tuna in Water']  >= 3
#making sure that at least 3 different kinds of proteins are selected


# In[9]:


prob.solve()
prob. solver
LpStatus[prob.status]

print('Total Dollars Cost', prob.objective.value())

for var in prob.variables():
    if (var.value()) > 0:     
        print((var.name,var.value())) 
        
# my final output shows that if I selected a diet that met the minimum and maximum restrictions of calories/nutrition,
# as well as making sure that whatever I chose has greater than .1 serving, as well as only choosing broccoli or celery, and
# lastly ensuring that I select at least 3 different kinds of meats the minimum cost per person would be $4.38

#The selected foods and # of serving sizes are also listed below

