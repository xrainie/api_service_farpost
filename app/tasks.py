from celery import shared_task
from .models import Promo
from .utils import PromoData
from .serializers import PromoSerializer

@shared_task
def update_promo_data():
    data = PromoData().load()
    if not data:
        return None
    Promo.objects.all().delete()
    for promo in data:
        Promo.objects.create(author=promo['author'], title=promo['title'], views=promo['views'])

