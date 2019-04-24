create table iiot.sensor(
   id integer NOT NULL   DEFAULT NEXTVAL(('iiot.iiotseq'::text)::regclass),
   device_id integer NOT NULL,
   port_id integer NOT NULL
)
TABLESPACE      tbs_iiot
;

ALTER TABLE iiot.sensor ADD CONSTRAINT "pk_sensor"
        PRIMARY KEY (id)
;

ALTER TABLE iiot.sensor  
  ADD CONSTRAINT idx_sensor_uniq UNIQUE (device_id, port_id)
;
