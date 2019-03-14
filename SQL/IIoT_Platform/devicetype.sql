/* Drop Tables */

DROP TABLE IF EXISTS iiot.devicetype CASCADE
;

/* Create Tables */

CREATE TABLE iiot.devicetype
(
        id integer NOT NULL   DEFAULT NEXTVAL(('iiot.iiotseq'::text)::regclass),
        code varchar(50) NOT NULL,
        name varchar(100) NULL,
        description varchar(150) NULL,
        vendor varchar(100) NULL,
        payloadlen integer NULL
)
TABLESPACE      tbs_iiot
;

/* Create Primary Keys, Indexes, Uniques, Checks */

ALTER TABLE iiot.devicetype ADD CONSTRAINT "pk_devicetype"
        PRIMARY KEY (id)
;
