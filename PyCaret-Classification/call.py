import httpx

user = {
  "Age": 25,
  "Experience": 10,
  "Income": 100000,
  "Family": 6,
  "CCAvg": 0.46,
  "Education": 3,
  "Mortgage": 0,
  "SecuritiesAccount": 0,
  "CDAccount": 0,
  "Online": 0,
  "CreditCard": 0,
  "version": 1
}

response = httpx.post("https://8000-alihussaini-loanclassif-9dnige8fzup.ws-us88.gitpod.io/loans", json=user)

try: 
    if response.json()['prediction']:
        print(response.json()['prediction'][0])
except:
    print(response.json())