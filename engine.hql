


CREATE EXTERNAL TABLE IF NOT EXISTS camera_data (
    camera_id STRING,
    location STRING,
    priority STRING,
    video_file STRING,
    v_date STRING,
    hour STRING,
    person INT,
    backpack INT,
    car INT,
    bicycle INT,
    dog INT,
    cat INT,
    redshirt INT,
    blueshirt INT,
    blackshirt INT,
    redcar INT,
    bluecar INT,
    blackcar INT,
    racecar INT,
    alto INT,
    pequeno INT,
    blueshoes INT,
    redshoes INT,
    blackshoes INT,
    bluepants INT,
    redpants INT,
    blackpants INT

)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
LOCATION '/user/hadoop/warehouse/';


CREATE TABLE IF NOT EXISTS persons_per_camera AS
SELECT
    camera_id,
    location,
    priority,
    video_file,
    v_date,
    SUM(person) AS total_persons
FROM camera_data
GROUP BY
    camera_id,
    location,
    priority,
    video_file,
    v_date
ORDER BY total_persons DESC;


CREATE TABLE IF NOT EXISTS backpacks_per_camera AS
SELECT
    camera_id,
    location,
    priority,
    video_file,
    v_date,
    SUM(backpack) AS total_backpacks
FROM camera_data
GROUP BY
    camera_id,
    location,
    priority,
    video_file,
    v_date
ORDER BY total_backpacks DESC;



CREATE TABLE IF NOT EXISTS redshirts_per_camera AS
SELECT
    camera_id,
    location,
    priority,
    video_file,
    v_date,
    SUM(redshirt) AS total_redshirts
FROM camera_data
GROUP BY
    camera_id,
    location,
    priority,
    video_file,
    v_date
ORDER BY total_redshirts DESC;

CREATE TABLE IF NOT EXISTS cars_per_camera AS
SELECT
    camera_id,
    location,
    priority,
    video_file,
    v_date,
    SUM(car) AS total_cars
FROM camera_data
GROUP BY
    camera_id,
    location,
    priority,
    video_file,
    v_date
ORDER BY total_cars DESC;

CREATE TABLE IF NOT EXISTS bicycles_per_camera AS
SELECT
    camera_id,
    location,
    priority,
    video_file,
    v_date,
    SUM(bicycle) AS total_bicycles
FROM camera_data
GROUP BY
    camera_id,
    location,
    priority,
    video_file,
    v_date
ORDER BY total_bicycles DESC;

CREATE TABLE IF NOT EXISTS dogs_per_camera AS
SELECT
    camera_id,
    location,
    priority,
    video_file,
    v_date,
    SUM(dog) AS total_dogs
FROM camera_data
GROUP BY
    camera_id,
    location,
    priority,
    video_file,
    v_date
ORDER BY total_dogs DESC;

CREATE TABLE IF NOT EXISTS cats_per_camera AS
SELECT
    camera_id,
    location,
    priority,
    video_file,
    v_date,
    SUM(cat) AS total_cats
FROM camera_data
GROUP BY
    camera_id,
    location,
    priority,
    video_file,
    v_date
ORDER BY total_cats DESC;

CREATE TABLE IF NOT EXISTS blueshirts_per_camera AS
SELECT
    camera_id,
    location,
    priority,
    video_file,
    v_date,
    SUM(blueshirt) AS total_blueshirts
FROM camera_data
GROUP BY
    camera_id,
    location,
    priority,
    video_file,
    v_date
ORDER BY total_blueshirts DESC;

CREATE TABLE IF NOT EXISTS blackshirts_per_camera AS
SELECT
    camera_id,
    location,
    priority,
    video_file,
    v_date,
    SUM(blackshirt) AS total_blackshirts
FROM camera_data
GROUP BY
    camera_id,
    location,
    priority,
    video_file,
    v_date
ORDER BY total_blackshirts DESC;

CREATE TABLE IF NOT EXISTS redcars_per_camera AS
SELECT
    camera_id,
    location,
    priority,
    video_file,
    v_date,
    SUM(redcar) AS total_redcars
FROM camera_data
GROUP BY
    camera_id,
    location,
    priority,
    video_file,
    v_date
ORDER BY total_redcars DESC;

CREATE TABLE IF NOT EXISTS altos_per_camera AS
SELECT
    camera_id,
    location,
    priority,
    video_file,
    v_date,
    SUM(alto) AS total_altos
FROM camera_data
GROUP BY
    camera_id,
    location,
    priority,
    video_file,
    v_date
ORDER BY total_altos DESC;

CREATE TABLE IF NOT EXISTS pequenos_per_camera AS
SELECT
    camera_id,
    location,
    priority,
    video_file,
    v_date,
    SUM(pequeno) AS total_pequenos
FROM camera_data
GROUP BY
    camera_id,
    location,
    priority,
    video_file,
    v_date
ORDER BY total_pequenos DESC;

CREATE TABLE IF NOT EXISTS blueshoes_per_camera AS
SELECT
    camera_id,
    location,
    priority,
    video_file,
    v_date,
    SUM(blueshoes) AS total_blueshoes
FROM camera_data
GROUP BY
    camera_id,
    location,
    priority,
    video_file,
    v_date
ORDER BY total_blueshoes DESC;

CREATE TABLE IF NOT EXISTS redshoes_per_camera AS
SELECT
    camera_id,
    location,
    priority,
    video_file,
    v_date,
    SUM(redshoes) AS total_redshoes
FROM camera_data
GROUP BY
    camera_id,
    location,
    priority,
    video_file,
    v_date
ORDER BY total_redshoes DESC;

CREATE TABLE IF NOT EXISTS bluecars_per_camera AS
SELECT
    camera_id,
    location,
    priority,
    video_file,
    v_date,
    SUM(bluecar) AS total_bluecars
FROM camera_data
GROUP BY
    camera_id,
    location,
    priority,
    video_file,
    v_date
ORDER BY total_bluecars DESC;

CREATE TABLE IF NOT EXISTS blackshoes_per_camera AS
SELECT
    camera_id,
    location,
    priority,
    video_file,
    v_date,
    SUM(blackshoes) AS total_blackshoes
FROM camera_data
GROUP BY
    camera_id,
    location,
    priority,
    video_file,
    v_date
ORDER BY total_blackshoes DESC;

CREATE TABLE IF NOT EXISTS bluepants_per_camera AS
SELECT
    camera_id,
    location,
    priority,
    video_file,
    v_date,
    SUM(bluepants) AS total_bluepants
FROM camera_data
GROUP BY
    camera_id,
    location,
    priority,
    video_file,
    v_date
ORDER BY total_bluepants DESC;

CREATE TABLE IF NOT EXISTS redpants_per_camera AS
SELECT
    camera_id,
    location,
    priority,
    video_file,
    v_date,
    SUM(redpants) AS total_redpants
FROM camera_data
GROUP BY
    camera_id,
    location,
    priority,
    video_file,
    v_date
ORDER BY total_redpants DESC;

CREATE TABLE IF NOT EXISTS blackpants_per_camera AS
SELECT
    camera_id,
    location,
    priority,
    video_file,
    v_date,
    SUM(blackpants) AS total_blackpants
FROM camera_data
GROUP BY
    camera_id,
    location,
    priority,
    video_file,
    v_date
ORDER BY total_blackpants DESC;







SELECT * FROM redshirts_per_camera;

