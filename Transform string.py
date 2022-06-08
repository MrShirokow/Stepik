with open ('input.txt') as file_in, open("out.txt", 'w') as file_out:
    chars = [c for c in file_in.readline().strip()]

    current_position = 0
    result = ''
    lenght = len(chars)

    while current_position < lenght - 1:
        count = ''
        if chars[current_position].isalpha():
            temp = chars[current_position]
            current_position += 1
            while current_position != lenght and chars[current_position].isdigit():
                count += chars[current_position]
                current_position += 1
            result += temp * int(count)

    file_out.write(result)