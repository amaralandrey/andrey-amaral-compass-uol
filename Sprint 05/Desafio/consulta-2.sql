SELECT 
	SUM(CASE WHEN categoria_de_manejo = 'Parque' AND uf = 'PA' THEN 1 ELSE 0 END) 			 
	AS total_parques_pa, 
	SUM(CASE WHEN categoria_de_manejo = 'Parque' AND uf = 'MA' THEN 1 ELSE 0 END) 
	AS total_parques_ma
FROM s3object;
