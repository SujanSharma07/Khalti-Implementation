from django.shortcuts import render
import requests
from django.http import JsonResponse
# Create your views here.


def home(request):
    if request.method == 'POST':
        data = request.POST
        print("DATA IS ",data)
        token = data['token']
        amount = data['amount']
   
        url = "https://khalti.com/api/v2/payment/verify/"
        params = {
        "token": token,
        "amount": amount
        }
        headers = {
        "Authorization": "Key test_secret_key_f85495d44530418491c4cf92d1cccac0"
        }

        response = requests.post(url, params, headers = headers)
        if response.status_code == 200:
            return JsonResponse({'data':amount,'status':"Success"})

        else:
            return JsonResponse({'data':amount,'status':"Error"})

    return render(request,'home.html')


