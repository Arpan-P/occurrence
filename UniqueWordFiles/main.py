import os

for i in os.listdir("./text_file_bunch"):
    fileWrite = open("./text_file_bunch/" + i, "a")
    fileRead = open("./text_file_bunch/" + i, "r")

    listOfWords = []

    for seperateLine in fileRead.read().splitlines():
        listOfWords.extend(seperateLine.split(" "))

    listOfUniqueWords = list(set(listOfWords))
    fileWrite.write(str(listOfUniqueWords))
