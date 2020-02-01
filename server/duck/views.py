from django.shortcuts import render

# Create your views here.
def test_page(request):
    return render(request, 'duck/example.html')
