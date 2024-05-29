from django.shortcuts import render, get_object_or_404, redirect
from .models import Car, Comment
from .forms import CommentForm
from django.contrib.auth.decorators import login_required

def index (request):
    cars = Car.objects.all().order_by("price")
    return render(request,'app1/index.html', {"cars": cars})

@login_required(login_url="/users/login/")
def blogs(request):
    search_query = request.GET.get('blogsearch', '')

    cars = Car.objects.filter(name__icontains=search_query)
    if 'reset' in request.GET:
        cars = Car.objects.all()

    return render(request, 'app1/blogs.html', {"cars": cars})

@login_required
def comments(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    comments = car.comment.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = car
            comment.user = request.user
            comment.save()
            return redirect('comments', car_id=car.id)
    else:
        form = CommentForm()

    return render(request, 'app1/comments.html', {
        'car': car,
        'comments': comments,
        'form': form
    })

def car_detail(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    return render(request, 'app1/car_detail.html', {'car': car})


def list_of_cars(request):
    if 'reset' in request.GET:
        selected_cartypes = []
        min_price = ''
        max_price = ''

    else:
        selected_cartypes = request.GET.getlist('cartype')
        min_price = request.GET.get('min_price', '')
        max_price = request.GET.get('max_price', '')


    what = request.GET.get('what', 'model')
    isAsc = request.GET.get('isAsc', 'True')


    cars = Car.objects.all()
    if selected_cartypes:
        cars = cars.filter(type__in=selected_cartypes)

    if min_price:
        cars = cars.filter(price__gte=min_price)

    if max_price:
        cars = cars.filter(price__lte=max_price)


    sedan , hatchback , electric, station = "","","",""
    if "Sedan" in selected_cartypes:
        sedan = "checked"
    if "Hatchback" in selected_cartypes:
        hatchback= "checked"
    if "Electric" in selected_cartypes:
        electric = "checked"
    if "Station" in selected_cartypes:
        station = "checked"


    if what == 'price':
        if isAsc == 'True':
            cars = cars.order_by("price")
        else:
            cars = cars.order_by("-price")
    elif what == 'name':
        if isAsc == 'True':
            cars = cars.order_by("name")
        else:
            cars = cars.order_by("-name")
    elif what == 'model':
        if isAsc == 'True':
            cars = cars.order_by("model")
        else:
            cars = cars.order_by("-model")
    elif what == 'type':
        if isAsc == 'True':
            cars = cars.order_by("type")
        else:
            cars = cars.order_by("-type")
    return render(request, 'app1/list_of_cars.html', {
        "cars": cars,
        "what": what,
        "isAsc": isAsc,
        "sedan": sedan,
        "hatchback": hatchback,
        "electric":electric,
        "station": station,
        "min_price": min_price,
        "max_price": max_price
    })


def car_types(request):
    car_type = request.GET.get('car_type', "Hatchback")
    car_types = Car.objects.filter(type=car_type)

    if 'reset' in request.GET:
        min_price = ''
        max_price = ''
    else:
        min_price = request.GET.get('min_price', '')
        max_price = request.GET.get('max_price', '')

    what = request.GET.get('what', 'model')
    isAsc = request.GET.get('isAsc', 'True')

    if min_price:
        car_types = car_types.filter(price__gte=min_price)

    if max_price:
        car_types = car_types.filter(price__lte=max_price)

    if what == 'price':
        if isAsc == 'True':
            car_types = car_types.order_by("price")
        else:
            car_types = car_types.order_by("-price")
    elif what == 'name':
        if isAsc == 'True':
            car_types = car_types.order_by("name")
        else:
            car_types = car_types.order_by("-name")
    elif what == 'model':
        if isAsc == 'True':
            car_types = car_types.order_by("model")
        else:
            car_types = car_types.order_by("-model")

    return render(request, 'app1/car_type.html', {
        "car_type": car_type,
        "what": what,
        "isAsc": isAsc,
        "cars": car_types,
        "min_price": min_price,
        "max_price": max_price,
    })

def search(request):
    if 'reset' in request.GET:
        selected_cartypes = []
        min_price = ''
        max_price = ''

    else:
        selected_cartypes = request.GET.getlist('cartype')
        min_price = request.GET.get('min_price', '')
        max_price = request.GET.get('max_price', '')

    search_query = request.GET.get('search', '')
    what = request.GET.get('what', 'model')
    isAsc = request.GET.get('isAsc', 'True')

    cars = Car.objects.filter(name__icontains=search_query)

    if selected_cartypes:
        cars = cars.filter(type__in=selected_cartypes)

    if min_price:
        cars = cars.filter(price__gte=min_price)

    if max_price:
        cars = cars.filter(price__lte=max_price)


    sedan , hatchback , electric , station= "","","", ""
    if "Sedan" in selected_cartypes:
        sedan = "checked"
    if "Hatchback" in selected_cartypes:
        hatchback= "checked"
    if "Electric" in selected_cartypes:
        electric = "checked"
    if "Station" in selected_cartypes:
        station = "checked"


    if what == 'price':
        if isAsc == 'True':
            cars = cars.order_by("price")
        else:
            cars = cars.order_by("-price")
    elif what == 'name':
        if isAsc == 'True':
            cars = cars.order_by("name")
        else:
            cars = cars.order_by("-name")
    elif what == 'model':
        if isAsc == 'True':
            cars = cars.order_by("model")
        else:
            cars = cars.order_by("-model")
    elif what == 'type':
        if isAsc == 'True':
            cars = cars.order_by("type")
        else:
            cars = cars.order_by("-type")
    return render(request, 'app1/search.html', {
        "cars": cars,
        "what": what,
        "isAsc": isAsc,
        "sedan": sedan,
        "hatchback": hatchback,
        "electric": electric,
        "station": station,
        "min_price": min_price,
        "max_price": max_price,
        "search_query": search_query,
    })
# Create your views here.

