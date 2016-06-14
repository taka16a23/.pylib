
class WindowClient:
    """Class WindowClient
    """
    # Attributes:
    
    # Operations
    def get_title(self):
        """function get_title
        
        returns str
        """
        return None # should raise NotImplementedError()
    
    def set_title(self, title):
        """function set_title
        
        title: str
        
        returns None
        """
        return None # should raise NotImplementedError()
    
    def get_wmclass(self):
        """function get_wmclass
        
        returns WMClass
        """
        return None # should raise NotImplementedError()
    
    def set_wmclass(self, wmclass):
        """function set_wmclass
        
        wmclass: WMClass
        
        returns None
        """
        return None # should raise NotImplementedError()
    
    def get_bounds(self):
        """function get_bounds
        
        returns Rectangle
        """
        return None # should raise NotImplementedError()
    
    def set_bounds(self, rectangle):
        """function set_bounds
        
        rectangle: Rectangle
        
        returns None
        """
        return None # should raise NotImplementedError()
    
    def set_bounds(self, newx, newy, width, height):
        """function set_bounds
        
        newx: int
        newy: int
        width: int
        height: int
        
        returns None
        """
        return None # should raise NotImplementedError()
    
    def get_point(self):
        """function get_point
        
        returns Point
        """
        return None # should raise NotImplementedError()
    
    def set_point(self, point):
        """function set_point
        
        point: Point
        
        returns None
        """
        return None # should raise NotImplementedError()
    
    def set_point(self, newx, newy):
        """function set_point
        
        newx: int
        newy: int
        
        returns None
        """
        return None # should raise NotImplementedError()
    
    def get_size(self):
        """function get_size
        
        returns Dimension
        """
        return None # should raise NotImplementedError()
    
    def set_size(self, size):
        """function set_size
        
        size: Dimension
        
        returns None
        """
        return None # should raise NotImplementedError()
    
    def set_size(self, width, height):
        """function set_size
        
        width: int
        height: int
        
        returns None
        """
        return None # should raise NotImplementedError()
    
    def minimize(self):
        """function minimize
        
        returns None
        """
        return None # should raise NotImplementedError()
    
    def is_minimized(self):
        """function is_minimized
        
        returns bool
        """
        return None # should raise NotImplementedError()
    
    def maximize(self):
        """function maximize
        
        returns None
        """
        return None # should raise NotImplementedError()
    
    def is_maximized(self):
        """function is_maximized
        
        returns bool
        """
        return None # should raise NotImplementedError()
    
    def activate(self):
        """function activate
        
        returns None
        """
        return None # should raise NotImplementedError()
    
    def deactivate(self):
        """function deactivate
        
        returns None
        """
        return None # should raise NotImplementedError()
    
    def set_always_on_top(self):
        """function set_always_on_top
        
        returns None
        """
        return None # should raise NotImplementedError()
    
    def unset_always_on_top(self):
        """function unset_always_on_top
        
        returns None
        """
        return None # should raise NotImplementedError()
    
    def is_always_on_top(self):
        """function is_always_on_top
        
        returns bool
        """
        return None # should raise NotImplementedError()
    
    def set_always_on_bottom(self):
        """function set_always_on_bottom
        
        returns None
        """
        return None # should raise NotImplementedError()
    
    def unset_always_on_bottom(self):
        """function unset_always_on_bottom
        
        returns None
        """
        return None # should raise NotImplementedError()
    
    def is_always_on_bottom(self):
        """function is_always_on_bottom
        
        returns bool
        """
        return None # should raise NotImplementedError()
    
    def set_fullscreen(self):
        """function set_fullscreen
        
        returns None
        """
        return None # should raise NotImplementedError()
    
    def unset_fullscreen(self):
        """function unset_fullscreen
        
        returns None
        """
        return None # should raise NotImplementedError()
    
    def is_fullscreened(self):
        """function is_fullscreened
        
        returns bool
        """
        return None # should raise NotImplementedError()
    
    def set_shade(self):
        """function set_shade
        
        returns None
        """
        return None # should raise NotImplementedError()
    
    def unset_shade(self):
        """function unset_shade
        
        returns None
        """
        return None # should raise NotImplementedError()
    
    def is_shaded(self):
        """function is_shaded
        
        returns bool
        """
        return None # should raise NotImplementedError()
    
    def show(self):
        """function show
        
        returns None
        """
        return None # should raise NotImplementedError()
    
    def restore(self):
        """function restore
        
        returns None
        """
        return None # should raise NotImplementedError()
    
    def close(self):
        """function close
        
        returns None
        """
        return None # should raise NotImplementedError()
    
    def delete(self):
        """function delete
        
        returns None
        """
        return None # should raise NotImplementedError()
    
    def ping(self):
        """function ping
        
        returns bool
        """
        return None # should raise NotImplementedError()
    
    def destroy(self):
        """function destroy
        
        returns None
        """
        return None # should raise NotImplementedError()
    
    def move_cursor_to(self, point):
        """function move_cursor_to
        
        point: Point
        
        returns None
        """
        return None # should raise NotImplementedError()
    
    def move_cursor_to(self, newx, newy):
        """function move_cursor_to
        
        newx: int
        newy: int
        
        returns None
        """
        return None # should raise NotImplementedError()
    
    def send_key(self, code, modifiers, pressed = True, x = 0, y = 0):
        """function send_key
        
        code: int
        modifiers: int
        pressed: bool
        x: int
        y: int
        
        returns Cookie
        """
        return None # should raise NotImplementedError()
    
    def send_button(self, code, modifiers, pressed = True, x = 0, y = 0):
        """function send_button
        
        code: int
        modifiers: int
        pressed: bool
        x: int
        y: int
        
        returns Cookie
        """
        return None # should raise NotImplementedError()
    

