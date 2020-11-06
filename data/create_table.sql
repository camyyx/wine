Create Table winePred(id int, fixed_acidity double precision, volatile_acidity double precision, citric_acid double precision, residual_sugar double precision, chlorides double precision , free_sulfur_dioxide double precision, total_sulfur_dioxide double precision, density double precision, pH double precision, sulphates double precision, alcohol double precision, quality double precision, wine_type text);

COPY winePred
FROM '/docker-entrypoint-initdb.d/data.csv'
DELIMITER ',' CSV HEADER;