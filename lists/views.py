from django.shortcuts import redirect, render
from lists.models import Item, List

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    countList = Item.objects.filter(list_id=list_.id).count()
    if countList == 0 :
        comment = 'yey, waktunya berlibur'
    if (countList < 5) and (countList != 0) :
        comment = 'sibuk tapi santai'
    if countList >= 5 :
        comment = 'oh tidak'
    return render(request, 'list.html', {'list': list_, 'comment':comment})
    
def home_page(request):
    #if request.method == 'POST':
     #   Item.objects.create(text=request.POST['item_text'])
      #  return redirect('/lists/the-only-list-in-the-world/')   
    comment = 'yey, waktunya berlibur'    
    return render(request, 'home.html', {'comment':comment})

def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/%d/' % (list_.id,))
    
def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/%d/' % (list_.id,))
