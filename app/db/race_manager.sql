DROP TABLE IF EXISTS races;
DROP TABLE IF EXISTS runners;

CREATE TABLE runners (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR (255),
    last_name VARCHAR (255)
);

CREATE TABLE races (
    id SERIAL PRIMARY KEY,
    title VARCHAR (255),
    distance DECIMAL,
    elevation INT,
    runner_time DECIMAL,
    runner_id INT REFERENCES runners(id)
);
