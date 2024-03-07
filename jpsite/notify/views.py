import requests
from posts.models import Product
from django.shortcuts import get_object_or_404 ,render ,redirect

def notify_line(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        idline = request.POST.get('idline')
        if idline:  # ตรวจสอบว่ามีข้อมูล idline หรือไม่
            username = request.user.username
            message = f'ผู้ใช้ {username} สนใจสินค้า {product.name} ราคา {product.price} บาท  ติดต่อกลับ Line: {idline}'

            line_notify_token = 'Sla1EbAaDCYVTawesVP3UQsS5DZvTEcuGhLzx4ZhpVF'
            line_notify_api = 'https://notify-api.line.me/api/notify'
            headers = {'Authorization': f'Bearer {line_notify_token}'}
            payload = {'message': message}
            response = requests.post(line_notify_api, headers=headers, data=payload)

            if response.status_code == 200:
                return render(request, 'notify/notify_success.html', {'idline': idline})
            else:
                return render(request, 'notify/notify_error.html')
        else:
            return render(request, 'notify/notify_error.html', {'error_message': 'กรุณากรอก ID Line'})

    return render(request, 'notify/notify_error.html', {'error_message': 'Invalid request'})
