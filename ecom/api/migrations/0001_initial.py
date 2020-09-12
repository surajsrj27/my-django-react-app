from django.db import migrations
from api.user.models import CustomUser

class Migration(migrations.Migration):
    def seed_data(apps, schema_editor):
        user = CustomUser(name="suraj", email="suraj@gmail.com", is_staff=True, is_superuser=True, phone="8000123456", gender="Male")

        user.set_password("suraj")
        user.save()

    dependencies = [
        
    ]

    operations = [
        migrations.RunPython(seed_data),
    ]