from sys import exit, argv


def reverse_sentence(sentence: str):
    l = sentence.split(" ")
    l.reverse()
    reversed_sentence = ""
    for i in l:
        reversed_sentence += i+" "
    return reversed_sentence


try:
    f = open(
        # "D:\\EE2703\\Assignment 1\\Example netlist files-20220125\\ckt2.netlist"
        argv[1]
    )
    data = f.readlines()

    print("this is the original file  :\n")
    for i in data:
        print(i.rstrip("\n"))
    print("\n\n\n\n\n")
    CIRCUIT = ".circuit"
    END = ".end"

    # get the circuit definition place
    start = -2
    end = -2
    for i in range(len(data)):
        if CIRCUIT in data[i]:
            start = i+1
        if END in data[i]:
            end = i
            break

    if end == -2 and start >= 0:  # validationg the circuit definition
        print("Invalid circuit definition!")
        exit(0)

    lines = data[start:end]
    f.close()

    for i in range(len(lines)):
        lines[i] = reverse_sentence(
            lines[i].split("#")[0].rstrip(" ").rstrip("\n")
        ) 
    print("this is the result :\n")
    for line in lines:  # printing the lines
        print(line)
    print("argv is : ",argv)

except IOError:
    print("Invalid filename")
    exit()
