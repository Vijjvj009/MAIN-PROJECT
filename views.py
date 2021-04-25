from django.shortcuts import render
from .models import Customer,Login,Member,Activity,Product,Pstockentry,Pstock,Actentry,Cart
from datetime import date


def home(request):
    data=Product.objects.all()
    return render(request,'home.html',{'d':data})
def login(request):
    return render(request,'login.html')
def log(request):
    try:
        m=Login.objects.get(username=request.POST['phone'],password=request.POST['password'])
        if m.status == 1:
            request.session['user']=m.username
            data = Product.objects.all()
            return render(request, 'uhome.html', {'d': data})

        elif m.status == 2:
            request.session['user']=m.username
            data = Product.objects.all()
            return render(request, 'mhome.html', {'d': data})

            return render(request,'mhome.html')
        elif m.status == 0:

            return render(request,'adminhome.html')
        else:
            return render(request, 'login.html', {'error':"Your Username and Password didn't match."})
    except:
        return render(request,'login.html',{'error':'Invalid Uername or Password'})


def ureg(request):
    return render(request,'ureg.html')
def reg(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    phone = request.POST['phone']
    address = request.POST['address']
    city = request.POST['city']
    district = request.POST['district']
    pin = request.POST['pin']
    password = request.POST['pass']

    data=Customer(fname=fname,lname=lname,email=email,phone=phone,address=address,city=city,district=district,pin=pin)
    data.save()
    data1=Login(username=phone,password=password,status=1)
    data1.save()
    return render(request,'login.html')
def uhome(request):
    data=Product.objects.all()
    return render(request,'uhome.html',{'d':data})
def uprodetails(request):
    id = request.POST['id']
    data = Product.objects.filter(id=id)
    return render(request, 'uprodetails.html', {'data1': data})

def cart1(request):
    id = request.POST['id']
    data3=Product.objects.get(id=id)
    data = Product.objects.get(id=id)
    user = request.session['user']
    data1 = Customer.objects.get(phone=user)
    qty = request.POST['qty']
    gtotal=int(qty)*int(data.srate)
    data2 = Cart(pid=data3,user=user,qty=qty,gtotal=gtotal,status=0)
    data2.save()
    return render(request, 'gocart.html', {'i': data,'data1':data1, 'data2': data2 })
def gocart(request):
    id = request.session['user']
    data = Cart.objects.filter(user=id)
    return render(request,'cartdetails.html',{'data':data})
def cartdetails(request):
    id = request.session['user']
    data = Cart.objects.filter(user=id)
    return render(request, 'cartdetails.html', {'data': data})
def shopping(request):
    id = request.POST['id']
    data = Cart.objects.filter(id=id)
    user = request.session['user']
    data2 = Customer.objects.get(phone=user)
    return render(request, 'shopping.html', {'data1': data,'h':data2})
def mhome(request):
    data=Product.objects.all()
    return render(request,'mhome.html',{'d':data})
def mprodetails(request):
    id = request.POST['id']
    data = Product.objects.filter(id=id)
    return render(request, 'mprodetails.html', {'data1': data})

def registration(request):
    return render(request,'registration.html')
def memberreg(request):
    return render(request,'memberreg.html')
def memreg(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    adhno= request.POST['adhno']
    photo = request.FILES['file']
    hname = request.POST['hname']
    place = request.POST['place']
    pin = request.POST['pin']
    phone = request.POST['phone']
    caste = request.POST['caste']
    dob = request.POST['dob']
    doj= date.today()
    email = request.POST['email']
    password = request.POST['password']
    data = Member(fname=fname, lname=lname, adhno=adhno, photo=photo, hname=hname, place=place, pin=pin, phone=phone,caste=caste, dob=dob,doj=doj,email=email)
    data.save()
    data1 = Login(username=phone, password=password, status=2)
    data1.save()
    return render(request, 'memberreg.html')
def activityreg(request):
    return render(request,'activityreg.html')
def actreg(request):
    actname = request.POST['actname']
    amount = request.POST['amount']
    data=Activity(actname=actname,amount=amount)
    data.save()
    return render(request,'activityreg.html')
def productreg(request):
    return render(request,'productreg.html')
def proreg(request):
    pname = request.POST['pname']
    srate = request.POST['srate']
    photo = request.FILES['file']
    ptype = request.POST['ptype']
    punit = request.POST['punit']
    dp = request.POST['dp']
    doe = date.today()
    data=Product(pname=pname,srate=srate,photo=photo,ptype=ptype,punit=punit,dp=dp,doe=doe)
    data.save()
    return render(request,'productreg.html')
def show(request):
    return render(request,'show.html')
def productdetails(request):
    data=Product.objects.all()
    return render(request,'productdetails.html',{'d':data})

def editadminpro(request):
    id = request.POST['id']
    data = Product.objects.get(id=id)
    return render(request, 'editadminpro.html', {'data': data})

def update1(request):
    id=request.POST['id']
    data=Product.objects.get(id=id)
    data.pname=request.POST['pname']
    data.srate = request.POST['srate']
    data.photo = request.FILES['file']
    data.ptype = request.POST['ptype']
    data.punit = request.POST['punit']
    data.dp = request.POST['dp']
    data.save()
    data2=Product.objects.filter(id=id)
    return render(request, 'productdetails.html',{'d':data2})

def memberdetails(request):
    data = Member.objects.all()
    return render(request, 'memberdetails.html', {'d': data})

def memberdetails1(request):
    id = request.POST['id']
    data1 = Member.objects.filter(id=id)
    return render(request, 'memberdetails1.html', {'data1': data1})
def addingstock(request):
    data1=Product.objects.all()
    return render(request,'addingstock.html',{'d':data1})
def adstock(request):
    pname=request.POST['id']
    data = Product.objects.get(id=pname)
    try:
        data3 = Pstock.objects.get(pname=pname)
        return render(request, 'adstock.html', {'i': data, 'data3': data3})
    except:
        pass

    return render(request, 'adstock.html', {'i': data})
def ad1stock(request):
    pname = request.POST['id']

    qty = request.POST['qty']
    edate = date.today()
    data2 = Pstockentry(pname=pname,qty=qty,edate=edate)
    data2.save()
    try:
        data3=Pstock.objects.get(pname=pname)
        data3.cstock=int(data3.cstock)+int(qty)
        data3.save()
    except :
        data3=Pstock(pname=pname,cstock=qty)
        data3.save()

    data3 = Pstock.objects.get(pname=pname)
    data = Product.objects.get(id=pname)
    return render(request, 'adstock.html', {'i': data,'data3':data3})
def viewcustprofile(request):
    user=request.session['user']
    data=Customer.objects.get(phone=user)
    return render(request,'viewcustprofile.html',{'i':data})
def viewmemprofile(request):
    user=request.session['user']
    data=Member.objects.get(phone=user)
    return render(request,'viewmemprofile.html',{'i':data})
def search(request):

    return render(request, 'search.html')
def sear(request):
    id=request.POST['id']
    data=Product.objects.filter(id=id)
    return render(request,'search.html',{'d':data})
def editcustprofile(request):
    user = request.session['user']
    data = Customer.objects.get(phone=user)
    return render(request, 'editcustprofile.html', {'data': data})

def update(request):
    id=request.POST['id']
    data=Customer.objects.get(id=id)
    data.fname=request.POST['fname']
    data.lname = request.POST['lname']
    data.email = request.POST['email']
    data.phone = request.POST['phone']
    data.address = request.POST['address']
    data.city = request.POST['city']
    data.district = request.POST['district']
    data.pin = request.POST['pin']
    data.save()
    return render(request, 'viewcustprofile.html',{'i':data})
def actentry(request):
    data=Activity.objects.all()
    return render(request,'actentry.html',{'d':data})
def acte(request):
    data1 = Activity.objects.all()
    id = request.POST['id']
    data = Activity.objects.filter(id=id)
    actname = request.POST['id']
    actdate = request.POST['actdate']
    acttime= request.POST['acttime']
    venue=request.POST['venue']
    location=request.POST['location']
    data2 = Actentry(actname=actname,actdate=actdate,acttime=acttime,venue=venue,location=location)
    data2.save()
    return render(request, 'actentry.html', {'i': data, 'data2': data2 ,'d':data1})
def loan(request):
    return render(request,'loan.html')
def logout(request):
    try:
        del request.session['user']
    except KeyError:
        pass
    return render(request,'login.html')






