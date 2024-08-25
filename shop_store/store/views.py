from statistics import quantiles
from django.http import HttpResponse
from django.template import loader
from itertools import chain
from .models import  Top, Bottom, Acc, Dress
from django.http import JsonResponse

def store(request):
    myitems = list(Top.objects.all().values()) + list(Bottom.objects.all().values()) + list(Acc.objects.all().values()) + list(Dress.objects.all().values())
    template = loader.get_template('home.html')
    context = {
        'myitems': myitems,
    }
    return HttpResponse(template.render(context, request))

def detail(request, category, id):
    tops = Top.objects.filter(category=category, id=id)
    bottoms = Bottom.objects.filter(category=category, id=id)
    accs = Acc.objects.filter(category=category, id=id)
    dresses = Dress.objects.filter(category=category, id=id)

    p = list(chain(tops, bottoms, accs, dresses))

    template = loader.get_template('details.html')

    context = {
        'p': p
    }
    return HttpResponse(template.render(context, request))

def cart(request):
    p = list(Top.objects.all().values()) + list(Bottom.objects.all().values()) + list(Acc.objects.all().values()) + list(Dress.objects.all().values())
    template = loader.get_template('cart.html')
    
    if request.method == 'POST':
        # product_id = request.POST.get('product_id')  # Get the selected product ID
        quantity = int(request.POST.get('quantity', 1))  # Get the selected quantity, default to 1 if not provided

        # Store the product, quantity, and total in the cart
        # cart = request.session.get('cart', [])
        # product = get_object_or_404(Product, id=product_id)
        # total = p.price * quantity
        # cart.append({'product': product, 'quantity': quantity, 'total': total})
        # request.session['cart'] = cart

    # p = list(chain(p, quantity))

    context = {
        'p': p,
        # 'cart': cart,  # Pass the cart to the template context
    }
    return HttpResponse(template.render(context, request))





def account(request):
    myitems = list(Top.objects.all().values()) + list(Bottom.objects.all().values()) + list(Acc.objects.all().values()) + list(Dress.objects.all().values())
    template = loader.get_template('account.html')
    context = {
        'myitems': myitems,
    }
    return HttpResponse(template.render(context, request))

def contact(request):
    myitems = list(Top.objects.all().values()) + list(Bottom.objects.all().values()) + list(Acc.objects.all().values()) + list(Dress.objects.all().values())
    template = loader.get_template('contact.html')
    context = {
        'myitems': myitems,
    }
    return HttpResponse(template.render(context, request))

def login(request):
    myitems = list(Top.objects.all().values()) + list(Bottom.objects.all().values()) + list(Acc.objects.all().values()) + list(Dress.objects.all().values())
    template = loader.get_template('login.html')
    context = {
        'myitems': myitems,
    }
    return HttpResponse(template.render(context, request))