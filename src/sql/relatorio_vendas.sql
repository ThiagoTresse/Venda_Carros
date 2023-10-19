select vend.idvenda,
       vend.valorvenda,
       vend.datavenda,
       vend.idvendedor,
       vend.cliente,  
       vend.veiculo  
from venda vend
inner join clientes
on vend.cliente = c.cpfCliente
inner join veiculos
on vend.veiculo = veic.idCarro 
order by vend.idvenda