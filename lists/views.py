from django.shortcuts import render,redirect
from django.http import HttpResponse

from lists.models import Item

# Create your views here.
def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/lists/the-only-list-in-the-world/')

    return render(request,'lists/home.html')

def view_list(request):
    context = {'items': Item.objects.all()}
    return render(request,'lists/list.html',context)
