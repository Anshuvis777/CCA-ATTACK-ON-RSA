# server.py
import pickle
import sys, os, getopt
import sys, os
import random
import threading
import math
from string import ascii_letters, digits
from time import sleep

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from algorithm.rsa import RSA
from algorithm.utils import RSAUtils
from scripts.utils import CommunicationUtils

# def trick_victim_into_decrypting_chosen_chipertext(attacker, n, e, encrypted_block, r):
#     chosen_ciphertext_block = (encrypted_block * pow(r, e, n)) % n
#     attacker.send(str(chosen_ciphertext_block).encode("utf8"))
#     chosen_chiphertext_block_decrypted = int(attacker.recv(CommunicationUtils.BUFFER_SIZE).decode("utf8"))
#     return chosen_chiphertext_block_decrypted


# def trick_victim_into_decrypting_chosen_chipertext(attacker, n, e, encrypted_block, r):
#     chosen_ciphertext_block = (encrypted_block * pow(r, e, n)) % n
#     attacker.send(str(chosen_ciphertext_block).encode("utf8"))
#     chosen_ciphertext_response = attacker.recv(CommunicationUtils.BUFFER_SIZE).decode("utf8")
#     if chosen_ciphertext_response:  # Check if response is not empty
#         chosen_chiphertext_block_decrypted = int(chosen_ciphertext_response)
#         return chosen_chiphertext_block_decrypted
#     else:
#         print("Received empty response from the victim.")
#         return None  # Return None to indicate failure


# def extract_original_block(n, inverse_of_random_factor, chosen_chiphertext_block_decrypted):
#     original_block_decrypted_chars = (chosen_chiphertext_block_decrypted * inverse_of_random_factor) % n
#     return original_block_decrypted_chars

def main():
    bob_socket = CommunicationUtils.create_server_socket(CommunicationUtils.HOST, CommunicationUtils.PORT2)
    if bob_socket:
        print('Bob server socket created and listening')
    else:
        print('Failed to create Bob server socket')
        return

    try:
        connection, address = bob_socket.accept()
        if connection:
            print(f"Connection established with Alice: {address}")
            shared_file = "shared_rsa_params.pkl"
            with open(shared_file, "rb") as file:
                serialized_params = file.read()

            received_params = pickle.loads(serialized_params)
            d = received_params.d
            e = received_params.e
            n = received_params.n
            print("Received d:", d)
            print("Received e:", e)
            print("Received n:", n)

            message_length = int(connection.recv(CommunicationUtils.BUFFER_SIZE).decode("utf8"))
            block_tuples = CommunicationUtils.receive_all_blocks_at_once(connection, message_length)
            print('Chosen ciphertext:', block_tuples)

            decrypted_message = ""
            for block_tuple in block_tuples:
                encrypted_block = int(block_tuple.split("\t")[0])
                decrypted_block = RSA.decrypt_block(encrypted_block, d, n)
                decrypted_message += chr(decrypted_block)

            print("Decrypted message at Bob's side:\n", decrypted_message, "\n")
        else:
            print("No connection accepted.")
    except Exception as e:
        print("An error occurred:", e)
    finally:
        bob_socket.close()

if __name__ == "__main__":
    main()
