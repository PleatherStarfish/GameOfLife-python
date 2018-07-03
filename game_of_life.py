
# coding: utf-8

# In[43]:


import random

twodArray = []
rowList = []
startingChanceOfLife = 2

def weightedRandom(weight):
    randomInt = random.randint(0, 100)
    returnedInt = 0 if randomInt > weight else 1
    return returnedInt

for cols in range(0, 9):
    rowList = []
    for rows in range(0, 9):
        if (weightedRandom(startingChanceOfLife) == 1):
            rowList.append("x")
        else:
            rowList.append("o")
        
    twodArray.append(rowList)

print(twodArray[0][0])

    


# In[49]:


n = 3
m = 4
a = [[1] * m] * n
a[0][0] = 5
print(a)

