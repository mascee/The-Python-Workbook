# Exercise 136. Reverse Lookup.
# This program has a function reverseLookup that finds all the keys in a dictionary 
# that map to a specific value.
# The function takes the dictionary and the value to search for as its only parameters.
# It returns a list of keys from the dictionary that map to the provided value.


def reverseLookup(data, value):
    keys = []

    for key in data:
        if data[key] == value:
            keys.append(key)

    return keys

def main():
    items = {'Apple': 'Red',
              'Roses': 'Blue',
              'Sky': 'Blue',
              'Blood': 'Red',
              'Grass': 'Green',
              'Traffic Light': 'Red',
              'Chicks': 'Yellow',
              'Clouds': 'White',
              'Walls': 'White',
              'Chocolate': 'Brown',
              'Algae': 'Green',
              'Army': 'Red'
        
    }
    print(f"Here is the list of all Red items : {reverseLookup(items, 'Red')}")

if __name__ == "__main__":
    main()

