from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail
from django.contrib.auth.models import User

# Create your views here.
def inquiry(request):

    if request.method == "POST":

        
        title_car = request.POST['title_car']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_need = request.POST['customer_need']
        city = request.POST['city']
        state = request.POST['state']
        user_id = request.POST['user_id']
        car_id = request.POST['car_id']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']


        contact = Contact(customer_need=customer_need,
                          car_id=car_id,
                          title_car=title_car,
                          first_name=first_name,
                          last_name=last_name,
                          city=city,
                          state=state,
                          user_id=user_id,
                          email=email,
                          phone=phone,
                          message=message)

        admin_info = User.objects.get(is_superuser=True) #per importare info da Admin
        admin_email = admin_info.email
        send_mail(
            'Nuova Email di Richiesta',
            'Ti e\' arrivata una richiesta per la macchina' + title_car + 'Entra nella Dashboard per visualizzarla',
            'service.testingapps@gmail.com',
            [admin_email],
            fail_silently=False,
        )
        

        contact.save()
        messages.success(request, "Grazie per l'interesse, vi contatteremo al piu presto.")
        return redirect('/cars/'+ car_id)