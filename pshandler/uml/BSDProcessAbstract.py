from PosixProcessAbstract import PosixProcessAbstract

class BSDProcessAbstract(PosixProcessAbstract):
    """Abstract class BSDProcessAbstract
    """
    # Attributes:
    
    # Operations
    def io_counters(self):
        """function io_counters
        
        returns named_tuple
        """
        raise NotImplementedError()
    

