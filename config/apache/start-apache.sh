#!/bin/sh

set -e

. /etc/apache2/envvars
ulimit -n 8192
mkdir /var/run/apache2
mkdir /var/lock/apache2
chown root:www-data /var/lock/apache2
exec /usr/sbin/apache2 -k start -DFOREGROUND