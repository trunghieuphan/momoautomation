# -*- coding: utf-8 -*-
from appium import webdriver
from appium.webdriver.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import WebDriverException
from datetime import datetime
from robot.libraries.BuiltIn import BuiltIn
import os.path
from utils.robotlibcore import keyword

class AppiumKeywords(object):
    
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = '1.0.0'
    ENGINE_NAME = 'appium'
    LOCATOR_SEPARATORS = [':', '=']
    
    def __init__(self):
        self._LOCATOR_STRATEGIES = {
                                    'id'            : By.ID, 
                                    'name'          : By.NAME, 
                                    'css'           : By.CSS_SELECTOR, 
                                    'cssselector'   : By.CSS_SELECTOR, 
                                    'xpath'         : By.XPATH,
                                    'text'          : By.LINK_TEXT,
                                    'linktext'      : By.LINK_TEXT,
                                    'link_text'     : By.LINK_TEXT,
                                    'link text'     : By.LINK_TEXT,
                                    'tag'           : By.TAG_NAME,
                                    'tagname'       : By.TAG_NAME,
                                    'tag_name'      : By.TAG_NAME,
                                    'tag name'      : By.TAG_NAME,
                                    'class'         : By.CLASS_NAME,
                                    'classname'     : By.CLASS_NAME,
                                    'class_name'    : By.CLASS_NAME,
                                    'class name'    : By.CLASS_NAME
                                    }
                
    @keyword    
    def start_driver(self, host='127.0.0.1', port='4723', desired_capabilities=None, implicit_wait=False, implicit_wait_time=10):
        """Start driver on HTTP host (default is localhost) and port (default is Appium server port 4723).
        
        The ``desired_capabilities`` argument is the device configuration info to run test on, see https://github.com/appium/appium/blob/master/docs/en/writing-running-appium/caps.md for details 
        The ``implicit_wait`` argument if True will make the driver to wait in `implicit_wait_time` when it's looking for element.
        The ``implicit_wait_time`` argument with default value is 10 seconds, is the waiting time to wait for an Element (UI Object) appears on screen 
        """
        url = 'http://' + host + ':' + port + '/wd/hub'
        self.driver = webdriver.Remote(url, desired_capabilities)
        self.implicit_wait = implicit_wait
        self.implicit_wait_time = implicit_wait_time
        
    @keyword
    def get_page_source(self):
        """Get the XML/JSON content which is the representation of UI Objects hierarchy of the current screen"""
        return self.driver.page_source

    @keyword
    def stop_driver(self):
        if(self.driver is not None):
            self.driver.quit()
    
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
        element = self._findElementWithWait(locator, wait_time)
        element.click()
    
    @keyword  
    def enter_text(self, locator, text, append=False, wait_time=None):
        element = self._findElementWithWait(locator, wait_time)  
        if(append):
            element.clear()
        element.send_keys(text)   
       
    @keyword
    def clear_text(self, locator, wait_time=None):
        element = self._findElementWithWait(locator, wait_time)  
        element.clear()
           
    @keyword          
    def get_text(self, locator, wait_time=None):    
        element = self._findElementWithWait(locator, wait_time)
        return element.text
     
    @keyword           
    def capture_screen_shot(self):
        outputdir = BuiltIn().get_variable_value('${OUTPUTDIR}')
        current = datetime.now()
        file_name = '%d_%d_%d_%d_%d_%d.png' % (current.year, current.month, current.day, current.hour, current.minute, current.second)  
        path = os.path.join(outputdir, file_name)
        self.driver.save_screenshot(path)    
        print '*HTML* Screenshot <img src="'+ file_name +'"/>'
    
    @keyword
    def is_text_present(self, text): 
        return text in self.driver.page_source
    
    @keyword   
    def is_element_present(self, locator, wait_time=None): 
        try:
            element = self._findElementWithWait(locator, wait_time)
            return element is not None
        except WebDriverException:
            return False
    
    @keyword
    def find_element(self, locator, parent_element=None, wait_time=None):
        if(parent_element):
            by, locatorVal = self._parse_locator(locator)
            return parent_element.find_element(by, locatorVal)
        else:
            return self._findElementWithWait(locator, wait_time)        
    
    @keyword  
    def wait_for_element(self, locator, time_out=30):
        by, locatorVal = self._parse_locator(locator)
        return WebDriverWait(self.driver, float(time_out)).until(expected_conditions.presence_of_element_located((by, locatorVal)))
    
    @keyword
    def swipe_right(self, percentage=65, duration=None):
        screen_size = self.driver.get_window_size()
        start_x = 0
        start_y = end_y = int(screen_size['height'] / 2)
        end_x = int(screen_size['width'] * percentage / 100)
        self.swipe(start_x, start_y, end_x, end_y, duration)
    
    @keyword   
    def swipe_left(self, percentage=65, duration=None):       
        screen_size = self.driver.get_window_size()
        """step back 1px off-set from the right"""
        start_x = screen_size['width'] - 1
        end_x = int(screen_size['width'] * (100-percentage) / 100)
        start_y = end_y = int(screen_size['height'] / 2)    
        self.swipe(start_x, start_y, end_x, end_y, duration)    
    
    @keyword
    def swipe_down(self, percentage=50, duration=None):    
        screen_size = self.driver.get_window_size()
        start_x = end_x = int(screen_size['width']/2)   
        start_y = 1
        end_y = int(screen_size['height'] * percentage / 100)
        self.swipe(start_x, start_y, end_x, end_y, duration)
      
    @keyword
    def swipe_up(self, percentage=50, duration=None): 
        screen_size = self.driver.get_window_size()
        start_x = end_x = int(screen_size['width'] / 2)
        """Step up 1px off-set"""
        start_y = screen_size['height']-1
        end_y = int(screen_size['height'] * percentage/100)
        self.swipe(start_x, start_y, end_x, end_y, duration)
    
    @keyword
    def swipe(self, start_x, start_y, end_x, end_y, duration=None):   
        self.driver.swipe(start_x, start_y, end_x, end_y, duration)
        
    def _findElementWithWait(self, locator, wait_time=None):
        if type(locator) is str or type(locator) is unicode:
            by, locatorVal = self._parse_locator(locator)
            if(wait_time):
                return self.wait_for_element(locator, wait_time)
            elif(self.implicit_wait):
                return self.wait_for_element(locator, self.implicit_wait_time)
            else:
                return self.driver.find_element(by, locatorVal)
        elif type(locator) is WebElement:
            raise RuntimeError('Find element from WebElement has not been supported.')     
        else:
            raise ValueError('Locator should be String or WebElement') 

    def _parse_locator(self, locator):
        """Detect if this is an explicit locator strategy in form of locator_strategy : value"""
        separator_index = -1
        indexes = []
        for sep in self.LOCATOR_SEPARATORS:
            index = locator.find(sep)
            if(index != -1):
                indexes.append(index)
        if len(indexes) > 0:   
            separator_index = min(indexes)    
        if(separator_index == -1):
            raise ValueError("Unable to handle locator '%s'." % locator)
        locatorKey = locator[: separator_index].strip().lower()
        locatorVal = locator[separator_index+1 :].strip()
        if(self._LOCATOR_STRATEGIES.has_key(locatorKey) == False):
            raise ValueError("Unable to handle locator '%s'." % locatorKey)
        by = self._LOCATOR_STRATEGIES[locatorKey]    
        return by, locatorVal
