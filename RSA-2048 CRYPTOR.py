from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

code = 'nooneknows'
key = RSA.generate(2048)
data = b'Hello World!'


def get_RSA_keys():
    #private_key
    encrypted_key = key.exportKey(
        passphrase = code,
        pkcs = 8,
        protection = "scryptAndAES128-CBC"
    )

    with open('my_private_rsa_key.bin', 'wb') as f:
        f.write(encrypted_key)

    #public_key
    with open('my_rsa_public.pem', 'wb') as f:
        f.write(key.publickey().exportKey())

    encypt_RSA(data)


def encypt_RSA(data):
    with open('encrypted_data.bin', 'wb') as out_file:
        recipient_key = RSA.import_key(
            open('my_rsa_public.pem').read()
        )

        session_key = get_random_bytes(16)

        cipher_rsa = PKCS1_OAEP.new(recipient_key)
        out_file.write(cipher_rsa.encrypt(session_key))

        cipher_aes = AES.new(session_key, AES.MODE_EAX)
        ciphertext, tag = cipher_aes.encrypt_and_digest(data)

        out_file.write(cipher_aes.nonce)
        out_file.write(tag)
        out_file.write(ciphertext)


def decrypt_RSA():
    with open('encrypted_data.bin', 'rb') as encrypted_data:
        private_key = RSA.import_key(
            open('my_private_rsa_key.bin').read(),
            passphrase = code
        )

        enc_session_key, nonce, tag, ciphertext = [
            encrypted_data.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1)
        ]

        cipher_rsa = PKCS1_OAEP.new(private_key)
        session_key = cipher_rsa.decrypt(enc_session_key)

        cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
        data = cipher_aes.decrypt_and_verify(ciphertext, tag)

    print(data)


def main():
    #get_RSA_keys()
    decrypt_RSA()


if __name__ == '__main__':
    main()
