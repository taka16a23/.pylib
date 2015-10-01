class Shell :
	'''(NULL)'''
	def __init__(self) :
		pass
	def read (self) :
		# returns 
		pass
	def write (self, line) :
		# returns 
		pass
	def exit_status (self) :
		# returns 
		pass
class Script :
	'''(NULL)'''
	def __init__(self) :
		self.receiver = None # 
		pass
	def execute (self, shell) :
		# returns 
		pass
class Decrypt (Script) :
	'''(NULL)'''
	def __init__(self) :
		pass
	def execute (self, shell) :
		# returns 
		pass
class Reboot (Script) :
	'''(NULL)'''
	def __init__(self) :
		pass
	def execute (self, shell) :
		# returns 
		pass
class Update (Script) :
	'''(NULL)'''
	def __init__(self) :
		pass
	def execute (self, shell) :
		# returns 
		pass
class PexShell (Shell) :
	'''(NULL)'''
	def __init__(self) :
		self.shell = None # 
		pass
	def read (self) :
		# returns 
		pass
	def write (self, line) :
		# returns 
		pass
	def exit_status (self) :
		# returns 
		pass
class SSHShell (Shell) :
	'''(NULL)'''
	def __init__(self) :
		self.shell = None # 
		pass
	def read (self) :
		# returns 
		pass
	def write (self, line) :
		# returns 
		pass
	def exit_status (self) :
		# returns 
		pass
class Receiver :
	'''(NULL)'''
	def __init__(self) :
		pass
	def append (self, str) :
		# returns 
		pass
	def pop (self) :
		# returns 
		pass
class TCPDump (Script) :
	'''(NULL)'''
	def __init__(self) :
		pass
	def execute (self, shell) :
		# returns 
		pass
class WakeOnLan (Script) :
	'''(NULL)'''
	def __init__(self) :
		pass
	def execute (self, shell) :
		# returns 
		pass
