#! /bin/sh
docker exec  db /bin/bash -c " cd tmp ; cat size.sql | psql -U postgres  postgres | awk 'NR==3' | xargs "

