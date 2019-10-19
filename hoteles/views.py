from django.shortcuts import render
hoteles = [
    {
        'city':'Bogotá',
        'user':{
            'administrador': 'Pedro Pérez',
        },
        'foto':'https://picsum.photos/200/200/?image=1036'
    },
    {
        'city':'Medellin',
        'user':{
            'administrador': 'Javier Pérez',
        },
        'foto':'https://picsum.photos/200/200/?image=903'
    },
    {
        'city':'Pasto',
        'user':{
            'administrador': 'María López',
        },
        'foto':'https://picsum.photos/200/200/?image=1076'
    },
]
def lista_hoteles(request):
    return render(request, 'feed.html', {'data':hoteles})
# Create your views here.

