from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>First page.</h1>")

def postDetail(request, image_id):
    return HttpResponse("<h2>Details for image :" + str(image_id) +" </h2>")