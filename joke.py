   1 #!/usr/bin/python3                                                                                                                                     
   2 import requests                                                                                                                                        
   3 from requests.exceptions import HTTPError                                                                                                              
   4                                                                                                                                                        
   5 import argparse                                                                                                                                        
   6                                                                                                                                                        
   7 class joke_request:                                                                                                                                    
   8     def __init__(self, joke_type='single', category='Any', lang='en'):                                                                                 
   9         self.joke_type = joke_type                                                                                                                     
  10         self.category = category                                                                                                                       
  11         self.lang = lang                                                                                                                               
  12         self.joke = self.request_joke(joke_type, category, lang)                                                                                       
  13                                                                                                                                                        
  14     def request_joke(self, joke_type, category, lang):                                                                                                 
  15         try:                                                                                                                                           
  16             response = requests.get(f"https://v2.jokeapi.dev/joke/{category}?lang={lang}&type={joke_type}")                                            
  17             response.raise_for_status()                                                                                                                
  18                                                                                                                                                        
  19             # Access Json, print joke                                                                                                                  
  20             json_response = response.json()                                                                                                            
  21                                                                                                                                                        
  22             if json_response["error"] == True:                                                                                                         
  23                 return json_response["message"]                                                                                                        
  24             elif json_response["type"] == 'single':                                                                                                    
  25                 return json_response["joke"]                                                                                                           
  26                                                                                                                                                        
  27             elif json_response["type"] == 'twopart':                                                                                                   
  28                 return json_response["setup"] + '\n' + json_response["delivery"]                                                                       
  29                                                                                                                                                        
  30                                                                                                                                                        
  31         except HTTPError as http_err:                                                                                                                  
  32             print(f'HTTP error occurred: {http_err}')                                                                                                  
  33         except Exception as err:                                                                                                                       
  34             print(f'Other error occurred: {err}')                                                                                                      
  35                                                                                                                                                        
  36     # Get Joke and print                                                                                                                               
  37     def get_joke(self):                                                                                                                                
  38         return f'{self.joke}'                                                                                                                          
  39                                                                                                                                                        
  40                                                                                                                                                        
  41 # Main Function                                                                                                                                        
  42 if __name__ == '__main__':                                                                                                                             
  43     parser = argparse.ArgumentParser(description='Joke Mixer: Make a random joke')                                                                     
  44     parser.add_argument('-t', default='single', metavar='type', help='*Single, Twopart')                                                               
  45     parser.add_argument('-c', default='Any', metavar='category', help='*Programming, Misc, Dark, Pun, Spooky, Christmas')                              
  46     parser.add_argument('-l', default='en', metavar='language', help='cs (Czech), de (German), *en (English), es (Spanish), fr (French), pt (Portugues$
  47     args = parser.parse_args()                                                                                                                         
  48                                                                                                                                                        
  49     print(joke_request(args.t, args.c, args.l).get_joke())    
