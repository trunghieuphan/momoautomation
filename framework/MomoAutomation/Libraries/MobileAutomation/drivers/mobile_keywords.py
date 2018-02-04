from utils.robotlibcore import keyword

class MobileKeywords:
    
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = '1.0.0'
    """Default engine"""
    ENGINE_NAME = 'appium'  
    
    
    """Call back to the correct engine with keyword name and parameters"""
    def _do_action(self, keyword_name, keyword_args):
        """Specify engine for the first run"""
        if self.ENGINE is None:
            for library in self.libraries:
                if(library.NAME == self.ENGINE_NAME):
                    self.ENGINE = library
                    break
        """No library is explicitly declared? So, appium""" 
        if self.ENGINE is None:
            from drivers.appium_keywords import AppiumKeywords
            self.ENGINE = AppiumKeywords()
        """Is this keyword implemented in this library?"""
        for method_name in dir(self.ENGINE):
            print ''
                

    @keyword    
    def start_driver(self, host='127.0.0.1', port='4723', desired_capabilities=None, implicit_wait=False, implicit_wait_time=10):
        """Start driver on HTTP host (default is localhost) and port (default is Appium server port 4723).
        
        The ``desired_capabilities`` argument is the device configuration info to run test on, see https://github.com/appium/appium/blob/master/docs/en/writing-running-appium/caps.md for details 
        The ``implicit_wait`` argument if True will make the driver to wait in `implicit_wait_time` when it's looking for element.
        The ``implicit_wait_time`` argument with default value is 10 seconds, is the waiting time to wait for an Element (UI Object) appears on screen 
        """
        pass
        
    @keyword
    def get_page_source(self):
        """Get the XML/JSON content which is the representation of UI Objects hierarchy of the current screen"""
        return ''

    @keyword
    def stop_driver(self):
        pass
    
    @keyword
    def tap(self, locator, wait_time=None): 
        """Click on an Element which is identified by ``locator``

        The ``locator`` argument should be provided in format locator_strategy:some_value

        Examples:
        | ID:the object id |
        | NAME:the object name |
        | XPATH:xpath of the object |
        | CSS:css_selector of the object |
        | TEXT:link text of the object |
        | TAG:tag_name of the object |
        | CLASS:class_name of the object |
        """
        pass
    
    @keyword    
    def enter_text(self, locator, text, append=False, wait_time=None):
        pass  
       
    @keyword
    def clear_text(self, locator, wait_time=None):
        pass
           
    @keyword            
    def get_text(self, locator, wait_time=None):    
        return ''
     
    @keyword            
    def capture_screen_shot(self):
        pass
    
    @keyword 
    def is_text_present(self, text): 
        return True
    
    @keyword
    def is_element_present(self, locator, wait_time=None): 
        return True
    
    @keyword
    def find_element(self, locator, parent_element=None, wait_time=None):
        return None       
    
    @keyword    
    def wait_for_element(self, locator, time_out=30):
        pass
    
    @keyword
    def swipe_right(self, percentage=65, duration=None):
        pass
    
    @keyword
    def swipe_left(self, percentage=65, duration=None):       
        pass   
    
    @keyword    
    def swipe_down(self, percentage=50, duration=None):    
        pass
      
    @keyword  
    def swipe_up(self, percentage=50, duration=None): 
        pass
    
    @keyword
    def swipe(self, start_x, start_y, end_x, end_y, duration=None):   
        pass
        