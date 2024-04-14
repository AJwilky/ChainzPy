import requests
from bs4 import BeautifulSoup


def set_data_to_json(value):
    global DATA_TO_JSON
    DATA_TO_JSON = value

def set_api_key(api_key):
    global KEY
    KEY = api_key




def getAddressBalance(crypto, address):
    global KEY
    r = requests.get(f'https://chainz.cryptoid.info/{crypto}/api.dws?q=getbalance&a={address}&key={KEY}')
    data = r.json()
    print(data)



def getAddressBalanceUSD(crypto, cryptoabbr, address):
    global KEY
    r = requests.get(f'https://coinmarketcap.com/currencies/{crypto}/')
    soup = BeautifulSoup(r.text, 'html.parser')
    price_find = soup.find(class_='sc-f70bb44c-0 jxpCgO base-text')
    str_price = str(price_find)
    stripedPrice = str_price.strip('<span class="sc-f70bb44c-0 jxpCgO base-text">')
    striped2Price = stripedPrice.strip('</')
    final_price = striped2Price.replace(",", "").replace("$", "")
    float_price = float(final_price)
    print(final_price)
    print(float_price)

    

    r1 = requests.get(f'https://chainz.cryptoid.info/{cryptoabbr}/api.dws?q=getbalance&a={address}&key{KEY}')
    data = r1.text
    crypto_bal = float(data)
    print(crypto_bal)
    crypto_to_usd = float_price * crypto_bal
    crypto_in_usd = "${:,.2f}".format(crypto_to_usd)
    print(crypto_in_usd) # prints the amount of money in a users wallet in USD


    

def getAddressInfo(cryptoabbr, address):
    global KEY
    r = requests.get(f'https://chainz.cryptoid.info/{cryptoabbr}/api.dws?q=addressinfo&a={address}&key={KEY}')
    data = r.json()
    if DATA_TO_JSON == True:
        print(data)
    elif DATA_TO_JSON == False:
        print(f'Balance: {data['balance']} | Transaction Count: {data['transactionCount']} | First Block: {data['firstBlock']} | Last Block: {data['lastBlock']}')
    
    


    

def getRichestRank(cryptoabbr, address):
    global KEY
    r = requests.get(f'https://chainz.cryptoid.info/{cryptoabbr}/api.dws?q=richrank&a={address}&key={KEY}')
    print(r.text) # Prints the rank of the users address in terms of amount of crypto being held inside 
    





def getTotalRecievedAmount(cryptoabbr, address):
    global KEY
    r = requests.get(f'https://chainz.cryptoid.info/{cryptoabbr}/api.dws?q=getreceivedbyaddress&a={address}&key={KEY}')
    print(r.text) # prints the amount the wallet has recieved 





def getTransactionSummary(cryptoabbr, txhash):
    global KEY
    r = requests.get(f'https://chainz.cryptoid.info/{cryptoabbr}/api.dws?q=txinfo&t={txhash}&key={KEY}')
    data = r.json()
    print(data) # prints all the transaction data in json when given a txid




def getRecentTransactions(cryptoabbr, txhash,):
    global KEY
    r = requests.get(f'https://chainz.cryptoid.info/{cryptoabbr}/api.dws?q=lasttxs&key={KEY}&t={txhash}')
    data = r.json()
    print(data) # prints the 10 most recent transactions given a transaction hash do not include coinbase and stake transactions



    
