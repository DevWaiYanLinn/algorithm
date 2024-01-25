n = int(input("Please enter number : "))

if n >= 2:
    direction = ["right", "down", "left", "top"]
    frames = []
    current_row = 0

    for i in range(n):
        f = [0 for _ in range(n)]
        frames.append(f)

    current_number = -1
    current_index = -1

    while n > 0:
        current_direction = direction[0]
        for i in range(n):
            if current_direction == "right":
                current_index = current_index + 1
                current_number = current_number + 1
                frames[current_row][current_index] = current_number

            if current_direction == "down":
                frames[current_row + 1][current_index] = current_number + 1
                current_number = current_number + 1
                current_row = current_row + 1

            if current_direction == "left":
                current_number = current_number + 1
                current_index = current_index - 1
                frames[current_row][current_index] = current_number

            if current_direction == "top":
                current_row = current_row - 1
                current_number = current_number + 1
                frames[current_row][current_index] = current_number

        if current_direction == "right" or current_direction == "left":
            n = n - 1

        temp = direction[0]
        del direction[0]
        direction.append(temp)

    for f in frames:
        print(f)
else:
    print('"n" must be greater than or equal 2')
