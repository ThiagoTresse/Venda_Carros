SELECT
    vend.idvenda,
    vend.valorvenda,
    vend.datavenda,
    vend.idvendedor,
    c.cpfcliente,
    veic.idcarro
FROM
    LABDATABASE.VendaVeiculo vend
INNER JOIN
    LABDATABASE.Cliente c ON vend.cpfCliente = c.cpfCliente
INNER JOIN
    LABDATABASE.Veiculo veic ON vend.idCarro = veic.idCarro 
ORDER BY
    vend.idvenda