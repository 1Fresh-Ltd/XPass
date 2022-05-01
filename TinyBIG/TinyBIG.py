print("Welcome to TinyBIG")
leakedpasswords = ["123", "1234", "12345", "123456", "123098", "qwerty", "qwerty123", "password", "mnbvc", "lkjhg", "poiuy", "abcdefg"]
checkfor = input("Check your password for leaks:")
if checkfor in leakedpasswords: 
	print('Your password contains at our leaked passwords base!')
    print("Try to change your password for your own safety!")
    print("or just do nothing...")
else:
	print("Good news! Your password not contains in our base!")