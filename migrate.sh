#!/bin/bash

./manage.py schemamigration rmnd --auto
./manage.py migrate rmnd
