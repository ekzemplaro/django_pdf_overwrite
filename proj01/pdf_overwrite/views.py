# --------------------------------------------------------------------
#
#	overwrite/views.py
#
#						Jan/04/2019
# --------------------------------------------------------------------
import	sys
import	os
import	glob

from datetime import datetime
#
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from pdfrw import PdfReader
from pdfrw.buildxobj import pagexobj
from pdfrw.toreportlab import makerl
#
from reportlab.pdfgen import canvas
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.pdfbase import pdfmetrics

# ------------------------------------------------------------------
def index(request):
	message = ""
	message += 'pdf_overwrite からのメッセージです。<br />'
	message += str(request.user.id) + '&nbsp;&nbsp;'
	message += request.user.username + '<p />'
	dd = {
		'hour': datetime.now().hour,
		'minute': datetime.now().minute,
		'message': message,
	}
	return render(request, 'pdf_overwrite/pdf_overwrite.html', dd)
#
# ------------------------------------------------------------------
@csrf_exempt 
def pdf_main_proc(request):
	response = None
	sys.stderr.write("*** pdf_main_proc *** start ***\n")
#
	if (request.method == 'POST'):
		flags = None
#
		pdf_out = request.POST['pdf_out']
		receiver = request.POST['receiver']
		price = request.POST['price']
		str_message = ""
		str_message += "*** message ***\n"
		str_message += "receiver: " + receiver + "\n"
		str_message += "price: " + price + "\n"
		str_message += "*** message ***\n"
#
		sys.stderr.write("*** receiver: " + receiver+ "\n")
		sys.stderr.write("price: " + price + "\n")
		try:
			response = pdf_generate_proc(pdf_out,receiver,price)
		except Exception as ee:
			sys.stderr.write("*** error *** in pdf_generate_proc ***\n")
			sys.stderr.write(str(ee) + "\n")
#
	sys.stderr.write("*** pdf_main_proc *** end ***\n")
#
	str_out = "Success"
	return response
#	return HttpResponse(str_out)
# --------------------------------------------------------------------
def pdf_generate_proc(pdf_out,receiver,price):
	sys.stderr.write("*** pdf_generate_proc *** start ***\n")
#
	response = HttpResponse(content_type='application/pdf')
	file_pdf = "media/documents/" + pdf_out
	file_template = "media/templates/template_seikyusho.pdf"

	response['Content-Disposition'] = 'attachment; filename=' + file_pdf
	# Create the PDF object, using the response object as its "file."
#
#
	cc = canvas.Canvas(response)
	cc = canvas.Canvas(file_pdf)
#
#
	fontname_g = "HeiseiKakuGo-W5"
	pdfmetrics.registerFont (UnicodeCIDFont (fontname_g))
	cc.setFont(fontname_g,16)
	#
	page = PdfReader(file_template,decompress=False).pages
	pp = pagexobj(page[0])
	cc.doForm(makerl(cc, pp))
#

	today = datetime.today()
	str_today = today.strftime('%Y-%m-%d')
	#
	cc.drawString(400, 800, str_today)
	cc.drawString(100, 725, receiver)
	cc.drawString(100, 680, str(price))
	#
	cc.showPage()
	cc.save()
	sys.stderr.write("*** pdf_generate_proc *** end ***\n")
#
	return response
# --------------------------------------------------------------------
def list_dir_proc(request):
	str_out = ""
#	files = os.listdir(settings.BASE_DIR + "/media/documents/")
	files = glob.glob(settings.BASE_DIR + "/media/documents/*.pdf")
	for file in files:
#		str_out += file + "<br />"
		str_out += os.path.basename(file) + "<br />"
#
	return HttpResponse(str_out)
# ------------------------------------------------------------------
