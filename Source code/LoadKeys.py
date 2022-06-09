import rsa


def load_keys(username):

    # the path and name of file that contain the public key
    directoryname1 = 'Users Keys/'+username + 'pubkey.pem'
    # open file and read the public key
    with open(directoryname1, 'rb') as f:
        pubKey = rsa.PublicKey.load_pkcs1(f.read())

    # the path and name of file that contain the private key
    directoryname2 = 'Users Keys/'+username + 'privkey.pem'
    # open file and read the private key
    with open(directoryname2, 'rb') as f:
        privKey = rsa.PrivateKey.load_pkcs1(f.read())

    return pubKey, privKey
