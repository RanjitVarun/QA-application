from django.http import JsonResponse

def custom404(request, exception=None):
    return JsonResponse({
        'status_code': 404,
        'error': 'The resource was not found'
    })
   

def custom500(request):
    return JsonResponse({
        'status_code': 500,
        'error': 'Internal Server Error'
    })