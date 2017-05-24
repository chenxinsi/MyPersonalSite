#coding:utf-8
##from django.http import HttpResponse

##def index(request):
##    return HttpResponse(u"welcome!")
from django.shortcuts import render
 
 
def home(request):
    string = u"心思的个人网页"
    TutorialList = ['HTML', 'CSS', 'JAVASCRIPT', 'Python', 'Django']
    info_dict = {'name1': u'张三', 'name2': u'李四'}
   # return render(request, 'home.html', {'TutorialList': TutorialList})
    #return render(request, 'home.html', {'info_dict': info_dict})
    return render(request, 'index.html')
