class information:
    def __init__(self,km,passengers):
        self.km=km
        self.passengers=passengers


class auto(information):
    def __init__(self,km,passengers):

        cost = 3 + ((km - 1) * 10)
        if passengers > 4:
            cost = cost * 1.5
        print("The total cost of the journey for", passengers, "passengers is ₹{:.2f}".format(cost))
class micro(information):
    def __init__(self,km,passengers):

        cost = 3 + ((km - 1) * 20)
        if passengers > 5:
            cost = cost * 1.5
        print("The total cost of the journey for", passengers, "passengers is ₹{:.2f}".format(cost))

class macro(information):
    def __init__(self,km,passengers):

        cost = 3 + ((km - 1) * 30)
        if passengers > 5:
            cost = cost * 1.5
        print("The total cost of the journey for", passengers, "passengers is ₹{:.2f}".format(cost))
class prime(information):
    def __init__(self,km,passengers):

        cost = 3 + ((km - 1) * 40)
        if passengers > 8:
            cost = cost * 1.5
        print("The total cost of the journey for", passengers, "passengers is ₹{:.2f}".format(cost))
class outstation(information):
    def __init__(self,km,passengers):

        cost = 3 + ((km - 1) * 50)
        if passengers > 12:
            cost = cost * 1.5
        print("The total cost of the journey for", passengers, "passengers is ₹{:.2f}".format(cost))

print("Ola Cabs for services -\n" 
      "Press\n"
      "1.Auto\n"
      "2.Micro cab\n"
      "3.Macro cab\n"
      "4.Prime sedan\n"
      "5.Out station\n")

select = input("_______")

km = float(input("Enter the distance of the taxi ride in kilometres (KM): "))
passengers = int(input("Enter the number of passengers: "))
m=information(km,passengers)

if select == '1':
    print("Auto")
    m=auto(m.km,m.passengers)


elif select == '2':
    print("Tata Nano")
    m=micro(m.km,m.passengers)

elif select == '3':
    print("Maruti Suzuki Ertiga")
    m=macro(m.km,m.passengers)


elif select == '4':
    print ("Mahindra Scorpio")

    m=prime(m.km,m.passenger)


elif select == '5':
    print("Toyota Innova Crysta")
    m=outstation(m.km,m.passengers)





else:
	print("Invalid input")