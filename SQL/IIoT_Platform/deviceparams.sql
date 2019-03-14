/* Drop Tables */

DROP TABLE IF EXISTS iiot.deviceparams CASCADE
;

/* Create Tables */

CREATE TABLE iiot.deviceparams
(
        id integer NOT NULL   DEFAULT NEXTVAL(('iiotseq'::text)::regclass),
        code varchar(50) NOT NULL,
        name varchar(50) NULL,
        description varchar(100) NULL
)
TABLESPACE      tbs_iiot
;

/* Create Primary Keys, Indexes, Uniques, Checks */

ALTER TABLE iiot.deviceparams ADD CONSTRAINT "pk_deviceparams"
        PRIMARY KEY (id)
;