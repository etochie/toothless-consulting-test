import stripe
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.core.models import Item
from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY

class BuyItemView(APIView):
    def get(self, request, pk):
        item = Item.objects.get(pk=pk)
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': item.name,
                    },
                    'unit_amount_decimal': item.price,
                },
                'quantity': 1
            }],
            mode='payment',
            success_url='https://example.com/success',
            cancel_url='https://example.com/cancel'
        )

        return Response({'response':session.id})

class ItemView(APIView):
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, pk):
        item = Item.objects.get(pk=pk)
        return Response({'item': item}, template_name='core/item_template.html')

