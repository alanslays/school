CREATE DATABASE IF NOT EXISTS mojabaza
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE mojabaza;

CREATE TABLE IF NOT EXISTS filmy (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tytul VARCHAR(255) NOT NULL,
    rezyser VARCHAR(255) NOT NULL,
    rok INT NOT NULL,
    ocena DECIMAL(3,1) NOT NULL
);

INSERT INTO filmy (tytul, rezyser, rok, ocena) VALUES
('Inception', 'Christopher Nolan', 2010, 8.8),
('The Matrix', 'Lana Wachowski, Lilly Wachowski', 1999, 8.7),
('Fight Club', 'David Fincher', 1999, 8.8);
