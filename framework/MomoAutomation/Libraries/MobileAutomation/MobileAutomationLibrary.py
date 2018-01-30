from utils.robotlibcore import DynamicCore
from drivers.appium_keywords import AppiumKeywords

class MobileAutomationLibrary(DynamicCore):
    
    """MobileAutomationLibrary is a light weight, flexible testing library for Momo App UI Automation. Documentation and examples"""
    
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = '1.0.0'

    def __init__(self):
        print 'Initializing...'
        libraries = [
            AppiumKeywords(),
            """AlertKeywords(self),
            BrowserManagementKeywords(self),
            CookieKeywords(self),
            ElementKeywords(self),
            FormElementKeywords(self),
            FrameKeywords(self),
            JavaScriptKeywords(self),
            RunOnFailureKeywords(self),
            ScreenshotKeywords(self),
            SelectElementKeywords(self),
            TableElementKeywords(self),
            WaitingKeywords(self),
            WindowKeywords(self)"""
        ]
        DynamicCore.__init__(self, libraries)
        """self.ROBOT_LIBRARY_LISTENER = LibraryListener()
        self._element_finder = ElementFinder(self)"""

    def run_keyword(self, name, args, kwargs):
        try:
            return DynamicCore.run_keyword(self, name, args, kwargs)
        except Exception:
            raise
