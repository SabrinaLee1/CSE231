#####################################
# Programming Project 03
#
#constants
#loop over some value
#   print welcome statement
#   collect inputs
#   process inputs
#   if statements for different cases
#       have neither square footage or max monthly
#       have square footage, no max monthly
#       have max monthly, no square footage
#       have both
#ask to go again
#####################################

# given constants
NUMBER_OF_PAYMENTS = 360    
SEATTLE_PROPERTY_TAX_RATE = 0.0092
SAN_FRANCISCO_PROPERTY_TAX_RATE = 0.0074
AUSTIN_PROPERTY_TAX_RATE = 0.0181
EAST_LANSING_PROPERTY_TAX_RATE = 0.0162
AVERAGE_NATIONAL_PROPERTY_TAX_RATE = 0.011
SEATTLE_PRICE_PER_SQ_FOOT = 499.0
SAN_FRANCISCO_PRICE_PER_SQ_FOOT = 1000.0
AUSTIN_PRICE_PER_SQ_FOOT = 349.0
EAST_LANSING_PRICE_PER_SQ_FOOT = 170.0
AVERAGE_NATIONAL_PRICE_PER_SQ_FOOT = 244.0
APR_2023 = 0.0668

#begin loop
keep_going = 'Y'
while keep_going != 'N':
    print("\nMORTGAGE PLANNING CALCULATOR\n============================ "
    "\n\nEnter a value for each of the following items or type 'NA' "
    "if unknown ")
    #collect inputs
    location = input("\nWhere is the house you are considering "
    "(Seattle, San Francisco, Austin, East Lansing)? ")
    #assign seattle values to location
    if location == 'Seattle':
        proptery_tax = (SEATTLE_PROPERTY_TAX_RATE)
        price_per_sqfoot = (SEATTLE_PRICE_PER_SQ_FOOT)
    #assinf san fran values to location
    elif location == 'San Francisco':
        proptery_tax = (SAN_FRANCISCO_PROPERTY_TAX_RATE) 
        price_per_sqfoot = (SAN_FRANCISCO_PRICE_PER_SQ_FOOT)
    #assign austin values to location
    elif location == 'Austin':
        proptery_tax = (AUSTIN_PROPERTY_TAX_RATE)
        price_per_sqfoot = (AUSTIN_PRICE_PER_SQ_FOOT)
    #assign el values to location
    elif location == 'East Lansing':
        proptery_tax = (EAST_LANSING_PROPERTY_TAX_RATE)
        price_per_sqfoot = (EAST_LANSING_PRICE_PER_SQ_FOOT)
    #assign national avg values to location
    else:
        location != 'Seattle'and'San Francisco'and'Austin'and'East Lansing'
        location = 'the average U.S. housing market'
        proptery_tax = (AVERAGE_NATIONAL_PROPERTY_TAX_RATE)
        price_per_sqfoot = (AVERAGE_NATIONAL_PRICE_PER_SQ_FOOT)
    #collect inputs
    square_footage = input("\nWhat is the maximum square footage"
    " you are considering? ")
    maxmonthly_payment = input("\nWhat is the maximum monthly "
    "payment you can afford? ")
    down_payment = input("\nHow much money can you put down"
    " as a down payment? ")
    #fix for down payment
    if down_payment != 'NA':
        down_payment = float(down_payment) 
    else:
        down_payment == 'NA'
        down_payment = 0
    #fix for percent rate
    percent_rate = input("\nWhat is the current annual percentage rate? ")
    if percent_rate != 'NA':
        percent_rate = float(percent_rate)/100
    else:
        percent_rate == 'NA'
        percent_rate = APR_2023
    #fix for unknown location
    if location == 'the average U.S. housing market':
        print("\nUnknown location. Using national averages"
        " for price per square foot and tax rate.")
    #have neither square footage or max monthly
    if square_footage == 'NA' and maxmonthly_payment == 'NA':
        print("\nYou must either supply a desired square footage"
        " or a maximum monthly payment. Please try again.")
    #have square footage but no max montly
    elif square_footage != 'NA' and maxmonthly_payment == 'NA':
        square_footage = float(square_footage)
        total_cost = (square_footage * price_per_sqfoot)
        principal_mortgage = (total_cost - down_payment)
        monthly_tax = (total_cost * proptery_tax) / 12
        N = NUMBER_OF_PAYMENTS
        monthly_payment = principal_mortgage*((percent_rate/12)\
        * (1+(percent_rate/12))**N)/((1+(percent_rate/12))**N-1)
        final = monthly_payment + monthly_tax
        print('\n\nIn {}, an average {} sq. foot house would cost ${}.'
        '\nA 30-year fixed rate mortgage with a down payment of ${} at '
        '{:.1%} APR results\n\tin an expected monthly payment of ${:.2f}'
        ' (taxes) + ${:.2f} (mortgage payment) = ${:.2f}'.format(location,\
        int(square_footage),int(total_cost),int(down_payment),percent_rate,\
        monthly_tax,monthly_payment,final))
        payment_sched = input("\nWould you like to print the monthly"
        " payment schedule (Y or N)? ")
        #ammorization table calcuations if yes
        if payment_sched == 'Y':
            i = percent_rate /12
            n = NUMBER_OF_PAYMENTS 
            print('\n Month |  Interest  |  Principal  |   Balance    ')
            print('================================================')
            for month in range (1, n+1):
                interest_payment = principal_mortgage * i
                principal_payment = monthly_payment - interest_payment
                print('{:^7d}| ${:>9.2f} | ${:>10.2f} | ${:>11.2f}'.format(\
                month, interest_payment, principal_payment, principal_mortgage))
                principal_mortgage = principal_mortgage - principal_payment
        # if no ammorization table wanted
        else:
            if payment_sched == 'N':
                pass
    #have no square footage but have max monthly
    elif square_footage == 'NA' and maxmonthly_payment != 'NA':
        maxmonthly_payment = float(maxmonthly_payment)
        N = NUMBER_OF_PAYMENTS
        principal_mortgage =((((1 + (percent_rate/12)) ** N) - 1) * \
        maxmonthly_payment) / (((1+(percent_rate/12)) ** N)*(percent_rate/12))
        square_footage =(down_payment+principal_mortgage) / price_per_sqfoot 
        total_cost = square_footage * price_per_sqfoot
        print('\n\nIn {}, a maximum monthly payment of ${:.2f} allows'
        ' the purchase of a house of {} sq. feet for ${}' 
        '\n\t assuming a 30-year fixed rate mortgage with a'
        ' ${} down payment at {:.1%}'
        ' APR.'.format(location,maxmonthly_payment,int(square_footage),\
        int(total_cost),int(down_payment),percent_rate )) 
    # have both!
    else:
        square_footage != 'NA' and maxmonthly_payment != 'NA'
        maxmonthly_payment = float(maxmonthly_payment)
        square_footage = float(square_footage)
        total_cost = (square_footage * price_per_sqfoot)
        principal_mortgage = (total_cost - down_payment)
        monthly_tax = (total_cost * proptery_tax) / 12
        N = NUMBER_OF_PAYMENTS
        monthly_payment = principal_mortgage * ((percent_rate/12) * \
        ( 1 + (percent_rate/12) )**N ) / ( ( 1 + (percent_rate/12) )**N - 1 )
        final = monthly_payment + monthly_tax
        #if they cannot afford the house based on max monthly
        if float(maxmonthly_payment) < float(final):
            print('\n\nIn {}, an average {} sq. foot house would cost ${}.'
            '\nA 30-year fixed rate mortgage with a down payment of ${} at '
            '{:.1%} APR results'
            '\n\tin an expected monthly payment of ${:.2f} (taxes) + ${:.2f} '
            '(mortgage payment) = ${:.2f}'.format(location,\
            int(square_footage), int(total_cost),int(down_payment),\
            percent_rate, monthly_tax,monthly_payment, final))
            print('Based on your maximum monthly payment of ${:.2f} '
            'you cannot afford this house.'.format(maxmonthly_payment))
        # if they can afford the house based on max monthly
        else:
            print('\n\nIn {}, an average {} sq. foot house would cost ${}.'
            '\nA 30-year fixed rate mortgage with a down payment of ${} at'
            ' {:.1%} APR results'
            '\n\tin an expected monthly payment of ${:.2f} (taxes)'
            ' + ${:.2f} (mortgage payment) = ${:.2f}'.format(location,\
            int(square_footage),int(total_cost), int(down_payment),\
            percent_rate, monthly_tax, monthly_payment, final))
            print('Based on your maximum monthly payment of ${:.2f}'
            ' you can afford this house.'.format(maxmonthly_payment))
        payment_sched = input("\nWould you like to print the monthly"
        " payment schedule (Y or N)? ")
        #calculation for ammorization, if yes
        if payment_sched == 'Y':
            i = percent_rate /12
            n = NUMBER_OF_PAYMENTS 
            print('\n Month |  Interest  |  Principal  |   Balance    ')
            print('================================================')
            for month in range (1, n+1):
                interest_payment = principal_mortgage * i
                principal_payment = monthly_payment - interest_payment
                print('{:^7d}| ${:>9.2f} | ${:>10.2f} | ${:>11.2f}'.format(\
                month, interest_payment, principal_payment, principal_mortgage))
                principal_mortgage = principal_mortgage - principal_payment
        else:
            if payment_sched == 'N':
                pass
    #main loops keep going
    keep_going = input("\nWould you like to make another attempt (Y or N)? ")
#if they dont want to keep going
while keep_going == 'N':
    break
