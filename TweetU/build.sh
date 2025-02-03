pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser --noinput || true