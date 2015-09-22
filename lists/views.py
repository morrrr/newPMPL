from django.shortcuts import redirect, render
from lists.models import Item, List

def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})
    
def home_page(request):
    #if request.method == 'POST':
     #   Item.objects.create(text=request.POST['item_text'])
      #  return redirect('/lists/the-only-list-in-the-world/')
    
    if Item.objects.count() == 0 :
        comment = 'yey, waktunya berlibur'
    if (Item.objects.count() < 5) and (Item.objects.count() != 0) :
        comment = 'sibuk tapi santai'
    if Item.objects.count() >= 5 :
        comment = 'oh tidak'   
        
    return render(request, 'home.html', {'comment':comment})

def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/the-only-list-in-the-world/')