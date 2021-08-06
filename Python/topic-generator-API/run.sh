#! /bin/sh

# default run on localhost and port 5000
export FLASK_APP=gen-topic
#flask run

# if you want to listen to public IP
#flask run --host 0.0.0.0

# running under gunicorn
# gunicorn gen-topic:app
gunicorn -b 0.0.0.0:5000 gen-topic:app
