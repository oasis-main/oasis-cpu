import os
import sys
import rusty_pipes

#set proper path for modules
sys.path.append('/home/pi/oasis-grow')
sys.path.append('/usr/lib/python37.zip')
sys.path.append('/usr/lib/python3.7')
sys.path.append('/usr/lib/python3.7/lib-dynload')
sys.path.append('/home/pi/.local/lib/python3.7/site-packages')
sys.path.append('/usr/local/lib/python3.7/dist-packages')
sys.path.append('/usr/lib/python3/dist-packages')

#all functions depend on subprocess module
def reset_device_state():
    reset_d = rusty_pipes.Open(["cp", "/home/pi/oasis-grow/defaults/device_state_default_template.json", "/home/pi/oasis-grow/configs/device_state.json"])
    reset_d.wait()

def reset_control_params():
    reset_c = rusty_pipes.Open(["cp", "/home/pi/oasis-grow/defaults/control_params_default_template.json", "/home/pi/oasis-grow/configs/control_params.json"])
    reset_c.wait()
    
def reset_sensor_data():
    reset_s = rusty_pipes.Open(["cp", "/home/pi/oasis-grow/defaults/sensor_data_default_template.json", "/home/pi/oasis-grow/configs/sensor_data.json"])
    reset_s.wait()

def reset_access_config():
    reset_a = rusty_pipes.Open([ "cp", "/home/pi/oasis-grow/defaults/access_config_default_template.json", "/home/pi/oasis-grow/configs/access_config.json"])
    reset_a.wait()

def reset_hardware_config():
    reset_h = rusty_pipes.Open(["cp", "/home/pi/oasis-grow/defaults/hardware_config_default_template.json", "/home/pi/oasis-grow/configs/hardware_config.json"])
    reset_h.wait()

def reset_feature_toggles():
    reset_f = rusty_pipes.Open(["cp", "/home/pi/oasis-grow/defaults/feature_toggles_default_template.json", "/home/pi/oasis-grow/configs/feature_toggles.json"])
    reset_f.wait()

def reset_power_data():
    reset_p = rusty_pipes.Open(["cp", "/home/pi/oasis-grow/defaults/power_data_default_template.json", "/home/pi/oasis-grow/configs/power_data.json"])
    reset_p.wait()

#new generic function for working on arbitrary structs with defaults
def reset_config_path(path: str):
    filename = os.path.basename(path)
    f_name, f_ext = os.path.splitext(filename)
    default_path = "/home/pi/oasis-grow/defaults/" + f_name + "_default_template.json"
    
    if os.path.exists(default_path):
        reset_path = rusty_pipes.Open(["cp", default_path, path])
        reset_path.wait()
    else:
        print("Cannot reset struct because a default config file does not exist.")

#will be deprecated for rust implementation    
def reset_locks():
    reset_lox = rusty_pipes.Open(["cp", "/home/pi/oasis-grow/defaults/locks_default_template.json", "/home/pi/oasis-grow/configs/locks.json"])
    reset_lox.wait()

def reset_nonhw_configs():
    reset_device_state()
    reset_control_params()
    reset_sensor_data()
    reset_access_config()

def reset_data_out():
    clear_image_feed = rusty_pipes.Open(["rm", "-rf", "/home/pi/oasis-grow/data_out/image_feed"])
    clear_image_feed.wait()
    clear_sensor_feed = rusty_pipes.Open(["rm", "-rf", "/home/pi/oasis-grow/data_out/sensor_feed"])
    clear_sensor_feed.wait()
    clear_dir = rusty_pipes.Open(["rm", "-rf", "/home/pi/oasis-grow/data_out"])
    clear_dir.wait()
    
    new_dir = rusty_pipes.Open(["mkdir", "/home/pi/oasis-grow/data_out"])
    new_dir.wait()
    new_image_feed = rusty_pipes.Open(["mkdir", "/home/pi/oasis-grow/data_out/image_feed"])
    new_image_feed.wait()
    new_sensor_feed = rusty_pipes.Open(["mkdir", "/home/pi/oasis-grow/data_out/sensor_feed"])
    new_sensor_feed.wait()

def reset_image_feed():
    clear_image_feed = rusty_pipes.Open(["rm", "-rf", "/home/pi/oasis-grow/data_out/image_feed"])
    clear_image_feed.wait()
    new_image_feed = rusty_pipes.Open(["mkdir", "/home/pi/oasis-grow/data_out/image_feed"])
    new_image_feed.wait()
    
#function that runs all the other functions
def reset_all():
    reset_device_state()
    reset_feature_toggles()
    reset_control_params()
    reset_access_config()
    reset_hardware_config()
    reset_feature_toggles()
    reset_data_out()
    reset_sensor_data()
    reset_power_data()
    reset_image_feed()

if __name__ == '__main__':
    reset_all()

