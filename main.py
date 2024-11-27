from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")              # Initializes the FPDF object
pdf.set_auto_page_break(auto=False, margin=0)                    # Disables automatic page breaks to have more control over page layout.

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()  # Adding the master page

    # set the header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 0, 0)  # RGB=100,100,100 gives grey = 254,0,0 gives red
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    for y in range(20, 298, 10):                            # This loop draws horizontal lines from the left (x=10) to the right (x=200) at every 10 mm from 20 mm down to 298 mm.
        pdf.line(10, y, 200, y)
       

    # Set the footer for master page
    pdf.ln(265)                               # Adds 265 line breaks in mm

    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(10, 10, 250)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    for i in range(row["Pages"] - 1):         # To add multiple pages of each topic
        pdf.add_page()

        # set the footer
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(10, 10, 250)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

        for y in range(20, 298, 10):           # To add multiple lines in rest of the pages
            pdf.line(10, y, 200, y)

# pdf.add_page()

# pdf.set_font(family="Times", style="B", size=12)
# pdf.cell(w=0, h=12, txt="Hello there", align="L", ln=1)

# pdf.set_font(family="Times", size=12)            # keep size and h = same   # takes 3 argu(family,style='B',size)
# pdf.cell(w=0, h=12, txt="Hi there", align="L", ln=1)   # takes 5 argu(width, height,text, align,ln,border)


pdf.output("output.pdf")
