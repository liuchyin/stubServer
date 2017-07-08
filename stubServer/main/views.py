# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
from django.http import StreamingHttpResponse
def index(request):
	return HttpResponse("Hi, this is a stub server for api test!")



def file_iterator(fname, chunk_size = 512):
	with open(fname) as f:
		while True:
			c = f.read(chunk_size)
			if c:
				yield c
			else:
				break

def files(request, filename):
	response = StreamingHttpResponse(file_iterator('files/' + filename))
	response['Content-Type'] = 'application/octet-stream'
	response['Content-Disposition'] = 'attachment;filename="{0}"'.format(filename)

	return response

@csrf_exempt
def testpost(request):
	if request.method == 'POST':
			res = ''
			for key, value in request.POST.items():
					res += '%s : %s\n' % (key, value)
			
			for fname in request.FILES.keys():
					fd = open('files/' + fname, 'wb')
					tmpfile = request.FILES[fname]
					for chuck in tmpfile.chunks():
							fd.write(chuck)
					fd.close()
					res += '%s(file) : /main/files/%s\n' % (fname, fname)
	htmlres = res.replace('\n', '<br>')
	return HttpResponse(htmlres)

def testget(request):
	if request.method == 'GET':
			res = ''
			for key, value in request.GET.items():
					res += '%s : %s\n' % (key, value)
	print res
	htmlres = res.replace('\n', '<br>')
	return HttpResponse(htmlres)

# Create your views here.
