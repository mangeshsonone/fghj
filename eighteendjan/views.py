from tokenize import Name
from django.shortcuts import render
# from testapp.models import student
from testapp.models import children

def add(request):
    return render(request,'index.html')

def show(request):
    print('hello')
    name=request.POST.get('name')
    branch=request.POST.get('branch')
    division=request.POST.get('division')
    data=children.objects.create(Name=name,Branch=branch,Division=division)
    data.save()
    return render(request,'index.html')

# def showdetails(request):
#     print('hello')
#     obj=student.objects.all()
#     return render(request,'show.html',{'view':obj})
