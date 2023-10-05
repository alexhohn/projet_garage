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
    country TEXT,
    name_resp TEXT,
    telephone INTEGER,
    email TEXT,
    Unique (name)
);

-- table manufacturer
CREATE TABLE IF NOT EXISTS manufacturer (
    id_manufacturer INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    adress TEXT,
    zip INTEGER,
    country TEXT
);

-- table area
CREATE TABLE IF NOT EXISTS area (
    id_area INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

-- table piece
CREATE TABLE IF NOT EXISTS piece (
    id_piece INTEGER PRIMARY KEY AUTOINCREMENT,
    manufacturer_id INTEGER,
    name TEXT NOT NULL,
    ean_number INTEGER,
    description TEXT,
    unit_price DECIMAL(2, 10),
    FOREIGN KEY (manufacturer_id) REFERENCES manufacturer(id_manufacturer),
    UNIQUE (ean_number)
);

--table article
CREATE TABLE IF NOT EXISTS article (
    id_article INTEGER PRIMARY KEY AUTOINCREMENT,
    piece_id INTEGER,
    supplier_id INTEGER,
    quantitiy_stock INTEGER,
    last_purchase_date TEXT NOT NULL,
    last_sale_date TEXT NOT NULL,
    selling_price DECIMAL(2, 10),    
    picture_path TEXT,
    FOREIGN KEY (piece_id) REFERENCES piece(id_piece)
    FOREIGN KEY (supplier_id) REFERENCES supplier(id_supplier)
);

--table INTEGERermédiaire article_area
CREATE TABLE IF NOT EXISTS article_area (
    id_article_area INTEGER PRIMARY KEY AUTOINCREMENT,
    article_id INTEGER,
    area_id INTEGER,
    FOREIGN KEY (article_id) REFERENCES article(id_article),
    FOREIGN KEY (area_id) REFERENCES area(id_area),
    UNIQUE (article_id, area_id)
    );

--table vehicule
CREATE TABLE IF NOT EXISTS vehicule (
    id_vehicule INTEGER PRIMARY KEY AUTOINCREMENT,
    manufacturer_id INTEGER,
    model TEXT NOT NULL,
    year INTEGER NOT NULL,
    engine_type TEXT NOT NULL,
    FOREIGN KEY (manufacturer_id) REFERENCES manufacturer(id_manufacturer)
    );

--table INTEGERermédiaire piece_vehicule
CREATE TABLE IF NOT EXISTS piece_vehicule (
    id_piece_vehicule INTEGER PRIMARY KEY AUTOINCREMENT,
    piece_id INTEGER,
    vehicule_id INTEGER,
    FOREIGN KEY (piece_id) REFERENCES piece(id_piece),
    FOREIGN KEY (vehicule_id) REFERENCES vehicule(id_vehicule),
    UNIQUE (piece_id, vehicule_id)
    );

--Fin création des tables--

-- Insertion dans la table supplier
INSERT INTO supplier (name, adress, zip, country, name_resp, telephone, email)
VALUES ('Supplier 1', 'Address 1', 12345, 'Country 1', 'Manager 1', 123456789, 'email1@example.com');

-- Insertion dans la table manufacturer
INSERT INTO manufacturer (name, adress, zip, country)
VALUES ('Manufacturer 1', 'Manufacturer Address 1', 54321, 'Manufacturer Country 1');

-- Insertion dans la table area
INSERT INTO area (name)
VALUES ('Area 1');

-- Insertion dans la table piece (4 pièces)
INSERT INTO piece (manufacturer_id, name, ean_number, description, unit_price)
VALUES (1, 'Piece 1', 1234567890123, 'Description for Piece 1', 10.50),
       (1, 'Piece 2', 2345678901234, 'Description for Piece 2', 15.75),
       (1, 'Piece 3', 3456789012345, 'Description for Piece 3', 20.00),
       (1, 'Piece 4', 4567890123456, 'Description for Piece 4', 25.25);

-- Insertion dans la table article (5 articles)
INSERT INTO article (piece_id, supplier_id, quantitiy_stock, last_purchase_date, last_sale_date, selling_price, picture_path)
VALUES (1, 1, 100, '2023-10-01', '2023-10-02', 12.50, 'path/to/picture1.jpg'),
       (2, 1, 150, '2023-10-03', '2023-10-04', 18.75, 'path/to/picture2.jpg'),
       (3, 1, 200, '2023-10-05', '2023-10-06', 22.00, 'path/to/picture3.jpg'),
       (4, 1, 250, '2023-10-07', '2023-10-08', 27.25, 'path/to/picture4.jpg'),
       (1, 1, 300, '2023-10-09', '2023-10-10', 30.50, 'path/to/picture5.jpg');

-- Insertion dans la table article_area (5 articles)
INSERT INTO article_area (article_id, area_id)
VALUES (1, 1),
       (2, 1),
       (3, 1),
       (4, 1),
       (5, 1);

-- Insertion dans la table vehicule
INSERT INTO vehicule (manufacturer_id, model, year, engine_type)
VALUES (1, 'Car Model 1', 2023, 'Petrol');

-- Insertion dans la table piece_vehicule (4 pièces)
INSERT INTO piece_vehicule (piece_id, vehicule_id)
VALUES (1, 1),
       (2, 1),
       (3, 1),
       (4, 1);


--Requête pour afficher toutes les pièces
SELECT 
    piece.id_piece,
    piece.manufacturer_id,
    piece.name AS piece_name,
    piece.ean_number,
    piece.description,
    piece.unit_price,
    article.quantitiy_stock,
    article.last_purchase_date,
    article.last_sale_date,
    article.selling_price,
    article.picture_path,
    area.name AS area_name
FROM 
    piece
JOIN 
    article ON piece.id_piece = article.piece_id
JOIN 
    article_area ON article.id_article = article_area.article_id
JOIN 
    area ON article_area.area_id = area.id_area
ORDER BY piece.name;


--Requête pour afficher toutes les pièces de l'area 1
SELECT 
    piece.id_piece,
    piece.manufacturer_id,
    piece.name AS piece_name,
    piece.ean_number,
    piece.description,
    piece.unit_price,
    article.quantitiy_stock,
    article.last_purchase_date,
    article.last_sale_date,
    article.selling_price,
    article.picture_path
FROM 
    piece
JOIN 
    article ON piece.id_piece = article.piece_id
JOIN 
    article_area ON article.id_article = article_area.article_id
WHERE 
    article_area.area_id = 1;