drop DATABASE dataP;
CREATE DATABASE IF NOT EXISTS dataP;
USE dataP;
CREATE TABLE products(
    idProducto INT(4)  NOT NULL AUTO_INCREMENT,
    categoria varchar(60) not null,
    idDescripcion INT(4) not null,
    CONSTRAINT pkides PRIMARY KEY(idProducto)
);

CREATE TABLE detallesProductos(
    idProducto INT(4) not null AUTO_INCREMENT,
    Nombre varchar(100) not null,
    costo varchar(8) not null,
    linkImagen varchar(200) not null,
    CONSTRAINT fkidProducto 
    FOREIGN KEY (idProducto) 
    REFERENCES products(idProducto)
    );
