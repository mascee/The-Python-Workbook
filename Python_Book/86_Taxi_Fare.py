# This program writes a function that calculates taxi fair.
# Base fare $4.00
# Plus $0.25 for every 140 meters travelled.

# Function that takes distance in km, converts to meters and computes taxi fare.
def taxi_fare(distance):
    BASE_FARE = 4
    RATE = 0.25
    distance_meters = distance*1000
    total = BASE_FARE + (distance_meters / 140) * RATE
    return total

def main():
    dist = float(input("how many km did you ride? "))
    total = taxi_fare(dist)
    print(f"Your fare is ${total:.2f}. ")

main()