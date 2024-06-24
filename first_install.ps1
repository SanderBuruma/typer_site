python -m venv venv
./venv/Scripts/Activate.ps1
pip install -r requirements.txt
Copy-Item -Path "typer_site/settings.example.py" -Destination "typer_site/settings.py"
python manage.py migrate
python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@admin.admin', 'admin')"