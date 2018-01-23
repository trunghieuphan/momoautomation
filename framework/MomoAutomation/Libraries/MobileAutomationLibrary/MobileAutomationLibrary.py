from robot.api.deco import keyword

class MobileAutomationLibrary:

    def get_keyword_names(self):
        return [name for name in dir(self) if hasattr(getattr(self, name), 'robot_name')]
    
    def run_keyword(self, name, args):
        print "Running keyword '%s' with arguments %s." % (name, args)

    @keyword
    def start_driver(self, host='127.0.0.1', port='4723', desired_capabilities=None, implicit_wait=False, implicit_wait_time=10):
        print 'Call start_driver of actual engine'
        
    @keyword
    def get_page_source(self):
        print 'Call get_page_source of actual engine'
        
    @keyword
    def stop_driver(self):
        print 'Call stop_driver of actual engine'

    @keyword
    def tap(self, locator, wait_time=None): 
        print 'Call tap of actual engine'
        
    @keyword    
    def enter_text(self, locator, text, append=False, wait_time=None):
        print 'Call enter_text of actual engine'
           
    @keyword   
    def clear_text(self, locator, wait_time=None):
        print 'Call clear_text of actual engine'
        
    @keyword            
    def get_text(self, locator, wait_time=None):   
        print 'Call get_text of actual engine' 
        
    @keyword            
    def capture_screen_shot(self):
        print 'Call capture_screen_shot of actual engine'
        
    @keyword 
    def is_text_present(self, text): 
        print 'Call is_text_present of actual engine'

    @keyword
    def is_element_present(self, locator, wait_time=None): 
        print 'Call is_element_present of actual engine'
        
    @keyword
    def find_element(self, locator, parent_element=None, wait_time=None):
        print 'Call find_element of actual engine'
             
    @keyword    
    def wait_for_element(self, locator, time_out=30):
        print 'Call wait_for_element of actual engine'
        
    @keyword
    def swipe_right(self, percentage=65, duration=None):
        print 'Call swipe_right of actual engine'

    @keyword 
    def swipe_left(self, percentage=65, duration=None):   
        print 'Call swipe_left of actual engine'    
   
    @keyword    
    def swipe_down(self, percentage=50, duration=None):  
        print 'Call swipe_down of actual engine'  

    @keyword    
    def swipe_up(self, percentage=50, duration=None): 
        print 'Call swipe_up of actual engine'

    @keyword 
    def swipe(self, start_x, start_y, end_x, end_y, duration=None):   
        print 'Call swipe of actual engine'

        
        