from utils import unzip_with_7z

zip_file_path = 'congrats.7z' # keep as is
dest_path = '.' # keep as is

find_me = '' # 2 letters are missing!
secret_password = find_me + 'bcmpda'

# WRITE YOUR CODE BELOW
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for letter in alphabet:
  success = False
  for letter2 in alphabet:
    find_me = letter + letter2
    secret_password = find_me + 'bcmpda'
    if unzip_with_7z(zip_file_path, dest_path, secret_password):
      success = True
      break
  if success:
    break
