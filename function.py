def countWordFromFile():
    fileName=input("Enter The File Name:-")
    numberOfWords=0
    file=open("Test.txt",'r')
    for line in file:
        words=line.split()
        numberOfWords=numberOfWords+len(words)
    print("Number Of Words: ")
    print(numberOfWords)
countWordFromFile()