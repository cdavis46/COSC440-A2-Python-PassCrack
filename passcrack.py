import sys
import os.path
import crypt

def getHash(user, shadow):
   shadowFile = open(shadow, 'r')
 
   for line in shadowFile:
      line = line.split(":")
      if line[0] == user:
         if line[1] == "*":
            sys.exit("Warning: User Does Not Have A Password.")
         else:
            return line[1]
   sys.exit("Warning: User Does Not Exist.")


def passCracker(hash, dict):
   d = open(dict, 'r')

   # GET HASH PROPERTIES
   enc = hash.split("$")
   c_type = enc[1]
   salt = enc[2]
   full_salt = '${}${}$'.format(c_type, salt)

   for pw in d:
      #print "pw = ", pw
      #print "hash = ", hash
      #print "cryptstuf = ", crypt.crypt(pw.strip(), full_salt)
      #print "======"
      if crypt.crypt(pw.strip(), full_salt) == hash:
         sys.exit("Complete! Recovered password is: " + pw)
   sys.exit("Warning: Password Not Found In Dictionary.")

