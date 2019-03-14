/* Drop Sequences for Autonumber Columns */

DROP SEQUENCE IF EXISTS iiot.iiotseq
;

/* Drop Tables */

DROP TABLE IF EXISTS iiot.iiotseq CASCADE
;

/* Create Tables */

CREATE TABLE iiot.measurement
(
        id integer NOT NULL   DEFAULT NEXTVAL(('iiot.iiotseq'::text)::regclass),
        code varchar(50) NOT NULL,
        description varchar(100) NULL
)
TABLESPACE      tbs_iiot
;

/* Create Primary Keys, Indexes, Uniques, Checks */

ALTER TABLE iiot.measurement ADD CONSTRAINT pk_measurement
        PRIMARY KEY (id)
;

/* Create Table Comments, Sequences for Autonumber Columns */

CREATE SEQUENCE iiot.iiotseq INCREMENT 1 START 1
;
