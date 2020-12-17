def eval_expr(s,d={}):
	list=[]
	s=s.split()
	for i in s:
		if i=="+":
			A=list.pop()
			B=list.pop()
			C=A+B
			list.append(C)
		elif i=="-":
			A=list.pop()
			B=list.pop()
			C=B-A
			list.append(C)
		elif i=="*":
			A=list.pop()
			B=list.pop()
			C=A*B
			list.append(C)
		elif i=="/":
			A=list.pop()
			B=list.pop()
			C=B//A
			list.append(C)
		elif i.isalpha():
			list.append(d[i])
		else:
			i=int(i)
			list.append(i)
	return list.pop()

def to_infix(s):
	s=s.split()
	list=[]
	for i in s:
		if i=="+":
			A=list.pop()
			B=list.pop()
			list.append('( '+B+' '+i+' '+A+' )')
		elif i=="-":
			A=list.pop()
			B=list.pop()
			list.append('( '+B+' '+i+' '+A+' )')
		elif i=="*":
			A=list.pop()
			B=list.pop()
			list.append('( '+B+' '+i+' '+A+' )')
		elif i=="/":
			A=list.pop()
			B=list.pop()
			list.append('( '+B+' '+i+' '+A+' )')
		else:
			list.append(i)
	return list.pop()


def to_postfix(s):
	s=s.split()
	list1=[]
	list2=[]
	for i in s:
		if i=="(":
			continue
		if i==")":
			A=list1.pop()
			B=list1.pop()
			C=list2.pop()
			list1.append(B+' '+A+' '+C)
		elif i=="+" or i=="-" or i=="*" or i=="/":
			list2.append(i)
		else:
			list1.append(i)
	return list1.pop()
			
