from django.http import JsonResponse
from django.views.decorators.http import require_GET
from .models import Client, Message
from datetime import datetime, timedelta

@require_GET
def check_account_number(request, account_number):
    # Проверяем, существует ли клиент с указанным номером счета
    try:
        client = Client.objects.get(account_number=account_number)
        date_obj = client.date_to
        formatted_date = date_obj.strftime("%Y.%m.%d")
        date2_obj = datetime.combine(date_obj, datetime.min.time())
        if datetime.now() + timedelta(days=3) > date2_obj:
            days3 = True
        else:
            days3 = False
        return JsonResponse({'exists': True,
                             'date_to': formatted_date,
                             '3_left': days3,
                             })
    except Client.DoesNotExist:
        return JsonResponse({'exists': False})


@require_GET
def send_message(request):
    try:
        message = Message.objects.get()
        return JsonResponse({'comment': message.message,
                             })
    except Message.DoesNotExist:
        return JsonResponse({'comment': "0"})