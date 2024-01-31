#imports
from datetime import date
print("Hello World!")
print(date.today())



#  #imports the sys module
# import sys 
# print(sys.argv) #Printing all command-line arguments:
# print(sys.argv[0]) #Printing all command-line arguments:
# print(sys.argv[1])





# #for loops and while loops
# #================while loop==============
# user_input=""
# inputs=[]
# while user_input.lower()!="done":
#     user_input=input("Enter a value or done.")
#     if user_input.lower() !="done":
#         inputs.append(user_input)
        
# print(inputs)
# print("======================================")


# #================ for loop=================
# from time import sleep
# countdown =[1,2,3,4,5,6,7,7]
# for number in countdown:
#    print(number)
#    sleep(1)#time it takes to print next value
# print("Blast off!!")


# #=============strings methods==========
# ++++++++ways to format string:++++++++++++++++++++++++
#                  1.using % formatter.
#                  2.using format() in string.
#                  3.using f-strings.



# ===================#title()it displays string in caps
# name="gideon kipkorir yegon"
# print(name.title())

# #=================split() it separates the string at every space.
# print(name.split()) 


#======================= #find() and count() it searches for a string.
# temperatures="Saturn has a daytime temperature of -170 degrees Celcius, while Mars has -28 celsius."
# print(temperatures.find("Moon"))
# print(temperatures.count("Mars"))


#======================== #lower() and upper()it converts string to lowercase characters
# text="The Moon and the Earth"
# print(text.lower())
# print(text.upper())
# ==========================#format()
# mass_percentage="1/6"
# print("""You are lighter on the {moon},because on the {moon} youwould weigh about {mass}of weight on Earth.""".format(moon="Moon", mass=mass_percentage))


# #----------------python lists--------------------------
# planets=["Mercury","Venus","Earth","Mars","Jupyter","Saturn","Uranus","Neptune"]
# print(planets)
# print("The First planet is ", planets[0]) #Access list items by index
# #assigning a new value to a python list
# planets[3]="Red planet"
# print("mars is",planets[3])
# #Determine the length of a list
# number_of_planets=len(planets)
# print("The number of planets is", number_of_planets)
# #Appending values to a list
# planets.append("pluto")
# #Remove values from lists
# planets.pop()
# print(planets)
# #Use negative indexes
# print("The last planet is ",planets[-1])
# #Find a value in a list
# jupyter_index=planets.index("Jupyter")
# print("Jupiter is the ", jupyter_index + 1, "from the sun" )


# #Store numbers in lists
# gravity_on_planets=[1.54,2.66,3.655,4.785,5.89,6.88,7.77,8.455]
# print("The snallest gravity in the solar system is;", min(gravity_on_planets))
# print("The largest gravity on earth is:", max(gravity_on_planets))

# #Slice lists
# planets_before_earth=planets[0:2]
# print(planets_before_earth)


# #Join lists
# amalthea_group = ["Metis", "Adrastea", "Amalthea", "Thebe"]
# galilean_moons = ["Io", "Europa", "Ganymede", "Callisto"]

# regular_setlite_moons = amalthea_group +galilean_moons
# print(regular_setlite_moons)

# #Sort lists
# regular_setlite_moons.sort() #ascending order
# regular_setlite_moons.sort(reverse=True) #descending order

# print(regular_setlite_moons)


# #===========================python functions===============================
# #Functions with no arguments
# def myname():
#     print("Gideon Kipkorir Yegon")
# #output=
# myname()
# #output is None

# def rockets_parts():
#     return "propellant, payload, structure"

# rockets_parts()
# #output
# #required arguments
# any([True,False,False])
# #optional arguments
# str()
# str(15)

# #requiring an argument
# def distance_from_earth(destination):
#     if destination =="moon":
#         return "238.855"
#     else:
#         return "Unable to compute to tha destination"
    
# distance_from_earth("moon")
# #multiple equired argments
# def days_to_complete(distance,speed):
#     hours=distance/speed
#     return hours/24
# days_to_complete(238855,75)
# #functions as arguments
# round(days_to_complete(23885575,75))
# #using keyword arguments
# from datetime import timedelta,datetime
# def arrival_time(hours=51):
#     now=datetime.now() #datetime moduledefine the curent time.
#     arrival=now+timedelta(hours=hours) #timedelta module allow the addittion operation that results in new time object. 
#     return arrival.strftime("Arrival:%A %H:%M")
# arrival_time()

# #mixing arguments and keyword arguments
# from datetime import timedelta,datetime
# def arrival_time( destination,hours=51):
#     now=datetime.now() #datetime moduledefine the curent time.
#     arrival=now+timedelta(hours=hours) #timedelta module allow the addittion operation that results in new time object. 
#     return arrival.strftime(f"{destination} Arrival:%A %H:%M")
# arrival_time()

# #variabe arguments
# def sequence_time(*args):
#     total_minutes=sum(args)
#     if total_minutes<60:
#         return f"Total time to launch is {total_minutes} minutes"
#     else:
#         return f"Total time  to launch is {total_minutes/60} hours"
    
# sequence_time(4,55,5) #function ccall
 

#  #Variable keyword arguments
# def crew_members(**kwargs):
#     print(f"{len(kwargs)} astronauts assigned for this mision:")
#     for title,name in kwargs.items():
#         print(f"{title}:{name}")

# crew_members(captain="Neil Armstrong", pilot="Buzz Aldrin", command_pilot="Michael_collins")


#================python dictionaries =====================================
#Create a dictionary
planets = {
     "name":"Earth",
     "moons":1
 }  
#Read dictionary values
print(planets.get("name"))
print(planets["name"])

#Modify dictionary values
planets.update({"name":"Makemake",
                "moons":79})
planets["name"]="Makemake"
#Add and remove keys
planets["orbital period"]=4333
planets.pop("orbital period")
# ==========================Nested dictionary

planets = {
    "name": "Jupyter",
    "moons": 79,
    "diameter": {
        "polar": 133709,
        "equatorial": 142984
    }
}

print(f'{planets["name"]} polar diameter: {planets["diameter"]["polar"]}') #prints polar diameter
#Dynamic programming with dictionaries
#Retrieve all keys and values
rainfall = {
    'october': 3.5,
    'november': 4.2,
    'december': 2.1
}
for key in rainfall.keys():
    print(f'{key}: {rainfall[key]}cm')

#Determine if a key exists in a dictionary
if 'december' in rainfall:
    rainfall['december'] = rainfall['december'] + 1
else:
    rainfall['december'] = 1


#Retrieve all values
total_rainfall = 0
for value in rainfall.values():
    total_rainfall = total_rainfall + value

print(f'There was {total_rainfall}cm in the last quarter.')