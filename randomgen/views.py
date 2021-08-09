from django.shortcuts import render
import random
import string
# Create your views here.
def home(request):
    return render(request,"homepage.html")

def generator(request):
    return render(request,"passwordgen.html")

def passwordView(request):
    letters = list('QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm')
    password_len=int(request.GET.get('charlen'))
    special_char_len=int(request.GET.get('specials'))
    digital_len=int(request.GET.get('numbers'))
    randomPassword=''
    specialChars=list('!@#$%^&*_-+=,<>?/:;')

    if special_char_len > 0:
        randomPassword+=''.join(random.choice(specialChars) for i in range(special_char_len))

    if digital_len > 0:
        randomPassword+=''.join(random.choice(string.digits) for i in range(digital_len))

    randomPassword+=''.join(random.choice(letters) for i in range(password_len-digital_len-special_char_len))

    finalPassword=''.join(random.sample(randomPassword,len(randomPassword)))

    return render(request,"viewPassword.html",{'password':finalPassword})
