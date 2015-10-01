from DiaryDatabase import DiaryDatabase

class DiaryDatabaseClient:
    """Class DiaryDatabaseClient
    """
    # Attributes:
    database = None  # (DiaryDatabase) 
    
    # Operations
    def iter_notes(self):
        """function iter_notes
        
        returns 
        """
        return None # should raise NotImplementedError()
    
    def list_by_date(self, year = None, month = None, day = None):
        """function list_by_date
        
        year: 
        month: 
        day: 
        
        returns 
        """
        return None # should raise NotImplementedError()
    
    def list_by_date_range(self, start, end):
        """function list_by_date_range
        
        start: 
        end: 
        
        returns 
        """
        return None # should raise NotImplementedError()
    
    def list_by_search_text(self, regexp = ''):
        """function list_by_search_text
        
        regexp: str
        
        returns 
        """
        return None # should raise NotImplementedError()
    
    def close(self):
        """function close
        
        returns 
        """
        return None # should raise NotImplementedError()
    

