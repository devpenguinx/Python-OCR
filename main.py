from cgitb import text
from itertools import tee
from PyPDF2 import PdfFileReader, PdfFileWriter
import os

directorypath = 'E:/'
for filename in os.listdir(directorypath):
    f = os.path.join(directorypath, filename)
    if os.path.isfile(f):
        file_path = f
        pdf = PdfFileReader(file_path)

        with open('image.txt', 'w') as l:
            pageobj = pdf.getPage(0)

            txt = pageobj.extract_text()
            l.write(txt)

        with open('image.txt', 'r') as l:

            for line in l:
                if 'Document' in line:
                    index = 0
                    index = line.find('Document')
                    # print(line)
                    #print('index', index)
                    name = ''
                    name = 'E:/I' + line[index + 13:]
                    name = name.strip('\n')
                    name += '.pdf'
                    print('name:', name)
                    if not os.path.exists(name):
                        # print('renamed')
                        os.rename(f, name)
