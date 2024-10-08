# CCA-ATTACK-ON-RSA
#CHOOSEN CIPHER TEXT ATTACK  ON RSA
Chosen Ciphertext Attack
I implemented a chosen ciphertext attack where the attacker can decrypt any message without learning the key regardless its size.

Scenario
A legitimate user "Bob" sends a message that is intercepted by an attacker "Eve"
Eve manipulates the message by multiplying it by a random number r raised to the power of e mod n (these are public values that are within the access of anybody including the attacker)
Now Eve can use this manipulated message as a chosen ciphertext and send it to Bob
Bob decrypts the message, but from Bob's perspective the message is corrupt (the multiplication that Eve performed has changed the message and made it unintelligible), let that Bob uses a protocol that returns back corrupt messages (without encrypting it again, as it's no use to encrypt a corrupt message) to the one who sent it (to request re-transmission for example)
Eve will calculate the inverse of r mod n using extended Euclidean algorithm and multiply the message returned from Bob with the inverse of r to retrieve the original message without the need of learning the key and regardless its size



**RSA attack/Chosen ciphertext attack :**

This is the basic demonstration of chosen ciphertext attack on RSA cryptosystem. Here, eve(attacker) manipulates the chosen ciphertext and get to know about the original message of the encrypted RSA system.


**features:**

1.pair of key generation(public, private), public key encryption, private key decryption

2.socket connection between different user(sender, receiver,attacker)

3.handling of corrupt message by receiver using set of protocols

4.decryption of corrupt message without using key(keyless decryption)

**Working mechanism :**

1.Alice encrypt original message M into ciphertext C and send C to communication channel

2.Eve catch the ciphertext C 

3.Eve generate random integer r and encrypt it to get r1 and multiply r1 with C to get C1

4.Eve send C1 to Bob and Bob decrypt it to get Message M1

5.Bob knows that message M1 is corrupted and sent it back to sender (Eve)

6.Eve calculate inverse of r and multiply it to message M1 to get original message M

![image](https://github.com/Braham1234/RSA-cryptosystem-Chosen-ciphertext-attack/assets/143471590/2260a2d9-b8e2-4532-b355-5bdcad59c579)


**Proof :**

![image](https://github.com/Braham1234/RSA-cryptosystem-Chosen-ciphertext-attack/assets/143471590/0a9d3f4e-6e26-404d-ba04-8233f9086f75)


**How to run :**

first run **bob.py** than **alice.py** and atlast **eve.py**

**command :**

bob.py : python bob.py

alice.py : python alice.py

eve.py : python eve.py

**Screenshots:**

Alice:

![image](https://github.com/Braham1234/RSA-cryptosystem-Chosen-ciphertext-attack/assets/143471590/6f39fb45-887c-4329-8963-cd36f58d7e0b)
![image](https://github.com/Braham1234/RSA-cryptosystem-Chosen-ciphertext-attack/assets/143471590/a6725fc6-e6ac-4ffa-b12f-c6b1dbead13f)


Bob:

![image](https://github.com/Braham1234/RSA-cryptosystem-Chosen-ciphertext-attack/assets/143471590/a05d06f3-f631-41c8-86d1-f0cb883a42c1)






