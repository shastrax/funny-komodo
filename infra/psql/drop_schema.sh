#!/bin/bash
#
# Title:drop_schema.sh
# Description: remove schema
# Development Environment: OS X 10.15.2/postgres 9.6.16
# Author: G.S. Cole (guy at shastrax dot com)
#
export PGDATABASE=komodo_v1
export PGHOST=localhost
export PGPASSWORD=komodoboy
export PGUSER=komodo_admin
#
psql $PGDATABASE -c "drop table fortune"
#
