select veic.idCarro,
       veic.modelo,
       veic.cor,
       veic.anoCarro,
       veic.chassiCarro,
       veic.tipoCambio,
       veic.fabricante
  from veiculos veic
 order by veic.modelo