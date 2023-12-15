import csv
from django.core.management.base import BaseCommand, CommandParser
from restaurant.models import Booking


class Command(BaseCommand):
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('booking_mock_data', type=str)
        return super().add_arguments(parser)
    
    def handle(self, *args, **options):
        csv_file = options['booking_mock_data']
        self.import_data(csv_file)
    
    def import_data(self, csv_file):
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                Booking.objects.create(
                    name=row['name'],
                    no_of_guests = row['no_of_guests'],
                    booking_date = row['booking_date'],
                )
        self.stdout.write(self.style.SUCCESS('Data imported successfully'))