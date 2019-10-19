from django.http import HttpResponse
import json

def test1(request):
    return HttpResponse('Pagina 2')

def test2(request):
    numbers = [int(i) for i in request.GET['numbers'].split(",")]
    sorted_ints = sorted(numbers)
    
def test4(request, name, country):
    if country == "Colombia":
        message = 'Eres {}, de nacionalidad colombiana'.format(name)
    else:
        message = 'No eres {}, de nacionalidad colombiana'.format(name)
    return HttpResponse(message)

  
    data = {
        'status': 'OK',
        'numbers': sorted_ints,
        'message': 'Request.successfully'
        
    }

    return HttpResponse(
        json.dumps(data, indent = 4),
        content_type='application/json'
    )

