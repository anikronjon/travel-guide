#!/bin/bash

sudo chmod a+x /wait-for-it.sh

if [ -f /code/backend/uwsgi_app.sock ]; then
    touch /code/backend/uwsgi_app.sock
fi