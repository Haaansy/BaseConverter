def slice_per(source, step):
    return [source[i::step] for i in range(step)]

def BinOctal(number):
    set = []
    output = ''
    
    
    for i, v in enumerate(number):
        set.append(v)
    
    while(len(set) % 3 != 0):
        set.insert(0, '0')
    
    parts = [set[i:i+3] for i in range(0, len(set), 3)]
    
    for i, v in enumerate(parts):
        c = 2
        value = 0
        
        for j, k in enumerate(parts[i]):
            parts[i][j] = int(k) * (2 ** c)
            c -= 1
            value += parts[i][j]
            
        output += str(value)
    
    return output        

def BinDecimal(number):
    set = []
    
    for digit in number:
        set.append(int(digit))
        
    length = len(set)
    
    for i, v in enumerate(set):
        set[i] = v * ( 2 ** ( length - 1 ))
        length -= 1
        
    return sum(set)

def BinHexadecimal(number):
    set = []
    output = ''
    
    
    for i, v in enumerate(number):
        set.append(v)
    
    while(len(set) % 4 != 0):
        set.insert(0, '0')
    
    parts = [set[i:i+4] for i in range(0, len(set), 4)]
    
    for i, v in enumerate(parts):
        c = 3
        value = 0
        
        for j, k in enumerate(parts[i]):
            parts[i][j] = int(k) * (2 ** c)
            c -= 1
            value += parts[i][j]
            
        if value == 10:
            value = 'A'
        elif value == 11:
            value = 'B'
        elif value == 12:
            value = 'C'
        elif value == 13:
            value = 'D'
        elif value == 14:
            value = 'E'
        elif value == 15:
            value = 'F'
        output += str(value)
    
    return output

def DecBinary(number):
    temporary = ''
    
    num = int(number)
    
    while num > 0:
        if num % 2 == 0:
            temporary += '0'
        elif num % 2 == 1:
            temporary += '1'
        else:
            break
        num = num // 2
        
    output = ''
    for i in temporary:
        output = i + output
         
    return int(output)

def DecOctal(number):
    temporary = ''
    
    num = int(number)
    
    while num!=0:
        rem = num % 8
        temporary += str(rem)
        num = int(num/8)
        
    output = ''
    for i in temporary:
        output = i + output
         
    return output

def DecHexadecimal(number):
    temporary = ''
    
    num = int(number)
    
    while num!=0:
        rem = num % 16
        if rem == 10:
            rem = 'A'
        elif rem == 11:
            rem = 'B'
        elif rem == 12:
            rem = 'C'
        elif rem == 13:
            rem = 'D'
        elif rem == 14:
            rem = 'E'
        elif rem == 15:
            rem = 'F'
        temporary += str(rem)
        num = int(num/16)
        
    output = ''
    for i in temporary:
        output = i + output
         
    return output

def OctalBin(number):
    key = {
        0 : '000',
        1 : '001',
        2 : '010',
        3 : '011',
        4 : '100',
        5 : '101',
        6 : '110',
        7 : '111'
    }
    
    set = []
    
    output = ''
    
    for i, v in enumerate(number):
        set.append(v)
    
    for i, v in enumerate(set):
        set[i] = key[int(v)]
        
    for item in set:
        output += item
    
    return int(output)

def OctalDecimal(number):
    set = []
    for v in number:
        set.append(int(v))
        
    length = len(set)
    for i, v in enumerate(set):
        set[i] = v * ( 8 ** (length - 1))
        length -= 1
        
    return sum(set)

def OctalHexadecimal(number):
    Binary = OctalBin(number)
    output = BinHexadecimal(Binary)
    
    return output
    
def HexaBin(number):
    key = {
        '0' : '0000',
        '1' : '0001',
        '2' : '0010',
        '3' : '0011',
        '4' : '0100',
        '5' : '0101',
        '6' : '0110',
        '7' : '0111',
        '8' : '1000',
        '9' : '1001',
        'A' : '1010',
        'B' : '1011',
        'C' : '1100',
        'D' : '1101',
        'E' : '1110',
        'F' : '1111'
    }
    
    set = []
    
    output = ''
    
    for i, v in enumerate(number):
        set.append(v)
    
    for i, v in enumerate(set):
        set[i] = key[v]
        
    for item in set:
        output += item
    
    return int(output)

def HexaDec(number):
    set = []
    for v in number:
        set.append(v)
        
    length = len(set)
    
    for i, v in enumerate(set):
        if v == 'A':
            set[i] = 10 * ( 16 ** (length - 1))
        elif v == 'B':
            set[i] = 11 * ( 16 ** (length - 1))
        elif v == 'C':
            set[i] = 12 * ( 16 ** (length - 1))
        elif v == 'D':
            set[i] = 13 * ( 16 ** (length - 1))
        elif v == 'E':
            set[i] = 14 * ( 16 ** (length - 1))
        elif v == 'F':
            set[i] = 15 * ( 16 ** (length - 1))
        else:
            set[i] = int(v) * ( 16 ** (length - 1))
        length -= 1
        
    return sum(set)

def HexaOctal(number):
    Binary = HexaBin(number)
    output = BinOctal(str(Binary))
    
    return output

def main():
    while True:
        base = input('which base would you like to use? ( Binary, Octal, Decimal, Hexadecimal ): ')
        if base.lower() not in ('binary', 'octal', 'decimal', 'hexadecimal'):
            print('Invalid Selection. Binary, Octal, Decimal, or Hexadecimal only.')
        else:
            break
        
    if base.lower() == 'binary':
        while True:
            try:
                number = input("\nPlease enter a binary number: [ 0 & 1 ]: ")
                for digit in (number):
                    if digit not in ('0', '1'):
                        raise ValueError
            except ValueError:
                print("Enter a Binary number. Please try again.")
            else:
                break     
        
        oct = BinOctal(str(number)) 
        dec = BinDecimal(str(number))
        hex = BinHexadecimal(str(number))
                    
        print('Binary: ', number)
        print('Decimal: ', dec) 
        print('Octal: ', oct)
        print('Hexadecimal: ', hex)
        redo()
    elif base.lower() == 'octal':
        while True:
            try:
                number = input("\nPlease enter an octal number: [ 0 - 7 ]:")
                for digit in (number):
                    if digit not in ('0', '1', '2', '3', '4', '5', '6', '7'):
                        raise ValueError
            except ValueError:
                print("Enter an Octal number. Please try again.")
            else:
                break 
            
        bin = OctalBin(number)
        dec = OctalDecimal(number)
        hex = OctalHexadecimal(number)
            
        print('Octal: ', number)
        print('Binary: ', bin)
        print('Decimal: ', dec)
        print('Hexadecimal: ', hex)
        redo()
    elif base.lower() == 'decimal':
        while True:
            try:
                number = int(input("\nPlease enter a Decimal number: [ 0 - 9 ]:"))
            except ValueError:
                print("Enter a Decimal number. Please try again.")
            else:
                break
            
        bin = DecBinary(number)
        oct = DecOctal(number)
        hex = DecHexadecimal(number)
        
        print('Decimal: ', number)
        print('Binary: ', bin)
        print('Octal: ', oct)
        print('Hexadecimal: ', hex)   
        redo()
    elif base.lower() == 'hexadecimal':
        while True:
            try:
                number = input("\nPlease enter a Hexadecimal number: [ 0 - F ]:")
                for digit in (number):
                    if digit not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'):
                        raise ValueError
            except ValueError:
                print("Enter a Hexadecimal number. Please try again.")
            else:
                break
            
        bin = HexaBin(number)
        dec = HexaDec(number)
        oct = HexaOctal(number)
        
        print('Hexadecimal: ', number)
        print('Binary: ', bin)
        print('Decimal: ', dec)
        print('Octal: ', oct)
        redo()

def redo():
    choices = input('Would you like to convert another number? [ Y / N ]: ')
    if choices.lower() == 'y':
        main()
    else:
        print('Thank you, Goodbye!')
        quit()
        
main()
    
