file = open("newfile.txt", 'wt')
string = " hello \n\
my name is ahmed \n\
and i hate her \n\
         "
file.write(string)
file.close()

print (file)