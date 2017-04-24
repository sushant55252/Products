



from django.shortcuts import redirect, render

from .models import Product


def index(request):
    if request.method == 'POST':
        Product.objects.create(name = request.POST['name'], description = request.POST['description'], weight = request.POST['weight'], price = request.POST['price'], cost = request.POST['cost'], category = request.POST['category'])
        products = Product.objects.all()
        print products
        for info in products:
            print info.name, info.description, info.weight, info.price, info.cost, info.category
        return redirect('/')
    return render(request, 'apps/index.html')
