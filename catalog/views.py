import json

from django.http import JsonResponse
from django.shortcuts import render

from catalog.models import Users


# Create your views here.

def home(request):
    return render(request, 'home.html')

def contacts(request):
    contact_information = {}
    name = request.POST.get('name')
    phone = request.POST.get('phone')
    message = request.POST.get('message')
    contact_information = {
                            'name':name,
                           'phone': phone,
                           'message': message
                           }
    print(contact_information)
    return render(request, 'contacts.html')

# def post(self, request):
#
#     user_data = json.loads(request.body)
#
#     user = Users()
#
#     user.name = user_data.get('name')
#     user.phone = user_data.get('phone')
#     user.message = user_data.get('message')
#
#     user.save()
#
#     return JsonResponse({
#         'name': user.name,
#         'phone': user.phone,
#         'message': user.message
#     })