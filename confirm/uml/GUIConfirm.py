from Confirm import Confirm

class GUIConfirm(Confirm):
    """Class GUIConfirm
    """
    # Attributes:
    __title = None  # (string) 
    __msg = None  # (string) 
    
    # Operations
    def confirm(self):
        """function confirm
        
        returns bool
        """
        return None # should raise NotImplementedError()
    
    def get_title(self):
        """function get_title
        
        returns string
        """
        return None # should raise NotImplementedError()
    
    def set_title(self, title):
        """function set_title
        
        title: string
        
        returns void
        """
        return None # should raise NotImplementedError()
    
    def get_msg(self):
        """function get_msg
        
        returns string
        """
        return None # should raise NotImplementedError()
    
    def set_msg(self, msg):
        """function set_msg
        
        msg: string
        
        returns void
        """
        return None # should raise NotImplementedError()
    

