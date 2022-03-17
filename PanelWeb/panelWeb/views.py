from django.http import HttpResponse
import datetime
from django.template import Template, Context

class Persona(object):
	def __init__(self, nombre, apellido):
		self.nombre = nombre
		self.apellido = apellido

def construtor(request):
	p1 = Persona("Hernan","Escalante")
	doc_externo = open("/mnt/c/Users/hescalag/Documents/Hernan/webPanel/PanelWeb/PanelWeb/plantillas/plantilla.html")
	plt = Template(doc_externo.read())
	doc_externo.close()
	contexto = Context({"name":p1.nombre, "lastName":p1.apellido})
	document = plt.render(contexto)
	return HttpResponse(document)


def despedida(request):
	return HttpResponse("Hasta Luego")


def fechahora(request):
	fecha = datetime.datetime.now()
	html = """
	<html>
		<body>
			<h1>fecha y hora %s</h1>
		</body>
	</html>""" % fecha
	return HttpResponse(html)

def edad(resquest, ano):
	edadActual = 18
	periodo = ano - 2019
	edadFut = edadActual + periodo
	html = """
	<html>
		<body>
			<h1>en el año %s tendras %s años</h1>
		</body>
	</html>""" %(ano, edadFut)
	return HttpResponse(html)
