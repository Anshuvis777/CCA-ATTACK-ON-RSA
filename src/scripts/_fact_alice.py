# client.py
import pickle
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
IS_NOT_INTERACTIVE = False

def main():
    client_socket = CommunicationUtils.create_client_socket(CommunicationUtils.HOST,CommunicationUtils.PORT1)
    if client_socket:
        print('connected to Alice for manipulation')
    else:
        print('not connected from Alice')
        return
    shared_file = "shared_rsa_params.pkl"
    rsa = RSA()
    rsa.generate_key(IS_NOT_INTERACTIVE)
    print(rsa.params.d)
    print(rsa.params.e)
    
    # Serialize the rsa.params object
    serialized_params = pickle.dumps(rsa.params)
    
    # Check if the shared file exists
    if not os.path.exists(shared_file):
        print("Shared file does not exist. Creating a new file.")
    
    # Write the serialized params to the shared file (overwriting any existing content)
    with open(shared_file, "wb") as file:
        file.write(serialized_params)
    
    
    client_socket2 = CommunicationUtils.create_client_socket(CommunicationUtils.HOST,CommunicationUtils.PORT2)
    if client_socket2:
        print('connected to Alice for manipulation')
    else:
        print('not connected from Alice')
        return


    
    CommunicationUtils.send_public_key(client_socket, rsa)
    # original_message = generate_random_message((rsa.key_length - 8) * random.choice(range(1, 11)))
    original_message = input("Please enter your message: ")
    print("Original message at alice is sending to bob user side:\n", original_message, "\n")
    CommunicationUtils.send_encrypted_messages(client_socket, rsa.params.e, rsa.params.n, rsa.key_length, original_message)
    CommunicationUtils.send_encrypted_messages(client_socket2, rsa.params.e, rsa.params.n, rsa.key_length, original_message)

    


if __name__ == "__main__":
    main()