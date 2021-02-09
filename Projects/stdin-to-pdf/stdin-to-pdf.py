from fpdf import FPDF
pdf = FPDF()
pdf.add_page()
txt = input("Set author name: ")
pdf.set_author(txt)
filename = input("Set file name: ")
pdf.set_font("Arial", size=12)
print("Start typing, type /stop to save and exit")
while True:
    line = input()
    if line == "/stop":
        break
    pdf.cell(200, 10, txt=line, ln=1, align="L")

pdf.output(filename+".pdf")
print("file saved to ./"+filename+".pdf")