#!/bin/sh

# requires South:
# pip install south

./manage.py schemamigration remind --auto
./manage.py migrate remind
