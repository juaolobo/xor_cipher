# Atividade Prática - Palestra de Cripto HSC

Essa atividade foi feita para vocês colocarem a mão na massa um pouco.
O tipo de criptografia implementado aqui é um tipo que vocês não viram ainda,
a criptografia por meio da operação XOR (XOR Cipher). É sugerido que vocês pesquisem como essa criptografia
funciona, antes de tudo, e vocês verão que ela é muito similar às que foram explicadas na palestra.

## Parte 1

Primeiramente, para vocês se familiarizarem com a operação, façam uma função que
recebe duas strings em hexadecimal e retorna o XOR das duas, também em hexadecimal.
Para testar a corretude do seu programa, se ele receber as strings 
`1c0111001f010100061a024b53535009181c` e `686974207468652062756c6c277320657965`
de entrada, deve retornar `746865206b696420646f6e277420706c6179`. 

## Parte 2
Agora, a parte legal.
Um pedaço de comunicação foi interceptado durante uma sessão de CTF que não fazia sentido para nenhum dos membros, eventualmente foi
descoberto que ele não fazia parte de nenhuma das challenges do evento. Depois de um pouco de análise notamos que a mensagem
é o resultado de uma mensagem comum que sofreu um XOR com uma letra do alfabeto. Descubra o que foi dito e por que utilizaram 
essa letra como chave de encriptação.
`0b0c010c4d0a0c01081f0c4d09024d0400081e080e414d1d021f4d1c18084d1b020e081e4d081e190c024d0201050c0309024d03021e1e0c1e4d0e02001803040e0c0e02081e524d1d021f4d1e04030c014d004d084d0c4d1d1f040008041f0c4d0108191f0c4d090c4d000403050c4d0e020004090c4d1d1f080b081f04090c`
(Dica : cada byte (letra) é representado por dois números hexadecimais)