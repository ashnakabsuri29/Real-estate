from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth.models import User , auth
from .models import city ,flats,contact ,contact_us, enquiry , enquiry_us
from django.template.loader import render_to_string, get_template
from django.conf import settings
from django.core.mail import EmailMessage
from django.contrib import messages


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')   
            return redirect('login') 
    else:
        return render(request,'login.html')    


def register1(request):
    

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
       

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request ,'Enter a unique username')
                return redirect('register1')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'The email is already registered')
                return redirect('register1')

            else:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                
                return render(request , 'login.html')
            
        else:
            messages.info(request,'password not matching')
            return redirect('register1')
        return redirect('/')

    else:
       return render(request,'register1.html')


def logout(request):
    auth.logout(request)      
    return redirect('/') 

def search(request):
    
    ct = city.objects.all()
        
    return render(request,'search.html',{'city':ct})
    
    

def detail(request,id):
    
    flat = flats.objects.filter(city=id)
    print("hellooooooooooo")
    
    
    return render(request,'detail.html',{'Property':flat})


def index(request):
    
    return render(request,'index.html')


def sell(request):
    if request.method == 'POST':
        owner_fullname = request.POST['owner_fullname']
        owner_email = request.user.email
        owner_contact = request.POST['owner_contact']
        address = request.POST['address']
        bhk = request.POST['bhk']
        est_year = request.POST['est_year']
        sqr_ft = request.POST.get('squareFeet')
        rate = request.POST.get('rate')
        ct = request.POST.get('cities')
        # files = request.FILES

        image = request.FILES['img']
        print(image)
        rent = request.POST.get('flexRadioDefault')
        sell = request.POST.get('flexRadioDefault')
        if  rent == 'on':
            rent =True
            sell = False
        else:
            sell = True
            rent = False
        print('hii')
        # flats.objects.create(city=ct)
        print('ashna')
        # flats.objects.create(city=ct)
        # flats.objects.get_or_create(city=city(id=ct))
        
        f = flats(owner_fullname=owner_fullname,owner_email=owner_email,owner_contact=owner_contact,address=address,bhk=bhk,est_year= est_year,sqr_ft=sqr_ft,rate=rate,city_id=ct,img1=image,rent=rent,sell=sell)
        f.save()
        return redirect('search')
    else:
        
        # flat =flats.objects.all()
        ct = city.objects.all()
        
        return render(request,'sell.html',{'city':ct})

def contact(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        message = request.POST['message']

        print(first_name)
        c = contact_us(first_name=first_name,last_name=last_name,email=email,mobile=mobile,message=message)
        c.is_active = False
        c.save()
        
    return redirect('/')
    
def enquiry(request,id):
    request.session['flat_id'] = id
   
    return render(request,'enquiry.html')  
   
    
def enquiry_confirmation(request):
     if request.method == 'POST':
        fullName = request.POST['fullName']
        email = request.user.email
        phoneNo = request.POST['phoneNo'] 
        message = request.POST['message']
        flat_id = request.session.get('flat_id')  

        e = enquiry_us(name=fullName,email=email,mobile=phoneNo,flats_id=flat_id,message=message)
        e.save()
        
        flat = flats.objects.get(id=flat_id)
        print(flat.owner_email)

        message = render_to_string('email.html', {'fullName':fullName, 'email':email,  'phoneNo':phoneNo,'message':message,'flat_id':flat_id})
        msg = EmailMessage(
            'Acres real estate',
            message,
            settings.EMAIL_HOST_USER,
            [flat.owner_email]
        )
        msg.content_subtype = "html"  # Main content is now text/html
        msg.send()

        message = " Hi,"+fullName+ " your email has been send to " +flat.owner_email
        msg = EmailMessage(
            'Acres real estate',
            message,
            settings.EMAIL_HOST_USER,
            [request.user.email]
        )
        msg.content_subtype = "html"  # Main content is now text/html
        msg.send()
        return redirect('/')


    
