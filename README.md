% Atividade Prática - Palestra de Cripto HSC

Essa atividade foi feita para vocês colocarem a mão na massa um pouco.
O tipo de criptografia implementado aqui é um tipo que vocês não viram ainda,
a criptografia por meio da operação XOR (XOR Cipher). É sugerido que vocês pesquisem como essa criptografia
funciona, antes de tudo, e vocês verão que ela é muito similar às que foram explicadas na palestra.

Primeiramente, para vocês se familiarizarem com a operação, façam uma função que
recebe duas strings em hexadecimal e retorna o XOR das duas, também em hexadecimal.
Para testar a corretude do seu programa, se ele receber as strings 
`1c0111001f010100061a024b53535009181c` e `686974207468652062756c6c277320657965`
de entrada, deve retornar `746865206b696420646f6e277420706c6179`. 

Agora, a parte legal.
Um pedaço de comunicação foi interceptado durante uma sessão de CTF que não fazia sentido para nenhum dos membros, eventualmente foi
descoberto que ele não fazia parte de nenhuma das challenges do evento. Depois de um pouco de análise notamos que a mensagem
é o resultado de uma mensagem comum que sofreu um XOR com uma letra do alfabeto. Descubra o que foi dito e por que utilizaram 
essa letra como chave de encriptação.
`bc1c4dac181fc4d924d4081e8e414d1d21f4d1c1884d1b2e81e4d81e19c24d215c3924d321e1ec1e4de201834ece281e524d1d21f4d1e43c14d04d844dc4d1d1f40841fc4d18191fc4d9c4d0435c4de2049c4d1d1f8b41f49c`
(Dica: realize a decodificação primeiro em formato hexadecimal e depois traduza para texto.)