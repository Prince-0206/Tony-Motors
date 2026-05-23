#!/bin/bash
set -e

cd "$(dirname "$0")"

echo "Making migrations..."
python manage.py makemigrations store --no-input 2>/dev/null || true

echo "Running migrations..."
python manage.py migrate

echo "Seeding data if needed..."
python manage.py shell -c "
from store.models import Product
if Product.objects.count() == 0:
    exec(open('store/seed.py').read())
    print('Seeded!')
else:
    print('Data already seeded, skipping.')
"

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Creating superuser if not exists..."
python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@tonymotors.com', 'admin123')
    print('Superuser created: admin / admin123')
else:
    print('Superuser already exists.')
"

echo "Starting Django on port 8000..."
exec python manage.py runserver 0.0.0.0:8000
