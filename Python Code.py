# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 20:11:22 2023

@author: kdp4
"""

import pyodbc 

print(pyodbc.drivers())

cnxt = pyodbc.connect('driver={SQL Server};'
                              'server=CYPRESS.csil.sfu.ca;'
                              'uid=s_kdp4;'
                              'pwd=gQr2mmryE7mb2GY7;'
                              'database=kdp4354')



cursor = cnxt.cursor()


def Login(user_id):
    
    search_for_user = cursor.execute("SELECT U.user_id FROM user_yelp U WHERE user_id = (?)", (user_id, ))
    
    
    if search_for_user.rowcount == 0:
        print("User id not in DB")
        return False
        
    else:
        print("Successfully Logged in")
        return True
    
    

def Search_business():
    names = input("Enter the name of the business\n")
    stars = float(input("Enter the minimum amount of stars the business has\n"))
    city = input("Enter the city of the business\n")
    
    which = input("What do you want to order by, name, city, or stars\n")
    
    if which == "stars":
        star_business = cursor.execute("SELECT * FROM business B WHERE B.name = ? AND B.stars >= ? AND B.city = ? ORDER BY B.stars", (names, stars, city, ))
        if star_business.rowcount == 0:
            print("There are no businesses that fit this criteria")
        else:
            return star_business.fetchall()
        
    if which == "name":
        name_business = cursor.execute("SELECT * FROM business B WHERE B.name = ? AND B.stars >= ? AND B.city = ? ORDER BY B.name", (names, stars, city, ))
        if name_business.rowcount == 0:
            print("There are no businesses that fit this criteria")
        else:
            return name_business.fetchall()
    
    
    if which == "city":
        city_business = cursor.execute("SELECT * FROM business B WHERE B.name = ? AND B.stars >= ? AND B.city = ? ORDER BY B.city", (names, stars, city, ))
        if city_business.rowcount == 0:
            print("There are no businesses that fit this criteria")
        else:
            return city_business.fetchall()



def Search_Users():
    names = input("Enter the name of the user\n")
    stars = float(input("Enter the minimum number of reviews the user has submitted\n"))
    review_count = input("Enter the average stars the user gives\n") 
    
    star_user = cursor.execute("SELECT * FROM user_yelp, (SELECT AVG(F.stars) AS STARS FROM user_yelp F GROUP BY F.user_ids) AS S WHERE U.name = ? AND S.STARS >= ? AND U.review_count >= REVIEWS = ? ORDER BY U.name", (names, stars, review_count, ))
    if star_user.rowcount == 0:
        print("There are no businesses that fit this criteria")
    else:
        star_user.fetchall()
    return star_user

   

def Make_Friend(user_id):
    star_user = cursor.execute("SELECT * FROM friendship WHERE user_id = ?", (user_id, ))
    friend = input("Enter the UID of a user you want to be friends with\n")
 
    if star_user.rowcount == 0:
        print("The user was not found in the table")
        
    else:
        cursor.execute("UPDATE friendship SET friend = ? WHERE user_id = ?", (user_id, friend, ))
        
    
  
def Review_Business(user_id):
    bus_id = input("Enter the business_id that you want to review\n")    
    
    star_count = float(input("Enter the number of stars of the business\n"))
    
    while star_count < 1 or star_count > 5:
        input("Please enter a number between 1 and 5")
        if star_count > 1 or star_count < 5:
            break

    review_id = input("Enter a review id\n")
    
    new_rev = cursor.execute("INSERT INTO review(review_id, user_id, business_id, stars, useful, funny, cool, date) VALUES(?, ?, ?, ?, DEFAULT, DEFAULT, DEFAULT, DEFAULT)", (review_id, user_id, bus_id, star_count, ))

    
    return new_rev


start_menu = int(input("1. Login 2. Exit\n"))


if start_menu == 1:
    user_id = input("ENTER YOU UID\n")
    var = Login(user_id)
    print(var)
  
    while var == True:       
        if var == True:
            start = ("Press a button\n")
            print("1. Search for a business\n")
            print("2. Search for a user\n")
            print("3. Add a friend\n")
            print("4. Add a review\n")
            print("Press anything else to quit\n")
            user_input = int(input())
            if user_input == 1:
                Searched_business = Search_business()
                print(Searched_business)
            elif user_input == 2:
                Searched_users = Search_Users()
                print(Searched_users)
            elif user_input == 3:
                New_friend = Make_Friend(user_id)
            elif user_input == 4:
                pass
                New_review = Review_Business(user_id)
            else:
                print("Exiting the application")
                break
                
elif start_menu == 2:
    print("Exited out of the user menu")            
        
        
        
        




