Encrypted Strings
==================
Credit to Jason Van Zanten for the original code this is based upon

The Bash and Python scripts included here contain functions that use 'openssl' to generate encrypted strings with unqiue hashes and passphrases required for decoding and the functions to use those values to decrypt the strings.

The most obvious use case is passing credentials from a JSS policy to a script running on the client.  This is usually done when some action using an API (either the JSS API or another API) is required.  The password for this service account can be encrypted using these functions to better protect it.

The encrypted string would be entered as a policy parameter.  The unique 'salt' and 'passphrase' values would be present in the script downloaded to the client.  This requires any party to have access to the script code as well as the policy in the JSS in order to decrypt the string.

Here are examples of these functions in both languages:

```bash
~$ GenerateEncryptedString "Captain Hammer"
Encrypted String: U2FsdGVkX18/iRQ6O7Hr+pouW8TAl0RcrUByBUzavuY=
Salt: 3f89143a3bb1ebfa | Passphrase: 67a61589eb6fb3874052333b

~$ DecryptString U2FsdGVkX18/iRQ6O7Hr+pouW8TAl0RcrUByBUzavuY= 3f89143a3bb1ebfa 67a61589eb6fb3874052333b
Captain Hammer
```

```python
>>> import subprocess

>>> GenerateEncryptedString("Doctor Horrible")
Encrypted String: U2FsdGVkX1/+1bcze4/E7R3wCfEru9qnHWG5da7p+bg=
Salt: fed5b7337b8fc4ed | Passphrase: bbf59ee05d84e8c8d5190b31

>>> DecryptString('U2FsdGVkX1/+1bcze4/E7R3wCfEru9qnHWG5da7p+bg=', 'fed5b7337b8fc4ed', 'bbf59ee05d84e8c8d5190b31')
'Doctor Horrible'
```
