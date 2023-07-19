#!/usr/bin/env python
# coding: utf-8

# ## Assignment-1: Operators | Loops
# ## Q1. Write a Python program to get the Fibonacci series between 0 to 50
# 
# # Note : The Fibonacci Sequence is the series of numbers :
# 
# # 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
# 
# # Every next number is found by adding up the two numbers before it.
# 
# # Expected Output : 1 1 2 3 5 8 13 21 34

# In[2]:


a = 0
b = 1

while b<=50: 
    print(b, end=" ")
    a,b=b,a+b


# ## Q2. Write a Python program that accepts a word from the user and reverse it.
# # Sample Test Case
# 
# 
# 
# # Input : Edyoda
# 
# # output: adoydE

# In[3]:


variable = input("Please input a word to reverse:")

for value in range(len(variable)-1, -1, -1):
    print(variable[value], end="")
print()


# ## Q3. Write a Python program to count the number of even and odd numbers from a series of numbers.
# 
# 
# 
# # Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
# 
# # Expected Output :
# 
# # Number of even numbers : 4
# 
# # Number of odd numbers : 5

# In[2]:


numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) # Declaring the tuple
count_odd = 0
count_even = 0
for x in numbers:
        if x % 2 == 0:
    	     count_even+=1
        else:
    	     count_odd+=1
print("Number of even numbers :",count_even)
print("Number of odd numbers :",count_odd)


# In[ ]:




