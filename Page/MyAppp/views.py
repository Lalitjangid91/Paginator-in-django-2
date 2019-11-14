from django.shortcuts import render
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from .models import Images
# Create your views here.
def Home(request):
    user_list = Images.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(user_list,3)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, 'MyApp/home.html', {'users': users})