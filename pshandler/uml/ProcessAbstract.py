
class ProcessAbstract:
    """Abstract class ProcessAbstract
    """
    # Attributes:
    
    # Operations
    def get_pid(self):
        """function get_pid
        
        returns int
        """
        raise NotImplementedError()
    
    def get_parent(self):
        """function get_parent
        
        returns Process
        """
        raise NotImplementedError()
    
    def get_name(self):
        """function get_name
        
        returns str
        """
        raise NotImplementedError()
    
    def get_path(self):
        """function get_path
        
        returns str
        """
        raise NotImplementedError()
    
    def get_status(self):
        """function get_status
        
        returns str
        """
        raise NotImplementedError()
    
    def get_cmdline(self):
        """function get_cmdline
        
        returns str
        """
        raise NotImplementedError()
    
    def get_username(self):
        """function get_username
        
        returns str
        """
        raise NotImplementedError()
    
    def get_create_time(self):
        """function get_create_time
        
        returns float
        """
        raise NotImplementedError()
    
    def get_cwd(self):
        """function get_cwd
        
        returns str
        """
        raise NotImplementedError()
    
    def get_nice(self):
        """function get_nice
        
        returns int
        """
        raise NotImplementedError()
    
    def get_memory_info(self):
        """function get_memory_info
        
        returns namedtuple
        """
        raise NotImplementedError()
    
    def set_nice(self, value):
        """function set_nice
        
        value: int
        
        returns None
        """
        raise NotImplementedError()
    
    def suspend(self):
        """function suspend
        
        returns None
        """
        raise NotImplementedError()
    
    def resume(self):
        """function resume
        
        returns None
        """
        raise NotImplementedError()
    
    def terminate(self):
        """function terminate
        
        returns None
        """
        raise NotImplementedError()
    
    def kill(self):
        """function kill
        
        returns None
        """
        raise NotImplementedError()
    
    def is_running(self):
        """function is_running
        
        returns bool
        """
        raise NotImplementedError()
    
    def threads(self):
        """function threads
        
        returns list
        """
        raise NotImplementedError()
    
    def list_children(self):
        """function list_children
        
        returns list
        """
        raise NotImplementedError()
    
    def recursive_children(self):
        """function recursive_children
        
        returns list
        """
        raise NotImplementedError()
    
    def get_cpu_percent(self):
        """function get_cpu_percent
        
        returns float
        """
        raise NotImplementedError()
    
    def get_cpu_times(self):
        """function get_cpu_times
        
        returns named_tuple
        """
        raise NotImplementedError()
    
    def list_open_files(self):
        """function list_open_files
        
        returns list
        """
        raise NotImplementedError()
    
    def list_connection(self, king = 'inet'):
        """function list_connection
        
        king: str
        
        returns list
        """
        raise NotImplementedError()
    
    def send_signal(self, sig):
        """function send_signal
        
        sig: int
        
        returns None
        """
        raise NotImplementedError()
    
    def wait(self, timeout = None):
        """function wait
        
        timeout: int
        
        returns 
        """
        raise NotImplementedError()
    

