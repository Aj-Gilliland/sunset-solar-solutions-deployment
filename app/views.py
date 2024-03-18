from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from typing import List
from dataclasses import dataclass
import requests
from .models import EmpApp,create_EmpApp, all_EmpApp, create_ConApp, all_ConApp
from .forms import EmpAppForm, ConForm
#################################################################################################
def home (request:HttpRequest)->render:
    return render(request, "home.html")
#################################################################################################
def contact (request:HttpRequest)->render:
    form = ConForm()
    if request.GET:
        form = ConForm(request.GET)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            note = form.cleaned_data['note']
            create_ConApp(name, email, note)
            print(all_ConApp())#for testing ,delete later
            return render(request, "contact.html", {'form':form, 'name':name, 'email':email, 'note':note})
        else:
            return render(request, "contact.html", {'form':form})
        
    return render(request, "contact.html", {'form':form})
#################################################################################################
#this will of course be put into POST later
def donate (request:HttpRequest)->render:
    #coin payments api looking pretty cool
    #this end point will be changed to buying the t-shirt sold, and will need to take in address, name, size, and color through a form
    url = "https://api.printify.com/v1/shops.json"# end point and vVkeyVv
    api_key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIzN2Q0YmQzMDM1ZmUxMWU5YTgwM2FiN2VlYjNjY2M5NyIsImp0aSI6ImVjY2MwMjZkNjhjYTQ2MTliNWZmNzM2YmIzNjIzYjczZmE2MWNlNTVkYTQ1Mjc0NDg2NmM5YjE1ZjE0YTBiNTQwNDlhYTQ1MTE0ZmFjZjM2IiwiaWF0IjoxNzAxMDQwMjE5LjA5NzE4NiwibmJmIjoxNzAxMDQwMjE5LjA5NzE4OSwiZXhwIjoxNzMyNjYyNjE5LjA5MDY1MSwic3ViIjoiMTYwNDYxODgiLCJzY29wZXMiOlsic2hvcHMubWFuYWdlIiwic2hvcHMucmVhZCIsImNhdGFsb2cucmVhZCIsIm9yZGVycy5yZWFkIiwib3JkZXJzLndyaXRlIiwicHJvZHVjdHMucmVhZCIsInByb2R1Y3RzLndyaXRlIiwid2ViaG9va3MucmVhZCIsIndlYmhvb2tzLndyaXRlIiwidXBsb2Fkcy5yZWFkIiwidXBsb2Fkcy53cml0ZSIsInByaW50X3Byb3ZpZGVycy5yZWFkIl19.ASQD3Sl0peGHdy6tmOpnzpDgfZ1c7c93f2DWhW6F-aQ5F0v4KsRwNZ9-8aSKuGpDIY-gnAAJ2a7dsy7hh9k" # Replace "YOUR_API_KEY_HERE" with your actual Printify API key
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }
    response = requests.get(url, headers=headers)# currently using get for now, might use post

    if response.status_code == 200: 
        print("API request successful")
        print(response.json())
    else:
        print(f"API request failed with status code {response.status_code}")
        print(f'!!!!!ERROR!!!!! {response.text}')

    return render(request, "donate.html")
#################################################################################################
#takes in form data and puts it into the data base (could build admin page to view)
def career (request:HttpRequest)->render:
    form = EmpAppForm()
    if request.POST:
        form = EmpAppForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            position = form.cleaned_data['position']
            number = form.cleaned_data['number']
            email = form.cleaned_data['email']
            create_EmpApp(first_name, last_name, position, number, email)
            print(all_EmpApp())#for testing ,delete later
            return render(request, "career.html", {'form':form})
        else:
            return render(request, "career.html", {'form':form})
        
    return render(request, "career.html", {'form':form})
#################################################################################################
