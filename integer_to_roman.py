def intToRoman(num: int) -> str:
	d = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
	s, q, m, n = '', num, 1, 5
	while q:
		q, r = divmod(q, 10)
		if 0 < r < 4: s = r*d[m]+s
		elif r == 4: s = d[m]+d[n]+s
		elif r == 5: s = d[n]+s
		elif 5 < r < 9: s = d[n]+(r-5)*d[m]+s
		elif r == 9: s = d[m]+d[m*10]+s
		m, n = 10*m, 10*n
	return s

print(intToRoman(2994))