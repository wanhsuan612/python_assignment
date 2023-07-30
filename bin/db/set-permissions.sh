#!/bin/bash

# Grant privileges for user
mysql -p$MARIADB_ROOT_PASSWORD -e "CREATE USER '$MARIADB_USER'@'localhost' IDENTIFIED BY '$MARIADB_PASSWORD';
GRANT ALL PRIVILEGES ON $MARIADB_DATABASE.* TO '$MARIADB_USER'@'localhost';
FLUSH PRIVILEGES;"
