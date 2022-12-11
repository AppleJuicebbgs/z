import requests
#import json
import time

def main(proxy):
  session = requests.Session()
  
  proxies = { 
    'https': f'http://{proxy}',
    'http': f'http://{proxy}',
  }
  
  try:
    response = session.post(
      'https://kz.mostbeautygirl.com/contests',
      
      files = (
        ('id', (None, 143010)),
      ),
      
      proxies = proxies,
  
      timeout = 10
    )
  
    print('Success!', response.text, response.status_code)
    #print(json.dumps(session.cookies.get_dict(), sort_keys=True, indent=4))
  except Exception as e:
    print(f'Error: {e}')

if __name__ == "__main__":
  print('Starting.\n')
  
  with open('proxies.txt', 'r') as f:
    print(f'File: {f}')
    
    for proxy in f.readlines():
      proxy = proxy.strip()
      
      print(f'\nProxy: {proxy}')
      main(proxy)

      #time.sleep(3)
