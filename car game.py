command = ""
started = False
stopped = False
while True :
    command = input("> ").lower()
    if command == "start" :
        if  started :
            print("Car already started")
        else :
            started = True
            print("Car started....")
    elif command == "stop" :
        if (not started) or stopped :
            print("Car already stopped")
        else : 
            stopped = True   
            print("Car stopped....")
    elif command == "help" :    
      print(""" 
 start - To start the car
 stop - To stop the car
 quit - To quit     
            """)
    elif command == "quit" :
      break        
    else :
       print("Sorry, i dont understand that") 

