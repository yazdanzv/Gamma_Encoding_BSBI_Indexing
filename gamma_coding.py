class GammaCoding:
    @staticmethod
    def encode(number):  # Method to encode an individual integral number
        bin_num = bin(number)
        offset = bin_num[3:]  # Calculate the offset
        length = '1' * len(offset) + '0'  # Calculate the length
        gamma_code = length + offset
        return gamma_code

    @staticmethod
    def encode_list(lst: list):  # Method to encode a list of integral numbers
        code = ""
        for i in range(len(lst)):
            code += GammaCoding.encode(int(lst[i]))  # Final code
        return code

    @staticmethod
    def decode(code):  # Method to decode the coded string to the list of integral numbers
        count = 0
        lst_binary = []  # Final list of binary number
        lst_decimal = []  # Final list of decimal numbers
        i = 0
        while i < len(code):
            if code[i] == '1':  # Checks the length
                count += 1
                i += 1
            else:
                i += 1
                lst_binary.append(code[i:i + count])  # Append the offset
                i += count
                count = 0
        for i in range(len(lst_binary)):  # Add the highest 1 value to offsets
            lst_binary[i] = '1' + lst_binary[i]
            lst_decimal.append(int(lst_binary[i], 2))  # Calculate decimal numbers
        return lst_binary, lst_decimal  # Return both lists
