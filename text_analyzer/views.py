from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def  homepage(request):
    return render(request,"homepage.html")

def analyzed_text(request):
    input_text = request.GET.get('input_text', 'No text entered.')
    capitalize = request.GET.get('Capitalize','')
    remove_punctuation = request.GET.get('remove_punctuation','') 
    remove_space = request.GET.get('remove_space','') 
    analyzed_text = input_text
    
    if input_text == '':
        return HttpResponse("ERROR : NO TEXT GIVEN.")
        
           
    if remove_punctuation == 'on':
        punctuations = '''"~!@#$%^&*()_+=-{}[]|\;:'"<>,.?/'''
        analyzed_text = ""
        for char in input_text:
            if char not in punctuations:
                analyzed_text = analyzed_text + char
                
    if capitalize == 'on':
        analyzed_text = analyzed_text.title()
                
    if remove_space == 'on':
        analyzed_text = analyzed_text.replace(" ", "")
    
    
        
    context = {
        'analyzed_text': analyzed_text
    }
    return render(request,"analyzed_text.html",context)
