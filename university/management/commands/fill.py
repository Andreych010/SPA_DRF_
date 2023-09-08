from django.core.management import BaseCommand
from university.models import Payments


class Command(BaseCommand):

    def handle(self, *args, **options):
        payments_list = [
            {'client': 'Сидоров', 'date_payment': '12.09.2023', 'amount_payment': '90000', 'method_payment': 'spot'},
            {'client': 'Иванов', 'date_payment': '12.09.2022', 'amount_payment': '60000', 'method_payment': 'spot'},
            {'client': 'Светланова', 'date_payment': '12.05.2023', 'amount_payment': '85000', 'method_payment': 'cashless'},

        ]
        payments_create = []
        for payments_item in payments_list:
            payments_create.append(Payments(**payments_item))
        Payments.objects.bulk_create(payments_create)
