print ("hello welcome to Sal's Ships!!!")
weight = float(input("please type in the weight of your item in lb so select the most cost effective shipping."))

if (weight <= 2) == True:
    B = weight * 4.50
    A = weight * 1.50 + 20
    C = 125
    if A < B and A < C:
        print ("Ship by ground for a total of : ", A)
    elif B < C:
        print ("Ship by drone for a total of : ", B)
    else:
        print("Ship by Flat Rate for a total of : ", C)

elif ( 2 < weight  <= 6) == True:
    B = weight * 9.00
    A = weight * 3.00 + 20
    C = 125
    if A < B and A < C:
        print ("Ship by ground for a total of : ", A)
    elif B < C:
        print ("Ship by drone for a total of : ", B)
    else:
        print("Ship by Flat Rate for a total of : ", C)

elif ( 6 < weight <= 10) == True:
    B = weight * 12.00
    A = weight * 4.00 + 20
    C = 125
    if A < B and A < C:
        print ("Ship by ground for a total of : ", A)
    elif B < C:
        print ("Ship by drone for a total of : ", B)
    else:
        print("Ship by Flat Rate for a total of : ", C)

elif ( weight > 10) == True:
    B = weight * 14.25
    A = weight * 4.75 + 20
    C = 125
    if A < B and A < C:
        print ("Ship by ground for a total of : ", A)
    elif B < C:
        print ("Ship by drone for a total of : ", B)
    else:
        print("Ship by Flat Rate for a total of : ", C)

else:
    print("please try a full number")


