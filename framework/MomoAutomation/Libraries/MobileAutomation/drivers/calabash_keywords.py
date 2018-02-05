# -*- coding: utf-8 -*-
from robot.libraries.BuiltIn import BuiltIn
from utils.robotlibcore import keyword
from robot.libraries.Remote import Remote
from datetime import datetime
import os.path

class CalabashKeywords(object):
    
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = '1.0.0'
    ENGINE_NAME = 'calabash'
    
    def __init__(self):
        self._LOCATOR_STRATEGIES = {}
        self.built_in = BuiltIn()
    
    @keyword    
    def start_driver(self, host='127.0.0.1', port='8270', desired_capabilities=None, implicit_wait=False, implicit_wait_time=10):
        remote_url = "http://" + host + ":" + port
        self.built_in.import_library(_CalabashRemoteLibrary.full_qualifiy_name(), remote_url)
        self._get_library().run_keyword('calabash_start_driver', args=[desired_capabilities], kwargs={})
        
    @keyword
    def stop_driver(self):
        self._get_library().run_keyword('calabash_stop_driver', args=[], kwargs={})
        
    @keyword    
    def get_page_source(self):
        self._get_library().run_keyword('calabash_get_page_source', args=[], kwargs={})

    @keyword  
    def tap(self, locator, wait_time=None):  
        if(wait_time):
            self.wait_for_element(locator, wait_time)
        self._get_library().run_keyword('calabash_tap_element', args=[locator], kwargs={})
      
    @keyword  
    def enter_text(self, locator, text, append=False, wait_time=None):
        if(wait_time):
            self.wait_for_element(locator, wait_time)
        if(append is False):
            self._get_library().run_keyword('calabash_clear_text', args=[locator], kwargs={}) 
        self._get_library().run_keyword('calabash_enter_text', args=[locator, text], kwargs={})   

    @keyword       
    def clear_text(self, locator, wait_time=None):
        if(wait_time):
            self.wait_for_element(locator, wait_time)
        self._get_library().run_keyword('calabash_clear_text', args=[locator], kwargs={})
            
    @keyword              
    def get_text(self, locator, wait_time=None):    
        if(wait_time):
            self.wait_for_element(locator, wait_time)
        return self._get_library().run_keyword('calabash_get_text', args=[locator], kwargs={}) 
    
    @keyword       
    def capture_screen_shot(self):
        outputdir = BuiltIn().get_variable_value('${OUTPUTDIR}')
        current = datetime.now()
        file_name = '%d_%d_%d_%d_%d_%d.png' % (current.year, current.month, current.day, current.hour, current.minute, current.second)  
        path = os.path.join(outputdir, file_name)
        saved_image_path = self._get_library().run_keyword('calabash_capture_screen_shot', args=[path], kwargs={})
        saved_image_name = os.path.basename(saved_image_path)
        print '*HTML* Screenshot <img src="'+ saved_image_name +'"/>'
    
    @keyword 
    def is_text_present(self, text): 
        return self._get_library().run_keyword('calabash_is_text_present', args=[text], kwargs={})
       
    @keyword   
    def is_element_present(self, locator, wait_time=None): 
        return self._get_library().run_keyword('calabash_is_element_present', args=[locator], kwargs={})
        
    @keyword
    def find_element(self, locator, parent_element=None, wait_time=None):
        raise RuntimeError("find_element keyword has not supported by Calabash engine, because it is called remotely")    
       
    @keyword
    def wait_for_element(self, locator, time_out=30):
        self._get_library().run_keyword('calabash_wait_for_element', args=[locator, time_out], kwargs={})
    
    @keyword
    def swipe_right(self, percentage=65, duration=None):
        screen_size = self._get_screen_size()
        start_x = 0
        start_y = int(screen_size['height'] / 2)
        self._get_library().run_keyword('calabash_swipe', args=['right', start_x, start_y], kwargs={})
    
    @keyword
    def swipe_left(self, percentage=65, duration=None):       
        screen_size = self._get_screen_size()
        """step back 1px off-set from the right"""
        start_x = screen_size['width'] - 1
        start_y = int(screen_size['height'] / 2)    
        self._get_library().run_keyword('calabash_swipe', args=['left', start_x, start_y], kwargs={})
    
    @keyword
    def swipe_down(self, percentage=50, duration=None):    
        screen_size = self._get_screen_size()
        start_x = int(screen_size['width']/2)   
        start_y = 1
        self._get_library().run_keyword('calabash_swipe', args=['down', start_x, start_y], kwargs={})
    
    @keyword
    def swipe_up(self, percentage=50, duration=None): 
        screen_size = self._get_screen_size()
        start_x = int(screen_size['width'] / 2)
        """Step up 1px off-set"""
        start_y = screen_size['height']-1
        self._get_library().run_keyword('calabash_swipe', args=['up', start_x, start_y], kwargs={})
    
    @keyword
    def swipe(self, start_x, start_y, end_x, end_y, duration=None):   
        raise RuntimeError("swipe keyword has not been supported by Calabash engine")
        
    def _findElementWithWait(self, locator, wait_time=None):
        pass 

    def _parse_locator(self, locator):
        pass
    
    def _get_screen_size(self):
        return self._get_library().run_keyword('calabash_get_screen_size', args=[], kwargs={})
    
    def _get_library(self):
        lib = self.built_in.get_library_instance(name=_CalabashRemoteLibrary.full_qualifiy_name())
        if(lib):
            return lib
        raise RuntimeError(_CalabashRemoteLibrary.full_qualifiy_name() + " is not used")
    
"""Wrapper of Remote library"""    
class _CalabashRemoteLibrary(Remote):
    @staticmethod
    def full_qualifiy_name():
        return 'drivers.calabash_keywords._CalabashRemoteLibrary'