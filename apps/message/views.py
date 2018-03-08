import random

from django.shortcuts import render

# Create your views here.
from message.models import UserMessage


def getform(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        message = request.POST.get('massage', '')
        address = request.POST.get('address', '')
        email = request.POST.get('email', '')
    # all_message = UserMessage.objects.filter(name='metianyan', address='河南')
    # if all_message:
    #     message = all_message[0]

    # for message in all_message:
    #     print(message.name)
    user_message = UserMessage()
    user_message.name = name
    user_message.message = message
    user_message.address = address
    user_message.email = email
    user_message.object_id = random.random(1, 1000)
    user_message.save()
    return render(request, 'message_form.html', {'my_message':message})