from bitcoinlib.wallets import Wallet
import bitcoinlib.wallets as w
from bitcoinlib.mnemonic import Mnemonic
from bitcoinlib.services.bitcoind import BitcoindClient
from bitcoinlib.services.services import Service

passphrase = 'large number order north island smart deal clever upgrade avocado city unhappy'
NETWORK = 'testnet' 

# Remember to send bitcoin back to tb1qm5tfegjevj27yvvna9elym9lnzcf0zraxgl8z2

if not (w.wallet_exists('myTestWallet')):
    wallet = Wallet.create('myTestWallet', keys=passphrase, network=NETWORK)
    print("Wallet created")
else:
    print("Wallet exists")
    
myWallet = Wallet('myTestWallet')

#w.wallet_empty('myTestWallet')

print("-------------------------")
print(myWallet.addresslist())
print("-------------------------")
print(myWallet.new_key())
print("-------------------------")
print(myWallet.addresslist())

myWallet.send_to('mhmDhpgADWxHQLR7EVDiHQBAGHgCL5XxjQ', '0.00005 TBTC', fee=500)
myWallet.scan()
myWallet.info()

for i in range(1,21):
    print("within (i) blocks you need (Service(network='testnet').estimatefee(i))")
    
# '1EUEDt4yZgkg1T2pesk69UyqQUExxaQjsG'
