import requests,os
os.system("clear")
website = input("\033[0;36mEnter the website link: ")
website = website.replace("https://","").replace(" http://","").replace("/","")
url = f"https://api.hackertarget.com/hostsearch/?q={website}"
response = requests.get(url)
if response.status_code == 200:
    subdomains = response.text
    print('\033[0;34m',subdomains)
else:
  print("\033[0;31Try again")