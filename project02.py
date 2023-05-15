####################################
# programming project 02
#
#print greeting and promt statements
#input if you would like to continue
#loop while calculating customer summary
#   inputs for all customer information
#   while loop for class code
#       validate code
#   if statement for odometer reading fix
#       calculations
#   begin if statemets for budget, daily, and weekly codes
#   if 'bd'
#       calculations
#   iF 'd'
#       calcualtions
#   if 'w'
#       calculations
#   print customer summary
#   input if you would like to continue
#display closing message
####################################

print() #begin print statements
print('Welcome to Horizons car rentals. \n')
print('At the prompts, please enter the following: ')
print("\tCustomer's classification code (a character: BD, D, W) ")
print("\tNumber of days the vehicle was rented (int)")
print("\tOdometer reading at the start of the rental period (int)")
print("\tOdometer reading at the end of the rental period (int)")

answer = input('\nWould you like to continue (A/B)? ')#prompt to continue
while answer == 'A':
    class_code = input('\nCustomer code (BD, D, W): ') #input for costumer code
    #validate code
    while(class_code != 'BD' and class_code != 'D' and class_code != 'W'):
        print("\n\t*** Invalid customer code. Try again. ***")
        class_code = input('\nCustomer code (BD, D, W): ')
    days_rented = int(input('\nNumber of days: '))
    start_reading = int(input('\nOdometer reading at the start: '))
    end_reading = int(input('\nOdometer reading at the end:   '))
    if end_reading < start_reading:
        #if odometer reading at end is less then start, fix
        holder = 1000000 + end_reading
        total_miles = (holder - start_reading)/10
    else: 
        total_miles = float(end_reading - start_reading)/10
    total_charge=0#set total charge
    if class_code == 'BD':#budget code calculations
        base_charge = 40.0 * days_rented
        mileage_charge = total_miles * 0.25
        total_charge = (base_charge + mileage_charge)
    elif class_code == 'D':#daily code calculations
        avg_daily = float(total_miles) / days_rented
        base_charge = 60.00 * days_rented
        if avg_daily <= 100:#no charge under 100 miles
            mileage_charge = 0.00
        else:
            #find daily number of miles over 100
            miles = (avg_daily -100) * days_rented
            mileage_charge = miles * .25#calculate charge for miles over
        total_charge = (base_charge + mileage_charge)
    else: 
        if days_rented % 7 == 0:#if weeks is easy calculation
            weeks_rented = int(days_rented/7)#calculate number of weeks rented
        else:
            #calulation for incomplete weeks
            weeks_rented = int(days_rented/7) + 1
        avg_weekly = float(total_miles/weeks_rented) 
        base_charge = 190 * weeks_rented
        if avg_weekly <= 900 :#no charge for under 900
            mileage_charge = 0
        elif avg_weekly < 1500 :#inbetween 900 and 1500 
            mileage_charge = weeks_rented *100#charge miles over
        else: #over 1500 and charge for miles over
            mileage_charge = (200 * weeks_rented) + (avg_weekly - 1500)\
             * 0.25 * weeks_rented
        total_charge = float(base_charge + mileage_charge)
    print("\n\nCustomer summary:")#print customer summary
    print("\tclassification code:", class_code)
    print("\trental period (days):", days_rented)
    print("\todometer reading at start:", start_reading)
    print("\todometer reading at end:  ", end_reading)
    print("\tnumber of miles driven: ", total_miles)
    print("\tamount due: $", total_charge)
    answer = input('\nWould you like to continue (A/B)? ')#prompt to continue
    
print("\nThank you for your loyalty.")#closing message







