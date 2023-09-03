#!/bin/bash

set -e

mkdir -p database

flask db init
flask db migrate
flask db upgrade