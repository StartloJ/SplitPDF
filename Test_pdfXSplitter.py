from pyPdf import PdfFileWriter, PdfFileReader
import os
from glob import glob

def get_file():
    lstFile = glob('resource\*.pdf')
    return lstFile

def splitXPDF(pdfFileName):
    try:
        inputpdf = PdfFileReader(open(pdfFileName , "rb"))

        print '[+] Total Page : ' + str(inputpdf.getNumPages())

        setpath = pdfFileName[pdfFileName.find('\\')+1:pdfFileName.find('.')]
        lstName = []
        with open("nameFile.base", "r") as nameFile:
                lstName = nameFile.read().split('\n')
                
        if(inputpdf.getNumPages() == len(lstName)):
            for i in xrange(inputpdf.numPages):
                output = PdfFileWriter()
                output.addPage(inputpdf.getPage(i))
                if(os.path.isdir('resault') != True):
                    os.mkdir('resault')
                if(os.path.isdir('resault\\'+setpath) != True):
                    os.mkdir('resault\\'+setpath)
                
                with open('resault\\' + setpath + '\\' + lstName[i] + '.pdf' , 'wb') as outputStream:
                    output.write(outputStream)
                print '[+] Generate Page '+ str(i+1) + ' with File : ' + lstName[i] + '.pdf'

        else:
            print '[-] Number of Name in \'nameFile.base\' is not match with Number Page in PDF.'
    except IOError:
        print '[-] Cannot Openfile.'
    

if __name__ == '__main__':
    AllFile = get_file()
    for fly in AllFile:
        splitXPDF(fly)