myDict = {
            "Fast" : "In a quick manner",    
            "Pooja" : "A girl name",
            "Marks" : [1,2,5],
            "anotherdict" : {"Harry" : "Player"}
            # 1: 2

        }

# print(myDict["Fast"])
# print(myDict["Pooja"])
# print(myDict["Marks"])
# print(myDict["anotherdict"]["Harry"])  #Nested Dictionary
# print(myDict[1])

# print(myDict.keys());
# print(list(myDict.keys()));
# print(myDict.values());
# print(myDict.items());
# updateDict = {"Lavish" : "Friend"} 
# myDict.update(updateDict)
# print(myDict)

print(myDict.get("Pooja"))  #Print value associated with key "Pooja"
print(myDict["Pooja"])      #Print value associated with key "Pooja"

#The Difference between .get and [] syntax in the dictionaries

print(myDict.get("Pooja1")) #Returns None as "Pooja1" is not present in the dictionary 
print(myDict["Pooja1"])     #Throws an Error as "Pooja1" is not present in the dictionary   
