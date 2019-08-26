from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
w, h = A4
# Dibujar una línea horizontal.
x = 10
y = h - 80
c = canvas.Canvas("hola-mundo.pdf", pagesize=A4)
c.drawString(185, h - 50, "Instituto Politecnico La Esperanza")
c.drawString(200, h - 60, "Reporte de Estudiantes")
c.line(x, y, x + 500, y)
c.showPage()
c.save()
