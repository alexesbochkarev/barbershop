

def get_client_ip(request):
    """
    Функция get_client_ip() получает request и из него извлекает данные об IP адресе.
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    ip = x_forwarded_for.split(',')[0] if x_forwarded_for else request.META.get('REMOTE_ADDR')
    return ip