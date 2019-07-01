numbers = []
def TowersofHanoi():
    # Proram to simulate Towers of hanoi
    # Objective is to move the disks from A to C 
    # with B as a temporary varialbel
        print ("Program to simulate Towers of Hanoi")
        print ("Users will input numbers of disks, which is 'A'")
        print ("The disks have to be moved from A to C")
        print ("With B as temporary placeholder") 
        Num = int (input("Enter the number of disks to be moved:"))
        Src = Num
        Aux = 0
        Dst = 0
        print ("you have entered %d disks to be moved")
        print ("Source is -->", Src)
        print ("Auxillary is -->", Aux)
        print ("Destination is -->", Dst)
        print ("Disk positions after the placement:")
        #B = A-1
        #print B
        while Num >= 1: 
            print (Num)
            Aux = Num-1
            Src = Src-Aux   
            Dst = Src   
            print ("Source is -->", Src)
            print ("Auxillary is -->", Aux)
            print ("Destination is -->", Dst)
            Src = Aux
            Num = Num-1
            numbers.append(Dst)
        print (numbers)
        print ("The task of accomplishing the movements of disk is over")
        print ("This completes TOWERS OF HANOI!")
        print ("Final disk positions are:")
        print ("Source is -->", Src)
        print ("Auxillary is -->", Aux)
        print ("Destination is -->", len(numbers))
TowersofHanoi()
