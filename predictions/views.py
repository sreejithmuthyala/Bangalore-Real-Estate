from datetime import datetime
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import broker_loctions, mailsbox
from . import util

# Create your views here.
def hello(request):
    return HttpResponse('Hello World')

def lore(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request,'main.html')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    else:
        return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def customer(request):
    return render(request,'customer_register.html')

def broker(request):
    return render(request,'broker_register.html')

def customer_register(request):
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email=request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:

            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('customer_register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('customer_register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name= last_name )
                user.save()
                return redirect('login')
    return render(request, 'customer_register.html')

def broker_register(request):
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email=request.POST['email']
        locations= request.POST['locations']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:

            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('broker_register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('broker_register')
            else:
                user = mailsbox.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name= last_name )
                user.save()
                locations=[i for i in locations.split(',')]
                locations=list(set(locations))
                if len(locations)==0:
                    messages.info(request,'Please provide atleast one location')
                    return redirect('broker_register')
                for i in locations:
                    broker=broker_loctions.objects.create(username=username,location=i)
                    broker.save()
                return redirect('login')
    return redirect('login')

def main(request):
    if request.method=='POST':
        to_user = request.POST['touser']
        body = request.POST['body']
        subject = request.POST['subject']
        current_user = request.user
        time = datetime.now()
        formatedDate = time.strftime("%H:%M %Y-%m-%d")
        sent_mail=mailsbox.objects.create(datetime=formatedDate,from_user=current_user.username, subject=subject, body=body,to_user=to_user)
        sent_mail.save()

        return render(request, 'main.html')

    

def estimate_price(request):
    if request.method=='POST':
        area = request.POST['area']
        bhk = request.POST['bhk']
        bathrooms =request.POST['bathrooms']
        location = request.POST['location']

        estimated_price = util.get_estimated_price(location,area,bhk,bathrooms)
        brokerlist=broker_loctions.objects.filter(location=location).values_list('username')
        # print(brokerlist[0][0])
        n=len(brokerlist)
        bl=[]
        for i in range(n):
            bl.append(brokerlist[i][0])
        print(estimated_price)
        return render(request,'price.html',{'estimated_price':estimated_price, 'bl':bl})

def compose(request):
    return render(request,'compose.html')

def sent(request):
    sentmails=mailsbox.objects.filter(from_user=request.user.username).values_list('datetime','from_user','subject','body','to_user')
    n=len(sentmails)
    print(n)
    if n==0:
        sm2='No Sent Mails to display'
        return render(request,'sent.html',{'sm3':sm2})
    sm=[]
    
    for i in range(n-1,-1,-1):
        l=[]
        l.append(sentmails[i][0])
        l.append(sentmails[i][4])
        l.append(sentmails[i][2])
        l.append(sentmails[i][3])
        # print(sentmails[i])
        sm.append(l)
    
    return render(request,'sent.html',{'sm1':sm})

def receive(request):
    receivedmails=mailsbox.objects.filter(to_user=request.user.username).values_list('datetime','from_user','subject','body','to_user')
    n=len(receivedmails)
    print(n)
    if n==0:
        rm2='No Received Mails To Display'
        return render(request,'received.html',{'rm2':rm2})
    rm=[]
    for i in range(n-1,-1,-1):
        l=[]
        l.append(receivedmails[i][0])
        l.append(receivedmails[i][1])
        l.append(receivedmails[i][2])
        l.append(receivedmails[i][3])
        rm.append(l)
    return render(request,'received.html',{'rm1':rm})