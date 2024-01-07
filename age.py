driving = input('請問您有無開過車？')
if driving != '有' and driving != '沒有':
	print('只能輸入有或沒有，你這不聽話的小調皮')
	raise SystemExit #觸發程式終止，或使用迴圈回到上一層
age = input('請問您的年齡？')
age = int(age)
if driving == '有':
	if age >= 18:
		print('您通過測驗了')
	else:
		print('奇怪 你怎麼會有開過車')
elif driving == '沒有':
	if age >= 18:
		print('您可以考駕照啦，快去')
	else:
		print('很好，再等等吧')
else:
	print('只能輸入有或沒有，你這不聽話的小調皮')