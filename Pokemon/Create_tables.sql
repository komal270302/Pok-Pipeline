CREATE TABLE pokemon (
    id INT PRIMARY KEY,
    name NVARCHAR(50),
    height INT,
    weight INT,
    base_experience INT
);

CREATE TABLE type (
    id INT IDENTITY(1,1) PRIMARY KEY,
    name NVARCHAR(50) UNIQUE
);

CREATE TABLE pokemon_type (
    pokemon_id INT FOREIGN KEY REFERENCES pokemon(id),
    type_id INT FOREIGN KEY REFERENCES type(id)
);

CREATE TABLE ability (
    id INT IDENTITY(1,1) PRIMARY KEY,
    name NVARCHAR(50) UNIQUE
);

CREATE TABLE pokemon_ability (
    pokemon_id INT FOREIGN KEY REFERENCES pokemon(id),
    ability_id INT FOREIGN KEY REFERENCES ability(id)
);

CREATE TABLE pokemon_stats (
    pokemon_id INT FOREIGN KEY REFERENCES pokemon(id),
    stat_name NVARCHAR(50),
    stat_value INT,
    PRIMARY KEY (pokemon_id, stat_name)
);
