def getAllSubsequences(word):
    subsequences = []
    def getAllSubsequences(word, subseq, i):
        if i == len(word):
            if len(subseq) > 0:
                subsequences.append(subseq)
            return

        getAllSubsequences(word, subseq+word[i], i+1)
        getAllSubsequences(word, subseq, i+1)

    getAllSubsequences(word, "", 0)
    return subsequences

print(getAllSubsequences("1A2b"))
print(getAllSubsequences("abcd"))
print(getAllSubsequences(""))
