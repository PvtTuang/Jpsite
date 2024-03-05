from django.http import JsonResponse
import requests
from posts.models import Product
from django.shortcuts import get_object_or_404

def notify_line(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        idline = request.POST.get('idline')
        username = request.user.username
        message = f'ผู้ใช้ {username} สนใจสินค้า {product.name} ราคา {product.price} บาท  ติดต่อกลับ Line: {idline}'

        line_notify_token = 'Sla1EbAaDCYVTawesVP3UQsS5DZvTEcuGhLzx4ZhpVF'
        line_notify_api = 'https://notify-api.line.me/api/notify'
        headers = {'Authorization': f'Bearer {line_notify_token}'}
        payload = {'message': message}
        response = requests.post(line_notify_api, headers=headers, data=payload)

        if response.status_code == 200:
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': response.text})

    return JsonResponse({'error': 'Invalid request'})
