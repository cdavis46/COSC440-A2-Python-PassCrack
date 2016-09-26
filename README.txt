#### RUNNING THE PROGRAM ####

# You MUST have root access (sudo) in order to run this program!
# Once you have the files from GitHub...

# cd to dir with files
# create user "testuser" with password as a word from "words.txt"
sudo useradd testuser
sudo passwd testuser

# run "pwcracker.py" using python on testuser
sudo python pwcracker.py testuser

# It may take some time (30 seconds or so)
# If successful, you will see the password you created for testuser displayed to the terminal
