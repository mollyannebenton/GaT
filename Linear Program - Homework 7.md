```python
#import pulp and pandas
from pulp import *
import pandas as pd

#I first imported the pulp and pandas packages
```


```python
#read file
diet = pd.read_csv(r"C:\Users\molly\OneDrive\Documents\GaT\Modeling\Week 7\diet.csv")
diet

#then imported the file from my local machine
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Foods</th>
      <th>Price/ Serving</th>
      <th>Serving Size</th>
      <th>Calories</th>
      <th>Cholesterol mg</th>
      <th>Total_Fat g</th>
      <th>Sodium mg</th>
      <th>Carbohydrates g</th>
      <th>Dietary_Fiber g</th>
      <th>Protein g</th>
      <th>Vit_A IU</th>
      <th>Vit_C IU</th>
      <th>Calcium mg</th>
      <th>Iron mg</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Frozen Broccoli</td>
      <td>0.16</td>
      <td>10 Oz Pkg</td>
      <td>73.8</td>
      <td>0.0</td>
      <td>0.8</td>
      <td>68.2</td>
      <td>13.6</td>
      <td>8.5</td>
      <td>8.0</td>
      <td>5867.4</td>
      <td>160.2</td>
      <td>159.0</td>
      <td>2.3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Carrots,Raw</td>
      <td>0.07</td>
      <td>1/2 Cup Shredded</td>
      <td>23.7</td>
      <td>0.0</td>
      <td>0.1</td>
      <td>19.2</td>
      <td>5.6</td>
      <td>1.6</td>
      <td>0.6</td>
      <td>15471.0</td>
      <td>5.1</td>
      <td>14.9</td>
      <td>0.3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Celery, Raw</td>
      <td>0.04</td>
      <td>1 Stalk</td>
      <td>6.4</td>
      <td>0.0</td>
      <td>0.1</td>
      <td>34.8</td>
      <td>1.5</td>
      <td>0.7</td>
      <td>0.3</td>
      <td>53.6</td>
      <td>2.8</td>
      <td>16.0</td>
      <td>0.2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Frozen Corn</td>
      <td>0.18</td>
      <td>1/2 Cup</td>
      <td>72.2</td>
      <td>0.0</td>
      <td>0.6</td>
      <td>2.5</td>
      <td>17.1</td>
      <td>2.0</td>
      <td>2.5</td>
      <td>106.6</td>
      <td>5.2</td>
      <td>3.3</td>
      <td>0.3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Lettuce,Iceberg,Raw</td>
      <td>0.02</td>
      <td>1 Leaf</td>
      <td>2.6</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.8</td>
      <td>0.4</td>
      <td>0.3</td>
      <td>0.2</td>
      <td>66.0</td>
      <td>0.8</td>
      <td>3.8</td>
      <td>0.1</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>62</th>
      <td>Crm Mshrm Soup,W/Mlk</td>
      <td>0.65</td>
      <td>1 C (8 Fl Oz)</td>
      <td>203.4</td>
      <td>19.8</td>
      <td>13.6</td>
      <td>1076.3</td>
      <td>15.0</td>
      <td>0.5</td>
      <td>6.1</td>
      <td>153.8</td>
      <td>2.2</td>
      <td>178.6</td>
      <td>0.6</td>
    </tr>
    <tr>
      <th>63</th>
      <td>Beanbacn Soup,W/Watr</td>
      <td>0.67</td>
      <td>1 C (8 Fl Oz)</td>
      <td>172.0</td>
      <td>2.5</td>
      <td>5.9</td>
      <td>951.3</td>
      <td>22.8</td>
      <td>8.6</td>
      <td>7.9</td>
      <td>888.0</td>
      <td>1.5</td>
      <td>81.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>64</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>65</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>Minimum daily intake</td>
      <td>1500.0</td>
      <td>30.0</td>
      <td>20.0</td>
      <td>800.0</td>
      <td>130.0</td>
      <td>125.0</td>
      <td>60.0</td>
      <td>1000.0</td>
      <td>400.0</td>
      <td>700.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>66</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>Maximum daily intake</td>
      <td>2500.0</td>
      <td>240.0</td>
      <td>70.0</td>
      <td>2000.0</td>
      <td>450.0</td>
      <td>250.0</td>
      <td>100.0</td>
      <td>10000.0</td>
      <td>5000.0</td>
      <td>1500.0</td>
      <td>40.0</td>
    </tr>
  </tbody>
</table>
<p>67 rows × 14 columns</p>
</div>




```python
#remove last 3 rows
diet_data = diet[:64]
minimum_requirement = diet[65:66]
maximum_requirement = diet[66:67]

print(diet_data)
print(minimum_requirement)
print(maximum_requirement)

#I then seperated the data into 3 different tables.  the dataset that I will use called diet data, 
#the minimum requirement section and the maximum requirement section
```

                       Foods  Price/ Serving      Serving Size  Calories  \
    0        Frozen Broccoli            0.16         10 Oz Pkg      73.8   
    1            Carrots,Raw            0.07  1/2 Cup Shredded      23.7   
    2            Celery, Raw            0.04           1 Stalk       6.4   
    3            Frozen Corn            0.18           1/2 Cup      72.2   
    4    Lettuce,Iceberg,Raw            0.02            1 Leaf       2.6   
    ..                   ...             ...               ...       ...   
    59       Neweng Clamchwd            0.75     1 C (8 Fl Oz)     175.7   
    60           Tomato Soup            0.39     1 C (8 Fl Oz)     170.7   
    61  New E Clamchwd,W/Mlk            0.99     1 C (8 Fl Oz)     163.7   
    62  Crm Mshrm Soup,W/Mlk            0.65     1 C (8 Fl Oz)     203.4   
    63  Beanbacn Soup,W/Watr            0.67     1 C (8 Fl Oz)     172.0   
    
        Cholesterol mg  Total_Fat g  Sodium mg  Carbohydrates g  Dietary_Fiber g  \
    0              0.0          0.8       68.2             13.6              8.5   
    1              0.0          0.1       19.2              5.6              1.6   
    2              0.0          0.1       34.8              1.5              0.7   
    3              0.0          0.6        2.5             17.1              2.0   
    4              0.0          0.0        1.8              0.4              0.3   
    ..             ...          ...        ...              ...              ...   
    59            10.0          5.0     1864.9             21.8              1.5   
    60             0.0          3.8     1744.4             33.2              1.0   
    61            22.3          6.6      992.0             16.6              1.5   
    62            19.8         13.6     1076.3             15.0              0.5   
    63             2.5          5.9      951.3             22.8              8.6   
    
        Protein g  Vit_A IU  Vit_C IU  Calcium mg  Iron mg  
    0         8.0    5867.4     160.2       159.0      2.3  
    1         0.6   15471.0       5.1        14.9      0.3  
    2         0.3      53.6       2.8        16.0      0.2  
    3         2.5     106.6       5.2         3.3      0.3  
    4         0.2      66.0       0.8         3.8      0.1  
    ..        ...       ...       ...         ...      ...  
    59       10.9      20.1       4.8        82.8      2.8  
    60        4.1    1393.0     133.0        27.6      3.5  
    61        9.5     163.7       3.5       186.0      1.5  
    62        6.1     153.8       2.2       178.6      0.6  
    63        7.9     888.0       1.5        81.0      2.0  
    
    [64 rows x 14 columns]
       Foods  Price/ Serving          Serving Size  Calories  Cholesterol mg  \
    65   NaN             NaN  Minimum daily intake    1500.0            30.0   
    
        Total_Fat g  Sodium mg  Carbohydrates g  Dietary_Fiber g  Protein g  \
    65         20.0      800.0            130.0            125.0       60.0   
    
        Vit_A IU  Vit_C IU  Calcium mg  Iron mg  
    65    1000.0     400.0       700.0     10.0  
       Foods  Price/ Serving          Serving Size  Calories  Cholesterol mg  \
    66   NaN             NaN  Maximum daily intake    2500.0           240.0   
    
        Total_Fat g  Sodium mg  Carbohydrates g  Dietary_Fiber g  Protein g  \
    66         70.0     2000.0            450.0            250.0      100.0   
    
        Vit_A IU  Vit_C IU  Calcium mg  Iron mg  
    66   10000.0    5000.0      1500.0     40.0  
    


```python
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

```


```python
prob = LpProblem('Diet_Problem', LpMinimize)
food_vars = LpVariable.dicts("Food",food_name,lowBound=0,cat='Continuous')
prob += lpSum([price_per_serving[i]*food_vars[i] for i in food_name])

# I then created food vars to store my referenced variabled and created my objective function, stating that I want
# to minimize the cost per serving

```


```python
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
```


```python
prob.solve()
prob. solver
LpStatus[prob.status]

print('Total Dollars Cost', prob.objective.value())

for var in prob.variables():
    if (var.value()) > 0:     
        print((var.name,var.value())) 

# finally I outputted my data, showing the results to match the homework instructions.  I dont think anyone wants to eat
# 52 servings of celery so I will continue to refine my linear program


```

    Total Dollars Cost 4.337116797399999
    ('Food_Celery,_Raw', 52.64371)
    ('Food_Frozen_Broccoli', 0.25960653)
    ('Food_Lettuce,Iceberg,Raw', 63.988506)
    ('Food_Oranges', 2.2929389)
    ('Food_Poached_Eggs', 0.14184397)
    ('Food_Popcorn,Air_Popped', 13.869322)
    


```python
food_chosen = LpVariable.dicts("Chosen",food_name,0,1,cat='Binary')

for f in food_name:
    prob += food_vars[f] >= .1 * food_chosen[f]
#making sure that there is greater than .1 of a serving choosen    
    
prob += food_chosen['Frozen Broccoli'] + food_chosen['Celery, Raw'] <= 1
#making sure that if broccoli or celery is choosen there can only be one of them choosen

prob += food_chosen['Tofu'] + food_chosen['Roasted Chicken'] + food_chosen['Scrambled Eggs'] + food_chosen['Bologna,Turkey'] + food_chosen['Frankfurter, Beef'] + food_chosen['Ham,Sliced,Extralean'] +  food_chosen['Hamburger W/Toppings'] + food_chosen['Hotdog, Plain'] + food_chosen['Pork'] + food_chosen['White Tuna in Water']  >= 3
#making sure that at least 3 different kinds of proteins are selected
```


```python
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
```

    Total Dollars Cost 4.386623892919999
    ('Chosen_Bologna,Turkey', 1.0)
    ('Chosen_Scrambled_Eggs', 1.0)
    ('Chosen_Tofu', 1.0)
    ('Food_Bologna,Turkey', 0.1)
    ('Food_Celery,_Raw', 51.828354)
    ('Food_Frozen_Broccoli', 0.24571973)
    ('Food_Lettuce,Iceberg,Raw', 65.473378)
    ('Food_Oranges', 2.3402813)
    ('Food_Poached_Eggs', 0.028699764)
    ('Food_Popcorn,Air_Popped', 13.859221)
    ('Food_Scrambled_Eggs', 0.1)
    ('Food_Tofu', 0.1)
    
