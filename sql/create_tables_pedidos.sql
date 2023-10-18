/*Apaga os relacionamentos*/
ALTER TABLE LABDATABASE.VendaVeiculo DROP CONSTRAINT Cliente_VendaVeiculo_fk;
ALTER TABLE LABDATABASE.VendaVeiculo DROP CONSTRAINT Veiculo_VendaVeiculo_fk;

/*Apaga as tabelas*/
DROP TABLE LABDATABASE.Cliente;
DROP TABLE LABDATABASE.Veiculo;
DROP TABLE LABDATABASE.VendaVeiculo;

/*Apaga as sequences*/
DROP SEQUENCE idCarro_SEQ;
DROP SEQUENCE idVenda_SEQ;

/*Cria as sequences*/
CREATE SEQUENCE idCarro_SEQ;
CREATE SEQUENCE idVenda_SEQ;

/*Cria as tabelas*/
CREATE TABLE LABDATABASE.Cliente (
                cpfCliente VARCHAR(15) NOT NULL,
                idCliente NUMERIC(10) NOT NULL,
                nome VARCHAR(60) NOT NULL,
                email VARCHAR(40) NOT NULL,
                telefone NUMERIC(15) NOT NULL,
                endereco VARCHAR(255) NOT NULL,
                CONSTRAINT Cliente_pk PRIMARY KEY (cpfCliente)
);


CREATE TABLE LABDATABASE.Veiculo (
                idCarro NUMERIC DEFAULT idCarro_SEQ.NEXTVAL NOT NULL,
                modelo VARCHAR(100) NOT NULL,
                cor VARCHAR(100) NOT NULL,
                anoCarro NUMERIC NOT NULL,
                chassiCarro VARCHAR(18) NOT NULL,
                tipoCambio VARCHAR(50) NOT NULL,
                fabricante VARCHAR(25) NOT NULL,
                CONSTRAINT Veiculo_pk PRIMARY KEY (idCarro)
);


CREATE TABLE LABDATABASE.VendaVeiculo (
                idVenda NUMERIC DEFAULT idVenda_SEQ.NEXTVAL NOT NULL,
                valorVenda NUMERIC NOT NULL,
                dataVenda DATE NOT NULL,
                idVendedor NUMERIC NOT NULL,
                idCarro NUMERIC NOT NULL,
                cpfCliente VARCHAR(15) NOT NULL,
                CONSTRAINT VendaVeiculo_pk PRIMARY KEY (idVenda)
);


/*Cria os relacionamentos*/
ALTER TABLE LABDATABASE.VendaVeiculo ADD CONSTRAINT Cliente_VendaVeiculo_fk
FOREIGN KEY (cpfCliente)
REFERENCES LABDATABASE.Cliente (cpfCliente);



ALTER TABLE LABDATABASE.VendaVeiculo ADD CONSTRAINT Veiculo_VendaVeiculo_fk
FOREIGN KEY (idCarro)
REFERENCES LABDATABASE.Veiculo (idCarro);


/*Garante acesso total as tabelas*/
GRANT ALL ON LABDATABASE.Cliente TO LABDATABASE;
GRANT ALL ON LABDATABASE.Veiculo TO LABDATABASE;
GRANT ALL ON LABDATABASE.VendaVeiculo TO LABDATABASE;

ALTER USER LABDATABASE quota unlimited on USERS;