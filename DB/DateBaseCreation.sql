CREATE DATABASE IF NOT EXISTS dataWeb;
USE dataWeb;
CREATE TABLE products(
    idProducto INT(4)  NOT NULL AUTO_INCREMENT,
    idCategoria INT(4) not null,
    idDescripcion INT(4) not null,
    CONSTRAINT pkid PRIMARY KEY(idProducto, idCategoria)
);

CREATE TABLE detallesProductos(
    idProducto INT(4) not null,
    Nombre varchar(30) not null,
    costo decimal(8,2) not null,
    CONSTRAINT pkidProducto 
    FOREIGN KEY (idProducto) 
    REFERENCES products(idProducto)
    );
