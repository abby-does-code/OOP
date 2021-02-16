import car.py as car

print("Let's make your car.")
    
y  = input("What's  the year of your car? ")
mo = input("What's the model of your car? ")
m  = input("What's the make of your car? ")
my_car = car.Car(y, mo, m)

def main(my_car):
    move = input("Speed up or slow down? ")
    if move = 'speed up':
        my_car.accelerate()
    else:
        my_car.brake()

main()




