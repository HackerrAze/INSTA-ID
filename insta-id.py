import requests,os,json
os.system('clear')

kulAd = str(input("Kullanıcı Adı: "))

link = "https://www.instagram.com/{}/?__a=1".format(kulAd)

izin = requests.get(link)

js = json.loads(izin.text)
try:
    kid = js['graphql']['user']['id']
except Exception:
    print("\n")
    print("-"*71)
    print("Kullanıcı Adı Bulunamadı!")
    print("-"*71)
    exit()

print("\n")
print("="*71)
print("İd:",kid)
print("="*71)