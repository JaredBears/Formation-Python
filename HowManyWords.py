import re
def howMany(sentence):
    words = sentence.split(' ')
    wordcount = 0
    for word in words:
        print(word)
        wordCheck = re.match(r'^[a-zA-Z\-]+$|[a-zA-Z\-]+[.,?!]$', word)
        print(wordCheck)
        if wordCheck:
            wordcount += 1
    return wordcount