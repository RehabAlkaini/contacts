import json
print("------------------------------------------------------------------------------------------------------------------------")

print("                                                   CONTACTS                                                                                                 ")
print("------------------------------------------------------------------------------------------------------------------------")
#----------------------------------------------------------------------------------------------------------------------------------

def add_data():
    id = input("Enter the contact id:")
    with open("contact2.json","r") as getdata:
        data = json.load(getdata)
    
        if id  != data:
            print("The id is invild!!")
            input("Enter the contact id:")
        
    name = input("Enter the contact name:")
    no = input ("Enter the mobile number: ")
    email =input ("Enter the email: ")
    
    dic ={
        "Id :":id ,
        "Name :":name,
        "Mobile Numbe :":no,
        "Email :": email
    }
    
    with open("contact2.json","r") as getdata:
        data = json.load(getdata) #conver json to python
        data[no] = dic
        with open("contact2.json" , "w") as save:
            json.dump(data,save)  #convert python to json
            print ("Successful Added !")


# add_data()          
#----------------------------------------------------------------------------------------------------------------------------------

def view_data():
    with open("contact2.json","r") as view:
        data = json.load(view)
        
        for i,m in data.items():
            for x,n in m.items():
               print(x,n)
            print("\n")
                
# view_data()
#----------------------------------------------------------------------------------------------------------------------------------

def delete_data():
    name =input("Delete the contact name:")  
   
    with open("contact2.json","r") as getdata:
        data = json.load(getdata)
        if name in data:
             
        
             confirm = input("Do you want to delete this contact y/n ?:")
             if confirm =='y' or confirm =='Y':
                  data.pop(name)
                  with open("contact2.json","w") as delete:
                    data1 = json.dump(data ,delete)
                    print("Successful Delete !")
                 
             
# delete_data()
#----------------------------------------------------------------------------------------------------------------------------------
# def update_data():
#     id = input("Enter id: ")
#     with open("contact2.json","r") as getdata:
#         data = json.load(getdata)
#         if id  in data:
#             name = input("Enter New Name:")
#             no = input ("Enter the mobile number: ")
#             email =input ("Enter the email: ")
            
#             dic ={
#                 "Id:":id,
#                 "Name :" :name ,
#                 "Contact Numbe :" :no,
#                 "Email :" :email 
#             }
#             data[id] = dic
#             with open("contact2.json","w") as update:
#                 json.dump(data, update)
#                 print("Successful updated !")
# # update_data()
def update_data():
    id = input("Enter id : ")

    with open("contact2.json" , "r") as getdata :
        data = json.load(getdata) 

        if id in data:
            name =input("Enter New Name :")
            no =input("Enter New Phone Number :")
            email =input("Enter New Phone Email :")

            dic ={
            
         "Id :":id ,
        "Name :":name,
        "Mobile Numbe :":no,
        "Email :": email
    }
            
        

            data[id] = dic

            with open("contact2.json" , "w") as update :
                json.dump(data, update)
                print("Successfully Update")
#----------------------------------------------------------------------------------------------------------------------------------
def search_data():
    id = input("Enter id : ")
    
    with open("contact2.json" , "r") as getdata :
        data = json.load(getdata)
    
        if id in data:
            for i,m in data.items():
                if i==id:   
                    for x,n in m.items():
                        print(x,n)
# search_data()
#----------------------------------------------------------------------------------------------------------------------------------

def main():
    print("\n 1.Add new contac") 
    print("\n 2.Display contac ")
    print("\n 3.Delete contac")               
    print("\n 4.Edit contact")              
    print("\n 5.Search")
    print("\n 6.Exit")
    enter= int(input("\n Enter your choice: "))
    if enter == 1:
     add_data() 
     main()
    elif enter ==2 :
      view_data()
      main()
    elif enter ==3 :
      delete_data()
      main()
    
    elif enter ==4 :
     update_data()
     main()
    elif enter ==5 :
     search_data()
     main()
    
    else:
        print("\n THANK YOU ! AND COME AGAIN *_*")
main()        
        
        
    
     
    
          
                 
                
            
            
            
              