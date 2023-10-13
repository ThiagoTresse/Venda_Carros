select c.cpfCliente,
       c.idCliente,
       c.nome,
       c.email,
       c.telefone,
       c.endereco     
  from clientes c
 order by c.nome