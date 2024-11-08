# Exercise 1a
## Description 1a
Python Print Exercises. Print "Hello World!"
### Code answer 1a
```python
print("Hello World!")
```
# Exercise 1b
## Description 1b
Now try to assign "Hello World!" to the variable my_text.
### Code answer 1b
```python
my_text="Hello World!"
print(my_text) 
```

# Exercise 2a
## Description 2a
Assign: 3 to variable glass_of_water.
### Code answer 2a
```python
glass_of_water = 3
print("I drank", glass_of_water, "glasses of water today.")
```
# Exercise 2b
## Description 2b
Let's try to see what happens after assigning a new value to our variable. Note that program gets executed line by line.Place the variable: glass_of_water inside the print function and observe what happens.
### Code answer 2b
```python
glass_of_water=glass_of_water + 1
print(glass_of_water)
```

# Exercise 3a
## Description 3a
Python Data Type Exercises. Assign an integer to the variable, then print it.
### Code answer 3a
```python
men_stepped_on_the_moon=12
print(men_stepped_on_the_moon)
```
# Exercise 3b
## Description 3b
Now a string example. Type a couple of words or a short sentence for your variable, then print it.
### Code answer 3b
```python
my_reason_for_coding="Better work chances"
print(my_reason_for_coding)
```
# Exercise 3c
## Description 3c
Let's try to see what happens after assigning a new value to our variable. Assign a float with 2 decimals to the variable below.
### Code answer 3c
```python
global_mean_sea_level_2018=21
global_mean_sea_level_2018=21.36
print(global_mean_sea_level_2018)
```

# Exercise 9a
## Description 9a
Python String Exercises. Assign the string below to the variable in the exercise.
### Code answer 9a
```python
str="It's always darkest before dawn."
print(str)
```
# Exercise 9b
## Description 9b
By using first, second and last characters of the string, create a new string.
### Code answer 9b
```python
ans_1 = str[0]+str[1]+str[-1]
print(ans_1)
```
# Exercise 9c
## Description 9c
Replace the (.) with (!)
### Code answer 9c
```python
str = str.replace(".", "!")
print(str)
```

# Exercise 10a
## Description 10a
Python Len Exercises. Using len() function find out how many items are in the list.
### Code answer 10a
```python
lst=[11, 10, 12, 101, 99, 1000, 999]
answer_1= len(lst)
print(answer_1)
```
# Exercise 10b
## Description 10b
len() function can also tell the length of a string.
### Code answer 10b
```python
msg="Be yourself, everyone else is taken."
msg_length= len(msg)
print(msg_length)
```
# Exercise 10c
## Description 10c
How many keys are there in the dictionary?
### Code answer 10c
```python
dict={"Real Madrid": 13,"AC Milan": 7,"Bayern Munich":5 ,"Barcelona": 5, "Liverpool": 5}
ans_1= len(dict)
print(ans_1)
```

# Exercise 11a
## Description 11a
Python Sort Exercises. Sort the list in ascending order with .sort() method.
### Code answer 11a
```python
lst=[11, 100, 99, 1000, 999]
lst.sort()
print(lst)
```
# Exercise 11b
## Description 11b
This time sort the countries in alphabetic order.
### Code answer 11b
```python
lst=["Ukraine", "Japan", "Canada", "Kazakhstan", "Taiwan", "India", "Belize"]
lst.sort()
print(lst)
```
# Exercise 11c
## Description 11c
Now sort the list in descending order with .sort() method.
### Code answer 11c
```python
lst=[11, 100, 101, 999, 1001]
lst.sort(reverse=True)
print(lst)
```

# Exercise 12a
## Description 12a
Python Pop Exercises. Python pop method of lists and dictionaries. Pop the last item of the list below.
### Code answer 12a
```python
lst=[11, 100, 99, 1000, 999]
popped_item=lst.pop()
```
# Exercise 12b
## Description 12b
Python pop method to remove last list item. Remove "broccoli" from the list using .pop and .index methods.
### Code answer 12b
using .pop
```python
lst=["milk", "banana", "eggs", "bread", "broccoli", "lemons"]
item= lst.pop(4)
print(lst, item)
```
using .pop and .index
```python
lst=["milk", "banana", "eggs", "bread", "broccoli", "lemons"]
x= lst.index("broccoli")
item= lst.pop(x)
print(lst, item)
```
# Exercise 12c
## Description 12c
Pop method also saves the item being removed. Save Italy's GDP in a separate variable and remove it from the dictionary.
### Code answer 12c
```python
GDP_2018={"US": 21, "China": 16, "Japan": 5, "Germany": 4, "India": 3, "France": 3, "UK": 3, "Italy": 2}
italy_gdp = GDP_2018.pop("Italy")
print(GDP_2018)
print(italy_gdp, "trillion USD")
```