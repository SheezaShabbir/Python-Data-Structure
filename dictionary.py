thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
#dictionary is pair of key and value
#Access item using key
print(thisdict["model"])
#another get method
print(thisdict.get("model"))
thisdict["year"]=2018#updating method
#Print all key names in the dictionary, one by one:
for x in thisdict:
  print(x)
#Print all values in the dictionary, one by one:
for x in thisdict:
  print(thisdict[x])
#You can also use the values() function to return values of a dictionary:
for x in thisdict.values():
  print(x)
#Example
#Loop through both keys and values, by using the items() function:
for x, y in thisdict.items():
  print(x, y)
#The dict() Constructor
#It is also possible to use the dict() constructor to make a dictionary:

#Example
thisdict = dict(brand="Ford", model="Mustang", year=1964)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(thisdict)
