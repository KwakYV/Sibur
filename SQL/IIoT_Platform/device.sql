/* Drop Tables */

DROP TABLE IF EXISTS iiot.device CASCADE
;

/* Create Tables */

CREATE TABLE iiot.device
(
        id integer NOT NULL   DEFAULT NEXTVAL(('iiot.iiotseq'::text)::regclass),
        deveui bytea NOT NULL,
        deveuistr varchar(50) NOT NULL,
        name varchar(250) NULL,
        devicetypeid integer NULL,
        measurementid integer NOT NULL,
        factoryid integer NOT NULL,
	portnumber integer not null default 0
)
TABLESPACE      tbs_iiot
;

/* Create Primary Keys, Indexes, Uniques, Checks */

ALTER TABLE iiot.device ADD CONSTRAINT "pk_device"
        PRIMARY KEY (id)
;

ALTER TABLE iiot.device  
  ADD CONSTRAINT idx_dev_uniq UNIQUE (deveui, portnumber)
;
