a = 5
V = 32
G = 32
M = 36
NA = 44
NAC = 42


def info():
    print("Total number of Busses: ", a, "\nAvailable busses\n")

    print(

        "1.Volvo with ", V, "seats\n"
        "2.Garuda with", G, "seats\n"
        "3.Multi axle sleeper with ", M, "seats\n"
         "4.Non AC with", NA, "seats\n"
        "5.Non Ac sleeper with ",NAC, "seats\n")


print("\n\nWelcome! To Bus Reservation System\n")
restart = ('Y')

while restart != ('N', 'NO', 'n', 'no'):
    print("1.Check for Available busses")
    print("2.Reservation center")
    option = int(input("\nEnter your option : "))

    if option == 1:

        m = info()

        exit(0)

    elif option == 2:
        m = info()

        people = int(input("\nEnter no. of Ticket you want : "))
        print("select bus type:")
        select = input("_______")

        if select == '1':
            V -= people


        elif select == '2':
            G -= people

        elif select == '3':
            M -= people


        elif select == '4':
            NA -= people


        elif select == '5':
            NAC -= people



        name_l = []
        age_l = []
        sex_l = []
        for p in range(people):
            name = str(input("\nName : "))
            name_l.append(name)
            age = int(input("\nAge  : "))
            age_l.append(age)
            sex = str(input("\nMale or Female : "))
            sex_l.append(sex)
            print("Congrats! your ticket is booked............\n\n")
            print("Detials:\n","NAME: ",name,"\n","AGE: ",age,"\n","SEX: ",sex)
            m = info()
        print("Number of Available busses and seats now:")
        m=info()
        restart = str(input("\nTo Continue write 'yes' or to add someone write 'add': "))
        if restart in ('y', 'YES', 'yes', 'Yes'):
            restart = ('Y')
        else:
            x = 0

            m = info()
            print("\nTotal Ticket : ", people)
            for p in range(1, people + 1):
                print("Ticket : ", p)
                print("Name : ", name_l[x])
                print("Age  : ", age_l[x])
                print("Sex : ", sex_l[x])
                x += 1

                m = info()








