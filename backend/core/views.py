from django.http import JsonResponse


def health(request):
    return JsonResponse({
        "status": "ok",
        "service": "camershop-api",
        "version": "0.1.0",
    })
