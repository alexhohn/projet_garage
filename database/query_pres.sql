-- SQLite
--Requête pour afficher une liste de toutes les pièces
SELECT 
    piece.id_piece,
    piece.manufacturer_id,
    piece.name AS piece_name,
    piece.ean_number,
    piece.description AS piece_description,
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

--Requête pour afficher toutes les pièces de l'area 1
SELECT 
    piece.id_piece,
    piece.manufacturer_id,
    piece.name AS piece_name,
    piece.ean_number,
    piece.description AS piece_description,
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


--script d'insertion complète d'un article avec son emplacement
INSERT INTO article (piece_id, supplier_id, quantity_stock, last_purchase_date, last_sale_date, selling_price, picture_path)
VALUES 
(1, 1, 50, '2023-10-25', '2023-10-26', 19.99, 'path/to/new_picture.jpg');

-- Associer l'article à un emplacement de stockage
INSERT INTO article_area (article_id, area_id)
VALUES (LAST_INSERT_ROWID(), 1);  -- LAST_INSERT_ROWID() permet de selectionner l'id de la dernière ligne insérée

--Mettre à jour la quantité en stock d'un article : OK
UPDATE article
SET quantity_stock = 150
WHERE id_article = 1;

-- Obtenir la liste des articles dans une zone de stockage donnée : OK
SELECT a.id_article, a.piece_id, a.supplier_id, a.quantity_stock, a.last_purchase_date, a.last_sale_date, a.selling_price, a.picture_path
FROM article AS a
JOIN article_area AS aa ON a.id_article = aa.article_id
WHERE aa.area_id = 1;

-- Obtenir la liste des articles dans le stock avec leur quantité disponible : OK
SELECT id_article, piece_id, supplier_id, quantity_stock, last_purchase_date, last_sale_date, selling_price, picture_path
FROM article;

