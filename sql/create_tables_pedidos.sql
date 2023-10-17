/*Apaga os relacionamentos*/
ALTER TABLE LABDATABASE.Cliente DROP CONSTRAINT Cliente_FK;
ALTER TABLE LABDATABASE.Veiculo DROP CONSTRAINT Veiculo_FK;

/*Apaga as tabelas*/
DROP TABLE LABDATABASE.Cliente;
DROP TABLE LABDATABASE.Veiculo;
DROP TABLE LABDATABASE.VendaVeiculo;

/*Apaga as sequences*/
DROP SEQUENCE LABDATABASE.cpfCliente_SEQ;
DROP SEQUENCE LABDATABASE.idCarro_SEQ;
DROP SEQUENCE LABDATABASE.idVenda_SEQ;

/*Cria as tabelas*/
CREATE TABLE Cliente (
                cpfCliente VARCHAR(11) NOT NULL,
                idCliente NUMERIC NOT NULL,
                nome VARCHAR(50) NOT NULL,
                email VARCHAR(50) NOT NULL,
                telefone NUMERIC NOT NULL,
                endereco VARCHAR(255) NOT NULL,
                CONSTRAINT Cliente_pk PRIMARY KEY (cpfCliente)
);


CREATE TABLE Veiculo (
                idCarro NUMERIC NOT NULL,
                modelo VARCHAR(25) NOT NULL,
                cor VARCHAR(25) NOT NULL,
                anoCarro NUMERIC NOT NULL,
                chassiCarro NUMERIC NOT NULL,
                tipoCambio NUMERIC NOT NULL,
                fabricante VARCHAR(25) NOT NULL,
                CONSTRAINT Veiculo_pk PRIMARY KEY (idCarro)
);


CREATE TABLE VendaVeiculo (
                idVenda NUMERIC NOT NULL,
                valorVenda NUMERIC NOT NULL,
                dataVenda DATE NOT NULL,
                idVendedor NUMERIC NOT NULL,
                idCarro NUMERIC NOT NULL,
                cpfCliente VARCHAR(11) NOT NULL,
                CONSTRAINT VendaVeiculo_pk PRIMARY KEY (idVenda)
);


/*Cria as sequences*/
CREATE SEQUENCE LABDATABASE.cpfCliente_SEQ;
CREATE SEQUENCE LABDATABASE.idCarro_SEQ;
CREATE SEQUENCE LABDATABASE.idVenda_SEQ;

/*Cria os relacionamentos*/
ALTER TABLE VendaVeiculo ADD CONSTRAINT Cliente_VendaVeiculo_fk
FOREIGN KEY (cpfCliente)
REFERENCES LABDATABASE.Cliente (cpfCliente)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE VendaVeiculo ADD CONSTRAINT Veiculo_VendaVeiculo_fk
FOREIGN KEY (idCarro)
REFERENCES LABDATABASE.Veiculo (idCarro)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

/*Garante acesso total as tabelas*/
GRANT ALL ON LABDATABASE.Cliente TO LABDATABASE;
GRANT ALL ON LABDATABASE.Veiculo TO LABDATABASE;
GRANT ALL ON LABDATABASE.VendaVeiculo TO LABDATABASE;

ALTER USER LABDATABASE quota unlimited on USERS;