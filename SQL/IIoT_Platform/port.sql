CREATE TABLE iiot.port
(
        id integer NOT NULL   DEFAULT NEXTVAL(('iiot.iiotseq'::text)::regclass),
        port_code varchar(50),
        port_number integer NOT NULL,
        devicetype_id integer NOT NULL,
        measurement_id integer NOT NULL
)
TABLESPACE      tbs_iiot
;

ALTER TABLE iiot.port ADD CONSTRAINT "pk_port"
        PRIMARY KEY (id)
;

ALTER TABLE iiot.port  
  ADD CONSTRAINT idx_port_uniq UNIQUE (devicetype_id, port_number)
;

