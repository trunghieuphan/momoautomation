require 'calabash-cucumber/operations'

include Calabash::Cucumber
include Calabash::Cucumber::Core
include Calabash::Cucumber::TestsHelpers
include Calabash::Cucumber::QueryHelpers
include Calabash::Cucumber::WaitHelpers

#ENV['BUNDLE_ID'] = 'sh.calaba.CalSmoke-cal'
#ENV['DEVICE_TARGET'] = '37984baac6ff2598b162ed88e7015cd889e200d5'
#ENV['DEVICE_ENDPOINT'] = 'http://10.10.23.11:37265'
  
class CalabashRobotLibrary
    
    def calabash_start_driver(desired_caps={})
      if (!desired_caps.key?('BUNDLE_ID'))
        raise RuntimeError, 'BUNDLE_ID must be provided'
      end
      if (!desired_caps.key?('DEVICE_TARGET'))
        raise RuntimeError, 'DEVICE_TARGET must be provided'
      end
      if (!desired_caps.key?('DEVICE_ENDPOINT'))
        raise RuntimeError, 'DEVICE_ENDPOINT must be provided'
      end  
      ENV['BUNDLE_ID'] = desired_caps['BUNDLE_ID']
      ENV['DEVICE_TARGET'] = desired_caps['DEVICE_TARGET']
      ENV['DEVICE_ENDPOINT'] = desired_caps['DEVICE_ENDPOINT']  
      start_test_server_in_background
    end
    
    def calabash_stop_driver()
      #Stop calabash endpoint from the phone 
      stop_test_server
    end
    
    def calabash_get_page_source()
      return query("*").to_json
    end
        
    def calabash_tap_element(locator)
      touch(locator)
    end
   
    def calabash_enter_text(locator, text)
      touch(locator)
      keyboard_enter_text(text)
    end
  
    def calabash_get_text(locator)
      #Will consider to understand more about this index
      text_node_index = 0
      texts = query(locator, :text)
      return texts[0]
    end
    
    def calabash_clear_text(locator)
      clear_text(locator)
    end
    
    def calabash_capture_screen_shot(filePath)
      return screenshot({:name => filePath})
    end
    
    def calabash_is_text_present(text)
      search_pattern = "*" + escape_string(text) + "*"
      return element_exists("* {text LIKE '"+ search_pattern +"'}")     
    end  
    
    def calabash_is_element_present(locator)
      return element_exists(locator)
    end

    def calabash_wait_for_element(locator, time_out=30)
      wait_for_element_exists(locator, timeout: time_out)
    end  

    def calabash_get_screen_size()
      return screen_dimensions()
    end
   
    def calabash_swipe(direction, start_x, start_y)
      _dx = start_x.to_i
      _dy = start_y.to_i
      _force = :strong
      _direction = direction.downcase.to_sym
      _screen_direction = if (direction.downcase == 'up' or direction.downcase == 'down') then :vertical 
                          elsif (direction.downcase == 'left' or direction.downcase == 'right') then :horizontal 
                          else raise RuntimeError, 'Swipe direction should be up/down/left/right' end  
      swipe(direction = _direction, options = {:force => _force, :'swipe-delta' => {_screen_direction => {:dx => _dx, :dy => _dy}}})
    end
end
