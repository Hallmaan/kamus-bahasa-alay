import csv, shutil
from difflib import SequenceMatcher
from tempfile import NamedTemporaryFile
import numpy as np

def readKataData(fname):
    tempfile = NamedTemporaryFile(mode='w', delete=False)
    with open(fname, 'r') as read_file, tempfile:
        reader = csv.DictReader(read_file)
        header = reader.fieldnames
        writer = csv.DictWriter(tempfile, fieldnames=header)
        data_reader = list(reader)
        return data_reader

def readKataAlay(fname):
    tempfile = NamedTemporaryFile(mode='w', delete=False)
    with open(fname, 'r') as read_file, tempfile:
        reader = csv.DictReader(read_file)
        header = reader.fieldnames
        writer = csv.DictWriter(tempfile, fieldnames=header)
        data_reader = list(reader)
        return data_reader

def writeCsv(data, file):
    tempfile = NamedTemporaryFile(mode='w', delete=False)
    with open(file, 'r') as read_file, tempfile:

        reader = csv.DictReader(read_file, delimiter=',', skipinitialspace=True)
        header = reader.fieldnames
        writer = csv.DictWriter(tempfile, fieldnames=header)
        writer.writeheader()

        try:
            [writer.writerow({header[0]: data[i]['kata alay'], header[1]: data[i]['kode'], header[2]: data[i]['kata kamus'], header[3]: data[i]['matcher'],header[4]: data[i]['minimumEdit'], header[5]: data[i]['perbaikan_kata'], header[6]: data[i]['perbaikan_kata_2']}) for i, row
             in enumerate(list(data))]

            print('parsing success')
        except Exception as err:
            print(err)
    shutil.move(tempfile.name, file)

def levenshtein(seq1, seq2):
    size_x = len(seq1) + 1
    size_y = len(seq2) + 1
    matrix = np.zeros ((size_x, size_y))
    for x in range(size_x):
        matrix [x, 0] = x
    for y in range(size_y):
        matrix [0, y] = y

    for x in range(1, size_x):
        for y in range(1, size_y):
            if seq1[x-1] == seq2[y-1]:
                matrix [x,y] = min(
                    matrix[x-1, y] + 1,
                    matrix[x-1, y-1],
                    matrix[x, y-1] + 1
                )
            else:
                matrix [x,y] = min(
                    matrix[x-1,y] + 1,
                    matrix[x-1,y-1] + 1,
                    matrix[x,y-1] + 1
                )
    return (matrix[size_x - 1, size_y - 1])

def match_ratio(name1, name2):
    s = SequenceMatcher(None, name1, name2)
    return s.ratio()

def getDataKata(kataAlay, kode):
    dataKata = readKataData('KAMUSDUMMY.csv')
    listArray = []
    for x in dataKata:
        if x['kode'] == kode:
            dict = {}
            dict['kata alay'] = kataAlay
            dict['kode'] = x['kode']
            dict['kata kamus'] = x['katakunci']
            minimumEditDistance = levenshtein(kataAlay, x['katakunci'])
            sequenceMatchers = match_ratio(kataAlay, x['katakunci'])
            dict['matcher'] = round(sequenceMatchers, 3)
            dict['minimumEdit'] = minimumEditDistance
            listArray.append(dict)
    return listArray

def main(fname, writeFile):

    dataAlay = readKataAlay(fname)
    output = []

    for i in dataAlay:
        kata = getDataKata(i['kata alay'], i['kode'])
        if(len(kata) > 0):
            maxMatcher = max(kata, key=lambda x: x['matcher'])
            for z in kata:
                z['perbaikan_kata_2'] = ''
                z['perbaikan_kata'] = maxMatcher['kata kamus']
                if(z['matcher'] == maxMatcher['matcher']):
                    if(z['kata kamus'] != maxMatcher['kata kamus']):
                        if(z['minimumEdit'] >= maxMatcher['minimumEdit']):
                            z['perbaikan_kata_2'] = z['kata kamus']
                output.append(z)
    writeCsv(output, writeFile)

if __name__ == '__main__':
    main('OOVDUMMY.csv', 'write.csv')