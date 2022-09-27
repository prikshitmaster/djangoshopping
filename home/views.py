from django.shortcuts import render,HttpResponse

# Create your views here.
from home.models.product import Contact, Emailcollection, AdminProduct
from home.models.catorgry import Catorgry


def index(request):
    products = AdminProduct.get_all_product()
    categrories = Catorgry.get_all_categories()
    print(products)
    return render(request, 'index.html' )


def newsletterform(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        newsletter = Contact(username=username, email=email)
        newsletter.save()
        return HttpResponse("Form sumbit successfully ")

    else:
        return HttpResponse('error')

def contact(request):
    return render(request,'contact.html')

def shop(request):
    return render(request,'shop.html')

def detail(request):
    return render(request, 'detail.html')

def emailcollection(request):
    if request.method == "POST":
        email = request.POST["stayemail"]
        useremail = Emailcollection(email=email)
        useremail.save()
        return HttpResponse("Form sumbit successfully ")

    else:
        return HttpResponse('error')