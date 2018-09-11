def main():

	# Get user choice
	user_input = input('Encrypt [1] : Decrypt [2] >> ')
	choice = int(user_input)

	# Handle user choice
	if choice == 1:
		encrypt()
	elif choice == 2:
		decrypt()
	else:
		print('Invalid input!')
		main()

def encrypt():

	# Get user input
	user_input = input('Enter the word to encrypt: ')
	decrypted = list(user_input)

	# Encrypted char list
	encrypted = [''] * len(decrypted)

	user_input = input('Enter a shift value: ')
	shift = int(user_input)

	# Iterate through list and convert each character into ASCII code
	for i in range(len(decrypted)):
		ascii_code = ord(decrypted[i])

		# Add shift to ascii value
		encrypted_ascii_code = ascii_code + shift

		# Convert to encrypted char list
		encrypted[i] = chr(encrypted_ascii_code)

	# Print result
	print("The encrypted word is:", ''.join(encrypted))

def decrypt():

	# Get user choice
	user_choice = input('Known key [1] : Unknown key [2] >> ')
	choice = int(user_choice)

	# Handle user choice
	if choice == 1:
		pass
	elif choice == 2:
		crack()
	else:
		print('Invalid input!')
		decrypt()

	# Get user input
	user_input = input('Enter the word to decrypt: ')
	encrypted = list(user_input)

	# Decrypted char list
	decrypted = [''] * len(encrypted)

	user_input = input('Enter a shift value: ')
	shift = int(user_input)

	# Iterate through list and convert each character into ASCII code
	for i in range(len(encrypted)):
		ascii_code = ord(encrypted[i])

		# Add shift to ascii value
		decrypted_ascii_code = ascii_code - shift

		# Convert to decrypted char list
		decrypted[i] = chr(decrypted_ascii_code)

	# Print result
	print("The decrypted word is:", ''.join(decrypted))

def crack():
	# Get user input
	user_input = input('Enter the word to decrypt: ')
	encrypted = list(user_input)

	# Decrypted char list
	decrypted = [''] * len(encrypted)

	for i in range(1, 26):
		# Iterate through list and convert each character into ASCII code
		for j in range(len(encrypted)):
			ascii_code = ord(encrypted[j])

			# Add shift to ascii value
			decrypted_ascii_code = ascii_code - i

			# Convert to decrypted char list
			decrypted[j] = chr(decrypted_ascii_code)

		print(''.join(decrypted), 'was decrypted with a key value of: ', i)

	print('Done!')
	exit()




if __name__ == '__main__':
	main()