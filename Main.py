#Made by JaCrispy4939
import random
import time

def main():
  start()
  end()
  newtopics()

def start():
  with open("topics.txt", "r") as file:
      allText = file.read()
      words = list(map(str, allText.split()))
    
      # print random string
      print("Starting topic: " + random.choice(words))

def end():
  with open("topics.txt", 'r') as file:
    allText = file.read()
    word = list(map(str, allText.split()))

    print("Ending topic: " + random.choice(word))

def newtopics():
  newtopic = input("\n\nDo you want another topic? (y/n): ")
  if newtopic == "y":
    print("Getting new topic")
    print(".")
    time.sleep(.5)
    print("..")
    time.sleep(.5)
    print("...")
    time.sleep(.5)
    main()
  if newtopic == "n":
    print("Goodbye")
    time.sleep(2)
    exit()
  else:
    print("Please type y/n")
    newtopics()


main()
