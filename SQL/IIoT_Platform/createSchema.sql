CREATE SCHEMA iiot AUTHORIZATION iiot;


/* Drop Sequences for Autonumber Columns */

DROP SEQUENCE IF EXISTS iiot.iiotseq
;



/* Create Table Comments, Sequences for Autonumber Columns */

CREATE SEQUENCE iiot.iiotseq INCREMENT 1 START 1;
