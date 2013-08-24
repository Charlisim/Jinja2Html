# -*- coding: utf-8 -*-
from jinja2 import Template,Environment,  PackageLoader, FileSystemLoader
from jinja2.exceptions import TemplateNotFound
import sys, os

def get_info(args):
	if len(args) > 1:
		template_file = args[1]
		destination_file = args[2] if len(args) > 2 else None
		if destination_file is None:
			destination_file =  os.path.dirname(template_file) + os.path.sep + os.path.basename(template_file) + '_processed'
		if not os.path.dirname(destination_file):
			destination_file = os.path.dirname(template_file) + os.path.sep + destination_file
		print destination_file
		return template_file, destination_file
	else:
		text = 'Use: python jintohtml.py template_file [destination_file].' + '\n'
		text += 'If destination_file is not provided,' + '\n'
		text += 'destination file will be stored in the same folder of template_file with _processed'
		sys.exit(text)
def processTemplate(template_file):
	env = Environment(loader=FileSystemLoader(os.path.dirname(template_file)))
	try:
		template = env.get_template(os.path.basename(template_file))
	except TemplateNotFound:
		sys.exit("You must provide a valid template")
	return template.render()

def storeProcessedTemplate(processed_template, destination_file):
	f = None
	try:
		f = open(destination_file, 'w')
		f.writelines(processed_template)
	except Exception,e :
		sys.exit('Error writing file' + '\n' + e.strerror)
	finally:
		if f:
			f.close()
if __name__ == '__main__':
	template_file, destination_file = get_info(sys.argv)
	

	procesedTemplate = processTemplate(template_file).encode('utf-8')
	storeProcessedTemplate(procesedTemplate, destination_file)