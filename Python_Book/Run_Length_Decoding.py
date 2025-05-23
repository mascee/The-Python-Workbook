# Exercise 185. Run-Length Decoding
# Run-length encoding is a simple data compression technique that can be effective when 
# repeated values occur at adjacent position within a list.
# Compression is achieved by replacing groups of repeated values with one copy
# of the value, followed by the number of times that it should be repeated.
# Write a recursive function that decompresses a run-length encoded list.

def decode(data):
    # If there are only letters, return original list
    if all(isinstance(item, str) and item.isalpha() for item in data):
        return data
    for i in data:
        if data[i].isdigit():
            