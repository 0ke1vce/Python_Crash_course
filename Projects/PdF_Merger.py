# pip install pypdf2
import PyPDF2

pdfiles = ["1.pdf","2.pdf"]
merger = PyPDF2.PdfMerger()

for pdf in pdfiles:
    pd_file = open(pdf,'rb')
    pdfReader = PyPDF2.PdfReader(pd_file)
    merger.append(pd_file)
pd_file.close()
merger.write('merged.pdf')