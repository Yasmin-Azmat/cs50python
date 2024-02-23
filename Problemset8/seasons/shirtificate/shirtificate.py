from fpdf import FPDF

def main():
    name = input('Name: ')

    # Create a PDF object with A4 format, 'mm' unit, and 'Portrait' orientation
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    # Add header
    pdf.set_font('helvetica', 'B', 30)
    pdf.cell(200, 50, 'CS50 Shirtificate', ln=True, align='C')

    # Add shirt image
    pdf.image('C:\Python(Harvard)\Problemset8\seasons\shirtificate\shortificate.png', x=20, y=80, w=170)

    # Set text color to white for printing inside the shirt
    pdf.set_text_color(r=255, g=255, b=255)

    # Set position for the text inside the shirt
    pdf.set_x(20)
    pdf.set_y(150)

    # Print the name inside the shirt
    pdf.cell(170, 10, f'{name} took CS50', ln=True, align='C')

    # Save the PDF
    pdf.output('Text_On_Tshirt.pdf')

if __name__ == '__main__':
    main()
