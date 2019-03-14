/* Drop Tables */

DROP TABLE IF EXISTS iiot.data CASCADE
;

/* Create Tables */

CREATE TABLE iiot.data
(
	id integer NOT NULL   DEFAULT NEXTVAL(('iiot.iiotseq'::text)::regclass),
	devid integer NOT NULL,
	gateid integer NOT NULL,
	data bytea NULL,
	effdt date NOT NULL,
	ppndt timestamp without time zone NULL,
	fcntup integer NULL,
	freq integer NULL,
	rssi integer NULL,
	sf integer NULL,
	snr numeric(10,4) NULL
)
TABLESPACE	tbs_iiot
;

/* Create Primary Keys, Indexes, Uniques, Checks */

ALTER TABLE iiot.data ADD CONSTRAINT "pk_data"
	PRIMARY KEY (id)
;

