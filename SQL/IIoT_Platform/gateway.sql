DROP TABLE IF EXISTS iiot.gateway CASCADE
;

/* Create Tables */

CREATE TABLE iiot.gateway
(
        id integer NOT NULL   DEFAULT NEXTVAL(('iiot.iiotseq'::text)::regclass),
        code varchar(50) NOT NULL,
        name varchar(100) NULL,
        description varchar(150) NULL,
        fmwid bytea NOT NULL,
        factoryid integer NOT NULL
)
TABLESPACE      tbs_iiot
;

/* Create Primary Keys, Indexes, Uniques, Checks */

ALTER TABLE iiot.gateway ADD CONSTRAINT pk_gateway
        PRIMARY KEY (id)
;
