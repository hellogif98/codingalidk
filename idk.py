# write in file using with() function
with open('idk2.py','w') as file:
    file.write("hi i am a guy who is 1 year old ")
    file.close

# split into five words
with open('idk2.txt','r') as file:
    data = file.readlines()
    print("words in this file are........")
    for line in data:
        word = line.split()
        print(word)
file.close
    