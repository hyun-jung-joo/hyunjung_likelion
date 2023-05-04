from django.shortcuts import render

# Create your views here.
def listsHome(request):
	return render(request, 'lists.html')