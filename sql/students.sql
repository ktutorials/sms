-- Table: public."Students"

-- DROP TABLE public."Students";

CREATE TABLE public."Students"
(
    "Id" integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    "Name" character varying COLLATE pg_catalog."default" NOT NULL,
    "Age" numeric NOT NULL,
    "Grade" character varying COLLATE pg_catalog."default" NOT NULL,
    "IsFunClub" boolean NOT NULL,
    "Address" character varying COLLATE pg_catalog."default" NOT NULL,
    "EmergencyContact" character varying COLLATE pg_catalog."default" NOT NULL,
    "ParentContact" character varying COLLATE pg_catalog."default" NOT NULL,
    "Hobbies" character varying COLLATE pg_catalog."default",
    CONSTRAINT "Students_pkey" PRIMARY KEY ("Id")
)

TABLESPACE pg_default;

ALTER TABLE public."Students"
    OWNER to smsadmin;

GRANT ALL ON TABLE public."Students" TO smsadmin;

COMMENT ON TABLE public."Students"
    IS 'Students data is stored for SMS app.';