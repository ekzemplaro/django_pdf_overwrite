# --------------------------------------------------------------------
#
#	overwrite/lib/pdf_generate.py
#
#						Jan/13/2019
# --------------------------------------------------------------------
import	sys
import	os
import	glob

from datetime import datetime
#
from pdfrw import PdfReader
from pdfrw.buildxobj import pagexobj
from pdfrw.toreportlab import makerl
#
from reportlab.pdfgen import canvas
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.pdfbase import pdfmetrics

# ------------------------------------------------------------------
def pdf_generate_proc(file_template,file_pdf,receiver,price):
	sys.stderr.write("*** pdf_generate_proc *** start ***\n")
#
	pdf_canvas = canvas.Canvas(file_pdf)
#
	fontname_g = "HeiseiKakuGo-W5"
	pdfmetrics.registerFont (UnicodeCIDFont (fontname_g))
	pdf_canvas.setFont(fontname_g,16)
	#
	page = PdfReader(file_template,decompress=False).pages
	pp = pagexobj(page[0])
	pdf_canvas.doForm(makerl(pdf_canvas, pp))
#
	today = datetime.today()
	str_today = today.strftime('%Y-%m-%d')
	#
	pdf_canvas.drawString(400, 800, str_today)
	pdf_canvas.drawString(100, 725, receiver)
	pdf_canvas.drawString(100, 680, str(price))
	#
	draw_rect_proc(pdf_canvas)
#
	pdf_canvas.showPage()
	pdf_canvas.save()
#
	sys.stderr.write("*** pdf_generate_proc *** end ***\n")
#
	str_res = "Supdf_canvasess"
	return str_res
# --------------------------------------------------------------------
def draw_rect_proc(pdf_canvas):
	sys.stderr.write("*** draw_rect_proc *** start ***\n")
	xp = 30
	xlist = (xp, xp+310, xp+345, xp+385, xp+450, xp+520)
	yp = 290
	ylist = (yp,yp+25,yp+50,yp+75,yp+100,yp+125,yp+150,yp+175,yp+178,yp+200)

	pdf_canvas.grid(xlist, ylist)
	sys.stderr.write("*** draw_rect_proc *** end ***\n")
# --------------------------------------------------------------------
