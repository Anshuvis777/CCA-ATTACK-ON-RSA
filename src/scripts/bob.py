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
    rsa = RSA()
    # Generate RSA keys

    connection, address = bob_socket.accept()
    if connection:
        print(f"Connection established with Eve {address}")
        shared_file = "shared_rsa_params.pkl"
        with open(shared_file, "rb") as file:
                serialized_params = file.read()
            # Deserialize the received params
        received_params = pickle.loads(serialized_params)
        # Extract d, e, and n from received params
        d = received_params.d
        e = received_params.e
        n = received_params.n
        print("Received d:", d)
        print("Received e:", e)
        print("Received n:", n)
        CommunicationUtils.resend_back_corrupt_messages(rsa, connection,d,n)
    else:
        print("No connection accepted.")

if __name__ == "__main__":
    main()