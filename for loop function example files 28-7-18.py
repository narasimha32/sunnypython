
# coding: utf-8

# In[18]:


#narasimha.ee@gmail.com, 8555818296
# using for loop writing same message to number of persons
friendsname=['sushmitha','venki','ramesh','raju','suri','masthan','mothi','pavani']
for friends in friendsname:
    print('HI',friends,'Happy Friendship day')

print('Happy Friendsship day to all my friends')


# In[1]:


# friendship wishes to my family members
familyfriendsnames=('amma','nana','sushmitha','bava','akka','harikrishna mama','sudha akka','madhu mama','sushma akka','narayana mama','rama devi','naveen','swarna','chiini','sunil','lucky','kumar','mamatha','suhan','pandu')
for family in familyfriendsnames:
    print('Hi my dear family members',family,'Happy Friendsip Day')


# In[4]:


# friendship day wishes to future data scientists 
datascientistsnames=('pradeep sir','harsha anna','santhos','narendra','lilu','wamiq','ajaz')
for friends in datascientistsnames:
    print('Hi my dear future data scientists Happy Friendsip Day',friends)


# In[3]:


#prime numbers from 1-1001 using for and while loop 
for num in range(1,1001):
    fcount=0
    i=1
    while i<=num:
        if num%i==0:
            fcount+=1
        i+=1
    if fcount==2:
        print(num,end=' ')


# In[ ]:


for num in range(1001,10001):
    n=int(input('enter a number'))
    num1=num
    s=0
    while num>0:
        r=num%10
        s=s+(r**n)
        num=num//10
        if s==num1:
            print(num1,end=' ')
# plz resolve the the problem


# In[11]:


#prime numbers from 1-101 using for and while loop 
for num in range(1,101):
    fcount=0
    i=1
    while i<=num:
        if num%i==0:
            fcount+=1
        i+=1
    if fcount==2:
        print(num,end=' ')


# In[1]:


#armstrong numbers 1001-10001 using for and while loop 
for num in range(1001,10001):
    num1=num
    s=0
    while num>0:
        r=num%10
        s=s+(r**4)
        num=num//10
        if s==num1:
            print(num1,end=' ')


# In[5]:


# entering * in a unique order means incrementing order using for in for loop
n=int(input('enter a number'))
for i in range(1,(n+1)):
    for j in range(1,(i+1)):
        print('*',end=' ')
    print()


# In[7]:


# entering * in a unique order means decrementing order using for in while loop
n=int(input('enter a number'))
i=n
while i>=1:
    for j in range(1,(i+1)):
        print('*',end=' ')
    print()
    i-=1


# In[9]:


#break fuction 
i=1
while i<=10:
    if i==5:
        break
    print (i)
    i+=1


# In[10]:


#continue function
i=1
for i in range(1,11):
    if i==5:
        continue
    print(i)


# In[12]:


#continue function
i=1
for i in range(1,11):
    if i==5:
        continue
    print(i,end=' ')

