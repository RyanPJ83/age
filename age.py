wine = input('你有沒有喝過酒： ')
if wine != 'yes' and wine != 'no':
	print('請輸入yes or no')
	raise SystemExit
age = input('請輸入年齡： ')
age = int(age)
if wine == 'yes':
	if age >= 19:
		print('喝酒合法')
	elif age == 18:
		print('再忍一下')
	else:
		print('不合法偶')
elif wine == 'no':
	if age >= 18:
		print('可以學喝酒了')
	else:
		print('不要偷喝')