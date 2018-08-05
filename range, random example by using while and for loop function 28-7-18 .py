
# coding: utf-8

# In[1]:


#narasimha.ee@gmail.com
# range, rnadom functions examples
for i in range (10,-10):
    print('number',i)
# this programe cannot excute because the range function will ascending order only 
# if you want excute place third number -1 then excute 


# In[2]:


for i in range (10,-10,1):
    print('number',i)


# In[4]:


for i in range (10,-10,-1):
9    print('number',i)


# In[5]:


for i in range(-6,7):
    print(i,end=' ')


# In[8]:


n=int(input('enter anumber'))
for n in range(-n,n+1):
    print(n,end=' ')


# In[9]:


import random as r
a=r.randint(1,20)
b=r.randint(1,10)
c=int(input('what is the value of '+ str(a)+'+'+ str(b)+':'))
if c==a+b:
    print ('congrats you won')
else:
    print('sorry you lost bad luck try once again ')


# In[11]:


import random as r
a=r.randint(1,6)
b=int(input('dice rolled guess your number from 1 to 6:'))
if a==b:
    print('jackpot you won')
else:
    print('number on the dice is',a)
    print('sorry you lost')


# In[3]:


import random as r 
a=int(r.randint(1,2))
if a==1:
    A='HEADS'
else:
    A='TAILS'
b=input('coin tossed heads(h) or tails(t):')
if b=='h':
    B='HEADS'
else:
    B='TAILS'
if A==B:
    print('congrats you won the toss its:',B)
else:
    print('sorry you lost the toss its:',A)


# In[67]:


import random as r

a = int(r.randint(1,2))

if a == 1:
    A = 'HEADS'
else:
    A = 'TAILS'
    
b = input('coin tossed..heads(h) or tails(t) : ')

if b == 'h':
    B = 'HEADS'
else:
    B = 'TAILS'
    
    
if A == B:    
    print('CONGRATS you won the toss its :', A)
else:    
    print('SORRY you lost the toss its :', A)


# In[9]:


# entering * in a unique order means incrementing order using for in for loop
n=int(input('enter a number'))
for i in range(1,(n+1)):
    for j in range(1,(i+1)):
        print('*',end=' ')
    print()


# In[11]:


# first it completes inner loop for n-1 times then it goes to outer loop. assume column is i row is j
n=int(input('enter a number'))
for i in range(1,(n+1)):
    for j in range(1,(n+1)):
        print(i*j,end=' ')
    print()


# In[12]:


n=int(input('enter a number'))
for i in range(1,(n+1)):
    for j in range(1,(n+1)):
        print('*',end=' ')
    print()
# range 1 to 6 means it prints upto 5 only


# In[13]:


for n in range(1,10):
    print(n,end=' ')


# In[ ]:


for i in range (10,-10):
    print('number',i)
# this programe cannot excute because the range function will ascending order only 
# if you want excute place third number -1 then excute 


# In[14]:


'''entering * in a unique order means decrementing order using for in while loop 
because for loop can not work in decending order thats way i am using for with in while loop'''
n=int(input('enter a number'))
i=n
while i>=1:
    for j in range(1,(i+1)):
        print('*',end=' ')
    print()
    i-=1

