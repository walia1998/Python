#Append to an existing file called John Doe.txt
#It should contain data about John Doe.


f = open("John Doe.txt", "a")

string = '''

John Doe initially lived with Prikshit in Palampur, Himachal Pradesh. But he left the country due to certain reason 
 
'''
f.write(string)
f.close()