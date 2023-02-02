'''
Q. Create an array of integers with a starting number s, 
an increment value i, and a repetition count r given.
'''
# changed parameters to start, inc, rep to avoid confusion

def solution(start, inc, rep):
    return [(start + inc * i) for i in range(rep)]