read = open('in.txt', 'r')
write = open('out.txt', 'w')
# programador_who
listNumbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
listLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                'l', 'k', 'm', 'n',
                'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']

listForWritingNumbers = []
listForWritingLetters = []

firstLine = read.readline();
sizeLine = len(firstLine)

def separateNumbersAndWriteToFile():
    i = 0
    countNumbers = 0
    while(i < sizeLine):
        if firstLine[i] in listNumbers:
            listForWritingNumbers.append(firstLine[i])
            countNumbers += 1
        i += 1
    write.writelines(str(listForWritingNumbers))

def separeteLettersAndWriteToFile():
    i = 0
    countLetters = 0
    while(i < sizeLine):
        if firstLine[i] in listLetters:
            listForWritingLetters.append(firstLine[i])
            countLetters += 1
        i += 1
    write.writelines(str(listForWritingLetters))

separateNumbersAndWriteToFile()
write.writelines('\n')
separeteLettersAndWriteToFile()

read.close()
write.close()
