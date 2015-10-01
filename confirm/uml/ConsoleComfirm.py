from Confirm import Confirm

class ConsoleComfirm(Confirm):
    """Class ConsoleComfirm
    """
    # Attributes:
    __prompt = None  # (string) 
    
    # Operations
    def confirm(self):
        """function confirm
        
        returns bool
        """
        return None # should raise NotImplementedError()
    
    def get_prompt(self):
        """function get_prompt
        
        returns string
        """
        return None # should raise NotImplementedError()
    
    def set_prompt(self, prompt):
        """function set_prompt
        
        prompt: string
        
        returns void
        """
        return None # should raise NotImplementedError()
    
    def __input(self):
        """function input
        
        returns string
        """
        return None # should raise NotImplementedError()
    

