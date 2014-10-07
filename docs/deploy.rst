Deploy
======

Per eseguire il deploy in produzione bisogna eseguire i seguenti passi:

* Clonare il repository

cd /home
git clone git@github.com:openpolis/op-accesso.git
sudo chown -R www-data op-accesso/
cd op-accesso/

* Installare i packages necessari
sudo apt-get update
sudo apt-get install python-dev python-virtualenv
sudo apt-get install nginx
sudo apt-get install postgresql postgresql-contrib

# support for Pillow
http://pillow.readthedocs.org/en/latest/installation.html#external-libraries
http://stackoverflow.com/questions/13505621/cant-get-pil-to-correctly-install-on-ubuntu-12-04
sudo apt-get install python-imaging

* Creare il virtualenv

mkvirtualenv op-accesso
setvirtualenvproject

* Installare i requirements

pip install -r requirements/production.txt

* Configurare i settings (config/.env)

cp config/samples/.env config/.env
vi config/.env

    # Global accesso environment variables
    PROJECT_TITLE=OP-Accesso
    SECRET_KEY=aodkmdwkdudnoj$1234!@$1)l(hv%^3noxb1^m2wz&egtb1b(x
    ADMIN_NAME=admin
    ADMIN_EMAIL=admin@uact.it
    DEFAULT_FROM_EMAIL=no-replay@depp.it
    EMAIL_SUBJECT_PREFIX="[Accesso] "
    SERVER_EMAIL=root@depp.it
    DATABASE_URL=psql://postgres@localhost/

    # Development only
    # DEBUG=on

    # Production only
    ALLOWED_HOSTS=localhost,127.0.0.1
    AWS_SES_ACCESS_KEY_ID=YOUR-ACCESS-KEY-ID
    AWS_SES_SECRET_ACCESS_KEY=YOUR-SECRET-ACCESS-KEY
    AWS_SES_REGION_NAME=ue-west-1
    AWS_SES_REGION_ENDPOINT=email.ue-west-1.amazonaws.com

* Installare l'applicazione

python project/manage.py syncdb
python project/manage.py collectstatic --noinput
python project/manage.py compilemessages

* Aggiungere il processo uwsgi

cp config/samples/uwsgi.ini config/uwsgi.ini
vi config/uwsgi.ini

    # configuration file for uwsgi
    [uwsgi]

    # variables
    base = /home
    package_name = accesso
    repo_name = op-accesso
    repo_path = %(base)/%(repo_name)
    venv_path = %(base)/virtualenvs/%(repo_name)

    # config
    procname = %(repo_name)
    uid = www-data
    gid = www-data
    vacuum = true
    master = true
    processes = 4
    daemonize = %(repo_path)/resources/logs/accesso.log
    harakiri = 300
    harakiri-verbose = true

    # set the http port
    socket = %(repo_path)/accesso.sock

    # change to django project directory
    chdir = %(repo_path)/project
    home = %(venv_path)
    module = %(package_name).wsgi

ln -s /home/op-accesso/config/uwsgi.ini /etc/uwsgi/vassals/op-accesso.ini

* Aggiungere la configurazione per ngnix

cp config/samples/nginx.conf config/nginx.conf
vi config/nginx.conf

    upstream op-accesso {
        server unix:///home/op-accesso/op-accesso.sock;
    }

    server {
            listen 8010;
            server_name accesso.depp.it;
            charset utf-8;
            client_max_body_size 75M;

            access_log /var/log/nginx/op-accesso_access.log;
            error_log /var/log/nginx/op-accesso_error.log;

            # alias favicon.* to static
            location ~ ^/favicon.(\w+)$ {
                alias /home/op-accesso/resources/static/favicon.$1;
            }

            # alias robots.txt and humans.txt to static
            location ~ ^/(robots|humans).txt$ {
                alias /home/op-accesso/resources/static/$1.txt;
            }

            location /static {
                alias /home/op-accesso/resources/static;
            }
            location /media {
                alias /home/op-accesso/resources/media;
            }

            location / {
                uwsgi_pass op-accesso;
                include /etc/nginx/uwsgi_params;
            }
    }

sudo service nginx restart

* Configurazione servizio

/admin > login
modifica site
aggiungi social applications
