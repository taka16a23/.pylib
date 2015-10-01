from DiaryDatabase import DiaryDatabase

class GmailDiaryDatabase(DiaryDatabase):
    """Class GmailDiaryDatabase
    """
    # Attributes:
    ACCOUNT = 'taka16diary@gmail.com'  # (str) 
    PASSWORD = 'xwwrheownfdkbmao'  # (str) 
    __imap_client = None  # () 
    __cache_notes = None  # () 
    
    # Operations
    def iter_notes(self):
        """function iter_notes
        
        returns iter
        """
        return None # should raise NotImplementedError()
    
    def list_by_date(self, date):
        """function list_by_date
        
        date: 
        
        returns 
        """
        return None # should raise NotImplementedError()
    
    def list_by_year(self, year):
        """function list_by_year
        
        year: 
        
        returns 
        """
        return None # should raise NotImplementedError()
    
    def list_by_month(self, month):
        """function list_by_month
        
        month: 
        
        returns 
        """
        return None # should raise NotImplementedError()
    
    def list_by_day(self, day):
        """function list_by_day
        
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
    
    def list_by_search_text(self, regexp):
        """function list_by_search_text
        
        regexp: re.compile
        
        returns 
        """
        return None # should raise NotImplementedError()
    
    def close(self):
        """function close
        
        returns 
        """
        return None # should raise NotImplementedError()
    

