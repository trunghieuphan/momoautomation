from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn

ROBOT_LISTENER_API_VERSION = 2

def end_keyword(name, attrs): 
    if attrs['status'] == 'FAIL':
        for arg in attrs['args']:
            if(arg.startswith('${') and arg.endswith('}')):
                logger.info(str(arg) + ' = ' + str(BuiltIn().get_variable_value(arg)))
