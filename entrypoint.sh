#!/bin/sh


gunicorn django_project.wsgi:application --bind 0.0.0.0:8000