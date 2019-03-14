DROP TABLE IF EXISTS iiot.ln_devparam_dev CASCADE
;

/* Create Tables */

CREATE TABLE iiot.ln_devparam_dev
(
        devparamid integer NOT NULL,
        devid integer NOT NULL,
        paramval numeric(10,2) NULL,
        effdt date NULL
)
TABLESPACE      tbs_iiot
;

/* Create Primary Keys, Indexes, Uniques, Checks */

ALTER TABLE iiot.ln_devparam_dev ADD CONSTRAINT pk_devparam_dev
        PRIMARY KEY (devparamid, devid)
;