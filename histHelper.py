#****************************
# HW2 solution
#****************************

#*************************************************************************
# isNumericList(x)
# return True only if all items in the input list is numeric type
# i.e. float or integger
#
# inputs:
#   x: a list of integer or float
#
# returns: True if all items in x is numeric type, otherwise return False
#*************************************************************************
def isNumericList(x):
   for i in x:
      if not isinstance(i,int) and not isinstance(i,float):
         return False
   return True

#*************************************************************************
# checkInput(x)
# raise ValueError when error check failed.
#
# inputs:
#   x: anything
#
# returns: raise ValueError if
#          x is not a list or
#          x is empty list or
#          not all element in x is numeric
#*************************************************************************
def checkInput(x):
   if not isinstance(x,list):
      raise ValueError("input must be list")
   if len(x)==0:
      raise ValueError("input cannot be empty list")
   if not isNumericList(x):
      raise ValueError("element in list must be integer/float")      

#*************************************************************************
# calMax(x)
# returns the maximum value in x
#
# inputs:
#   x: a list of integer or float
#
# returns: the maximum value in x
#   
# example: 
# >>> calMax([1,2,3]) 
# >>> 3
#*************************************************************************
def calMax(x):
   checkInput(x)
   result = x[0]
   for i in range(1,len(x)):
      if x[i] > result:
         result = x[i]
   return result
   
#*************************************************************************
# calMin(x)
# returns the minimum value in x
#
# inputs:
#   x: a list of integer or float
#
# returns: the minimum value in x
#   
# example: 
# >>> calMin([1,2,3]) 
# >>> 1
#*************************************************************************
def calMin(x):
   checkInput(x)
   result = x[0]
   for i in range(1,len(x)):
      if x[i] < result:
         result = x[i]
   return result

#*************************************************************************
# mySort(li)
# sort the input numeric list in increasing order
#
# inputs:
#   li: a list of numeric elements
#
# returns: a sorted list
#*************************************************************************
def mySort(li):
   if len(li)==1:
      return li
   else:
      minVal = calMin(li)
      for i in range(len(li)):
         if li[i]==minVal:
            return [minVal] + \
                   mySort(li[:i]+li[i+1:])

#*************************************************************************
# calSum(x)
# returns the sum of x
#
# inputs:
#   x: a list of integer or float
#
# returns: the sum value of x
#   
# example: 
# >>> calMean([1,2,3,4]) 
# >>> 10
#*************************************************************************
def calSum(x):
   checkInput(x)
   s = 0
   for i in x:
      s+=i
   return s

#*************************************************************************
# calMean(x)
# returns the mean (i.e. average) of x
#
# inputs:
#   x: a list of integer or float
#
# returns: the mean (i.e. average) value of x
#   
# example: 
# >>> calMean([1,2,3,4]) 
# >>> 2.5
#*************************************************************************
def calMean(x):
   return calSum(x)/len(x)

#*************************************************************************
# calMedian(x)
# returns the median (i.e. when sorted in order, the middle value) of x.
# If there are an even number of items in x, the median would be the 
# average between the middle two items.
#
# inputs:
#   x: a list of integer or float
#
# returns: the median of x
#   
# example: 
# >>> calMedian([1,2,3,4]) 
# >>> 2.5
# >>> calMedian([1,2,3,4,5,6,7])
# >>> 4
#*************************************************************************
def calMedian(x):
   checkInput(x)
   sortedLi = mySort(x)
   midPoint = len(x)/2
   if len(x)%2==0:
      return calMean(sortedLi[int(midPoint-1):int(midPoint+1)])
   else:
      return sortedLi[int(midPoint)]
   
#*************************************************************************
# histHelper(x, breaks)
# returns a list containing the number of items falling into various bins
# defined by breaks.  “breaks” divides the full range of values of x (i.e.
# minimum to maximum value of x) into equal bins.  For example, given the
# range of 0 to 100, if breaks=4, the bins would corresponds to {0 to 25},
# {>25 to 50}, {>50 to 75} and {>75 to 100}
#
# inputs:
#   x: a list of integer or float
#   breaks: an integer indicating how many bins to divide the items in x
#
# returns: a list containing counts of items in each bin
#   
# example: 
# >>> histHelper([1,2,3,4,5,5,5,6,7,8,9],3) 
# >>> [3,5,3]
# >>> histHelper([1,2,3,4,4,4,5,6,7],2)
# >>> [6,3]
#*************************************************************************
def histHelper(x,breaks):
   checkInput(x)
   sortedLi = mySort(x)
   bk = (sortedLi[len(x)-1] - sortedLi[0])/breaks
   result = []
   for i in range(breaks):
      # note: the first bin includes the min value,
      # therefore, need the "- (1 if i==0 else 0)"
      l = sortedLi[0]+bk*(i) - (1 if i==0 else 0)
      u = sortedLi[0]+bk*(i+1)
      result = result + [calSum([j>l and j<=u for j in x])]
   return(result)
