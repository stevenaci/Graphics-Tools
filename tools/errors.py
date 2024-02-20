

_ERROR_STR_ = "PROCESS FAILED:\n {} " 
    
def process_error(error_msg):
    print(_ERROR_STR_.format(error_msg))

if __name__ == "__main__":
    process_error("one131")
    