#This is required for the code to make a pdf
from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", "B", 16)
pdf.cell(40, 10, "Todo List:")
pdf.set_font("helvetica", "", 14)

userinput = ""

#I'm using a term that isn't used in regular speech unless you have a
#vernacular that spans multiple decades of slang, like me
while userinput != "donezo!":
    userinput = input("What do you need to do?\n")
    if userinput == "donezo!":
        pdf.write(1, "")
    else:
        pdf.write(15,"\n" + userinput)

pdf.output("Todo-List.pdf")
