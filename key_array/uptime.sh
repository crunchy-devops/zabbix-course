#! /bin/sh
docker exec  db /bin/bash -c " cd tmp ; cat uptime.sql | psql -U postgres  postgres | awk 'NR==3' "
