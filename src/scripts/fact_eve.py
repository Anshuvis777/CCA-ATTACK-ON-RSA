import pickle
import sys, os
import random
import threading
import math
from string import ascii_letters, digits
from time import sleep

from factors import find_divisor
IS_NOT_INTERACTIVE = False

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from algorithm.rsa import RSA
from algorithm.utils import RSAUtils
from scripts.utils import CommunicationUtils

def generate_random_message(length_in_bits):
    message = ""
    while (len(message.encode("utf8")) * 8) < length_in_bits:
        message += str(random.choice(ascii_letters + digits))
    return message

def trick_victim_into_decrypting_chosen_chipertext(attacker, n, e, encrypted_block, r):
    chosen_ciphertext_block = (encrypted_block * pow(r, e, n)) % n
    attacker.send(str(chosen_ciphertext_block).encode("utf8"))
    chosen_chiphertext_block_decrypted = int(attacker.recv(CommunicationUtils.BUFFER_SIZE).decode("utf8"))
    return chosen_chiphertext_block_decrypted

def extract_original_block(n, inverse_of_random_factor, chosen_chiphertext_block_decrypted):
    original_block_decrypted_chars = (chosen_chiphertext_block_decrypted * inverse_of_random_factor) % n
    return original_block_decrypted_chars

def reorder_characters_into_original_format(message_length, encrypted_block_length, original_block_decrypted_chars):
    original_block_decrypted_str = ""
    num_processed_bits = 0
    while num_processed_bits < encrypted_block_length:
        character = chr(original_block_decrypted_chars & 0xFF)
        original_block_decrypted_chars = original_block_decrypted_chars >> 8
        original_block_decrypted_str = character + original_block_decrypted_str
        num_processed_bits += 8
        message_length -= 1
    return original_block_decrypted_str

def main():
    attacker = CommunicationUtils.create_server_socket(CommunicationUtils.HOST, CommunicationUtils.PORT1)
    if attacker:
        print('connected to Alice for manipulation')
    else:
        print('not connected from Alice')
        return

    attacker2, address = attacker.accept()
    n, e = CommunicationUtils.receive_public_key(attacker2)
    message_length = int(attacker2.recv(CommunicationUtils.BUFFER_SIZE).decode("utf8"))
    block_tuples = CommunicationUtils.receive_all_blocks_at_once(attacker2, message_length)
    print('choosen ciphertext', block_tuples)
    # print('now Eve will try to connect to Bob for manipulation')





    shared_file = "shared_rsa_params.pkl"
    with open(shared_file, "rb") as file:
            serialized_params = file.read()
        # Deserialize the received params
    received_params = pickle.loads(serialized_params)
    # Extract d, e, and n from received params
    e = received_params.e
    n = received_params.n
    print("Received e:", e)
    print("Received n:", n)



    p = find_divisor(n)
    q = n // p

    # Printing the found factors
    print("Factorization results:")
    print("p:", p)
    print("q:", q)

    # Calculate phi(n)
    phi = (p - 1) * (q - 1)

    # Calculate the decryption key (d)
    d = RSAUtils.get_inverse(e, phi)

    print("value of d is ")
    print(d)
    print("\n")
    decrypted_message = ""

    # Decrypt each block of ciphertext
    for block_tuple in block_tuples:
        encrypted_block = int(block_tuple.split("\t")[0])
        decrypted_block = RSA.decrypt_block(encrypted_block, d, n)
        decrypted_message += chr(decrypted_block)

    print("Decrypted message at attacker side:\n", decrypted_message, "\n")
    attacker2.send(str(0).encode("utf8"))
    attacker2.close()

if __name__ == "__main__":
    main()