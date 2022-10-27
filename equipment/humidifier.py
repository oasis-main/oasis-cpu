#---------------------------------------------------------------------------------------
#Manages Hardware for Humidity
#---------------------------------------------------------------------------------------
#import shell modules
import sys
import signal

#set proper path for modules
sys.path.append('/home/pi/oasis-grow')

import rusty_pins
from peripherals import relays
from utils import concurrent_state as cs
from utils import error_handler as err

resource_name = "humidifier"
cs.check_lock(resource_name)

#setup GPIO
cs.load_state() #get configs
hum_GPIO = int(cs.structs["hardware_config"]["equipment_gpio_map"]["humidifier_relay"]) #heater pin pulls from config file
pin = rusty_pins.GpioOut(hum_GPIO)

if __name__ == '__main__':
    signal.signal(signal.SIGTERM, cs.wrapped_sys_exit)
    try:
        while True:
            if cs.structs["feature_toggles"]["hum_pid"] == "1":
                print("Running humidifier in pulse mode with " + cs.structs["control_params"]["hum_feedback"] + "%" + " power...")
                relays.actuate_slow_pwm(pin, float(cs.structs["control_params"]["hum_feedback"]), wattage=cs.structs["hardware_config"]["equipment_wattage"]["humidifier"], log="humidifier_kwh") #trigger appropriate response
            else:
                print("Running humidifier for " + cs.structs["control_params"]["humidifier_duration"] + " minute(s) on, " + cs.structs["control_params"]["humidifier_interval"] + " minute(s) off...")
                relays.actuate_interval_sleep(pin, float(cs.structs["control_params"]["humidifier_duration"]), float(cs.structs["control_params"]["humidifier_interval"]), duration_units= "minutes", sleep_units="minutes", wattage=cs.structs["hardware_config"]["equipment_wattage"]["humidifier"], log="humidifier_kwh")
            cs.load_state()
    except SystemExit:
        print("Humidifier was terminated.")
    except KeyboardInterrupt:
        print("Humidifier was interrupted.")
    except Exception:    
        print("Humidifier ncountered an error!")
        print(err.full_stack())
    finally:
        print("Shutting down humidifier...")
        cs.safety.unlock(cs.lock_filepath, resource_name)