command = ""
car_started = False

while True:
    command = input("> ").lower()
    if command == "help":
        print('''
start - to start the car
stop - to stop the car
quit - to exit game''')
    elif command == "start":
        if car_started:
            print("Car is already started... Moron... Idiot!")
        else:
            print("Car started... Ready to go.")
            car_started = True
    elif command == "stop":
        if car_started:
            print("Car stopped.")
            car_started = False
        else:
            print("Car is already stopped... Are you blind!?")
    elif command == "quit":
        break
    else:
        print("I don't understand...")
