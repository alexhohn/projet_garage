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
    unit_price DECIMAL(2, 10) NOT NULL,
    FOREIGN KEY (manufacturer_id) REFERENCES manufacturer(id_manufacturer),
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
    FOREIGN KEY (piece_id) REFERENCES piece(id_piece),
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

--table intermédiaire piece_vehicule
CREATE TABLE IF NOT EXISTS piece_vehicule (
    id_piece_vehicule INTEGER PRIMARY KEY AUTOINCREMENT,
    piece_id INTEGER NOT NULL,
    vehicule_id INTEGER NOT NULL,
    FOREIGN KEY (piece_id) REFERENCES piece(id_piece),
    FOREIGN KEY (vehicule_id) REFERENCES vehicule(id_vehicule),
    UNIQUE (piece_id, vehicule_id)
    );

--Fin création des tables--

-- Insertion des fournisseurs--
INSERT INTO supplier (name, adress, zip, country, name_resp, telephone, email)
VALUES 
        ('AutoParts Ltd', '1234 Rue de l'Auto, Paris', 75001, 'France', 'Jean Dupont', '0123456789', 'contact@autopartsltd.com'),
        ('CarPieces Inc', '5678 Car Ave, Lyon', 69002, 'France', 'Marie Curie', '9876543210', 'info@carpiecesinc.com'),
        ('MotoTech GmbH', '123 Autobahn, Berlin', 10115, 'Germany', 'Max Mustermann', '0301234567', 'service@mototech.de');

-- Insertion des fabricants--

INSERT INTO manufacturer (name, adress, zip, country) 
VALUES
        ('Renault', '1 Avenue Renault, Boulogne-Billancourt', 92100, 'France'),
        ('Peugeot', '75 Avenue de la Grande Armée, Paris', 75116, 'France'),
        ('Volkswagen', 'Berliner Ring 2, Wolfsburg', 38440, 'Germany');

INSERT INTO area (name)
VALUES
    ('Zone de Stockage 1'),
    ('Zone de Stockage 2'),
    ('Zone de Vente 1'),
    ('Zone de Vente 2'),
    ('Zone de Réception');

INSERT INTO piece (manufacturer_id, name, ean_number, description, unit_price) 
VALUES
        (1, 'Filtre à huile', '1234567890123', 'Filtre à huile pour moteur diesel', 15.99),
        (1, 'Bougie d’allumage', '1234567890124', 'Bougie d’allumage standard', 5.20),
        (1, 'Disque de frein', '1234567890125', 'Disque de frein avant pour Clio', 45.99),
        (2, 'Plaquette de frein', '1234567890126', 'Plaquettes de frein arrière pour 308', 35.50),
        (1, 'Filtre à air', '1234567890127', 'Filtre à air haute performance', 25.30),
        (2, 'Amortisseur', '1234567890128', 'Amortisseur arrière', 60.20),
        (3, 'Batterie de voiture', '1234567890129', 'Batterie 12V 60Ah', 89.99),
        (3, 'Alternateur', '1234567890130', 'Alternateur pour moteur essence', 120.40),
        (1, 'Démarreur', '1234567890131', 'Démarreur électrique', 75.25),
        (2, 'Radiateur', '1234567890132', 'Radiateur moteur pour 308', 110.50),
        (1, 'Courroie de distribution', '1234567890133', 'Kit de courroie de distribution', 99.99),
        (3, 'Phare avant', '1234567890134', 'Phare LED avant', 130.00),
        (2, 'Rétroviseur extérieur', '1234567890135', 'Rétroviseur gauche électrique', 45.75),
        (3, 'Essuie-glace', '1234567890136', 'Balais d’essuie-glace avant', 20.10),
        (1, 'Pompe à eau', '1234567890137', 'Pompe à eau pour moteur diesel', 65.00),
        (2, 'Injecteur', '1234567890138', 'Injecteur diesel haute performance', 150.00),
        (3, 'Capteur d’oxygène', '1234567890139', 'Capteur d’oxygène pour échappement', 80.20),
        (1, 'Thermostat', '1234567890140', 'Thermostat moteur', 22.50),
        (2, 'Pompe à carburant', '1234567890141', 'Pompe à carburant électrique', 70.00),
        (3, 'Silencieux d’échappement', '1234567890142', 'Silencieux d’échappement universel', 95.00),
        (1, 'Filtre à carburant', '1234567890143', 'Filtre à carburant pour diesel', 18.50);


-- Insertion des véhicules
INSERT INTO vehicule (manufacturer_id, model, year, engine_type) 
VALUES
        (1, 'Clio', 2020, 'Diesel'),
        (2, '308', 2019, 'Essence'),
        (3, 'Golf', 2021, 'Hybride');
        (1, 'Megane', 2018, 'Essence'),
        (2, '5008', 2020, 'Diesel'),
        (3, 'Polo', 2021, 'Electrique'),
        (1, 'Scenic', 2019, 'Hybride'),
        (2, '208', 2022, 'Essence'),
        (3, 'Tiguan', 2018, 'Diesel'),
        (1, 'Talisman', 2021, 'Essence'),
        (2, '3008', 2020, 'Hybride'),
        (3, 'Passat', 2019, 'Electrique'),
        (1, 'Kadjar', 2022, 'Diesel'),
        (2, '508', 2018, 'Essence'),
        (3, 'Arteon', 2021, 'Hybride'),
        (1, 'Zoe', 2020, 'Electrique'),
        (2, 'Rifter', 2019, 'Diesel'),
        (3, 'Touareg', 2022, 'Essence'),
        (1, 'Captur', 2018, 'Hybride'),
        (2, 'Traveller', 2021, 'Diesel'),
        (3, 'Beetle', 2020, 'Essence');


-- Insertion des articles
INSERT INTO article (piece_id, supplier_id, quantity_stock, last_purchase_date, last_sale_date, selling_price, picture_path) 
VALUES
        (1, 1, 50, '2023-10-01', NULL, 19.99, '/path/to/image1.jpg'),
        (2, 2, 30, '2023-09-15', '2023-10-10', 7.50, '/path/to/image2.jpg'),
        (3, 1, 40, '2023-08-25', NULL, 49.99, '/path/to/image3.jpg'),
        (4, 2, 25, '2023-09-10', '2023-10-05', 37.50, '/path/to/image4.jpg'),
        (5, 3, 30, '2023-07-20', NULL, 27.99, '/path/to/image5.jpg'),
        (6, 1, 15, '2023-09-30', NULL, 61.20, '/path/to/image6.jpg'),
        (7, 3, 20, '2023-08-15', '2023-09-25', 92.99, '/path/to/image7.jpg'),
        (8, 2, 10, '2023-10-02', NULL, 125.40, '/path/to/image8.jpg'),
        (9, 1, 35, '2023-09-05', NULL, 78.25, '/path/to/image9.jpg'),
        (10, 2, 50, '2023-07-30', '2023-08-20', 115.50, '/path/to/image10.jpg'),
        (11, 3, 45, '2023-09-20', NULL, 105.99, '/path/to/image11.jpg'),
        (12, 1, 20, '2023-08-05', '2023-09-15', 135.00, '/path/to/image12.jpg'),
        (13, 2, 25, '2023-10-03', NULL, 48.75, '/path/to/image13.jpg'),
        (14, 3, 30, '2023-09-01', '2023-10-01', 23.10, '/path/to/image14.jpg'),
        (15, 1, 40, '2023-07-15', NULL, 68.00, '/path/to/image15.jpg'),
        (16, 2, 35, '2023-08-10', '2023-09-10', 155.00, '/path/to/image16.jpg'),
        (17, 3, 20, '2023-09-25', NULL, 85.20, '/path/to/image17.jpg'),
        (18, 1, 15, '2023-10-04', NULL, 26.50, '/path/to/image18.jpg'),
        (19, 2, 10, '2023-08-20', NULL, 73.00, '/path/to/image19.jpg'),
        (20, 3, 50, '2023-07-05', '2023-08-10', 98.00, '/path/to/image20.jpg');