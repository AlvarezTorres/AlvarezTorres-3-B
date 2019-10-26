#!/usr/bin/env python
# coding: utf-8

# ## Introduction to Python
# #### With this manual all programer can do and learn programing language 

# #### A Good First Program 

# The first thing that you need to do is learn how isntall a text editor, run the tex editor, run the terminal and work with both of them. After that you can start the exercise 

# In[6]:


print("First introduction to Python")
print("Hello class")
print("You can put anything that you want to print in the screen")
print("Enjoy programing")


# Your first program should look like this, don't worry about if looks diferent thats depends of your text editor some editors use differents codes or lines to do the same thing 
# It's important keep in mind the next points: 
#     

# #### Comments and Pound Characters 

# The coments are so important to your programs with that you can know what's the work of that line and other use is to desability some instructions.
# 

# In[2]:


# you can read the function of some instruction later.
print("First introduction to Python")# all coments after this are ignored
print("Hello class")
# now this is an example of how disable a code 
# print("You can put anything that you want to print in the screen")
print("Enjoy programing")


# #### Numbers and Math

# Every program could have some basic operations there are the next:
# (+ plus) (-minus)(/slash, division)(* asterisk, mutiplied by)(% percent)(< less-than)(>greater-than)(<=less-than-equal)(>=greater-than-equal)
# Now this is an example of use this operations

# In[3]:


print("I will count mony:")
print("dollars", 30*15/2*1)
print("we will count litters:")
print(3+5*2+1)
print ("Is it true that 3*5<900/2")
print(3*5<900/2)


# In[8]:


Price_Smart_phone=1500
stock_Smart_phones=50
money_in_products=Price_Smart_phone*stock_Smart_phone
print("There are the phones in stock",stock_Smart_phones)
print("The total value of the phones are:$",money_in_products)
print("This is the price by each smart phone:$",Price_Smart_phone)


# #### More Variables and Printing
# We will use "format string" (double-quotes) taking a piece of text that you have been making a *string* it is how you make something that your program might give to a human.
# Example:

# In[9]:


My_girlfriends_name='Marisol.H'
My_height=1.77 #meters
Her_height=1.5 #meters
My_name= 'Adrian.A'
print(f"The name of my girlfrien is {My_girlfriends_name}.")
print(f"She is {Her_height} meters tall.")
print(f"My name is {My_name} and I am {My_height} meters tall.")


# #### Strings and Text
# You know how works strings but in this exercise we going to create a bunch of bariables with complex strings.
# 

# In[16]:


Types_of_cars=12
Tp=f"There are {Types_of_cars} types of cars."
w="Work"
N="don't"
y=f"Those who know {w} and those who {N}."
print(Tp)
print(y)
print(f"I said: {Tp}")
print(f"I also said: '{y}'")
z= False
A="Isn't that joke so funny?!{}"
print(A.format(z))
t="This is the left side of..."
e="a string with a right side."
print(t+e)

