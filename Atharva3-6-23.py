#!/usr/bin/env python
# coding: utf-8

# Atharva Kishor Salaskar

# In[13]:


#Q.1
#1
Set={"January",1,1,85,"Sunday","Sunday"}
Set


# In[16]:


Dict={"Day":"Sunday","Date":"16","year":2014,"Year":2014}
Dict


# In[33]:


#2

n=3
for i in range(n):
    print("",end= " ")
    for j in range(i+1):
        print("*",end=" ")
    print('')


# In[39]:


#3

i=1
n=5
while i<=n:
    print(i)
    i+=1


# In[41]:


#4

x=5;y=6

x,y=y,x
print(x)
print(y)


# In[45]:


#5

def Add(a,b):
    sum=a+b
    print('Sum =',sum)

Add(2,3)


# In[50]:


#6

l=list(range(1,11))
s=[number**2 for number in l]
print(s)


# In[55]:


#7

class Animal:
    def speak(self):
        print("I am an animal!")

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

# Create an instance of each class
dog = Dog()
cat = Cat()


# In[ ]:


# 8

#A card is drawn from an ordinary pack of 52 playing cards.
What is the probability that is a king;given that it is a face card

#10
Hypothesis Testing is a type of statistical analysis in which you put your assumptions about a population parameter to the test.
It is used to estimate the relationship between 2 statistical variables.

P values are used in hypothesis testing to help decide whether to reject the null hypothesis.#Q.2

Bernoulli Distribution-
P(x)=p^x*q^(1-x) 
eg-A student appering for exam.He passes or fails

Binomial Distribution-
P(x)=nCx*p^x*q^(n-x)
eg-No of rainy days in a month

Uniform Distribution-


# In[ ]:




