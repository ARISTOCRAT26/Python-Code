#import cmath
#   a=float(input("Enter a: "))
#   b=float(input("Enter b: "))
#   c=float(input("ENter c: "))
#   d=(b**2)-(4*a*c)
#   sol1=(-b-cmath.sqrt(d))/(2*a)  
#   sol2=(-b+cmath.sqrt(d))/(2*a)  
#   print('The solution are {0} and {1}'.format(sol1,sol2))

#import random
#n=random.randint(0,100)
#print(n)

#import calendar   
#yy = int(input("Enter year: "))  
#mm = int(input("Enter month: "))    
#print(calendar.month(yy,mm)) 

#n_terms=int(input("How many terms: "))
#n_1=0
#n_2=1
#count=0
#if n_terms<=0:
#    print("Ener positive number of terms")
#elif n_terms==1:
#    print("Fibonacci series upto ",n_terms," :")
#    print(n_1)
#else:
#    print("Fibonacci series is:")
#    while count<n_terms:
#        print(n_1)
#       nth=n_1+n_2
#        n_1=n_2
#       n_2=nth
#        count+=1    

# Importing InstagramUser from instagramy module  
from instagramy import InstagramUser as IU  
# Taking the Instagram account or User Name as input  
givenUN = input("Enter a valid and existing Instagram's user name: ")  
# Creating instance for giver User name  
unInstance = IU(givenUN)  
# Getting total number of followings  
followingNumber = unInstance.number_of_followings  
# Printing result in the output  
print('The total number of followings from the given user name by you is:', followingNumber) 
# Getting total number of followers of Instagram account  
followersNumber = unInstance.number_of_followers  
# Printing result in the output  
print('The total number of followers of the given Instagram user name by you is:', followersNumber)
# Getting total number of posts made  
postsNumber = unInstance.number_of_posts  
# Printing result in the output  
print('The total number of posts made by the given Instagram user name by you is:', postsNumber)
# Getting description of the account's bio  
instaBioDesc = unInstance.biography  
# Gettings links present in the account's bio  
instaBioLinks = unInstance.website  
# Printing result in the output  
print("Description of the bio of the Instagram account that you have provided in the input: ")  
print(instaBioDesc)  
print("Following links are present in the bio of Instagram account which you have provided: ")  
print(instaBioLinks)