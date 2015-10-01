from PosixProcessAbstract import PosixProcessAbstract

class LinuxProcessAbstract(PosixProcessAbstract):
    """Abstract class LinuxProcessAbstract
    """
    # Attributes:
    
    # Operations
    def get_ionice(self):
        """function get_ionice
        
        returns 
        """
        raise NotImplementedError()
    
    def set_ionice(self):
        """function set_ionice
        
        returns None
        """
        raise NotImplementedError()
    
    def io_counters(self):
        """function io_counters
        
        returns namedtuple
        """
        raise NotImplementedError()
    
    def rlimit(self):
        """function rlimit
        
        returns namedtuple
        """
        raise NotImplementedError()
    
    def get_cpu_affinity(self):
        """function get_cpu_affinity
        
        returns 
        """
        raise NotImplementedError()
    
    def set_cpu_affinity(self):
        """function set_cpu_affinity
        
        returns 
        """
        raise NotImplementedError()
    

