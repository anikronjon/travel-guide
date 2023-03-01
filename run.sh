#!/bin/bash

if [ -f /code/backend/uwsgi_app.sock ]; then
    touch /code/backend/uwsgi_app.sock
fi