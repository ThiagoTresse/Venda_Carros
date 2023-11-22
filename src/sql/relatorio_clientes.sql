select c.cpfCliente,
       c.idCliente,
       c.nome,
       c.email,
       c.telefone,
       c.endereco     
  from LABDATABASE.Cliente c
 order by c.nome