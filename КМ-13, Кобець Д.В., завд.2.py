magnitude=float(input("Enter the magnitude of the earthquake: "))
  
if magnitude <= 0 :
    print("That's not an earthquake...")
elif magnitude < 2 :
    print("That's a micro eartquake.")
elif magnitude < 3 :
    print ("That's a very minor eathquake.")
elif magnitude < 4 :
    print ("That's a minor earthquake.")
elif magnitude < 5 :
    print ("That's a light earthquake.")
elif magnitude < 6 :
    print ("That's a moderate earthquake.")
elif magnitude < 7 :
    print ("That's a strong earthquake.")
elif magnitude < 8 :
    print ("That's a major earthquake.")
elif magnitude < 10 :
    print ("That's a great earthquake.")
elif magnitude >= 10 :
    print ("That's a meteoric earthquake!")
