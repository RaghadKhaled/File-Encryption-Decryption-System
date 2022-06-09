# File Cryptography with AES and RSA

---

This is a college project required for an Information security course during my BSc studies.<br>
It is done as teamwork with my colleagues.

---

## Table of content
* [Project overview](#project-overview)
* [Tools](#tools)
* [How to run](#how-to-run)

---

### Project overview

We design a secure file sharing application. That contains GUI application where a user has to log in with a username and password for sharing (to send a file or receive a file). Each user has a pair of a private and public keys. The sender use a symmetric key to encrypt the file using the AES algorithm, and the symmetric key was encrypted by using the RSA algorithm and the receiver's public key. For decryption, the receiver uses its own private key to decrypt the symmetric key using the RSA and then uses that symmetric key to decrypt the file using the AES. The project workflow is illustrated in the figure below.

![image](https://user-images.githubusercontent.com/68460588/172827806-66f5bd81-002e-4c9b-ab82-33ab9d2ff4a1.png)


---

### Tools

Libraries: 
- Bcrypt
- AES
- RSA
- Secrets
- Tkinter


Softwares: 

- PyCharm

---

### How to run
- Download all files of code and open it in the programming enviremoner.
- Run the ‘main’ file to work with the program using GUI. All details about the GUI are illustrated in the Report. 
