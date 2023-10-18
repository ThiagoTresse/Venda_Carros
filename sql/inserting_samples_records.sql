/*INSERE DADOS NA TABELA DE Veiculo*/
INSERT INTO LABDATABASE.Veiculo VALUES('2122', 'Palio', 'preto', '2015', '21315136446', 'manual', 'Fiat');
INSERT INTO LABDATABASE.Veiculo VALUES('2124', 'Corsa', 'cinza', '2008', '32664996565', 'manual', 'Chevrolet');
INSERT INTO LABDATABASE.Veiculo VALUES('2123', 'Siena', 'preto', '2009', '62646462586', 'manual', 'Fiat');
INSERT INTO LABDATABASE.Veiculo VALUES('2129', 'Polo', 'branco', '2007', '26564989623', 'manual', 'Volkswagen');
INSERT INTO LABDATABASE.Veiculo VALUES('2126', 'Fiesta', 'vermelho', '2015', '26264889632', 'automatico', 'Ford');

/*INSERE DADOS NA TABELA DE clientes*/
INSERT INTO LABDATABASE.clientes VALUES('01234567891', '12345', 'JOÃO GABRIEL', 'joaogabriel@gmail.com', '27999125465', 'rua amazonia, 38, centro');
INSERT INTO LABDATABASE.clientes VALUES('20123456789', 'JOÃO GUILHERME', 'joaoguilherme@gmail.com', '27999945236', 'rua tapajos, 765, centro');
INSERT INTO LABDATABASE.clientes VALUES('32012345678', 'JOÃO JOSÉ', 'joaojose@gmail.com', '27992365445', 'rua limeira, 56, centro');
INSERT INTO LABDATABASE.clientes VALUES('43201234567', 'JOSÉ ANTÔNIO', 'joseantonio@gmail.com', '27998745234', 'rua do teste, 123, testando');
INSERT INTO LABDATABASE.clientes VALUES('45698752365', 'MAURICIO ALMEIDA', 'mauricioalmeida@hotmail.com', '27999992549', 'av vitoria, 456, laranjeiras')

/*INSER DADOS NA TABELA DE vendas*/
INSERT INTO LABDATABASE.VendaVeiculo VALUES('1525', '25000', '12052021', '152234', '2124', '01234567891')
INSERT INTO LABDATABASE.VendaVeiculo VALUES('1526', '45000', '12062022', '152233', '2122', '20123456789')
INSERT INTO LABDATABASE.VendaVeiculo VALUES('1527', '47000', '25092022', '152235', '2126', '45698752365')
INSERT INTO LABDATABASE.VendaVeiculo VALUES('1528', '27000', '01022023', '152233', '2123', '32012345678')
INSERT INTO LABDATABASE.VendaVeiculo VALUES('1529', '24000', '05052023', '152235', '2129', '43201234567')

COMMIT;