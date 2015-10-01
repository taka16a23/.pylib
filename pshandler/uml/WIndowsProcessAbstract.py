from ProcessAbstract import ProcessAbstract

class WIndowsProcessAbstract(ProcessAbstract):
    """Abstract class WIndowsProcessAbstract
    """
    # Attributes:
    
    # Operations
    def get_num_handles(self):
        """function get_num_handles
        
        returns 
        """
        raise NotImplementedError()
    
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
    

