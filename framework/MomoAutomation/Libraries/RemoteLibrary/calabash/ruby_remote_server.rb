if __FILE__ == $0
  require 'rubygems'
  require 'robot_remote_server'
  require 'calabash_robot_library'
  
  RobotRemoteServer.new(CalabashRobotLibrary.new,
                          host = 'localhost',
                          port = 8270)
end