def get_multiplied_digits(number):
    str_number = str(number)
    if len(str_number) > 1:
        first = int(str_number[0])
        transfer_value = get_multiplied_digits(int(str_number[1:]))
        if first == 0:
            return transfer_value
        else:
            return first * transfer_value

    else:
        if str_number != "0":
            return int(str_number)
        else:
            return 1

if __name__ == "__main__":
    result = get_multiplied_digits(40203)
    print(result)
    result2 = get_multiplied_digits(402030)
    print(result2)
