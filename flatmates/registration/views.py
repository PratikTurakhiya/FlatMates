from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.views.generic import TemplateView, ListView
from django.core.mail import send_mail
from .models import t3
from .models import owner,contactus,roomshare,review
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView 
from django.views import View
import math,random
from django.urls import reverse
from django.db.models import Q
from django.db import connection
#from .models import signup
# Create your views here.
def login(request):
    if request.method=='POST':
      username=request.POST['username']
      password1=request.POST['password']
      user=auth.authenticate(username=username,password=password1)  
      if user is not None:
          auth.login(request,user)
          return redirect('bg') 
      else:
          messages.info(request,'invalid credentials!')
          return redirect('login')
    else:
        return render(request ,'login.html')


def register(request):
     if request.method =='POST':
        firstname=request.POST['fname']
        lastname=request.POST['lname']
        username=request.POST['uname']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        otp=request.POST['otp']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'emailtaken')
                return redirect('register')
            elif otp!='4789':
                messages.info(request,'INVALID OTP')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=firstname,last_name=lastname)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'password not matching')
            return redirect('register')
     else:
        return render(request ,'register.html')
def home(request):
    return render(request,'home.html')

def bg(request):
    from .models import owner
    ow=owner.objects.all()
    return render(request,'bg.html',{'ow':ow})
    

def logout(request):
    auth.logout(request)
    return redirect('login')

def index(request):
    return render(request,'index.html')
 
def review(request):
   if request.method=='POST':
        from .models import review
        name=request.POST['name']
        lastname=request.POST['lastname']
        mo=request.POST['mo']
        email=request.POST['email']
        rating=request.POST['rating']
        des=request.POST['des']
        user =review(name=name,lastname=lastname,mo=mo,email=email,rating=rating,des=des)
        user.save()
        return redirect('bg')
   else:
        return render(request,'review.html')
def bar(request):
    from .models import owner
    ow=owner.objects.all()
    return render(request,'bar.html',{'ow':ow})

class SearchData(ListView):
    model = owner
    template_name = 'search_data.html'
    
    def get_queryset(self): 
        from .models import owner
        query = self.request.GET.get('q')
        object_list =owner.objects.filter(
        Q(name__icontains=query) | Q(city__icontains=query)
        )
        return object_list

class LowToHigh(ListView):
    model = owner
    template_name = 'LowToHigh.html'
    
    def get_queryset(self): 
        from .models import owner
        query = self.request.GET.get('q')
        h = owner.objects.all().order_by('price')
        return h

class HighToLow(ListView):
    model = owner
    template_name = 'HighToLow.html'
    
    def get_queryset(self): 
        from .models import owner
        query = self.request.GET.get('q')
        h = owner.objects.all().order_by('-price')
        return h

class Female(ListView):
    model = owner
    template_name = 'searchfemale.html'
    
    def get_queryset(self): 
        from .models import owner
        query = self.request.GET.get('q')
        object_list=owner.objects.filter(Q(avlgen__icontains="FEMALE"))
        return object_list

class Male(ListView):
    model = owner
    template_name = 'searchmale.html'
    
    def get_queryset(self): 
        from .models import owner
        query =self.request.GET.get('q')
        object_list=owner.objects.filter(Q(avlgen__icontains="MALE"))
        return object_list

def delete(request,id):
    if request.method == 'POST':
        from .models import owner
        queryset=owner.objects.get(id=id)
        queryset.delete()
        return redirect('screen')
    return render(request, 'delete.html')

def dele(request):
    from .models import owner
    ow=owner.objects.all()
    return render(request,'delete.html',{'ow':ow})

def img(request):
    if request.method=='POST':
      name=request.POST['nam']
      picture=request.FILES['file']
      drop=request.POST['dropdown']
      mul=request.POST.getlist('vehicle')
      dat=request.POST['birthday']
      user =t3(name=name,pic=picture,drop=drop,mul=mul, birthdate=dat)
      user.save()
      return redirect('check')
    else:
      return render(request,'testimg.html')

def check(request):
    #from .models import t3
    products= t3.objects.all()
    return render(request,'check.html',{'products':products})

#def owner(request):
 #   if request.method=='POST':
  #    nme=request.POST['Name']
   #   email=request.POST['Email']
    #  mo=request.POST['phone']
    #  picture=request.FILES['file']
    #  city=request.POST['City']
    #  address=request.POST['Address']
    #  flat=request.POST['Flattype']
    #  furnishing=request.POST['Furniture']
    #  avlfrom=request.POST['From']
    #  avlupto=request.POST['To']
    #  aminities=request.POST.getlist('vehicle')
    #  avlgender=request.POST['Gender']
    #  des=request.POST['Des']
    #  price=request.POST['price']
     # user =owner(name=nme,email=email,mo=mo,Pic=picture,city=city,address=address,flattype=flat,furnishing=furnishing,avlfrom=avlfrom,avlupto=avlupto,aminities=aminities,avlgen=avlgender,des=des,price=price)
     # user.save()
     # return redirect('index')
    #else:
    #  return render(request,'owner.html')
  

def screen(request):
    from .models import owner
    own=owner.objects.all()
    return render(request,'screen.html',{'own':own})


class screenview(DetailView):
    from .models import owner
    queryset = owner.objects.all()
    template_name = "detail.html"

def send(request):
     if request.method =='POST':
        email=request.POST['email']
        send_mail('FlatMates Verification','ONE TIME PASSWORD for FlatMates Verification is 4789','foodmartapp@gmail.com',[email],fail_silently=False)
        return redirect('register')
     else:
        return render(request,'send.html')

def profile(request):
    from django.contrib.auth.models import User
    pro=User.objects.all()
    return render(request,'profile.html',{'profile':pro})

def subprofile(request,id):
    if request.method=='POST':
        i=request.POST['id']
        firstname=request.POST['first_name']
        lastname=request.POST['last_name']
        pas=request.POST['password']
        a=User.objects.get(id=i)
        a.first_name=firstname
        a.last_name=lastname
        a.password=pas
        a.save()
        return render(request,'subprofile.html')
    else:
        obj=User.objects.get(id=id)
        return render(request,'subprofile.html',{'object':obj}) 

def owner(request):
    if request.method=='POST':
        from .models import owner
        nme=request.POST['Name']
        email=request.POST['Email']
        mo=request.POST['phone']
        picture=request.FILES['file']
        city=request.POST['City']
        address=request.POST['Address']
        flat=request.POST['Flattype']
        furnishing=request.POST['Furniture']
        avlfrom=request.POST['From']
        avlupto=request.POST['To']
        aminities=request.POST.getlist('vehicle')
        avlgender=request.POST['Gender']
        des=request.POST['Des']
        price=request.POST['price']
        user =owner(name=nme,email=email,mo=mo,Pic=picture,city=city,address=address,flattype=flat,furnishing=furnishing,avlfrom=avlfrom,avlupto=avlupto,aminities=aminities,avlgen=avlgender,des=des,price=price)
        user.save()
        return redirect('owner')
    else:
        return render(request,'owner.html')

def locate(request):
    if request.method=='POST':
        name=request.POST['NAME']
        email=request.POST['EMAIL']
        subject=request.POST['SUBJECT']
        message=request.POST['MESSAGE']
        user=contactus(name=name,email=email,subject=subject,mes=message)
        user.save()
        return redirect('bg')
    else:
        return render(request,'maps.html')

def homeshare(request):
    if request.method=='POST':
        from .models import roomshare
        name=request.POST['NAME']
        email=request.POST['EMAIL']
        mo=request.POST['PHONE']
        gender=request.POST['GENDER']
        address=request.POST['ADDRESS']
        neighborhood=request.POST['NEIGHBORHOOD']
        des=request.POST['DESCRIPTION']
        lgender=request.POST['ALLOWEDGEN']
        interest=request.POST.getlist('INTEREST')
        avlfrom=request.POST['FROM']
        avlupto=request.POST['TO']
        price=request.POST['PRICE']
        aminities=request.POST.getlist('AMINITIES')
        pic=request.FILES['IMAGE']
        city=request.POST['CITY']
        room=request.POST['BEDROOM']
        furnishing=request.POST['FURNISHING']
        hometype=request.POST['TYPE']
        bath=request.POST['BATH']    
        parking=request.POST['PARKING']
        user =roomshare(name=name,email=email,mo=mo,gender=gender,address=address,neighborhood=neighborhood,
        des=des,lgender=lgender,interest=interest,avlfrom=avlfrom,avlupto=avlupto,price=price,
        aminities=aminities,Pic=pic,city=city,room=room,furnishing=furnishing,hometype=hometype,bath= bath ,
        parking=parking)
        user.save()
        return redirect('homeshare')  
    else:    
        return render(request,'isharing.html')


def roomfind(request):
    from .models import roomshare
    share=roomshare.objects.all()
    return render(request,'matefinder.html',{'share':share})

class findview(DetailView):
    from .models import owner
    queryset = roomshare.objects.all()
    template_name = "roomfindp.html"

def homepage(request):
    return render(request,"homepage.html")