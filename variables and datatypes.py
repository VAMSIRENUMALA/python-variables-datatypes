#!/usr/bin/env python
# coding: utf-8

# In[ ]:


### Rules for naming variable


# In[1]:


course = 'Artificial intelligence and machine learning'


# In[21]:


course


# In[22]:


print(course)


# In[19]:


_names="vamsi","chari"


# In[20]:


_Names


# #### python is case sensitive
# #### variables are also case sensitive

# In[10]:


_names


# #### variables can start with only one symbol is underscore '_'

# In[13]:


roll no = '20jr1a05g9'
roll no


# #### variables shouldn't contain spaces

# In[16]:


9name=vamsi
9name


# #### variables shouldn't start with numbers

# ### Data Types

# In[24]:


x=17
type(x)


# #### int-integer(no decimal point)

# In[25]:


x=17.9
type(x)


# #### float-decimal point

# In[30]:


x=True
y=False
type(x)


# In[31]:


type(y)


# ##### bool-boolean-True/False

# In[32]:


course="AIML"
type(course)


# #### string-text/char

# In[33]:


y=1-2j
type(y)


# #### complex-with j(imaginary)

# #### Explicit Conversion

# #### on Int

# In[1]:


x=10
y=float(x)
y


# In[2]:


x=10
y=str(x)
y


# In[3]:


x=10
y=bool(x)
y


# In[4]:


x=10
y=complex(x)
y


# #### on complex

# In[5]:


p=4+3j
q=int(p)
q


# In[6]:


p=4+3j
q=float(p)
q
p


# In[7]:


p=4+3j
q=float(p)
q
p


# In[8]:


p=4+3j
q=str(p)
q
p


# #### complex datatype is only converted into String

# #### on float 

# In[10]:


y=3.90
p=int(y)
p


# In[11]:


q=complex(y)
q


# In[12]:


p=bool(y)
p


# In[13]:


p=str(y)
p


# #### on String

# In[14]:


m="abd"
n=int(m)
n


# In[15]:


m="abd"
n=float(m)
n


# In[16]:


m="abd"
n=complex(m)
n


# In[17]:


m="abd"
n=bool(m)
n


# #### String is only converted into boolean

# In[ ]:




