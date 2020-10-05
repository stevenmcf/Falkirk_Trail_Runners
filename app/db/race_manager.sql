DROP TABLE IF EXISTS race_results;
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
    date DATE,
    distance DECIMAL,
    elevation INT,
    runner_id INT REFERENCES runners(id)
);

CREATE TABLE race_results (
    id SERIAL PRIMARY KEY,
    race_id INT REFERENCES races(id),
    runner_id INT REFERENCES runners(id) ON DELETE CASCADE,
    time  DECIMAL
)
