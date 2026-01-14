import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lifeblood_connect.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Delete existing admin user if exists
User.objects.filter(username='admin').delete()

# Create new superuser
User.objects.create_superuser('admin', 'admin@lifebloodconnect.com', '1234')
print('✅ Superuser created successfully!')
print('Username: admin')
print('Password: 1234')
