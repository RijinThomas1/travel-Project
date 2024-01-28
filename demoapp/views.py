from django.http import HttpResponse
from django.shortcuts import render
from .models import place
from .models import team
# Create your views here.
def demo(request):
  # name="india"
  obj=place.objects.all()
  obj1=team.objects.all()
  return render(request,"index.html",{'result':obj,
                                      'result1':obj1,

                                      })
# def addition(request):
#   x=int(request.GET['num1'])
#   y=int(request.GET['num2'])
#   z=x+y
#   c=x-y
#   b=x*y
#   d=x/y
#   return render(request,"result.html",{
#     'result1' :z,
#     'result2' :c,
#      'result3':b,
#      'result4' :d,
#  })
#
# def about(request):
#     return render (request,"about.html")
#
# def contact(request):
#     return HttpResponse("hello am contact")