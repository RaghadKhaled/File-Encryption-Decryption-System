import LoadKeys  # to return the receiver public key

from Crypto.Cipher import AES
import struct
import rsa


def decrypt_file_and_key(username, filename):

	# load keys then take the private key of the user to use it in RSA decryption
	pubKey, privKey = LoadKeys.load_keys(username)
	user_private_key = privKey

	# decrypt key
	rsa_key_decrypt(user_private_key, filename)

	# decrypt file and return the plaintext in the file
	decryptedMSG = aes_file_decrypt(filename)

	# return the decrypted plaintext to appear in the window.
	# decode() method to remove prefix 'b' from the plaintext
	return decryptedMSG.decode()


def rsa_key_decrypt(user_private_key, filename):
	"""
	:param user_private_key: it is used in RSA decryption
	:param filename: filename of the original text
	:return:
	"""

	# get the name of file that contain the encrypted key
	# it has same name of original text file, with add 'encryptedKey'
	encryptedkey_filename = filename + 'encryptedKey.txt'

	# open the file and read the encrypted key
	with open(encryptedkey_filename, 'rb') as inputfile:
		encryptedkey = inputfile.read()

	# decrypt the key using RSA
	decryptedkey = rsa.decrypt(encryptedkey, user_private_key)

	# name for new file that will contain a key after decrypted
	output_filename = filename + 'decryptedKey.txt'
	# write decrypted key into new file
	with open(output_filename, 'wb') as outputfile:
		outputfile.write(decryptedkey)


def aes_file_decrypt(filename, chunk_size=2048):
	"""
	:param filename: the file that will be decrypted
	:param chunk_size: to read message as chunk(block)
	:return:
	"""

	# open file and read decrypted key
	decryptedkey_filename = filename + 'decryptedKey.txt'
	with open(decryptedkey_filename, 'rb') as inputfile:
		Key = inputfile.read(16)

	# store the name for the new file, will contain a message after decrypted
	output_filename = filename + 'decrypted.txt'
	# name of the file that contain the encrypted message
	encryptedMSG_filename = filename + 'encrypted.txt'

	# open the file that contain the decrypted message, name the object file as inputfile
	with open(encryptedMSG_filename, 'rb') as inputfile:
		# create and open new file to save the decrypted message into it, name the object file as outputfile
		with open(output_filename, 'wb') as outputfile:

			# read file size(original plaintext size), it used to check if it has been padded or not
			filesize = struct.unpack('<Q', inputfile.read(struct.calcsize('<Q')))[0]
			# read the iv to used it in ASA cipher decryption
			iv = inputfile.read(16)

			# create the AES cipher
			aes = AES.new(Key, AES.MODE_CBC, iv)

			while True:
				# the AES required the data to be in chunks, each chunk is multiple of 16 bytes
				# read the message as chunks
				data = inputfile.read(chunk_size)
				n = len(data)
				if n == 0:
					break
				# decrypt the message using AES
				decryptedMSG = aes.decrypt(data)

			# write in file the decrypted message
			outputfile.write(decryptedMSG)

			# remove padding if any
			outputfile.truncate(filesize)

	# return the decrypted message to be written in the window
	return decryptedMSG


