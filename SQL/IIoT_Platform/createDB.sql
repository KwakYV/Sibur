create role iiot with login password 'iiot';
create database iiot_db with owner iiot;

create tablespace tbs_iiot
owner iiot
location '/var/lib/postgresql/data/pg_tblspc/';

