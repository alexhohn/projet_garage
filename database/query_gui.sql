
--Requête pour afficher une liste de toutes les pièces
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


--Mettre à jour la quantité en stock d'un article :
UPDATE article
SET quantity_stock = 150
WHERE id_article = 1;

--Obtenir la liste des articles dans une zone de stockage donnée :
SELECT article.name, article.quantity_stock
FROM article
JOIN article_area ON article.id_article = article_area.article_id
WHERE article_area.area_id = 1;

--Obtenir la liste des articles par fournisseur :
SELECT article.name, supplier.name as supplier_name
FROM article
JOIN supplier ON article.supplier_id = supplier.id_supplier;

--Obtenir la liste des pièces par fabricant :
SELECT piece.name, manufacturer.name as manufacturer_name
FROM piece
JOIN manufacturer ON piece.manufacturer_id = manufacturer.id_manufacturer;

--Obtenir la liste des pièces associées à un véhicule :
SELECT piece.name, vehicule.model as vehicule_model
FROM piece
JOIN piece_vehicule ON piece.id_piece = piece_vehicule.piece_id
JOIN vehicule ON piece_vehicule.vehicule_id = vehicule.id_vehicule;

--Obtenir la liste des articles dans le stock avec leur quantité disponible :
SELECT article.name, article.quantity_stock
FROM article;

--Obtenir la liste des zones de stockage avec le nombre d'articles qu'elles contiennent :
SELECT area.name, COUNT(article_area.article_id) as article_count
FROM area
LEFT JOIN article_area ON area.id_area = article_area.area_id
GROUP BY area.name;

--Obtenir la liste des fournisseurs et le total des articles qu'ils fournissent :
SELECT supplier.name, COUNT(article.id_article) as article_count
FROM supplier
LEFT JOIN article ON supplier.id_supplier = article.supplier_id
GROUP BY supplier.name;

--Obtenir la liste des véhicules dans le stock :
SELECT vehicule.model, vehicule.year, manufacturer.name as manufacturer_name
FROM vehicule
JOIN manufacturer ON vehicule.manufacturer_id = manufacturer.id_manufacturer;

--Obtenir la quantité totale d'une pièce spécifique en stock :   
SELECT piece.name, SUM(article.quantity_stock) as total_quantity
FROM piece
JOIN article ON piece.id_piece = article.piece_id
WHERE piece.id_piece = 1;

--Obtenir la liste des articles dans une zone de stockage spécifique :
SELECT article.name, article.quantity_stock
FROM article
JOIN article_area ON article.id_article = article_area.article_id
WHERE article_area.area_id = 1;

--Obtenir la liste des pièces associées à un véhicule spécifique :
SELECT piece.name
FROM piece
JOIN piece_vehicule ON piece.id_piece = piece_vehicule.piece_id
JOIN vehicule ON piece_vehicule.vehicule_id = vehicule.id_vehicule
WHERE vehicule.id_vehicule = 1;