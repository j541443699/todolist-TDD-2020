from django.http import HttpResponse
from django.shortcuts import redirect, render
from lists.models import Item, List

def home_page(request):
    # if request.method == 'POST':
        # Item.objects.create(text = request.POST['item_text'])
        # return redirect('/lists/the-only-list-in-the-world/') 
        # Q：return redirect后，self.browser保存的页面发生了改变，是如何发生的？
        # Maybe：
        # 1.return redirect后，浏览器收到新的url，浏览器执行了get.(新url)来获得页面
        # 2.return redirect时，服务端执行get.(新url)获得页面，并将获得的页面同新url一起返回给浏览器
    return render(request, 'home.html')

def view_list(request, list_id):
    list_ = List.objects.get(id = list_id)
    # items = Item.objects.all()
    items = Item.objects.filter(list=list_)
    # return render(request, 'list.html',{'items':items})
    return render(request, 'list.html',{'list':list_})

def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text = request.POST['item_text'], list = list_)
    return redirect(f'/lists/{list_.id}/')

def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')
