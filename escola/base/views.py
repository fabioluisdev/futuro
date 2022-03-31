from django.http import HttpResponse


def home(request):
    return HttpResponse('Cursos de Aualizacao em TI')
