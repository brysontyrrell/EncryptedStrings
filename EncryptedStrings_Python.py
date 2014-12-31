#!/usr/bin/python2.7
# Python wrapper for 'openssl' to create an encrypted Base64 string for script parameters
# Additional layer of security when passing account credentials from the JSS to a client
import subprocess 

# Use GenerateEncryptedString() locally - DO NOT include in the script!
# The 'Encrypted String' will become a parameter for the script in the JSS
# The unique 'Salt' and 'Passphrase' values will be present in your script
def GenerateEncryptedString(inputString):
    '''Usage >>> GenerateEncryptedString("String")'''
    salt = subprocess.check_output(['/usr/bin/openssl', 'rand', '-hex', '8']).rstrip()
    passphrase = subprocess.check_output(['/usr/bin/openssl', 'rand', '-hex', '12']).rstrip()
    p = subprocess.Popen(['/usr/bin/openssl', 'enc', '-aes256', '-a', '-A', '-S', salt, '-k', passphrase], stdin = subprocess.PIPE, stdout = subprocess.PIPE)
    encrypted = p.communicate(inputString)[0]
    print("Encrypted String: %s" % encrypted)
    print("Salt: %s | Passphrase: %s" % (salt, passphrase))

# Include DecryptString() with your script to decrypt the password sent by the JSS
# The 'Salt' and 'Passphrase' values would be present in the script
def DecryptString(inputString, salt, passphrase):
    '''Usage: >>> DecryptString("Encrypted String", "Salt", "Passphrase")'''
    p = subprocess.Popen(['/usr/bin/openssl', 'enc', '-aes256', '-d', '-a', '-A', '-S', salt, '-k', passphrase], stdin = subprocess.PIPE, stdout = subprocess.PIPE)
    return p.communicate(inputString)[0]

# Alternative format for DecryptString function
def DecryptString(inputString):
    '''Usage: >>> DecryptString("Encrypted String")'''
    salt = ""
    passphrase = ""
    p = subprocess.Popen(['/usr/bin/openssl', 'enc', '-aes256', '-d', '-a', '-A', '-S', salt, '-k', passphrase], stdin = subprocess.PIPE, stdout = subprocess.PIPE)
    return p.communicate(inputString)[0]