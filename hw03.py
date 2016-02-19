def dec_to_bin(dec_num): # Number 2
    bin_num = bin(dec_num)
    print(dec_num, "in binary is", bin_num)


def hex_to_ascii(hex_string): # Number 3
    ascii_string = ""
    split = hex_string.split()
    for elem in split:
        dec_num = int(elem, 16)
        ascii_string += chr(dec_num)
    print(ascii_string)
               

def bin_to_hex(bin_num): # Number 4
    split = bin_num.split()
    hex_str = ""
    for elem in split:
        dec = int(elem, 2)
        hex_num = hex(dec)
        hex_str += hex_num
    hex_str = hex_str.replace("0x", "")
    new_hex_str = "0x"+hex_str
    print(new_hex_str)


def base8_to_dec(base8_num): # Number 5
    str_base8 = str(base8_num)
    reverse_base8 = str_base8[::-1]
    dec_val = 0
    for ind in range(0, len(reverse_base8)):
        int_num = int(reverse_base8[ind])
        dec_val += (8**(ind)) * int_num
    print("The octal number", base8_num, "as a decimal value is", dec_val)


def main():
    print("Problem 1 on word doc")
    print("")
    print("Problem 2:")
    dec_to_bin(57) #2a
    dec_to_bin(123) #2b
    dec_to_bin(85) #2c
    dec_to_bin(38) #2d
    print("")

    print("Problem 3:")
    #3a
    hex_to_ascii("0x41 0x53 0x43 0x49 0x49 0x20 0x77 0x68 0x61 0x74 0x20 0x79 0x6f 0x75 0x20 0x64 0x69 0x64 0x20 0x74 0x68 0x65 0x72 0x65")
    #3b
    hex_to_ascii("0x39 0x41 0x4d 0x20 0x69 0x73 0x20 0x74 0x6f 0x6f 0x20 0x65 0x61 0x72 0x6c 0x79 0x20 0x66 0x6f 0x72 0x20 0x63 0x6c 0x61 0x73 0x73")
    #3c
    hex_to_ascii("0x43 0x6f 0x6d 0x70 0x75 0x74 0x65 0x72 0x73 0x20 0x61 0x72 0x65 0x20 0x6d 0x61 0x67 0x69 0x63")
    #3d
    hex_to_ascii("0x57 0x68 0x61 0x74 0x20 0x74 0x68 0x65 0x20 0x68 0x65 0x78 0x3f") 
    print("")

    print("Problem 4:")
    bin_to_hex("0000 1011 1010 1110 1101 1110 1010 1101") #4a
    bin_to_hex("1100 1010 1111 1110 1111 1010 1100 1110") #4b
    bin_to_hex("1011 1110 1110 1111 1101 0000 0000 1101") #4c
    bin_to_hex("1111 1111 1111 1111 1001 0000 0110 0010") #4d
    print("")

    print("Problem 5:")
    base8_to_dec(10) #5a
    base8_to_dec(42) #5b
    base8_to_dec(77) #5c
    base8_to_dec(113) #5d
    
    


main()
