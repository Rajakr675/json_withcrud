
import json,os
day={}
while True:
    print("""
    press 1 for create
    press 2 for update
    press 3 for delete
    press 4 for read
    press 5 for exist""")

    def create():
        try:
            if  not os.path.exists('crud.json'):
                with open('crud.json','w') as p:
                    json.dump(day,p,indent=4)
            with open('crud.json','r') as p:
                d=json.load(p)
                p1=input("Enter Your Email :")
                if "@" in p1:
                    if str(p1) not in d:
                        with open('crud.json','w') as p4:
                            j={"Name":input("Enter Name>"),
                            "Age":int(input("Enter Age>"))}
                            d[str(p1)]=j
                            # with open('pra.json','w') as p:
                            json.dump(d,p4,indent=4)
                            
                    else:
                        print("Email not exist")
                else:
                    print("Please Enter Right Email")
                
        except:

            p1=input("Enter Your Email :")
            if "@" in p1:
                with open('crud.json','w') as p:
                    j={"Name":input("Enter Name>"),
                    "Age":int(input("Enter Age>"))}
                    day[str(p1)]=j
                    json.dump(day,p,indent=4)


    def update():
        try:
            
            p1=input("Enter Your Email :")
            if "@" in p1:
                with open("crud.json","r") as p:
                    d=json.load(p)
                    if p1 in d:
                        with open('crud.json','w') as p2:
                            j={"Name":input("Enter Name>"),
                            "Age":int(input("Enter Age>"))}
                            d[str(p1)]=j
                            
                            json.dump(d,p2,indent=4)
                    else:
                        print("Email not exist")
            
        except:
            print("Email not exist")


    def delete():
        try:
            
            p1=input("Enter Your Email :")
            if "@" in p1:
                with open("crud.json","r") as p:
                    d=json.load(p)
                    if p1 in d:
                        with open('crud.json','w') as p2:
                            d.pop(p1)
                            
                            json.dump(d,p2,indent=4)
                    else:
                        print("Email not exist")
        except:
            print("Email not exist")
        
    def read():
        try:
            
            p1=input("Enter Your Email :")
            if "@" in p1:
                with open("crud.json","r") as p:
                    d=json.load(p)
                    if p1 in d:
                        # with open('pra.json','w') as p2:
                            print(d[p1])
                            
                    else:
                        print("Email not exist")
        except:
            print("Email not exist")



    c=int(input("Choose your option : "))
    if c==1:
        create()
    elif c==2:
        update()
    elif c==3:
        delete()
    elif c==4:
        read()
    elif c==5:
        break

