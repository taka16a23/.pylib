
class PathHandler:
    """Abstract class PathHandler
    """
    # Attributes:
    
    # Operations
    def from_cwd(self):
        """function from_cwd
        
        returns Path
        """
        raise NotImplementedError()
    
    def chmod(self, mode):
        """function chmod
        
        mode: 
        
        returns None
        """
        raise NotImplementedError()
    
    def chown(self, uid, gid):
        """function chown
        
        uid: 
        gid: 
        
        returns None
        """
        raise NotImplementedError()
    
    def copy(self, dst, recusive = False, symlinks = False, ignore = None):
        """function copy
        
        dst: str
        recusive: bool
        symlinks: bool
        ignore: callable
        
        returns None
        """
        raise NotImplementedError()
    
    def copymode(self, dst):
        """function copymode
        
        dst: str
        
        returns None
        """
        raise NotImplementedError()
    
    def copystat(self, dst):
        """function copystat
        
        dst: str
        
        returns None
        """
        raise NotImplementedError()
    
    def exists(self):
        """function exists
        
        returns bool
        """
        raise NotImplementedError()
    
    def expanduser(self):
        """function expanduser
        
        returns Path
        """
        raise NotImplementedError()
    
    def expandvars(self):
        """function expandvars
        
        returns Path
        """
        raise NotImplementedError()
    
    def get_absolute(self):
        """function get_absolute
        
        returns Path
        """
        raise NotImplementedError()
    
    def get_atime(self):
        """function get_atime
        
        returns float
        """
        raise NotImplementedError()
    
    def get_basename(self):
        """function get_basename
        
        returns Path
        """
        raise NotImplementedError()
    
    def get_ctime(self):
        """function get_ctime
        
        returns float
        """
        raise NotImplementedError()
    
    def get_drive(self):
        """function get_drive
        
        returns Path
        """
        raise NotImplementedError()
    
    def get_dirname(self):
        """function get_dirname
        
        returns Path
        """
        raise NotImplementedError()
    
    def get_extension(self):
        """function get_extension
        
        returns str
        """
        raise NotImplementedError()
    
    def get_mtime(self):
        """function get_mtime
        
        returns float
        """
        raise NotImplementedError()
    
    def get_normal(self):
        """function get_normal
        
        returns Path
        """
        raise NotImplementedError()
    
    def get_owner(self):
        """function get_owner
        
        returns str
        """
        raise NotImplementedError()
    
    def get_size(self):
        """function get_size
        
        returns long
        """
        raise NotImplementedError()
    
    def get_stem(self):
        """function get_stem
        
        returns str
        """
        raise NotImplementedError()
    
    def get_real(self):
        """function get_real
        
        returns Path
        """
        raise NotImplementedError()
    
    def get_root(self):
        """function get_root
        
        returns Path
        """
        raise NotImplementedError()
    
    def get_relative(self, start = '.'):
        """function get_relative
        
        start: str
        
        returns Path
        """
        raise NotImplementedError()
    
    def isabsolute(self):
        """function isabsolute
        
        returns bool
        """
        raise NotImplementedError()
    
    def isdir(self):
        """function isdir
        
        returns bool
        """
        raise NotImplementedError()
    
    def isfifo(self):
        """function isfifo
        
        returns bool
        """
        raise NotImplementedError()
    
    def isfile(self):
        """function isfile
        
        returns bool
        """
        raise NotImplementedError()
    
    def ismount(self):
        """function ismount
        
        returns bool
        """
        raise NotImplementedError()
    
    def issymlink(self):
        """function issymlink
        
        returns bool
        """
        raise NotImplementedError()
    
    def join(self, path):
        """function join
        
        path: 
        
        returns Path
        """
        raise NotImplementedError()
    
    def listdir(self, pattern = None):
        """function listdir
        
        pattern: str
        
        returns list
        """
        raise NotImplementedError()
    
    def link(self, path):
        """function link
        
        path: 
        
        returns Path
        """
        raise NotImplementedError()
    
    def mkdir(self, mode, parents = False):
        """function mkdir
        
        mode: 
        parents: bool
        
        returns None
        """
        raise NotImplementedError()
    
    def move(self, dst):
        """function move
        
        dst: str
        
        returns Path
        """
        raise NotImplementedError()
    
    def open(self, mode, buffering):
        """function open
        
        mode: 
        buffering: 
        
        returns file
        """
        raise NotImplementedError()
    
    def conf(self, name):
        """function conf
        
        name: str
        
        returns int
        """
        raise NotImplementedError()
    
    def readlink(self):
        """function readlink
        
        returns Path
        """
        raise NotImplementedError()
    
    def remove(self):
        """function remove
        
        returns None
        """
        raise NotImplementedError()
    
    def rename(self, new, force = False):
        """function rename
        
        new: 
        force: bool
        
        returns 
        """
        raise NotImplementedError()
    
    def replace(self, target):
        """function replace
        
        target: str
        
        returns Path
        """
        raise NotImplementedError()
    
    def samefile(self, other):
        """function samefile
        
        other: str
        
        returns bool
        """
        raise NotImplementedError()
    
    def splitdrive(self):
        """function splitdrive
        
        returns tuple
        """
        raise NotImplementedError()
    
    def splitext(self):
        """function splitext
        
        returns tuple
        """
        raise NotImplementedError()
    
    def touch(self):
        """function touch
        
        returns None
        """
        raise NotImplementedError()
    
    def unlink(self):
        """function unlink
        
        returns None
        """
        raise NotImplementedError()
    
    def walk(self):
        """function walk
        
        returns iterator
        """
        raise NotImplementedError()
    
    def with_name(self, name):
        """function with_name
        
        name: str
        
        returns Path
        """
        raise NotImplementedError()
    
    def with_ext(self, suffix):
        """function with_ext
        
        suffix: 
        
        returns Path
        """
        raise NotImplementedError()
    

