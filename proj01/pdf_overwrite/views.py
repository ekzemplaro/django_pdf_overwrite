# --------------------------------------------------------------------
#
#	overwrite/views.py
#
#						Jan/13/2019
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

from pdf_overwrite.lib.pdf_generate import pdf_generate_proc

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
		file_template = "media/templates/template_seikyusho.pdf"
		file_pdf = "media/documents/" + pdf_out
		try:
			result = pdf_generate_proc(file_template,file_pdf,receiver,price)
		except Exception as ee:
			sys.stderr.write("*** error *** in pdf_generate_proc ***\n")
			sys.stderr.write(str(ee) + "\n")
#
	sys.stderr.write("*** pdf_main_proc *** end ***\n")
#
	str_out = "Success"
	return HttpResponse(str_out)
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
