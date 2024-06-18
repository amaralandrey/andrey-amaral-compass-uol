SELECT  
	nome_da_uc, 
	CAST(SUBSTRING(codigo_uc, 9) AS FLOAT) AS cod_uc_normalizado,
	SUBSTRING(categoria_iucn, 10) AS categoria_normalizada 
	FROM s3object 
WHERE categoria_de_manejo = 'Parque' AND (uf = 'PA' OR uf = 'MA')
