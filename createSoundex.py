import csv, shutil
from tempfile import NamedTemporaryFile

# ALGORITMA
# 1. Ambil huruf pertama dari kata
# 2. Ganti huruf selanjutnya dengan nilai angka pada tabel
# 3. Jika terdapat huruf yang lebih dari 1 kali, ambil 1 huruf saja dan abaikan huruf lain
# 4. Abaikan huruf dengan nilai angka nol (0)
# 5. Stop mengganti huruf dengan angka sampai 3 angka saja
# 6. Ambil huruf terakhir dari kata
# 7. Gabungkan huruf pertama + 3 angka + huruf terakhir menjadi 1 kode

zero = ['a', 'e', 'i', 'o', 'u']
one = ['w', 'y']
two = ['f', 'h', 'q', 's', 'v', 'x', 'z']
three = ['b', 'c', 'd', 'g', 'j', 'k', 'p', 't']
four = ['l']
five = ['m', 'n']
six = ['r']
library = {'zero': zero, 'one': one, 'two': two, 'three': three, 'four': four, 'five': five, 'six': six}


# func check count of code
def check_code(arg):
    code = {arg == 0: '000', arg == 1: '00'}.get(True, '0')
    return code


# func check character
def check_char(arg):
    key_dic = ''
    for key, val in library.items():
        if arg in val:
            key_dic = key
    return key_dic


# function change string to number
def string_to_number(arg):
    switcher = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6
    }
    return switcher.get(arg, "nothing")


# function process Kata
def processKata(kata):
    temp_kata = ''
    code = ''
    first_last = kata[:1].capitalize() + kata[1:].capitalize()
    for i in kata:
        if i not in temp_kata:
            temp_kata += i
    count_kata = len(temp_kata)

    for i in range(1, count_kata):
        key_dic = check_char(temp_kata[i])
        rpl_val = string_to_number(key_dic)
        if len(code) < 3:
            if rpl_val != 0:
                code += str(rpl_val)

    count_code = len(code)
    if count_code < 3:
        code += check_code(count_code)

    if len(first_last) > 1:
        last_result = first_last[0] + code + first_last[1]   # Jika tidak menggunakan last character
    else:
        last_result = first_last[0] + code + first_last[0]

    return (last_result)


def main(fname):
    tempfile = NamedTemporaryFile(mode='w', delete=False)
    with open(fname, 'r') as read_file, tempfile:
        reader = csv.DictReader(read_file)
        header = reader.fieldnames
        writer = csv.DictWriter(tempfile, fieldnames=header)

        data_reader = list(reader)
        soundex = [processKata(i.get('kata alay')) for i in data_reader]
        writer.writeheader()
        try:
            [writer.writerow({header[0]: row[header[0]], header[1]: row[header[1]], header[2]: soundex[i]}) for i, row
             in enumerate(data_reader)]

            print('parsing success')
        except Exception as err:
            print(err)
    shutil.move(tempfile.name, fname)


if __name__ == '__main__':
    main('OOVSOUNDEX.csv')