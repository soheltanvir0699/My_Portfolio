from django.core.mail import send_mail
from django.shortcuts import render
from .models import Product, Blog
# Create your views here.
from My_Personal_Portfolio.settings import EMAIL_HOST_USER


def index(request):
    all_Product = Product.objects.all()
    all_Blog = Blog.objects.all()
    return render(request, 'index.html', {'all_Product': all_Product, 'blog': all_Blog})


def send_email(request):
    print('working')
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        note = request.POST['message']
        number = request.POST['number']
        if name and email and note and number:
            print(name, note, email)
            print('email')
            email = send_mail(' from :{}'.format(email), 'Hey, it\'s {}. Phone Number: {} '.format(name, number) + note,
                              EMAIL_HOST_USER, ['soheltanvir0699@gmail.com', ], fail_silently=False)
            print(email)

            return render(request, 'index.html')

        else:
            return render(request, 'index.html')
