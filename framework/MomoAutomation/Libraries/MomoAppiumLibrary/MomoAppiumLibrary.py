# -*- coding: utf-8 -*-
from appium import webdriver
from appium.webdriver.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from datetime import datetime
from robot.libraries.BuiltIn import BuiltIn
import os.path

class MomoAppiumLibrary(object):
    
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = '1.0.0'
    
    def __init__(self):
        print 'Initializing...'
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
                
        
    def start_appium_driver(self, host='127.0.0.1', port='4723', desired_capabilities=None, implicit_wait=False, implicit_wait_time=10):
        url = 'http://' + host + ':' + port + '/wd/hub'
        self.driver = webdriver.Remote(url, desired_capabilities)
        self.implicit_wait = implicit_wait
        self.implicit_wait_time = implicit_wait_time
    
    def get_page_source(self):
        return self.driver.page_source

    def stop_appium_driver(self):
        self.driver.quit()

    def tap(self, locator, wait_time=None):    
        element = self._findElementWithWait(locator, wait_time)
        element.click()
        
    def enter_text(self, locator, text, append=False, wait_time=None):
        element = self._findElementWithWait(locator, wait_time)  
        if(append):
            element.clear()
        element.send_keys(text)   
       
    def clear_text(self, locator, wait_time=None):
        element = self._findElementWithWait(locator, wait_time)  
        element.clear()
                
    def get_text(self, locator, wait_time=None):    
        element = self._findElementWithWait(locator, wait_time)
        return element.text
        
    def wait_for_element(self, locator, time_out=30):
        by, locatorVal = self._parse_locator(locator)
        return WebDriverWait(self.driver, float(time_out)).until(expected_conditions.presence_of_element_located((by, locatorVal)))
                
    def capture_screen_shot(self):
        outputdir = BuiltIn().get_variable_value('${OUTPUTDIR}')
        current = datetime.now()
        file_name = '%d_%d_%d_%d_%d_%d.png' % (current.year, current.month, current.day, current.hour, current.minute, current.second)  
        path = os.path.join(outputdir, file_name)
        self.driver.save_screenshot(path)    
        print '*HTML* Screenshot <img src="'+ file_name +'"/>'
     
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
            raise RuntimeError('Locator should be String or WebElement') 

    def _parse_locator(self, locator):
        '''Detect if this is an explicit locator strategy in form of locator_strategy : value'''
        if(locator.find(':')) == -1:
            raise ValueError("Unable to handle locator '%s'." % locator)
        locatorKey = locator[: locator.find(':')].strip().lower()
        locatorVal = locator[locator.find(':')+1 :].strip()
        if(self._LOCATOR_STRATEGIES.has_key(locatorKey) == False):
            raise ValueError("Unable to handle locator '%s'." % locatorKey)
        by = self._LOCATOR_STRATEGIES[locatorKey]    
        return by, locatorVal
