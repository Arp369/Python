Programming_dictionary ={
    "Bug":"An error in the program that prevents the program from running as expected.",
    "Function":"A piece of code that you can call it over and over again.",
    "Loop":"The action of doing something again and again"
}

#Retriving data from dictionary
print(Programming_dictionary["Bug"])

#Adding data to the dictionary
Programming_dictionary["Datatype"] = "It defines the type of Data."
print(Programming_dictionary)

#Create an empty Dictionary
# empty_dictionary = {}

#Edit an empty dictionary
Programming_dictionary ["Bug"] = "A moth in your computer."
print(Programming_dictionary)

# #Wipe an existing dictionary
# Programming_dictionary = {}
# print(Programming_dictionary)

#Loop through the dictionary
for key in Programming_dictionary:
    print(key)
    print(Programming_dictionary[key])

##############################################
    
#Nesting 
Capitals = {
    "France" : "Paris",
    "Germany": "Berlin",
}

#Nesting lists in a dictionary

travel_log = {
    "France":{"cities_visited" : ["Paris", "Lille","Dijon"], "total_visits":12},
    "Germany" : {"citis_visited": ["Berlin","Hamburg"], "total_visits": 5}
}

#NEsting a dictionary in a list
travel_log = [
    {
        "country":"France",
        "cities_visited" : ["Paris", "Lille","Dijon"],
        "total_visits":12
    },
    {
        "country":"Germany" ,
        "citis_visited": ["Berlin","Hamburg"],
        "total_visits": 5
    }
]
