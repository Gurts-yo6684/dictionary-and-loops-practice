# this is what we will use for the video intro to dictionaries
 # dictionary = a collection of {key :value} pairs
#                ordered and changable. No duplicates

capitals = {"USA": "Washington DC",
            "India": "New Dejhi", 
            "China": "Bejing",
            "Russia": "Moscow"}
print(dir(capitals))
print(help(capitals))

print(capitals.get("India")) # This gets you the value next to the key



if capitals.get("Japan"):
    print("That capital exists")
else:
    print("That capital doesn't exist")

capitals.update({"Germany: Berlin"}) # This is used when you want to input another thing
print(capitals)

#capitals.pop("China")  # This is to remove a value
#capitals.popitem() # Removes latest item on the dictionary
#capitals.clear()
keys = capitals.keys()
print(keys)
for key in capitals.keys():
    print.key

values = capitals.values()
print(values)
for value in capitals.values():
    print(values)


items = capitals.items()
print(items)
for key, value in capitals.items():
    print(f"{key}: {value}")