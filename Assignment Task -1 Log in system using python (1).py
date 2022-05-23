#!/usr/bin/env python
# coding: utf-8

# In[3]:


def sign_up(user_name,password):
    SpecialSym=('@','_','!','#','$','%','^','&','*','(',')','<','>','?','/','|','}','','~',':')
    file=open("user_details.txt","r+")
    u=[]
    p=[]
    for i in file:
        a,b=i.split(",")
        b=b.strip()
        u.append(a)
        p.append(b)
    data=dict(zip(u,p))
    if "@" and '.' in user_name:
        if 5<len(password)<15:
            if "@" not in user_name[0]:
                if user_name.index(".")!=(user_name.index("@")+1):
                    if user_name[0] not in ('@','_','!','#','$','%','^','&','*','(',')','<','>','?','/','|','}','','~',':'):
                        if any(char.isdigit() for char in password):
                            if any(char.isupper() for char in password):
                                if any(char.islower() for char in password):
                                    if any(char in SpecialSym for char in password):
                                        if user_name not in data.keys():
                                                print("Registered successfully")
                                                file.write(f'{user_name},{password}\n')
                                                file.close()
                                        else:
                                            print(" user name already exists")
                                            user_name=input("Enter your user_name: ")
                                            password=input("Enter your password: ")
                                            sign_up(user_name,password)
                                    else:
                                        print("The password must contain a special character a uppercase and lower case letter and a number a")
                                        user_name=input("Enter your user_name: ")
                                        password=input("Enter your password: ")
                                        sign_up(user_name,password)
                                else:
                                    print("The password must contain a special character a uppercase and lower case letter and a number b")
                                    user_name=input("Enter your user_name: ")
                                    password=input("Enter your password: ")
                                    sign_up(user_name,password)      
                            else:
                                print("The password must contain a special character a uppercase and lower case letter and a number")
                                user_name=input("Enter your user_name: ")
                                password=input("Enter your password: ")
                                sign_up(user_name,password)
                                
                        else:
                            print("The password must contain a special character a uppercase and lower case letter and a number ")
                            user_name=input("Enter your user_name: ")
                            password=input("Enter your password: ")
                            sign_up(user_name,password)
                    else:
                        print("The password must contain a special character a uppercase and lower case letter and a number ")
                        user_name=input("Enter your user_name: ")
                        password=input("Enter your password: ")
                        sign_up(user_name,password)
                else:
                    print("Please enter a valid username ")
                    user_name=input("Enter your user_name: ")
                    password=input("Enter your password: ")
                    sign_up(user_name,password)
            else:
                print("The user name should not start with special character ")
                user_name=input("Enter your user_name: ")
                password=input("Enter your password: ")
                sign_up(user_name,password)
        else:
            print("The password length must be between 5 to 15 characters")
            user_name=input("Enter your user_name: ")
            password=input("Enter your password: ")
            sign_up(user_name,password)
    else:
        print("Please enter a valid user name ")
        user_name=input("Enter your user_name: ")
        password=input("Enter your password: ")
        sign_up(user_name,password)


def log_in(user_name,password):
    file=open("user_details.txt","r")
    u=[]
    p=[]
    for i in file:
        a,b=i.split(",")
        b=b.strip()
        u.append(a)
        p.append(b)
    data=dict(zip(u,p))
    if user_name in data.keys():
        if password==data[user_name]:
            print("login Sucessfull")
            print("Hi,",user_name[:(user_name.index("@"))])
        else:
            print(" Entered password is correct ")
            user_name=input("Enter your user_name: ")
            password=input("Enter your password: ")
            log_in(user_name,password)
    else:
        print("User name does not exists")
        user_name=input("Enter your user_name: ")
        password=input("Enter your password: ")
        log_in(user_name,password)
            
    

def forgot_password(user_name):
    file=open("user_details.txt","r")
    u=[]
    p=[]
    for i in file:
        a,b=i.split(",")
        b=b.strip()
        u.append(a)
        p.append(b)
    data=dict(zip(u,p))
    if user_name in data.keys():
        print("your password is",data[user_name])
    else:
        print("User Name does not exists ")

print("Welcome to Login System using file handling in python \nEnter 1 for signup \nEnter 2 for Login \nEnter 3 for forgot password")
a=int(input("Enter your choice: "))
if a==1:
    print("please enter the User Name and password to Register ")
    user_name=input("Enter your user_name: ")
    password=input("Enter your password: ")
    sign_up(user_name,password)
if a==2:
    print("please enter the User Name and password to login ")
    user_name=input("Enter your user_name: ")
    password=input("Enter your password: ")
    log_in(user_name,password)
    
if a==3:
    print("please enter the User Name")
    user_name=input("Enter your user_name: ")
    forgot_password(user_name)


# In[ ]:





# In[4]:





# In[5]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




