#!/bin/sh

# Kiểm tra và cấp quyền thực thi cho script
chmod u+x migration.sh

flask db init
flask db migrate
flask db upgrade
