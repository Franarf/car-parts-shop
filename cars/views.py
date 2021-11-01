from django.shortcuts import get_object_or_404, render
from .models import Car
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator



def cars(request):
    cars = Car.objects.order_by('-created_date')
    paginator = Paginator(cars, 12)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)

    model_search = Car.objects.values_list('model', flat=True).distinct()
    state_search = Car.objects.values_list('state', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = set(Car.objects.values_list('body_style', flat=True))
    fuel_type_search = Car.objects.values_list('fuel_type', flat=True).distinct()

    data = {
        'cars': paged_cars,
        'model_search' : model_search,
        'state_search' : state_search,
        'year_search' : year_search,
        'body_style_search' : body_style_search,
        'fuel_type_search': fuel_type_search,
    }
    return render(request, 'cars/cars.html', data)



def car_detail(request, id):
    single_car = get_object_or_404(Car, pk=id)

    data = {
        'single_car' : single_car,
    }
    return render(request, 'cars/car_detail.html', data)
    


def search(request):
    cars = Car.objects.order_by('-created_date')

    model_search = Car.objects.values_list('model', flat=True).distinct()
    state_search = Car.objects.values_list('state', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = set(Car.objects.values_list('body_style', flat=True))
    fuel_type_search = Car.objects.values_list('fuel_type', flat=True).distinct()

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            cars = cars.filter(description__icontains = keyword)

    if 'model' in request.GET:          #change name= in the html
        model = request.GET['model']
        if model:
            cars = cars.filter(model__iexact = model)

    if 'state' in request.GET:          #change name= in the html
        state = request.GET['state']
        if state:
            cars = cars.filter(state__iexact = state)

    if 'year' in request.GET:         
        year = request.GET['year']
        if year:
            cars = cars.filter(year__iexact = year)

    if 'body_style' in request.GET:         
        body_style = request.GET['body_style']
        if body_style:
            cars = cars.filter(body_style__iexact= body_style)
            

    if 'fuel_type' in request.GET:         
        fuel_type = request.GET['fuel_type']
        if fuel_type:
            cars = cars.filter(fuel_type__iexact= fuel_type)
            

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            cars = cars.filter(price__gte=min_price, price__lte=max_price)

    data = {
        
        'cars' : cars,
        'model_search' : model_search,
        'state_search' : state_search,
        'year_search' : year_search,
        'body_style_search' : body_style_search,
        'fuel_type_search': fuel_type_search,

    }

    return render(request, 'cars/search.html', data)