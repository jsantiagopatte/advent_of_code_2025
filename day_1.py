import os

if __name__ == "__main__":
    folder_name = "input_files"
    file_name = "day_1.txt"
    current_dir = os.getcwd()

    # Import file
    file = open(os.path.join(current_dir, folder_name, file_name), 'r')

    # pos = 50
    # count = 0
    # for line in file:
    #     prev_pos = pos
    #     data = line.strip()
    #     direction = data[0]
    #     distance = int(data[1:])
    #     # Process turn
    #     if direction == "L":
    #         turn = -distance
    #     elif direction == "R":
    #         turn = distance
    #     pos = pos + turn

    #     if pos == 0:
    #         count +=1

    #     # Check for negative
    #     if pos < 0:
    #         if prev_pos != 0:
    #             count += abs(pos // 100)
    #         while pos < 0:
    #             pos = pos + 100

    #     # Check for larger than 100
    #     if pos > 99:
    #         count += abs(pos // 100)
    #         while pos > 99:
    #             pos = pos - 100

    #     print(pos, distance, count)
        
        

    # print(f"Failed password: {count}")

    file = open(os.path.join(current_dir, folder_name, file_name), 'r')
    pos = 50
    count = 0
    i = 0
    for line in file:
        i+=1
        print(f"Line {i}")
        data = line.strip()
        direction = data[0]
        distance = int(data[1:])
        while distance > 0:
            if direction == "L":
                pos -= 1
            if direction == "R":
                pos += 1
            if pos % 100 == 0:
                count += 1
            distance -= 1
                 

    print(f"New password: {count}")