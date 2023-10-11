--Requête pour afficher une liste de toutes les pièces : OK
SELECT 
    piece.id_piece,
    piece.manufacturer_id,
    piece.name,
    piece.ean_number,
    piece.description,
    piece.unit_price,
    article.quantity_stock,
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


--Requête pour afficher toutes les pièces de l'area 1 :OK
SELECT 
    piece.id_piece,
    piece.manufacturer_id,
    piece.name AS piece_name,
    piece.ean_number,
    piece.description,
    piece.unit_price,
    article.quantity_stock,
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

--Mettre à jour la quantité en stock d'un article : OK
UPDATE article
SET quantity_stock = 150
WHERE id_article = 1;

-- Obtenir la liste des articles dans une zone de stockage donnée : OK
SELECT a.id_article, a.piece_id, a.supplier_id, a.quantity_stock, a.last_purchase_date, a.last_sale_date, a.selling_price, a.picture_path
FROM article AS a
JOIN article_area AS aa ON a.id_article = aa.article_id
WHERE aa.area_id = 1;

-- Obtenir la liste des articles par fournisseur : OK
SELECT a.id_article, a.piece_id, a.quantity_stock, a.last_purchase_date, a.last_sale_date, a.selling_price, a.picture_path
FROM article AS a
WHERE a.supplier_id = 1;

--Obtenir la liste des pièces par fabricant : OK
SELECT piece.name, manufacturer.name as manufacturer_name
FROM piece
JOIN manufacturer ON piece.manufacturer_id = manufacturer.id_manufacturer
WHERE manufacturer.id_manufacturer = 1;

--Obtenir la liste des pièces associées à un véhicule : OK
SELECT piece.name, vehicule.model as vehicule_model
FROM piece
JOIN piece_vehicule ON piece.id_piece = piece_vehicule.piece_id
JOIN vehicule ON piece_vehicule.vehicule_id = vehicule.id_vehicule
WHERE vehicule.id_vehicule = 2;

-- Obtenir la liste des articles dans le stock avec leur quantité disponible : OK
SELECT id_article, piece_id, supplier_id, quantity_stock, last_purchase_date, last_sale_date, selling_price, picture_path
FROM article;

--Obtenir la liste des zones de stockage avec le nombre d'articles qu'elles contiennent : OK
SELECT area.name, COUNT(article_area.article_id) as article_count
FROM area
LEFT JOIN article_area ON area.id_area = article_area.area_id
GROUP BY area.name;

--Obtenir la liste des fournisseurs et le total des articles qu'ils fournissent : OK
SELECT supplier.name, COUNT(article.id_article) as article_count
FROM supplier
LEFT JOIN article ON supplier.id_supplier = article.supplier_id
GROUP BY supplier.name;

--Obtenir la liste des véhicules dans la bd : OK
SELECT vehicule.model, vehicule.year, manufacturer.name as manufacturer_name
FROM vehicule
JOIN manufacturer ON vehicule.manufacturer_id = manufacturer.id_manufacturer;

--Obtenir la quantité totale d'une pièce spécifique en stock : OK
SELECT piece.name, SUM(article.quantity_stock) as total_quantity
FROM piece
JOIN article ON piece.id_piece = article.piece_id
WHERE piece.id_piece = 4;

 -- Obtenir la liste des articles dans une zone de stockage spécifique : OK
SELECT a.id_article, a.piece_id, a.supplier_id, a.quantity_stock, a.last_purchase_date, a.last_sale_date, a.selling_price, a.picture_path
FROM article AS a
JOIN article_area AS aa ON a.id_article = aa.article_id
WHERE aa.area_id = VotreZoneID;

--Obtenir la liste des pièces associées à un véhicule spécifique : OK
SELECT piece.name
FROM piece
JOIN piece_vehicule ON piece.id_piece = piece_vehicule.piece_id
JOIN vehicule ON piece_vehicule.vehicule_id = vehicule.id_vehicule
WHERE vehicule.id_vehicule = 1;

--script d'insertion complète d'un article avec son emplacement
INSERT INTO article (piece_id, supplier_id, quantity_stock, last_purchase_date, last_sale_date, selling_price, picture_path)
VALUES 
(1, 1, 50, '2023-10-25', '2023-10-26', 19.99, 'path/to/new_picture.jpg');

-- Associer l'article à un emplacement de stockage
INSERT INTO article_area (article_id, area_id)
VALUES (LAST_INSERT_ROWID(), 1);  -- LAST_INSERT_ROWID() permet de selectionner l'id de la dernière ligne insérée