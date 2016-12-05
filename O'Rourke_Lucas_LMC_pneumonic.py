'''
Lucas O'Rourke
hw05
Part 2 - disassembler.py
'''

INS_REF = {0: "DAT", 1: "ADD", 2: "SUB", 3: "STA", 5: "LDA", 6: "BRA", \
           7: "BRZ", 8: "BRP"}

def disassemble(operation_code):
    if operation_code == "901":
        return "INP"
    elif operation_code == "902":
        return "OUT"
    elif operation_code == "000":
        return "HLT"
    else:
        if int(operation_code[0]) in INS_REF:
            return str(INS_REF[int(operation_code[0])]) + " " + \
                   operation_code[1] + operation_code[2]


def main():
    seen_done = False
    print("Enter operation codes on seperate lines")
    inp_lst = []
    while seen_done == False:
        user_inp = input()
        inp_lst.append(user_inp)
        if user_inp == "000":
            seen_done = True
    print()
    print("LMC mnemonic instructions:")
    for elem in inp_lst:
        output = disassemble(elem)
        print(output)

if __name__ == "__main__":
    main()
