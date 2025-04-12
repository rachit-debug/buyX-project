from django.shortcuts import render
from mainpage.models import Contactdata
from django.http import JsonResponse
from django.shortcuts import redirect
# Create your views here.
from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import PasswordChangeForm,AuthenticationForm,SetPasswordForm
from django.core.mail import send_mail, EmailMultiAlternatives
from mainpage.models import *
import datetime
from django.contrib.auth.forms import PasswordChangeForm,AuthenticationForm,SetPasswordForm
# Create your views here.
def indexpage(request):
   blog=Blog.objects.all()
   allp=Product.objects.all()
   categories = Category.objects.all()  # Retrieve all categories
   painted_products = allp.filter(category__name="Painted")
   galvanised_products = allp.filter(category__name="Galvanised")
   block_products = allp.filter(category__name="Block")
   return render(request,'index.html',{'categories': categories,'blog':blog,'allp':allp,'painted_products':painted_products,'galvanised_products':galvanised_products,'block_products':block_products})
def about(request):
   blog=Blog.objects.all()
   allp=Product.objects.all()
   categories = Category.objects.all()  # Retrieve all categories
   painted_products = allp.filter(category__name="Painted")
   galvanised_products = allp.filter(category__name="Galvanised")
   block_products = allp.filter(category__name="Block")
   return render(request,'about.html',{'categories': categories,'blog':blog,'allp':allp,'painted_products':painted_products,'galvanised_products':galvanised_products,'block_products':block_products})
def service(request):
   blog=Blog.objects.all()
   allp=Product.objects.all()
   categories = Category.objects.all()  # Retrieve all categories
   painted_products = allp.filter(category__name="Painted")
   galvanised_products = allp.filter(category__name="Galvanised")
   block_products = allp.filter(category__name="Block")
   return render(request,'service.html',{'categories': categories,'blog':blog,'allp':allp,'painted_products':painted_products,'galvanised_products':galvanised_products,'block_products':block_products})
def team(request):
   blog=Blog.objects.all()
   allp=Product.objects.all()
   categories = Category.objects.all()  # Retrieve all categories
   painted_products = allp.filter(category__name="Painted")
   galvanised_products = allp.filter(category__name="Galvanised")
   block_products = allp.filter(category__name="Block")
   return render(request,'team.html',{'categories': categories,'blog':blog,'allp':allp,'painted_products':painted_products,'galvanised_products':galvanised_products,'block_products':block_products})
def team(request):
   blog=Blog.objects.all()
   allp=Product.objects.all()
   categories = Category.objects.all()  # Retrieve all categories
   painted_products = allp.filter(category__name="Painted")
   galvanised_products = allp.filter(category__name="Galvanised")
   block_products = allp.filter(category__name="Block")
   return render(request,'team.html',{'categories': categories,'blog':blog,'allp':allp,'painted_products':painted_products,'galvanised_products':galvanised_products,'block_products':block_products})
def contact(request):
   blog=Blog.objects.all()
   allp=Product.objects.all()
   categories = Category.objects.all()  # Retrieve all categories
   painted_products = allp.filter(category__name="Painted")
   galvanised_products = allp.filter(category__name="Galvanised")
   block_products = allp.filter(category__name="Block")
   return render(request,'contact.html',{'categories': categories,'blog':blog,'allp':allp,'painted_products':painted_products,'galvanised_products':galvanised_products,'block_products':block_products})

def myaboutpage(request):
   blog=Blog.objects.all()
   allp=Product.objects.all()
   categories = Category.objects.all()  # Retrieve all categories
   painted_products = allp.filter(category__name="Painted")
   galvanised_products = allp.filter(category__name="Galvanised")
   block_products = allp.filter(category__name="Block")
   return render(request,'myabout.html',{'categories': categories,'blog':blog,'allp':allp,'painted_products':painted_products,'galvanised_products':galvanised_products,'block_products':block_products})
def project(request):
   blog=Blog.objects.all()
   allp=Product.objects.all()
   categories = Category.objects.all()  # Retrieve all categories
   painted_products = allp.filter(category__name="Painted")
   galvanised_products = allp.filter(category__name="Galvanised")
   block_products = allp.filter(category__name="Block")
   return render(request,'portfolio.html',{'categories': categories,'blog':blog,'allp':allp,'painted_products':painted_products,'galvanised_products':galvanised_products,'block_products':block_products})
def submitquery(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        message = request.POST.get('message')
        sub = request.POST.get('subject')

        # Save the contact data
        obj = Contactdata(name=name, email=email, message=message, subject=sub)
        try:
            obj.save()
            # Pass a success message to the template
            return render(request, 'contact.html', {'success_message': 'Your data has been submitted successfully!'})
        except Exception as e:
            # Handle any errors during save
            return render(request, 'contact.html', {'error_message': 'An error occurred. Please try again.'})
    
    # If the request method is not POST, just render the form
    return render(request, 'contact.html')

def loginpage(request):
   blog=Blog.objects.all()
   allp=Product.objects.all()
   categories = Category.objects.all()  # Retrieve all categories
   painted_products = allp.filter(category__name="Painted")
   galvanised_products = allp.filter(category__name="Galvanised")
   block_products = allp.filter(category__name="Block")
   return render(request,'loginsign.html',{'categories': categories,'blog':blog,'allp':allp,'painted_products':painted_products,'galvanised_products':galvanised_products,'block_products':block_products})

def blogone(request):
   blog=Blog.objects.all()
   allp=Product.objects.all()
   categories = Category.objects.all()  # Retrieve all categories
   painted_products = allp.filter(category__name="Painted")
   galvanised_products = allp.filter(category__name="Galvanised")
   block_products = allp.filter(category__name="Block")
   return render(request,'blog1.html',{'categories': categories,'blog':blog,'allp':allp,'painted_products':painted_products,'galvanised_products':galvanised_products,'block_products':block_products})
def blogtwo(request):
   blog=Blog.objects.all()
   allp=Product.objects.all()
   categories = Category.objects.all()  # Retrieve all categories
   painted_products = allp.filter(category__name="Painted")
   galvanised_products = allp.filter(category__name="Galvanised")
   block_products = allp.filter(category__name="Block")
   return render(request,'blog2.html',{'categories': categories,'blog':blog,'allp':allp,'painted_products':painted_products,'galvanised_products':galvanised_products,'block_products':block_products})
def blogthree(request):
   blog=Blog.objects.all()
   allp=Product.objects.all()
   categories = Category.objects.all()  # Retrieve all categories
   painted_products = allp.filter(category__name="Painted")
   galvanised_products = allp.filter(category__name="Galvanised")
   block_products = allp.filter(category__name="Block")
   return render(request,'blog3.html',{'categories': categories,'blog':blog,'allp':allp,'painted_products':painted_products,'galvanised_products':galvanised_products,'block_products':block_products})

def login(request):
    blog=Blog.objects.all()
    allp=Product.objects.all()
    categories = Category.objects.all()  # Retrieve all categories
    painted_products = allp.filter(category__name="Painted")
    galvanised_products = allp.filter(category__name="Galvanised")
    block_products = allp.filter(category__name="Block")
    categories = Category.objects.all()  # Retrieve all categories
    allp=Product.objects.all()
    if request.method=='POST':
            uname=request.POST['username']
            ppass=request.POST['password']
            print(uname,ppass)
            user=auth.authenticate(username=uname,password=ppass)
            print("user jo login kr raha hai",user)
            if user is not None:
                auth.login(request,user)
                allp=Product.objects.all()
                if request.user.is_authenticated:
                   print("lkjhgfsdfghjkl")
                   return HttpResponseRedirect('/')
                print("lkjhgf")
                return render(request,'index.html',{'categories': categories})
               
            else:
                print("record not found") 
                messages.info(request,'Password or username is incorrect Or Create your new Account')  
                return HttpResponseRedirect('/')
                # this elif is for get request

def createaccount(request):
    categories = Category.objects.all()
    if request.method=='POST':
        f_name=request.POST['customername']
        u_name=request.POST['customerusernam']
        passw1=request.POST['customerpassword']
        email=request.POST['customeremail']
        phone1=request.POST['userphone']
        addre=request.POST['customeraddress']
        print(f_name)
        
        if User.objects.filter(username=u_name).exists():
            messages.info(request,'User Name already exists...')
            print("user pale se available hai")
            return render(request,'loginsign.html',{'categories': categories})    
        else:
            user=ExtendedUser.objects.create_user(first_name=f_name,username=u_name,email=email,phone_no=phone1,address=addre,password=passw1)
            user.save()
            user=auth.authenticate(username=u_name,password=passw1)
            if user is not None:
                auth.login(request,user)
                return HttpResponseRedirect('/')
            messages.add_message(request,messages.SUCCESS,' Account Created Successfully..!!!')
            print("user created")
            return HttpResponseRedirect('/')     
            messages.add_message(request,messages.SUCCESS,' Account Created Successfully..!!!')
            print("user created")
    return render(request,'loginsign.html',{'categories': categories})  



def logout(request):
   auth.logout(request)
   return redirect('/')


def productview(request,myid):
    categories = Category.objects.all()
    allcategories=Category.objects.all()
    blog=Blog.objects.all()
    myproducts=Product.objects.filter(id=myid)
    return render(request,'productview.html',{'myproducts':myproducts[0],'categories': categories,'blog':blog})

def myaddtocart(request):
    if request.method == 'POST':
        productt = request.POST.get('sendid')
        cart = request.session.get('cart', {})

        if cart:
            quantity = cart.get(productt)
            if quantity:
                cart[productt] = quantity + 1
            else:
                cart[productt] = 1
        else:
            cart = {productt: 1}

        # Save the updated cart in session
        request.session['cart'] = cart

        # Return a JsonResponse to indicate success
        return JsonResponse({'success': True, 'cart': cart})
    return JsonResponse({'success': False})

def mycart(request):
    allcategories=Category.objects.all()
    blog=Blog.objects.all()
    categories = Category.objects.all()  # Retrieve all categories
    allp=Product.objects.all()
    cart=request.session.get('cart')
    if not cart:
        request.session.cart={}
        return render(request,'showcart.html',{"categories":categories})
    print(request.session.get('cart'))
    print(request.session.get('cart').keys())
    print("list of keys = ",list(request.session.get('cart').keys()))
    ids=list(request.session.get('cart').keys())
    print(ids)
    myproducts=Product.objects.filter(id__in=ids)
    print(myproducts)
    return render(request,'showcart.html',{'myproducts':myproducts,"categories":categories})

def clearcart(request):
    # request.session.get('cart').clear()
    request.session['cart'] = {}
    print("cart clear")
    return HttpResponseRedirect('/')

def myaddtocarttcart(request):
    if request.method=='POST':
        productt=request.POST['sendid']
        remove=request.POST['remove']
        print(productt,remove)
        cart=request.session.get('cart')
        # print(cart)
        if cart:
           quantity = cart.get(productt)
           if quantity:
               if remove:
                   if quantity<=1:
                       cart.pop(productt)
                       print("pop kiya")
                   else:    
                      cart[productt] = quantity-1
                      print("-1 kiya")
               else:
                 cart[productt] = quantity+1  
                 print("+1 kita")
           else:
               cart[productt] = 1
        else:
            cart={}
            cart[productt] = 1
        request.session['cart'] = cart
        print( request.session['cart'])
        return HttpResponseRedirect('mycart')  

def myaddtocartcart(request):
    if request.method=='POST':
        productt=request.POST['sendid']
        cart=request.session.get('cart')
        # print(cart)
        if cart:
           quantity = cart.get(productt)
           if quantity:
                cart[productt] = quantity+1  
                print("+1 kita")
           else:
               cart[productt] = 1
        else:
            cart={}
            cart[productt] = 1
        request.session['cart'] = cart
        print( request.session['cart'])
        return HttpResponseRedirect('mycart') 

def removecatitem(request):
    if request.method=='POST':
        productt=request.POST['sendid']
        remove=request.POST['remove']
        print(productt,remove)
        cart=request.session.get('cart')
        # print(cart)
        if cart:
           quantity = cart.get(productt)
           if quantity:
               if remove:
                   if quantity:
                       cart.pop(productt)
                       print("pop kiya")
                   else:    
                       cart.pop(productt)
                       print("pop kiya")
               else:
                 cart[productt] = quantity+1  
                 print("+1 kita")
           else:
               cart[productt] = 1
        else:
            cart={}
            cart[productt] = 1
        request.session['cart'] = cart
        print( request.session['cart'])
        return HttpResponseRedirect('mycart')  
    

  
def userprofile(request):
    blog=Blog.objects.all()
    categories = Category.objects.all()  # Retrieve all categories
    allp=Product.objects.all()
    if request.user.is_authenticated:
        profile = ExtendedUser.objects.get(user=request.user)
        return render(request,"profiledashboard.html",{'categories': categories,'allp':allp,'blog':blog,'profile':profile})
    return render(request,'signup.html',{'categories': categories})
def myorders(request):
    if request.user.is_authenticated:
         tt=datetime.datetime.now()
         profile = ExtendedUser.objects.get(user=request.user)
         blog=Blog.objects.all()[:2]
         categories = Category.objects.all()  # Retrieve all categories
         allp=Product.objects.all()
         mcart=order.objects.filter(customer_no=request.user.id)
         count=0
         sscount=0
             
         for i in mcart:
             if i.status:
                 count=count+1
             else:
                 sscount=sscount+1
                 
             
         print(count)
         print(sscount)
         return render(request,'profiledashboard.html',{'mcart':mcart,'blog':blog,'categories':categories,'allp':allp,'profile':profile,'count':count,'tt':tt,'sscount':sscount})
    return render(request,'loginsign.html')


def mycart(request):
    allcategories=Category.objects.all()
    blog=Blog.objects.all()
    categories = Category.objects.all()  # Retrieve all categories
    allp=Product.objects.all()
    cart=request.session.get('cart')
    if not cart:
        request.session.cart={}
        return render(request,'showcart.html',{"categories":categories})
    print(request.session.get('cart'))
    print(request.session.get('cart').keys())
    print("list of keys = ",list(request.session.get('cart').keys()))
    ids=list(request.session.get('cart').keys())
    print(ids)
    myproducts=Product.objects.filter(id__in=ids)
    print(myproducts)
    return render(request,'showcart.html',{'myproducts':myproducts,"categories":categories})

def changepassword(request):
    if request.user.is_authenticated: 
        if request.method == "POST":
            fm = PasswordChangeForm(user=request.user,data=request.POST)
            if fm.is_valid():
                # print(fm)
                fm.save()
                update_session_auth_hash(request,fm.user)
                messages.success(request,'password change Successfully')
                return HttpResponseRedirect('profile')
        else:    
            fm=PasswordChangeForm(user=request.user)
        return render (request,'changepassword.html',{'form':fm})
    else:
        return HttpResponseRedirect('login')     

# another method to change password is old password nai hoga
def changepassword2(request):
    if request.user.is_authenticated: 
        if request.method == "POST":
            fm = SetPasswordForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                messages.success(request,'password change Successfully')
                return HttpResponseRedirect('profile')
        else:    
            fm=SetPasswordForm(user=request.user)
        return render (request,'changepassword.html',{'form':fm})
    else:
        return HttpResponseRedirect('login') 
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from .models import Quote

# def quotedata(request):
#     if request.method == 'POST':
#         # Retrieve form data from the POST request
#         company_name = request.POST.get('companyName')
#         phone = request.POST.get('phone')
#         email = request.POST.get('email')
#         country = request.POST.get('country')
#         scaffolding_type = request.POST.get('scaffoldingType')
#         quantity = request.POST.get('quantity')
        
#         # Handle the checkbox data for product finishes
#         product_finish = []
#         if 'galvanised' in request.POST:
#             product_finish.append('Galvanised')
#         if 'painted' in request.POST:
#             product_finish.append('Painted')
#         if 'block' in request.POST:
#             product_finish.append('Block')
        
#         # Save the data to the Quote model
#         quote = Quote(
#             company_name=company_name,
#             phone=phone,
#             email=email,
#             country=country,
#             scaffolding_type=scaffolding_type,
#             quantity=quantity,
#             product_finish=product_finish
#         )
#         quote.save()

#         # Send a confirmation email to the user
#         send_mail(
#             'Quote Submitted Successfully',
#             'Thank you for submitting your quote request. We will contact you soon.',
#             settings.DEFAULT_FROM_EMAIL,
#             [email],
#             fail_silently=False,
#         )

#         # Redirect to a success page or show a success message
#         return HttpResponse('Your quote request has been submitted successfully. We will contact you soon.')

#     # For GET requests, simply render the form
#     return render(request, 'quote_form.html')




def quotedata(request):
    if request.method == 'POST':
        # Retrieve form data from the POST request
        company_name = request.POST.get('companyName')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        country = request.POST.get('country')
        scaffolding_type = request.POST.get('scaffoldingType')
        quantity = request.POST.get('quantity')
        
        # Handle the checkbox data for product finishes
        product_finish = []
        if 'galvanised' in request.POST:
            product_finish.append('Galvanised')
        if 'painted' in request.POST:
            product_finish.append('Painted')
        if 'block' in request.POST:
            product_finish.append('Block')
        
        # Check if a quote with the same company name and phone number already exists
        existing_quote = Quote.objects.filter(company_name=company_name, phone=phone).first()
        
        if existing_quote:
            quote = Quote(
            company_name=company_name,
            phone=phone,
            email=email,
            country=country,
            scaffolding_type=scaffolding_type,
            quantity=quantity,
            product_finish=product_finish
            )
            quote.save()
            # If a quote with the same company name and phone already exists, redirect to the payment page
            return redirect('paynow')  # You should create a URL name for the paynow page
        
        # Save the new quote if no existing quote was found
        quote = Quote(
            company_name=company_name,
            phone=phone,
            email=email,
            country=country,
            scaffolding_type=scaffolding_type,
            quantity=quantity,
            product_finish=product_finish
        )
        quote.save()

        # Send a confirmation email to the user
        # send_mail(
        #     'Quote Submitted Successfully',
        #     'Thank you for submitting your quote request. We will contact you soon.',
        #     settings.DEFAULT_FROM_EMAIL,
        #     [email],
        #     fail_silently=False,
        # )

        # Redirect to a success page or show a success message
        messages.add_message(request, messages.INFO, "your quote submit successfully")

    # For GET requests, simply render the form
    return HttpResponseRedirect('/')
   
def paynow(request):
    return render(request, 'paynow.html')

def allproducts(request):
    x=Product.objects.all()
    return render(request,"allpropage.html",{'x':x})

def paymentpolicy(request):
     pay=Privacy_Policy.objects.all().first()
     return render(request,"paymentpolicy.html",{'pay':pay})

def refundpolicy(request):
     pay=Privacy_Policy.objects.all().first()
     return render(request,"refundpolicy.html",{'pay':pay})


def cancelpolicy(request):
     pay=Cancelation_Policy.objects.all().first()
     return render(request,"cancelpolicy.html",{'pay':pay})
def premium(request):
    return render(request,"premsubs.html")
