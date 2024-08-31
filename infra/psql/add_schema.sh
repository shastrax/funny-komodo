#!/bin/bash
#
# Title:add_schema.sh
# Description:
# Development Environment: OS X 10.15.2/postgres 12.12
# Author: G.S. Cole (guy at shastrax dot com)
#
export PGDATABASE=komodo_v1
export PGHOST=localhost
export PGPASSWORD=komodoboy
export PGUSER=komodo_admin
#
psql < fortune.psql
#
