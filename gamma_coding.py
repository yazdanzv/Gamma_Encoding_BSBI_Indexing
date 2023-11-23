class GammaCoding:
    @staticmethod
    def encode(number):
        bin_num = bin(number)
        offset = bin_num[3:]
        length = '1' * len(offset) + '0'
        gamma_code = length + offset
        return gamma_code

    @staticmethod
    def decode(code):
        count = 0
        lst_binary = []
        lst_decimal = []
        i = 0
        while i < len(code):
            if code[i] == '1':
                count += 1
                i += 1
            else:
                i += 1
                lst_binary.append(code[i:i + count])
                i += count
                count = 0
        for i in range(len(lst_binary)):
            lst_binary[i] = '1' + lst_binary[i]
            lst_decimal.append(int(lst_binary[i], 2))
        return lst_binary, lst_decimal
