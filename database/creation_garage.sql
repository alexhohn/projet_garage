-- table supplier
CREATE TABLE IF NOT EXISTS supplier (
    id_supplier INT PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    adress TEXT,
    zip INT,
    country TEXT,
    name_resp TEXT,
    telephone INT,
    email TEXT,
    Unique (name)
);

-- table manufacturer
CREATE TABLE IF NOT EXISTS manufacturer (
    id_manufacturer INT PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    adress TEXT,
    zip INT,
    country TEXT
);

-- table area
CREATE TABLE IF NOT EXISTS area (
    id_area INT PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

-- table piece
CREATE TABLE IF NOT EXISTS piece (
    id_piece INT PRIMARY KEY AUTOINCREMENT,
    manufacturer_id INT,
    name TEXT NOT NULL,
    ean_number INT UNIQUE,
    description TEXT,
    unit_price DECIMAL(2, 10),
    FOREIGN KEY (manufacturer_id) REFERENCES manufacturer(id_manufacturer),
    UNIQUE (ean_number)
);

--table article
CREATE TABLE IF NOT EXISTS article (
    id_article INT PRIMARY KEY AUTOINCREMENT,
    piece_id INT,
    supplier_id INT,
    quantitiy_stock INT,
    last_purchase_date TEXT NOT NULL,
    last_sale_date TEXT NOT NULL,
    selling_price DECIMAL(2, 10),    
    picture_path TEXT,
    FOREIGN KEY (piece_id) REFERENCES piece(id_piece)
    FOREIGN KEY (supplier_id) REFERENCES suplier(id_supplier)
);

--table intermédiaire article_area
CREATE TABLE IF NOT EXISTS article_area (
    id_article_area INT PRIMARY KEY AUTOINCREMENT,
    article_id INT,
    area_id INT,
    FOREIGN KEY (article_id) REFERENCES article(id_article),
    FOREIGN KEY (area_id) REFERENCES area(id_area),
    UNIQUE (article_id, area_id)
    );

--table vehicule
CREATE TABLE IF NOT EXISTS vehicule (
    id_vehicule INT PRIMARY KEY AUTOINCREMENT,
    manufacturer_id INT,
    model TEXT NOT NULL,
    year INT NOT NULL,
    engine_type TEXT NOT NULL,
    FOREIGN KEY (manufacturer_id) REFERENCES manufacturer(id_manufacturer)
    );

--table intermédiaire piece_vehicule
CREATE TABLE IF NOT EXISTS piece_vehicule (
    id_piece_vehicule INT PRIMARY KEY AUTOINCREMENT,
    piece_id INTEGER,
    vehicule_id INTEGER,
    FOREIGN KEY (piece_id) REFERENCES piece(id_piece),
    FOREIGN KEY (vehicule_id) REFERENCES vehicule(id_vehicule),
    UNIQUE (piece_id, vehicule_id)
    );

--Fin création des tables--