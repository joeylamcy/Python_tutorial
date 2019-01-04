
# coding: utf-8

# # Sample script 

# ![script_breakdown](./images/script_breakdown.png)

# # Comments
# Important to code readability! If you are collaborating with others, good comments should guide other people through your code. If you are doing a long project, you also need comments for yourselves to read when you revisit after a long time. 
# Therefore, you are **required** to write comments to build up this habit.

# # Basic statements
# - Assignment statements: `variable = value`
#     - `=` is assignment operator, *value* on the RHS of `=` is **assigned** to the *variable* on LHS.
#     - The *value* does not have to be an exact number, it can be obtained through an operation. (More about the types of *value* later)
#     - Let you figure out the rules on variable naming.
# - Print statements: `print('*what you want to print*')`
#     - `print` is the function name. A function should be followed with a pair of brackets
#     - Inside the brackets, you can put anything (normally a "*string*" or a *variable*)
# - (Command line only) "peek" statements: `variable` (not recommended)
#     - Type the *variable* in command line mode to see its assigned value quickly.

# # Data types of *value*

# In[1]:


# Integers
print(type(1))

# Float 
print(type(1.0))

# Complex
print(type(1.0+1.0j))

# Strings (characters)
print(type('Happy New Year!'))

# Boolean (True or False)
print(type(True))

# And many others not covered in this lab...


# # Arithmetics

# In[2]:


# Addition 
print(2+3.4) # => 5.4

# Subtraction
print(1.6-5.7) # => -4.1

# Multiplication 
print(3*4) # => 12

# Division
print(5/2) # => 2.5
# Note that unlike Python 2.X, Python 3.X always gives a floating point number, i.e. same as 5.0/2.0

# Floor division
print(5//2) # => 2
# i.e. no fractional part

# Modulus 
print(5%2) # => 1
# i.e. remainder after floor division

# Power 
print(2**3) # => 8


# # Organization types of *value*
# It is impractical to always use single values, especially when you have a large amount of data to process. Therefore you need to learn how to **group/organize** the values. 
# - List: `[value1, value2, value3]`
#     - List is defined by square brackets `[]`.
#     - Elements in a list are ordered. They are indexed by consecutive numbers.
#     - You can put values in a list. They should be delimited (separated) by `,`.
#     - Spaces are generally not important, some people use them to align different lines for better appearance.
#     - *Note: strings are actually list of characters.*
# - NumPy arrays: `numpy.array([value1, value2, value3])`
#     - NumPy arrays are like lists, but better supports multiple dimension structure, and faster numerical calculations.
#     - You have to load the NumPy library in order to use it. (e.g. `import numpy`) 
#     - Don't worry, there are easier ways to initialize them.
# - Dictionary: `{key1: value1, key2: value2, key3: value3}`
#     - Dictionary is defined by curly brackets `{}`.
#     - Elements in a dictionary are unordered. They are indexed by keys. 
#     - You can put pairs of key and value in a list.
#     - The pair should be formatted as `key:value`. Each pair is delimited (separated) by `,`.
#     - Each key should be unique to others.
# There are more, such as tuple and iterable, but not very important for beginners.
# 
# Note: actually they are still called data types in Python language. I just think that conceptually they are different. 

# ## How to access the values in a list (and NumPy array)?
# You can use index to refer to an element/value inside a list or dictionary. You can also refer to multiple consecutive elements/values through index slicing.
# 
# Syntax: `value = list[index]`
# 
# Index slicing rules: `start:end:stride`
# 1. Index start at the beginning from 0, or at the end from -1 (counting backwards). (see below) 
# 1. The `start` index is inclusive, while the `end` index is exclusive.
# 1. `stride` means the difference of the current and next indices. It can be negative (reverse the order).
# 1. Actually you can think of `end` and `stride` as optional arguments:
#     - when you only provide `start`, only the element at index `start` is returned.
#     - when you provide `start:end`, elements at indices `start`, `start+1`, ..., `end-2`, `end-1` are returned.
#     - when you provide `start:end:stride`, elements from indices `start`, `start+stride` onwards and before the `end` are returned

# In[3]:


# First assign a list to a variable and print it to screen
fruits = ['apple', 'orange', 'banana', 'grape', 'strawberry'] 
# index:     0         1         2         3          4
# index:    -5        -4        -3        -2         -1
print(fruits)


# In[4]:


# To access 'apple', we can use index 0 or -4
print(fruits[0])    
print(fruits[-5])    


# In[5]:


# To access 'apple', 'orange' and 'banana', you can use index slicing.
print(fruits[0:3])   
print(fruits[:3])   # If the index start from 0, you can omit it
print(fruits[0:-2]) # You can mix the two counting methods


# In[6]:


# To access all elements from 'orange' onwards, you can use a large index at the end, or simply omit it
print(fruits[1:])
print(fruits[1:9999])


# In[7]:


# To skip indices, you can use stride
print(fruits[::2])  # indices 0,2,4,6,8,etc. but indices from 6 onwards do not exist
print(fruits[:4:2]) # indices 0,2 (4 is exclusive)
print(fruits[::3])  # indices 0,3,6,9,etc. but indices from 6 onwards do not exist


# In[8]:


# To reverse the order, you can use a negative stride in index slicing
print(fruits[::-1])
print(fruits[:1:-1])


# ## How to add/modify/delete elements in a list (and NumPy array)?

# In[9]:


# To replace the 1st element by 'mango'
fruits[0] = 'mango'
print(fruits)


# In[10]:


# To add 'apple' to the end of list
print(fruits + ['apple']) # Note that I didn't change the list "fruits" here.
# Alternative:
fruits.append('apple') # Note that the list "fruits" is changed here.
print(fruits)
# It might not be a good idea to use append() in any command-line interfaces (CLIs)
# because repeating the operation gives different results.


# In[11]:


# To delete a value, you may use the funtction del()
del(fruits[-1])
print(fruits)


# In[12]:


# To insert 'apple' in between the 2nd and 3rd elements (of the appended list)
print(fruits[0:2] + ['apple'] + fruits[2:])


# ## How to access values in a dictionary?
# Remember that dictionary contains key-value pairs? Since they are indexed by keys, you can use key to access them.
# 
# Syntax: `value = dictionary['key']`

# In[13]:


# First assign a dictionary to a variable and print it to screen
site_info = {'Name':'Hong Kong', 'lat':22.3, 'lon':114.2, 'Time zone':'UTC+8', 'Currency':'HKD'}
print(site_info)


# In[14]:


# There are different syntax to access the values.
print(site_info['Name'])
print(site_info.get('Name'))


# In[15]:


# You can print out all keys and values
print(site_info.keys())
print(site_info.values())


# ## How to add/modify/delete elements in a dictionary?
# They are basically done in similar fashion as above: `dictionary['key'] = value`

# In[16]:


# To add a new key-value pair, e.g. 'country calling code': '+852'
site_info['Country calling code'] = '+852'
print(site_info)


# In[17]:


# To modify one of the existing key-value pair, e.g. refine 'lat': 22.3 into 'lat': 22.29
site_info['lat'] = 22.29
print(site_info)


# In[18]:


# To delete one of the existing key-value pair, e.g. 'Country calling code': '+852'
del(site_info['Country calling code'])
print(site_info)


# # Functions
# You have used several *functions* previously, but what is a function? 
# 
# A function is a block of organized, reusable code that is used to perform a single action. You may think of a function as a toaster. If you put a piece of bread in (input), it will heat the bread, and return the toast (output) to you. Moreover, as long as the input (a piece of bread) is the same, it will return the same output (a toast) to you. Therefore when you know that an action will be performed quite frequently, you may consider writing a function.
# 
# In Python, there are many pre-defined functions, e.g. `len()`, `range()`, `del()`, `print()`, etc... It is not practical to remember all of them, and thus **you need Google, and you also need to learn how to Google**.
# 
# On the other hand, you can also write your own function to do some specific action. It's quite simple. 
# 
# Syntax: (to define a function)
# ```Python
# def function1(input1, optional2=default):
# 
#     statement1 
# 
#     return output1
# ```
# Syntax: (to call a function, use either one of them)
# ```Python
# function(value1)
# function(value1,value2) 
# function(value1,optional2=value2)
# ```
# 
# Several points to note:
# 1. Start with keyword **def** to define a function
# 1. *input1* is the required input (argument) here. However, a function can be defined without any input.
# 1. *optional2* becomes an optional input (argument) because a default value is provided. Optional argument must come after **all** required inputs. 
# 1. The first line ends with a colon (:). Any lines afterwards should be preceded with a tab character.
# 1. At the last line, use keyword **return** followed by what you want to output. However, you may leave *output1* blank if there is no output. 

# ### Example: insert function for a list

# In[19]:


# Let's define a function to insert a new element after index n of a list, and return the new list
def insert(old_list,element,n):
    return old_list[:n] + [element] + old_list[n:]


# In[20]:


# Take a look at the list again before we use
print(fruits)


# In[21]:


# Again, let's insert 'apple' after 'orange'
fruits_new = insert(fruits,'apple',1)
print(fruits_new)


# 
# Next part: [Writing a Python script](./Part2_Writing_Script.ipynb)
