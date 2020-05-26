from django.http import HttpResponse
from django.shortcuts import redirect, render
from lists.models import Item

def home_page(request):
    # if request.method == 'POST':
        # Item.objects.create(text = request.POST['item_text'])
        # return redirect('/lists/the-only-list-in-the-world/') 
        # Q：return redirect后，self.browser保存的页面发生了改变，是如何发生的？
        # Maybe：
        # 1.return redirect后，浏览器收到新的url，浏览器执行了get.(新url)来获得页面
        # 2.return redirect时，服务端执行get.(新url)获得页面，并将获得的页面同新url一起返回给浏览器
    return render(request, 'home.html')

def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html',{'items':items})

def new_list(request):
    Item.objects.create(text = request.POST['item_text'])
    return redirect('/lists/the-only-list-in-the-world/')