import sys
import os.path
import crypt

import passcrack


if __name__ == "__main__":
	if len(sys.argv) < 2:
	   sys.exit("Error: Invalid Args.")

	shadow_file = "/etc/shadow"
	dict_file = "./words.txt"

	# GET REQUIRED ARGUMENTS
	user = sys.argv[1]

	# OPEN SHADOW FILE AND GET HASHED PASSWORD
	hash = passcrack.getHash(user, shadow_file)

	# CRACK THE PASSWORD
	passcrack.passCracker(hash, dict_file)

