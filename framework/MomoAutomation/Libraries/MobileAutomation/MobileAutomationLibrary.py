from utils.robotlibcore import DynamicCore
import sys, inspect
import drivers

class MobileAutomationLibrary(DynamicCore):
    
    """MobileAutomationLibrary is a light weight, flexible testing library for Momo App UI Automation. Documentation and examples"""
    
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = '1.0.0'
    """The ENGINE is being used. Appium is default option"""
    DEFAULT_ENGINE_NAME = 'appium'
    
    def __init__(self, engine_name=DEFAULT_ENGINE_NAME):
        
        self.libraries = []

        for name, obj in inspect.getmembers(sys.modules[drivers.__name__]):
            if inspect.isclass(obj):
                if not obj.__dict__.has_key('ENGINE_NAME'):
                    continue
                if str(obj.__dict__['ENGINE_NAME']).lower() == engine_name:
                    self.libraries.append(obj()) 
                     
        if len(self.libraries) == 0:
            raise RuntimeError("No engine is specified")   
                
        DynamicCore.__init__(self, self.libraries)
        """self.ROBOT_LIBRARY_LISTENER = LibraryListener()s
        self._element_finder = ElementFinder(self)"""

    def run_keyword(self, name, args, kwargs):
        try:          
            return DynamicCore.run_keyword(self, name, args, kwargs)
        except Exception:
            raise
