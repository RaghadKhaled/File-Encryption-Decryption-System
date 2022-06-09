
import rsa


def generate_keys(username):
    # generate keys, the size of key in bit is 1024
    (pubKey, privKey) = rsa.newkeys(1024)

    # the path and name of file that will contain the public key
    directoryname1 = 'Users Keys/'+username + 'pubkey.pem'
    # create and open the file, write the public key on it
    # the 'PEM' file format often used to store cryptographic keys
    with open(directoryname1, 'wb') as f:
        f.write(pubKey.save_pkcs1('PEM'))

    # the path and name of file that will contain the private key
    directoryname2 = 'Users Keys/'+username + 'privkey.pem'
    # create and open the file, write the public key on it
    # the 'PEM' file format often used to store cryptographic keys
    with open(directoryname2, 'wb') as f:
        f.write(privKey.save_pkcs1('PEM'))
