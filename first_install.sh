python -m venv venv
./venv/scripts/activate
pip install -r requirements.txt
cp typer_site/settings.example.py typer_site/settings.py
python manage.py migrate
python manage.py createsuperuser