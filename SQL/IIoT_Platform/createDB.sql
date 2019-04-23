create role iiot with login password 'iiot';
create database iiot_db with owner iiot;

create tablespace tbs_iiot
owner iiot
location '/var/lib/postgresql/data/pg_tblspc/';

CREATE SCHEMA iiot AUTHORIZATION iiot;


/* Drop Sequences for Autonumber Columns */

DROP SEQUENCE IF EXISTS iiot.iiotseq
;



/* Create Table Comments, Sequences for Autonumber Columns */

CREATE SEQUENCE iiot.iiotseq INCREMENT 1 START 1;
