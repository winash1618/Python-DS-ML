#!/bin/sh

psql --port 5432 -U mkaruvan << eof
CREATE DATABASE "piscineds";
ALTER USER "mkaruvan" WITH PASSWORD "mysecretpassword";
GRANT ALL PRIVILEGES ON DATABASE "mkaruvan" TO "mkaruvan";
eof