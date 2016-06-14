
class WindowObserver:
    """Class WindowObserver
    """
    # Attributes:
    
    # Operations
    def on_window_title_changed(self, window):
        """function on_window_title_changed
        
        window: WindowClient
        
        returns None
        """
        return None # should raise NotImplementedError()
    
    def on_window_maximized(self, window):
        """function on_window_maximized
        
        window: WindowClient
        
        returns None
        """
        return None # should raise NotImplementedError()
    
    def on_window_minimized(self, window):
        """function on_window_minimized
        
        window: WindowClient
        
        returns None
        """
        return None # should raise NotImplementedError()
    
    def on_window_fullscreened(self, window):
        """function on_window_fullscreened
        
        window: WindowClient
        
        returns None
        """
        return None # should raise NotImplementedError()
    
    def on_window_shaded(self, window):
        """function on_window_shaded
        
        window: WindowClient
        
        returns None
        """
        return None # should raise NotImplementedError()
    
    def on_window_destroyed(self, window_id):
        """function on_window_destroyed
        
        window_id: int
        
        returns None
        """
        return None # should raise NotImplementedError()
    
    def on_window_bounds_changed(self, window):
        """function on_window_bounds_changed
        
        window: WindowClient
        
        returns None
        """
        return None # should raise NotImplementedError()
    

