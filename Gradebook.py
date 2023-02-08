'''
Build a Gradebook.
 

EXAMPLE(S)
const gradebook = new Gradebook();

gradebook.recordGrade(90);
gradebook.recordGrade(100);

console.log(gradebook.min(), 90);
console.log(gradebook.max(), 100);
console.log(gradebook.average(), 95);
console.log(gradebook.mode(), 100);

console.log();
gradebook.recordGrade(90);
console.log(gradebook.min(), 90);
console.log(gradebook.max(), 100);
console.log(gradebook.average(), 93.3333333);
console.log(gradebook.mode(), 90);
'''
from collections import defaultdict
class Gradebook:
    def __init__(self):
        self.number = 0
        self.minimum = float("inf")
        self.maximum = float("-inf")
        self.freq = defaultdict(int)
        self.total = 0
        self.most_frequent = 0
    
    def recordGrade(self, grade: float):
        if grade < self.minimum: self.minimum = grade
        if grade > self.maximum: self.maximum = grade
        self.freq[grade] += 1
        if self.freq[grade] > self.freq[self.most_frequent]:
            self.most_frequent = grade
        self.total += grade
        self.number += 1

    def min(self) -> float:
        return self.minimum
    
    def max(self) -> float:
        return self.maximum

    def average(self) -> float:
        return self.total / self.number

    def mode(self) -> float:
        return self.most_frequent

gradebook = Gradebook()

gradebook.recordGrade(90);
gradebook.recordGrade(100);

print(gradebook.min(), 90);
print(gradebook.max(), 100);
print(gradebook.average(), 95);
print(gradebook.mode(), 100);


gradebook.recordGrade(90);
print(gradebook.min(), 90);
print(gradebook.max(), 100);
print(gradebook.average(), 93.3333333);
print(gradebook.mode(), 90);