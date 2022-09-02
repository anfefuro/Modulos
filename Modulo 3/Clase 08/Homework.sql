
-- Instrucción SQL N° 1

INSERT INTO fact_inicial (IdFecha, Fecha, IdSucursal, IdProducto, IdProductoFecha, IdSucursalFecha, IdProductoSucursalFecha)
SELECT	c.IdFecha, 
		g.Fecha,
		g.IdSucursal, 
        NULL AS IdProducto, 
        NULL AS IdProductoFecha, 
        g.IdSucursal * 100000000 + c.IdFecha IdSucursalFecha,
        NULL AS IdProductoSucursalFecha
FROM 	gasto g JOIN calendario c
	ON (g.Fecha = c.fecha)
WHERE g.IdSucursal * 100000000 + c.IdFecha NOT IN (	SELECT	v.IdSucursal * 100000000 + c.IdFecha 
													FROM venta v JOIN calendario c ON (v.Fecha = c.fecha)
													WHERE v.Outlier = 1);
-- Instrucción SQL N° 2

INSERT INTO fact_inicial (IdFecha, Fecha, IdSucursal, IdProducto, IdProductoFecha, IdSucursalFecha, IdProductoSucursalFecha)
SELECT	c.IdFecha, 
		co.Fecha,
		NULL AS IdSucursal, 
        co.IdProducto, 
        co.IdProducto * 100000000 + c.IdFecha AS  IdProductoFecha, 
        NULL IdSucursalFecha,
        NULL AS IdProductoSucursalFecha
FROM 	compra co JOIN calendario c
	ON (co.Fecha = c.fecha)
WHERE co.IdProducto * 100000000 + c.IdFecha NOT IN (SELECT	v.IdProducto * 100000000 + c.IdFecha 
													FROM venta v JOIN calendario c ON (v.Fecha = c.fecha)
													WHERE v.Outlier = 1);

-- Instrucción SQL N° 3

SELECT 	co.TipoProducto,
		co.PromedioVentaConOutliers,
        so.PromedioVentaSinOutliers
FROM
	(	SELECT 	tp.TipoProducto, AVG(v.Precio * v.Cantidad) as PromedioVentaConOutliers
		FROM 	venta v 
		JOIN producto p
		ON (v.IdProducto = p.IdProducto)
		JOIN tipo_producto tp
		ON (p.IdTipoProducto = tp.IdTipoProducto)
		GROUP BY tp.TipoProducto
	) co
JOIN
	(	SELECT 	tp.TipoProducto, AVG(v.Precio * v.Cantidad) as PromedioVentaSinOutliers
		FROM 	venta v 
		JOIN producto p
		ON (v.IdProducto = p.IdProducto and v.Outlier = 1)
		JOIN tipo_producto tp
		ON (p.IdTipoProducto = tp.IdTipoProducto)
		GROUP BY tp.TipoProducto
	) so
ON co.TipoProducto = so.TipoProducto;


CREATE VIEW kpi AS
SELECT 	co.TipoProducto,
		co.PromedioVentaConOutliers,
        so.PromedioVentaSinOutliers
FROM
	(	SELECT 	tp.TipoProducto, AVG(v.Precio * v.Cantidad) as PromedioVentaConOutliers
		FROM 	venta v 
		JOIN producto p
		ON (v.IdProducto = p.IdProducto)
		JOIN tipo_producto tp
		ON (p.IdTipoProducto = tp.IdTipoProducto)
		GROUP BY tp.TipoProducto
	) co
JOIN
	(	SELECT 	tp.TipoProducto, AVG(v.Precio * v.Cantidad) as PromedioVentaSinOutliers
		FROM 	venta v 
		JOIN producto p
		ON (v.IdProducto = p.IdProducto and v.Outlier = 1)
		JOIN tipo_producto tp
		ON (p.IdTipoProducto = tp.IdTipoProducto)
		GROUP BY tp.TipoProducto
	) so
ON co.TipoProducto = so.TipoProducto;


SELECT Precio * Cantidad AS [Total Ventas], 
FROM fact_venta
LEFT JOIN dim_prodcuto
ON fact_venta.IdProducto = dim_prodcuto.IdProducto
WHERE Fecha = (	SELECT MAX(Fecha)
				FROM fact_venta )

SELECT Precio * Cantidad AS [Total Ventas]
FROM fact_venta
LEFT JOIN dim_prodcuto
ON fact_venta.IdProducto = dim_prodcuto.IdProducto
WHERE Fecha = (	SELECT MIN(Fecha)
				FROM fact_venta )


SELECT fact_venta.IdProducto, Producto, Precio * Cantidad AS [Total Ventas]
FROM fact_venta
LEFT JOIN dim_prodcuto
ON fact_venta.IdProducto = dim_prodcuto.IdProducto
WHERE Fecha = (	SELECT MAX(Fecha)
				FROM fact_venta )
GROUP BY fact_venta.IdProducto, Producto

SELECT fact_venta.IdProducto, Producto, Precio * Cantidad AS [Total Ventas]
FROM fact_venta
LEFT JOIN dim_prodcuto
ON fact_venta.IdProducto = dim_prodcuto.IdProducto
WHERE Fecha = (	SELECT MIN(Fecha)
				FROM fact_venta )
GROUP BY fact_venta.IdProducto, Producto

SELECT Fecha, Precio * Cantidad AS [Total Ventas]
FROM fact_venta
GROUP BY Fecha

SELECT Fecha, MAX([Total Ventas])
FROM (	SELECT Fecha, Precio * Cantidad AS [Total Ventas]
		FROM fact_venta
		GROUP BY Fecha) AS ventas
GROUP BY Fecha