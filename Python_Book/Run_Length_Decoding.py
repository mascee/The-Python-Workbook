# Exercise 185. Run-Length Decoding
# Run-length encoding is a simple data compression technique that can be effective when 
# repeated values occur at adjacent position within a list.
# Compression is achieved by replacing groups of repeated values with one copy
# of the value, followed by the number of times that it should be repeated.
# Write a recursive function that decompresses a run-length encoded list.

def decode(data):
    if not data:
        return []
    
    symbol = data[0]
    count = data[1]

    expanded = [symbol] * count

    return expanded + decode(data[2:])    


def main():
    data = ["A", 6, "B", 4, "C", 2]
    print(decode(data))

if __name__ == "__main__":
    main()