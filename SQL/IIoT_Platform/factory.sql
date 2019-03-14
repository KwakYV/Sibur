
DROP TABLE IF EXISTS iiot.factory CASCADE
;

/* Create Tables */

CREATE TABLE iiot.factory
(
        id integer NOT NULL   DEFAULT NEXTVAL(('iiotseq'::text)::regclass),
        code varchar(50) NOT NULL,
        name varchar(150) NULL,
        description varchar(300) NULL
)
TABLESPACE      tbs_iiot
;

/* Create Primary Keys, Indexes, Uniques, Checks */

ALTER TABLE iiot.factory ADD CONSTRAINT pk_factory
        PRIMARY KEY (id)
;