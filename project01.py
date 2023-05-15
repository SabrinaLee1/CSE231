########################################
# Computer Project 1
#
# prompt for a number in rods and convert to float value
# print entered rod value in statement 
# artithemtic conversions from number of rods to new values 
# arithmetic conversion from hours to miuntes of walking speed
# print new rounded and converted results in statements
#######################################


rods_str = input("Input rods: ") #input for number of rods
rods_float = float(rods_str) #assign float value to rods
print("\nYou input", rods_float, "rods.\n") #print number of rods entered

meters_float = rods_float * 5.0292 #convert rods to meters
feet_float = meters_float / .3048 #convert rods to feet
miles_float = meters_float / 1609.34 #convert rods to miles
furlongs_float  = rods_float / 40 #convert rods to furlongs
time_to_walk_float = ((miles_float / 3.1) * (60)) #convert avg walking speed

print("Conversions")
print("Meters:", round(meters_float,3)) #print and round new value
print("Feet:", round(feet_float,3)) #print and round new value
print("Miles:", round(miles_float,3)) #print and round newvalue 
print("Furlongs:", round(furlongs_float,3)) #print and round new value
print("Minutes to walk", rods_float, "rods:", round(time_to_walk_float,3))\
#print and round new minutes

