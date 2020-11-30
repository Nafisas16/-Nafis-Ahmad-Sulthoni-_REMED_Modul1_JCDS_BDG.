# nomor 1
def find_short(string_input):
    x = string_input.split()
    # print(x)
    char_length = []
    for char in x:
        length = len(char)
        char_length.append(length)

    char_length.sort()
    print(f'The shortest word has {char_length[0]} char(s)')
    
# find_short('Many people get up early in the morning')
# find_short('Every office would getting newest monitor')
find_short('Create new file after this morning')


# nomor 2

def persistance(input_angka):
    if input_angka < 0:
        print('Please input positive number only')
        exit()
    str_input = str(input_angka)
    
    if len(str_input) == 2:
        print(len(str_input)+1)
        print(f'Because {str_input[0]} x {str_input[1]} = {int(str_input[0]) * int(str_input[1])}')
        print(f'So it takes three times multiplication until we get a single digit')
    elif len(str_input) == 1:
        print(len(str_input)-1)
        print(f'{input_angka} is already single digit')
        print(f'So it takes zero times multiplication until we get a single digit')

    elif len(str_input) == 3:
        print(len(str_input)+1)
        print(f'Because {str_input[0]} x {str_input[1]} x {str_input[2]} = {int(str_input[0]) * int(str_input[1]) * int(str_input[2])}')
        print(f'So it takes three times multiplication until we get a single digit')

persistance(999)
