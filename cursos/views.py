from django.shortcuts import render
from utils.cursos.factory import make_curso


# Create your views here.
def home(request):
    return render(request, 'cursos/pages/home.html', context={
        'cursos': [make_curso() for _ in range(10)],
    })


def curso(request, id):
    return render(request, 'cursos/pages/curso-view.html', context={
        'curso': make_curso(),
        'is_detail_page': True,
    })
