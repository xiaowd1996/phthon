import retxt = '''我的电子邮件tom@gmail.com.
         将什么发送到jerry123@163.com或者3123432@qq.com.
         若遇特殊情况打电话给18212344567.'''
print(re.findall('[a-zA-Z0-9]+@[a-z0-9]+\.com|\d{11}',txt))
