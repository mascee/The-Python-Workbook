# Exercise 186. Run-Length Encoding
# Write a recursive function that implements the run-length compression technique

def encode(data):
    if not data:
        return []
    index = 1
    while index < len(data) and data[index] == data[index -1]:
          index += 1
    
    current = [data[0], index]

    return current + encode(data[index : len(data)])

def main():
     s = input("Enter a list of characters: ")
     data = list(s)
     print("Encoded: ")
     print(encode(data))

if __name__ == "__main__":
     main()