password = 'a123456';
password1 = input('請輸入密碼 :')
i = 2;
while  password != password1:
	print('error!!!!!! 剩下', i, '次機會');
	i = i - 1;
	if i < 0:
		break;
	password1 = input('請輸入密碼 :');
if i >=0:
	print('Sucess');