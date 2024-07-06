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
