#!/bin/bash
#
# Title:genesis.sh
# Description:
# Development Environment: OS X 10.15.2/postgres 12.12
# Author: G.S. Cole (guy at shastrax dot com)
#
createuser -U postgres -d -e -E -l -P -r -s komodo_admin // komodoboy
// boris does not have user postgres
createuser -U gsc -d -e -E -l -P -r -s komodo_admin // komodoboy
#
createdb komodo_v1 --owner="komodo_admin"
#
create role komodo_admin with login;
alter role komodo_admin with password 'komodoboy';
#
alter role komodo_admin set client_encoding to 'utf8';
alter role komodo_admin set default_transaction_isolation to 'read committed';
alter role komodo_admin set timezone to 'UTC';
alter role komodo_admin with superuser createrole createdb;
#
# psql -U komodo_admin -d komodo_v1 -h localhost
#
create role komodo_ops with login;
alter role komodo_ops with password 'komodoxxx';
#
grant all privileges on database komodo_v1 to komodo_ops;
#
# psql -U komodo_ops -d komodo_v1 -h localhost
#