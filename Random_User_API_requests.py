from randomuser import RandomUser
import pandas as pd

#create a random user object, r.
r = RandomUser()
#get a list of random 10 users
some_list = r.generate_users(10)
#get full name,
name = r.get_full_name()
#10 users with full names and their email addresses
for user in some_list:
    print (user.get_full_name()," ",user.get_email())

#generate photos of the random 10 users.
for person in some_list:
    print(person.get_picture())

#create function which generates table with information about the users
def get_users():
    users =[]
     
    for user in RandomUser.generate_users(10):
        users.append({"Name":user.get_full_name(),"Gender":user.get_gender(),"City":user.get_city(),"State":user.get_state(),"Email":user.get_email(), "DOB":user.get_dob(),"Picture":user.get_picture()})
      
    return pd.DataFrame(users)   