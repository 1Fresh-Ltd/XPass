print("""\       
 _____ _             ____ ___ ____ 
 |_   _(_)_ __  _   _| __ )_ _/ ___|
   | | | | '_ \| | | |  _ \| | |  _ 
   | | | | | | | |_| | |_) | | |_| |
   |_| |_|_| |_|\__, |____/___\____|
                |___/               
""")
leakedpasswords = [
"123456",
"123456789",
"12345",
"qwerty",
"password",
"12345678",
"111111",
"123123",
"1234567890",
"1234567",
"qwerty123",
"000000",
"1q2w3e",
"aa12345678",
"abc123",
"password1",
"1234",
"qwertyuiop",
"123321",
"password123"
]
checkfor = input("Check your password for leaks:")
if checkfor in leakedpasswords: 
	print('Your password contains at our leaked/insequred passwords base!')
        print("Try to change your password for your own safety!")
        print("or just do nothing...")
else:
	print("Good news! Your password not contains in our base!")
