set1={"1","2","3","Hassan","Aliza"}
for x in set1:
    print(x)
set1.add("OK")
set1.update(["grapes","milk","boold"])
print(len(set1))
set1.remove("boold")#if item does not exist it will give error
set1.discard("grapes")#if item does not exist not give error
del set1 #it will delete whole set
set1.clear() #it will clear
thisset=set(("ok","NO"))#its the constructor of the set
