# creating a dictionary
dict = {
  "Germany": "Berlin", 
  "Canada": "Ottawa", 
  "England": "London"
}

print(dict)
dict["Italy"] = "Rome"
del dict["England"]
print(dict)
for i,v in dict.items():
    print("{} {}".format(i, v))