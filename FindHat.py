def findHat(dogs, bestFriend):
    queue = [bestFriend];
    alreadyAsked = [bestFriend];
    while queue:
        currentName = queue.pop();
        for name in dogs[currentName]:
            if(name == "HAT"):
                return currentName
            if(not name in alreadyAsked):
                queue.append(name)
                alreadyAsked.append(name)
    return "Couldn't find the hat"

dogsTestOne = {
  "Carter": ["Fido", "Ivy"],
  "Ivy": ["HAT"],
  "Loki": ["Snoopy"],
  "Pepper": ["Carter"],
  "Snoopy": ["Pepper"],
  "Fido": []}

print(findHat(dogsTestOne, "Loki") == "Ivy")
print(findHat(dogsTestOne, "Snoopy") == "Ivy")
print(findHat(dogsTestOne, "Ivy") == "Ivy")
print(findHat(dogsTestOne, "Fido") == "Couldn't find the hat")

dogsTestTwo = {
  "Zoe": ["Jono"],
  "Jono": ["Angus"],
  "Angus": ["Jono"],
  "Paavo": ["Zoe", "Oliver"],
  "Oliver": ["HAT"]}

print(findHat(dogsTestTwo, "Paavo") == "Oliver")
print(findHat(dogsTestTwo, "Oliver") == "Oliver")
print(findHat(dogsTestTwo, "Zoe") == "Couldn't find the hat")
print(findHat(dogsTestTwo, "Angus") == "Couldn't find the hat")
print(findHat(dogsTestTwo, "Jono") == "Couldn't find the hat")

dogsTestThree = {
  "Ariel": ["Bork"],
  "Bork": ["Cassie"],
  "Cassie": ["Drex"],
  "Drex": ["Zoe"],
  "Zoe": ["HAT"]}

print(findHat(dogsTestThree, "Ariel") == "Zoe")
print(findHat(dogsTestThree, "Bork") == "Zoe")
print(findHat(dogsTestThree, "Cassie") == "Zoe")
print(findHat(dogsTestThree, "Drex") == "Zoe")
print(findHat(dogsTestThree, "Zoe") == "Zoe")
