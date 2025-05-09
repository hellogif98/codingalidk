
#open file and read its contents 
file = open('ok.txt','r')
print(file.read())
file.close()

#open file and read uts begining in 8 characters 
file = open('ok.txt','r')
print("/n Read in parts \n")
print(file.read(8))
file.close()

#append your name and age in the file 
file = open('ok.txt','a')
file.write ("hello i am a cow that is 55 years old ")
file.close()