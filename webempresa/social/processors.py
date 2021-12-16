from .models import Link

def ctx_dict(request):
    dict = {}
    links = Link.objects.all()
    for link in links:
        dict[link.key] = link.url
    return dict