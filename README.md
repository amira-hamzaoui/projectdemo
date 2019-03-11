# download and install project
git clone https://github.com/amira-hamzaoui/sgav_project.git
python3.6 -m venv virtualenv
source virtualenv/bin/activate
pip install -r requirements.txt
./manage.py migrate
python manage.py runserver

#first install of environnent

sudo apt-get install postgresql postgresql-client
psql -U postgres
CREATE USER sgav__user WITH PASSWORD 'sgav;2019';
GRANT ALL ON DATABASE sgav_db TO sgav_user;