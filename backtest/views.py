from django.shortcuts import render

# Create your views here.



from django.http import HttpResponse
# Create your views here.

#importing loading from django template
from django.template import loader

from django.views.decorators.csrf import csrf_exempt

#disabling csrf (cross site request forgery)
@csrf_exempt

def index(request):
    template = loader.get_template('form.html')
    return HttpResponse(template.render())


def submit(request):

    #if post request came
    if request.method == 'GET':
        #getting values from GET
        capital = request.GET.get('capital')
        initialShare=request.GET.get('Initial share')
        numberOfShare=request.GET.get('Number of share')
        selectChoice=request.GET.get('select-choice')




        print(capital)
        print(initialShare)
        print(numberOfShare)
        print(selectChoice)


    return HttpResponse("submission successful")
