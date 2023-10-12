--supprmier les tables 
DROP TABLE IF EXISTS article_area;
DROP TABLE IF EXISTS article;
DROP TABLE IF EXISTS piece_vehicule;
DROP TABLE IF EXISTS vehicule;
DROP TABLE IF EXISTS piece;
DROP TABLE IF EXISTS area;
DROP TABLE IF EXISTS supplier;
DROP TABLE IF EXISTS manufacturer;

-- table supplier
CREATE TABLE IF NOT EXISTS supplier (
    id_supplier INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    adress TEXT,
    zip INTEGER,
    country TEXT NOT NULL,
    name_resp TEXT NOT NULL,
    telephone TEXT NOT NULL,
    email TEXT,
    Unique (name)
);

-- table manufacturer
CREATE TABLE IF NOT EXISTS manufacturer (
    id_manufacturer INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    adress TEXT,
    zip INTEGER,
    country TEXT  NOT NULL
);

-- table area
CREATE TABLE IF NOT EXISTS area (
    id_area INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

-- table piece
CREATE TABLE IF NOT EXISTS piece (
    id_piece INTEGER PRIMARY KEY AUTOINCREMENT,
    manufacturer_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    ean_number TEXT NOT NULL,
    description TEXT NOT NULL,
    unit_price DECIMAL(2, 10) NOT NULL DEFAULT 0,
    FOREIGN KEY (manufacturer_id) REFERENCES manufacturer(id_manufacturer) NOT NULL,
    UNIQUE (ean_number)
);

--table article
CREATE TABLE IF NOT EXISTS article (
    id_article INTEGER PRIMARY KEY AUTOINCREMENT,
    piece_id INTEGER NOT NULL,
    supplier_id INTEGER NOT NULL,
    quantity_stock INTEGER NOT NULL,
    last_purchase_date TEXT NOT NULL,
    last_sale_date TEXT,
    selling_price DECIMAL(2, 10),    
    picture_path TEXT NOT NULL,
    FOREIGN KEY (piece_id) REFERENCES piece(id_piece)
    FOREIGN KEY (supplier_id) REFERENCES supplier(id_supplier)
);

--table intermédiaire article_area
CREATE TABLE IF NOT EXISTS article_area (
    id_article_area INTEGER PRIMARY KEY AUTOINCREMENT,
    article_id INTEGER NOT NULL,
    area_id INTEGER NOT NULL,
    FOREIGN KEY (article_id) REFERENCES article(id_article),
    FOREIGN KEY (area_id) REFERENCES area(id_area),
    UNIQUE (article_id, area_id)
    );

--table vehicule
CREATE TABLE IF NOT EXISTS vehicule (
    id_vehicule INTEGER PRIMARY KEY AUTOINCREMENT,
    manufacturer_id INTEGER NOT NULL,
    model TEXT NOT NULL,
    year INTEGER NOT NULL,
    engine_type TEXT NOT NULL,
    FOREIGN KEY (manufacturer_id) REFERENCES manufacturer(id_manufacturer)
    );

--table INTEGERermédiaire piece_vehicule
CREATE TABLE IF NOT EXISTS piece_vehicule (
    id_piece_vehicule INTEGER PRIMARY KEY AUTOINCREMENT,
    piece_id INTEGER NOT NULL,
    vehicule_id INTEGER NOT NULL,
    FOREIGN KEY (piece_id) REFERENCES piece(id_piece),
    FOREIGN KEY (vehicule_id) REFERENCES vehicule(id_vehicule),
    UNIQUE (piece_id, vehicule_id)
    );

--Fin création des tables--

-- Insertion dans la table supplier
INSERT INTO supplier (name, adress, zip, country, name_resp, telephone, email)
VALUES 
    ('Supplier 1', 'Address 1', 12345, 'Country 1', 'Manager 1', 123456789, 'email1@example.com'),
    ('Supplier 2', 'Address 2', 23456, 'Country 2', 'Manager 2', 234567890, 'email2@example.com'),
    ('Supplier 3', 'Address 3', 34567, 'Country 3', 'Manager 3', 345678901, 'email3@example.com');

-- Insertion dans la table manufacturer
INSERT INTO manufacturer (name, adress, zip, country)
VALUES 
    ('Manufacturer 1', 'Manufacturer Address 1', 54321, 'Manufacturer Country 1'),
    ('Manufacturer 2', 'Manufacturer Address 2', 65432, 'Manufacturer Country 2'),
    ('Manufacturer 3', 'Manufacturer Address 3', 76543, 'Manufacturer Country 3');

-- Insertion dans la table area
INSERT INTO area (name)
VALUES 
    ('Area 1'),
    ('Area 2'),
    ('Area 3');

-- Insertion dans la table piece (6 pièces)
INSERT INTO piece (manufacturer_id, name, ean_number, description, unit_price)
VALUES 
    (1, 'Piece 1', 1234567890123, 'Description for Piece 1', 10.50),
    (1, 'Piece 2', 2345678901234, 'Description for Piece 2', 15.75),
    (1, 'Piece 3', 3456789012345, 'Description for Piece 3', 20.00),
    (2, 'Piece 4', 4567890123456, 'Description for Piece 4', 25.25),
    (2, 'Piece 5', 5678901234567, 'Description for Piece 5', 30.50),
    (3, 'Piece 6', 6789012345678, 'Description for Piece 6', 35.75);

-- Insertion dans la table article (8 articles)
INSERT INTO article (piece_id, supplier_id, quantity_stock, last_purchase_date, last_sale_date, selling_price, picture_path)
VALUES 
    (1, 1, 100, '2023-10-01', '2023-10-02', 12.50, 'path/to/picture1.jpg'),
    (2, 1, 150, '2023-10-03', '2023-10-04', 18.75, 'path/to/picture2.jpg'),
    (3, 1, 200, '2023-10-05', '2023-10-06', 22.00, 'path/to/picture3.jpg'),
    (4, 2, 250, '2023-10-07', '2023-10-08', 27.25, 'path/to/picture4.jpg'),
    (5, 2, 300, '2023-10-09', '2023-10-10', 30.50, 'path/to/picture5.jpg'),
    (6, 3, 350, '2023-10-11', '2023-10-12', 35.75, 'path/to/picture6.jpg'),
    (1, 3, 400, '2023-10-13', '2023-10-14', 40.00, 'path/to/picture7.jpg'),
    (2, 2, 450, '2023-10-15', '2023-10-16', 45.25, 'path/to/picture8.jpg');

-- Insertion dans la table article_area (8 articles)
INSERT INTO article_area (article_id, area_id)
VALUES 
    (1, 1),
    (2, 1),
    (3, 1),
    (4, 1),
    (5, 2),
    (6, 2),
    (7, 3),
    (8, 3);

-- Insertion dans la table vehicule (3 véhicules)
INSERT INTO vehicule (manufacturer_id, model, year, engine_type)
VALUES 
    (1, 'Car Model 1', 2023, 'Petrol'),
    (2, 'Car Model 2', 2023, 'Diesel'),
    (3, 'Car Model 3', 2023, 'Electric');

-- Insertion dans la table piece_vehicule (6 pièces)
INSERT INTO piece_vehicule (piece_id, vehicule_id)
VALUES 
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 2),
    (5, 3),
    (6, 3);