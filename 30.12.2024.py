#automatic garbage collection
import sys #system module
a=[1,2,3]
ref_count=sys.getrefcount(a)
print("Reference count is:",ref_count)

#by using another variable
import sys
a=[]#First the count is 2
b=a# after maping "b"  with "a" the reference count is increased by 1 .if "c" is given the reference count will be 4 .Here reference count is 3
print("Reference count is :",sys.getrefcount(a))


import gc #it will show how many objects are collected here there is no program after import gc so collected garbage is 0
collected=gc.collect()
print(f"Garbage collector {collected} objects")



import gc
gc.enable()
gc.disable()
l1=[1,2,3]
d1={'a':1,'b':2}
s1="Garbage collection"
del l1
del d1
del s1
print("Current Threshold",gc.get_threshold())
collected=gc.collect()
print(f"Garbage Collector colleceted {collected} objects")


