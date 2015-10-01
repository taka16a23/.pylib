from ProcessAbstract import ProcessAbstract

class PosixProcessAbstract(ProcessAbstract):
    """Abstract class PosixProcessAbstract
    """
    # Attributes:
    
    # Operations
    def get_uids(self):
        """function get_uids
        
        returns namedtuple
        """
        raise NotImplementedError()
    
    def get_gids(self):
        """function get_gids
        
        returns namedtuple
        """
        raise NotImplementedError()
    
    def get_terminal(self):
        """function get_terminal
        
        returns str
        """
        raise NotImplementedError()
    
    def num_fds(self):
        """function num_fds
        
        returns int
        """
        raise NotImplementedError()
    

