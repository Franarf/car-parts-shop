from django.contrib import messages
from django.shortcuts import redirect, render
from .models import Team
from cars.models import Car
from django.core.mail import send_mail
from django.contrib.auth.models import User

def home(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = Car.objects.order_by('-created_date')

    #retrieve values for the search form
   
    model_search = Car.objects.values_list('model', flat=True).distinct()
    state_search = Car.objects.values_list('state', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    # body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    body_style_search = set(Car.objects.values_list('body_style', flat=True))
    fuel_type_search = Car.objects.values_list('fuel_type', flat=True).distinct()

    if 'body_style' in request.GET:         
        body_style = request.GET['body_style']
        if body_style:
            cars = cars.filter(body_style__iexact= body_style) 

    data = {
        
        'teams' : teams,
        'featured_cars': featured_cars,
        'all_cars' : all_cars,
        'model_search' : model_search,
        'state_search' : state_search,
        'year_search' : year_search,
        'body_style_search' : body_style_search,
        'fuel_type_search': fuel_type_search,

    }
    return render(request, 'pages/home.html', data)


def about(request):
    teams = Team.objects.all()
    data = {
        'teams' : teams,
    }
    return render(request, 'pages/about.html', data)


def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']


        email_subject = ' Hai ricevuto una mail dal Negozio Auto per: ' + subject
        message_body = 'Name: ' + name + '. Email: '+ email + '. Phone: ' + phone + '. Message: ' + message
        

        admin_info = User.objects.get(is_superuser=True) #per importare info da Admin
        admin_email = admin_info.email
        send_mail(
            email_subject, 
            message_body,
            'service.testingapps@gmail.com',
            [admin_email],
            fail_silently=False,
        )

        messages.success(request, 'Grazie per averci contattato. Vi risponderemo appena possibile.')
        return redirect('contact')


    return render(request, 'pages/contact.html')