from django.shortcuts import render
from .models import Product
from .models import Contact
from .models import Orders

from math import ceil

# Create your views here.
from django.http import HttpResponse

def index(request):
    products= Product.objects.all()
    n= len(products)
    # print(products)
    nSlides= n//4 + ceil((n/4) - (n//4))
    # # params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'product': products}
    allprod = []
    catprod = Product.objects.values('category','id')
    cats= {item["category"] for item in catprod}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allprod.append([prod, range(1, nSlides), nSlides])

    #  params = {'allProd':allProd }    
    # allprod =[[products,range(1,nSlides),nSlides],
    # [products,range(1,nSlides),nSlides],[products,range(1,nSlides),nSlides],[products,range(1,nSlides),nSlides]]
    
    params = {'allprod' : allprod}
    return render(request,"mac/index.html", params)

def about(request):
    return render(request, 'mac/about.html')

def contact(request):
    if request.method=="POST":
        print(request)
        name=request.POST.get('name', 'name')
        email=request.POST.get('email', 'email')
        phone=request.POST.get('phone', 'phone')
        desc=request.POST.get('desc', 'desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, "mac/contact.html")

def tracker(request):
    return render(request,'mac/tracker.html')

def search(request):
    return render(request,'mac/search.html')

def productView(request, myid):
    product=Product.objects.filter(id=myid)
    print(product)
    return render(request, "mac/prodview.html",{'product':product[0]})


def checkout(request):
    if request.method=="POST":
        items_json= request.POST.get('itemsJson', '')
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        address=request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city=request.POST.get('city', '')
        state=request.POST.get('state', '')
        zip_code=request.POST.get('zip_code', '')
        phone=request.POST.get('phone', '')

        order = Orders(items_json= items_json, name=name, email=email, address= address, city=city, state=state, zip_code=zip_code, phone=phone)
        order.save()
        thank=True
        id=order.order_id
        return render(request, 'mac/checkout.html', {'thank':thank, 'id':id})
    return render(request, 'mac/checkout.html')
