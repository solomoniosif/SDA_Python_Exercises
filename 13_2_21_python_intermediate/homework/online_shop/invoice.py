from fpdf import FPDF


class Invoice:
    @classmethod
    def generate_invoice(self, cart):
        pdf = FPDF(orientation="P", unit="pt", format="A4")
        pdf.add_page()

        pdf.set_font(family='Arial', size=24, style='B')
        pdf.cell(w=0, h=80, txt=cart.user.name, border=1, align="C", ln=1)
        pdf.cell(w=100, h=40, txt="Period:", border=1)
        # pdf.cell(w=150, h=40, txt=bill.period, border=1, ln=1)
        # pdf.cell(w=0, h=30, txt="", border=0, ln=1)
        # pdf.cell(w=150, h=40, txt=flatmate1.name, border=0)
        # pdf.cell(w=50, h=40, txt=str(flatmate1.pays(bill, flatmate2)), border=0, ln=1)
        # pdf.cell(w=150, h=40, txt=flatmate2.name, border=0)
        # pdf.cell(w=50, h=40, txt=str(flatmate2.pays(bill, flatmate1)), border=0, ln=1)

        pdf.output(self.filename)
        return True