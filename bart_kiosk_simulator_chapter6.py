
fremont_richmond = ["Fremont", "Union City", "South Hayward", "Hayward", "Bayfair", "San Leandro", "Coliseum", "Fruitvale", "Lake Merritt", "12th St/Oakland City Center", "19th St/Oakland", "MacArthur", "Ashby", "Downtown Berkeley", "North Berkeley", "El Cerrito Plaza", "El Cerrito del Norte"]

dublin_pleasanton = ["Dublin/Pleasanton", "West Dublin/Pleasanton", "Castro Valley", "Bayfair", "San Leandro", "Coliseum", "Fruitvale", "Lake Merritt", "West Oakland", "Embarcadero", "Montgomery St", " Powell St", "Civic Center/UN Plaza", "16th St Mission", "24th St Mission", "Glen Park", "Balboa Park", "Daly City"]

# calculates how much money is stored on the clipper card
def bart_kiosk (bill1, bill5, bill10, bill20):
	return bill1 + bill5*5 + bill10*10 + bill20*20

# returns a statement that calculates your fare
def calculate_fare (list1, start, end):
	#print the origin, destination and total cost
	fare_price = abs(end - start) * 1.25
	print "Going from %s station to %s station will cost $%.2f" % (list1[start], list1[end], fare_price)
	return fare_price
	

# set the communute_allowance to the amount placed on the clipper card

communute_allowance = bart_kiosk(0,1,1,2)
fare_price = calculate_fare(fremont_richmond, 7, 2)

def calculate_weekly_commute (communute_allowance, fare_price):
	if fare_price*10 < communute_allowance:
		return "Bart, and you're there!"
	else: 
		return "Derp, you need more money."

print "Your communte will cost $%.2f per week" % (fare_price*10)
print "You have",communute_allowance, "on your clipper card"
print calculate_weekly_commute(communute_allowance, fare_price)



