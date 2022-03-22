from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template

class Persona(object):
	def __init__(self, nombre, apellido):
		self.nombre = nombre
		self.apellido = apellido

def construtor(request):
	temasCurso = ["Plantillas","Modelos","Formularios","Vistas","Depliegues"]
	p1 = Persona("Hernan","Escalante")
	
	#doc_externo = open("/mnt/c/Users/hescalag/Documents/Hernan/webPanel/PanelWeb/PanelWeb/Templates/template1.html")
	#plt = Template(doc_externo.read())
	#doc_externo.close()
	
	doc_externo = get_template('template1.html')

	#contexto = Context({"name":p1.nombre, "lastName":p1.apellido, "temas":temasCurso})
	
	document = doc_externo.render({"name":p1.nombre, "lastName":p1.apellido, "temas":temasCurso})
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
