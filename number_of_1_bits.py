def get_count_of_1_bits(number: int) -> int:
    count: int = 0
    while number > 0:
        if number & 1:
            count += 1
        number >>= 1
    return count


try:
    number1 = int(input("Enter an integer : "))
    print(get_count_of_1_bits(number1))
except ValueError:
    print("Invalid input. Please enter only integers.")
