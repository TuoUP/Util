class Print(object):
	"""
	get the infomation of the var ,include the print path of the var and the
	function name of var
	reference:
	https://www.cnblogs.com/snow-backup/p/4152837.html
	"""
	def __init__(self,dir_name):
		#make dir
		import os
		import time
		import re
		self.path = '/home/tete/Desktop/Debug_info/'+str(dir_name) + re.sub('\s','_',time.asctime()[4:-5])+'/'
		try:
			os.mkdir(self.path)
		except:
			pass
	
	def add_var(self,**kwargs):#
		with open(self.path + '/var.txt','a') as f:
			import sys
			import os
			f.write('file_name:  ')
			f.write(sys.argv[0][sys.argv[0].rfind(os.sep)+1:])
			f.write('\n')
			f.write('func_name:   ')
			f.write(sys._getframe().f_back.f_code.co_name)
			f.write('\n')
			for key,value in kwargs.items():
				f.write('{}:{:3}'.format(key,value))
				f.write('\n'*2)
			
	
	def add_step(self,text):#
		with open(self.path + '/step.txt','a') as f:
			import os
			import sys
			f.write('file_name:  ')
			f.write(sys.argv[0][sys.argv[0].rfind(os.sep)+1:])
			f.write('\n')
			f.write('func_name:   ')
			f.write(sys._getframe().f_back.f_code.co_name)
			f.write('\n')
			f.write(text)
			f.write('\n'*2)
			
	def read_me(self,text):
		with open(self.path + '/read_me.txt','a') as f:
			f.write(text)
    
if __name__ == '__main__':    
    token = Print('token')
    token.add_var(a = 1,b = 2,c =3)#signed_transaction = sign_tx
    def func():
        token.add_step('step1')
    func()
    token.read_me('just a test')
    
    
