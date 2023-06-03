from django.http import HttpResponse

def healthy_view(request):
  return HttpResponse(status=200)