score=int(input('请输入一个0~100的整数：'))


if score>=90:
    grade='A'
elif score>=80:
    grade='B'
elif score>=70:
    grade='C'
elif score>=60:
    grade='D'
else:
    grade='F'
print('grade='+ grade)
