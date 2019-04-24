psql -h 172.21.4.105 -d iiot_db -p 5432 -U iiot -w -f createSchema.sql
psql -h 172.21.4.105 -d iiot_db -p 5432 -U iiot -w -f device.sql
psql -h 172.21.4.105 -d iiot_db -p 5432 -U iiot -w -f devicetype.sql
psql -h 172.21.4.105 -d iiot_db -p 5432 -U iiot -w -f gateway.sql
psql -h 172.21.4.105 -d iiot_db -p 5432 -U iiot -w -f ln_devparam_dev.sql
psql -h 172.21.4.105 -d iiot_db -p 5432 -U iiot -w -f port.sql
psql -h 172.21.4.105 -d iiot_db -p 5432 -U iiot -w -f data.sql
psql -h 172.21.4.105 -d iiot_db -p 5432 -U iiot -w -f deviceparams.sql
psql -h 172.21.4.105 -d iiot_db -p 5432 -U iiot -w -f factory.sql
psql -h 172.21.4.105 -d iiot_db -p 5432 -U iiot -w -f measurement.sql
psql -h 172.21.4.105 -d iiot_db -p 5432 -U iiot -w -f sensor.sql
psql -h 172.21.4.105 -d iiot_db -p 5432 -U iiot -w -f grant

