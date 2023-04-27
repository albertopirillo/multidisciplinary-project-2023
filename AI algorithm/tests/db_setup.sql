CREATE EXTENSION citext;
CREATE DOMAIN EMAIL AS citext
  CHECK ( value ~ '^[a-zA-Z0-9.!#$%&''*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$' );

CREATE TABLE worker
(
   worker_id SERIAL PRIMARY KEY,
   name VARCHAR(30) NOT NULL,
   surname VARCHAR(30) NOT NULL,
   username VARCHAR(50) UNIQUE,
   email EMAIL UNIQUE,
   password VARCHAR(50) UNIQUE,
   birth_date DATE , -- NOT NULL
   address VARCHAR(50),
   city VARCHAR(50),
   country VARCHAR(50),
   genre VARCHAR(50),
   contact_email EMAIL,
   telephone_number VARCHAR(50),
   curriculum BYTEA, -- NOT NUL
   embedding FLOAT4 ARRAY[512] --NOT NULL
);

CREATE TABLE job_offer
(
   -- company_id SERIAL REFERENCES company(company_id),
   offer_id SERIAL PRIMARY KEY,
   title VARCHAR(50) NOT NULL,
   file BYTEA, -- NOT NULL
   embedding FLOAT4 ARRAY[512] -- NOT NULL
);

CREATE TABLE applies_to
(
    offer_id SERIAL REFERENCES job_offer(offer_id),
    worker_id SERIAL REFERENCES worker(worker_id)
);