# This program removes outliers from dataset (two largest and two smallest values)

data = []

def remove_outliers(data, num_outliers):
    if len(data) < num_outliers * 2:
        print("Not enough data to remove outliers. ")
        return data
    else:
        sorted_data = sorted(data)
        #Remove largest outliers
        for i in range(num_outliers):
            sorted_data.pop()
        
        #Remove smalles outliers
        for i in range(num_outliers):
            sorted_data.pop(0)

        return sorted_data
    

def main():
    data = []
    n = input("Enter integer(blank to quit): ")
    while n != "":
        data.append(n)
        n = input("Enter integer(blank to quit): ")

    if len(data) < 4:
        print("Not enough values to remove outliers. ")
    else:
        print(f"Data with outliers removed: {remove_outliers(data, 2)}")
    
if __name__ == "__main__":
    main()


