def xor(string1, string2):

	buf3 = []

	for i in range(len(string1)):
		a = int(string1[i], 16)
		b = int(string2[i], 16)
		buf3.append(a^b)

	buf = ''
	for i in buf3:
		buf += str(hex(i)[2:])
	print(buf)
	return buf

''' parte de criptografia, realizamos o XOR com a representacao ascii da letra e transformamos em hexadecimal.
 o else no codigo serve para poder saber a separacao entre as letras, com ele cada letra e representada por 2 numeros
 hexadecimais
  '''
def xor_encrypt(string, letter):
	# x = 'fala galera do imesec, por que voces estao olhando nossas comunicacoes? por sinal m e a primeira letra da minha comida preferida'
	encoded = bytes.fromhex(string.encode().hex())
	y = ''
	for byte in encoded:
		if len(hex(byte^ord(letter))[2:]) > 1:
			y += hex(byte^ord(letter))[2:] 
		else :
			y += '0' + hex(byte^ord(letter))[2:]

	print(y)
	return y
''' começa a parte de descriptografia
 0b0c010c4d0a0c01081f0c4d09024d0400081e080e414d1d021f4d1c18084d1b020e081e4d081e190c024d0201050c0309024d03021e1e0c1e4d0e020018030
 40e0c0e02081e524d1d021f4d1e04030c014d004d084d0c4d1d1f040008041f0c4d0108191f0c4d090c4d000403050c4d0e020004090c4d1d1f080b041f04090c
 '''
def xor_decrypt(string, letter):
	message = ''
	for i in range(0, len(string), 2): 
		a = int(string[i:i+2], 16)^ord(letter)
		message += chr(a)
	print(message)
	return message



def main():
	x = 'fala galera do imesec, por que voces estao olhando nossas comunicacoes? por sinal m e a primeira letra da minha comida preferida'
	string1 = '1c0111001f010100061a024b53535009181c'
	string2 = '686974207468652062756c6c277320657965'
	# a em ascii = 97
	teste = xor(string1, string2) 
	xor_ = xor_encrypt(x, 'm')
	# msg = xor_decrypt(xor_, 'm')
	letters = 'abcdefghijhijklmnopqrstuv'
	for l in letters:
		xor_decrypt(xor_, 'l')

main()

