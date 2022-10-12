#Your API Key : bf8f4be551d1fdaafa51016aeb87462d

# api_key = "bf8f4be551d1fdaafa51016aeb87462d"
# api_key = "b3ae9794d0b9b32b95d2f6fd5cb89d0a"
api_key = "7f03d4c7f7a1e60b7653a93d720381bb"
# api_key = "7a0b02329345d35dd5f8a916a0f39161"
# api_key = "ac5549ea4c42002d4a63472d839f934b"

import configparser




def get_api_key():
   config = configparser.RawConfigParser()
   config.read('config/configuration.txt')
    
   details_dict = dict(config.items('Finance Config'))
   print("configuration file details", details_dict)
   api_key = config.get('Finance Config', 'api_key')
   return api_key
   
   
if __name__ == "__main__":
    api_key = get_api_key()
    print("return api_key in main", api_key)