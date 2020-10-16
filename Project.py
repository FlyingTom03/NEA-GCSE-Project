import sys
import time
import os

def menu():
        f = open("menutext.txt", "r")
        for c in f.read():
            sys.stdout.write(c)
            time.sleep(0.000001)
        user=input("\n               Enter Choice: ")
        line = open ("line.txt", "r")
        for c in line.read():
            sys.stdout.write(c)
            time.sleep(0.000001)
        print("\n")
    
        if user=="1":
            enterrle()

        if user=="2":
            displayasciiart()

        if user=="3":
            convertrletoascii()

        if user=="4":
            convertasciitorle()

        if user=="5":
            end()
    
def enterrle():
    print ("Starting 'Enter RLE'...")
    time.sleep(0.5)
    rle_lines=0
    while rle_lines <2:
        rle_lines = int(input("How many lines of RLE do you want to enter? "))
        if rle_lines < 2:
            print ("The number of lines must be 2 or higher. Try again")

        else:
            buf = []
            for i in range(1, rle_lines + 1):
                line = input(f"Enter line {i} of {rle_lines}: ")
                buf.append(line)

            for i in buf:
                output = ""
                for j in range(0, len(i), 3):
                    count = int(i[j:j+2])
                    char = i[j+2]

                    for _ in range(count):

                        output += char

 

                print(output)
    line = open ("line.txt", "r")
    for c in line.read():
            sys.stdout.write(c)
            time.sleep(0.000001)
    print("\n")
    menu()
    
    


    
def displayasciiart():
    art=input("Enter file you want to be displayed: ")
    print("\n")
    print("                   ASCII Art ("+art+") :",end='')
    print("\n")

    logoart = open(art, "r")
    for c in logoart.read():
        sys.stdout.write(c)
        time.sleep(0.000001)

    line = open ("line.txt", "r")
    print("\n")
    for c in line.read():
        sys.stdout.write(c)
        time.sleep(0.0000001)
    print("\n")   
    menu()

def convertrletoascii():

    filename = input("Enter RLE filename: ")
        
    print(("\nConverting ") + (filename) + (" to ASCII Art:"))


    f = open(filename)
    print(f)
    print("\nCONVERTING RLE TO ASCII:\n")
    for line in f:
        line = line.strip()

        output = ""
        for index in range(0, len(line), 3):
            count = int(line[index:index+2])

            char = line[index+2]
            
            for _ in range(count):
                output += char
                
        for char in output:
            print(char, end="")
            time.sleep(0.005)

        print()
    line = open ("line.txt", "r")
    for c in line.read():
            sys.stdout.write(c)
            time.sleep(0.000001)
    print("\n")
    menu()

def line_to_rle(line):#takes single line of ascii input and converts it into RLE
    last = None
    count = None
    output = ""
    for char in line:
        if last is None:
            last = char
            count = 1

        elif last == char:
            count += 1

        else:
            tmp = None
            if count < 10:
                tmp = "0" + str(count)
            else:
                tmp = str(count)
            output += tmp + last

            last = char
            count = 1

    tmp = None
    if count < 10:
        tmp = "0" + str(count)
    else:
        tmp = str(count)

    output += tmp + last
    return output

def convertasciitorle ():
    filename = None
    while True:
        filename = input("Enter the ASCII file name: ")

        if not os.path.isfile(filename):
            print("That is not a valid file name. Make sure it is in the same directory as this \n script and try again.")
        else:
            print ("\n Converting the following to RLE...")
            line = open (filename, "r")
            for c in line.read():
                    sys.stdout.write(c)
                    time.sleep(0.000001)
            print("\n")
            break

    infile = open(filename)
    outfile = open("OutputRLE.txt", "w")

    infile_count = 0
    outfile_count = 0
    for line in infile:
        infile_count += len(line)
        rle = line_to_rle(line.strip()) + "\n"
        outfile_count += len(rle)

        outfile.write(rle)

    print("\nConverted To RLE code: \n")
    line = open ("OutputRLE.txt", "r")
    print (line)
    for c in line.read():
        sys.stdout.write(c)
        time.sleep(0.000001)
    print("file in: OutputRLE.txt \n")

    print(f"Difference in size: {infile_count - outfile_count}")

            

    line = open ("line.txt", "r")
    for c in line.read():
            sys.stdout.write(c)
            time.sleep(0.000001)
    print("\n")
    menu()
    
###

def end():
    print ("\nGoodbye")
    time.sleep(1.5)
    sys.exit


menu()
