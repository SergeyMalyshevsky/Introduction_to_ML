def write_answer(number, text):
	dir = "./answers/"
	filename = dir + "answer_{}.txt".format(number)
	
	if isinstance(text, float):
	    line = "{:0.2f}".format(text)
	else:
		line = text
		
	
	with open(filename, 'w+') as f:
		f.write(str(line))
	
	print("Answer {}: ".format(number), text)