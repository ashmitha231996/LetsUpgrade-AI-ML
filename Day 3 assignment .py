#!/usr/bin/env python
# coding: utf-8

# Write a program to subtract two complex numbers in Python.
# 

# In[1]:


a=(4+3j)
b=(3-7j)
c=a-b
print(c)


# Write a program to find the fourth root of a number.
# 

# In[18]:


a=int(input("enter the number "))
p=pow(a,(4));
print("Fourth Root of a is",p)


# Write a program to swap two numbers in Python with the help of a temporary variable

# In[19]:


x = input('Enter value of x: ')
y = input('Enter value of y: ')

# create a temporary variable and swap the values
temp = x
x = y
y = temp

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))


# Write a program to swap two numbers in Python without using a temporary variable.
# 

# In[21]:


x = 5
y = 10
x = x + y   

y = x - y  
  
x = x - y   
print("After Swapping: x =", x, " y =", y); 
  


# Write a program to convert fahrenheit to kelvin and celsius both

# In[23]:


def Fahrenheit_to_Kelvin(F): 
    return 273.5 + ((F - 32.0) * (5.0/9.0)) 
  
F = 100
print("Temperature in Kelvin ( K ) = {:.3f}" 
            .format(Fahrenheit_to_Kelvin( F ))) 


# In[25]:


celsius = float(input("Enter temperature in celsius: ")) 
fahrenheit = (celsius * 9/5) + 32 
print("%.2f Celsius is: %0.2f Fahrenheit" %(celsius, fahrenheit))


# Write a program to demonstrate all the available data types in Python. Hint: Use type() function.

# In[26]:


a = 5
print(a, "is of type", type(a))

a = 2.0
print(a, "is of type", type(a))

a = 1+2j
print(a, "is complex number?", isinstance(1+2j,complex))


# In[ ]:




