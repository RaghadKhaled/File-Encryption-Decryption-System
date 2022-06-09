import LoadKeys  # to return the receiver public key
import csv  # to open and write in csv file

from secrets import token_bytes  # to random 16 byte initialization vector(iv)
from Crypto.Cipher import AES  # to create AES cipher
import os  # to get file size
import struct  # to write file size in the file, we need this package
import rsa  # to create RSA cipher


def encrypt_file_and_key(receiver_name, filename):

	# load public key of receiver to use it in RSA encryption
	pubKeyReceiver, privKeyReceiver = LoadKeys.load_keys(receiver_name)
	receiver_public_key = pubKeyReceiver

	# write in cvs the receiver name and the file name will be send to it
	file = open('ReceiversMSG.csv', 'a+', newline='')
	csvwriter = csv.writer(file)

	new_receiver = [receiver_name, filename]
	csvwriter.writerow(new_receiver)
	file.close()

	# Generate random 16-Byte symmetric key
	Key = token_bytes(16)

	# encrypt file and return the cipher text in the file
	cipherMSG = aes_file_encrypt(Key, filename)

	# encrypt key
	rsa_key_encrypt(receiver_public_key, Key, filename)

	# return the cipher text to be appeared in the window
	return str(cipherMSG)


def aes_file_encrypt(key, filename, chunk_size=2048):
	"""
	:param key: the symmetric key
	:param filename: the file that will be encrypted
	:param chunk_size: to read message as chunk(block)
	:return: encrypted content(message) in the file
	"""

	# store the name for the new file, will contain a message after encrypted
	output_filename = filename + 'encrypted.txt'

	# store the file size (original message size before benign encrypted)
	# it used in the decryption to see if the message have been padded or not in the encryption.
	filesize = os.path.getsize(filename+'.txt')

	# generate the iv
	iv = token_bytes(16)
	# create the AES cipher
	aes = AES.new(key, AES.MODE_CBC, iv)

	# open the file that contain message, name the object file as inputfile
	with open(filename+'.txt', 'rb') as inputfile:
		# create and open new file to save the encrypted message into it, name the object file as outputfile
		with open(output_filename, 'wb') as outputfile:

			# write file size into the output file, to used it at receiver side and check the size of original message then see if it has been padded or not
			outputfile.write(struct.pack('<Q', filesize))
			# write the iv into the outputfile, to used it at receiver side while decryption
			outputfile.write(iv)

			while True:
				# the AES required the data to be in chunks, each chunk is multiple of 16 bytes
				# read the message as chunks
				data = inputfile.read(chunk_size)
				n = len(data)
				if n == 0:
					break
				# do padding if we need
				# (if the last chunk of the message is less than multiple of 16 byte, it will be padded (add space to complete the chunk size)
				elif n % 16 != 0:
					data += ' ' * (16 - n % 16)  # <- padded with spaces

				# encrypt the message using AES
				encryptedMSG = aes.encrypt(data)
				# write the encrypted message to the new file
				outputfile.write(encryptedMSG)

	# return the encrypted message to be written in the window
	return encryptedMSG


def rsa_key_encrypt(receiver_public_key, key, filename):
	"""
	:param receiver_public_key: the public key of the receiver to used it in the RSA encryption
	:param key: the data(symmetric key) that will encrypted
	:param filename: the file name of the message that are encrypted by the AES.
	:return:
	"""

	# store the name for the new file, will contain a key after encrypted
	output_filename = filename + 'encryptedKey.txt'

	# encrypt the key using RSA
	encrypted_key= rsa.encrypt(key, receiver_public_key)

	# write the encrypted key to the new file
	with open(output_filename, 'wb') as outputfile:
		outputfile.write(encrypted_key)

