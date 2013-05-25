from bitcoinrpc.authproxy import JSONRPCException, AuthServiceProxy

class BitcoinService:
    def __init__(self):
        self.access = AuthServiceProxy("http://root:heWDfRfDg@235429@127.0.0.1:8332")

    def getInfo(self):
        return self.access.getinfo()
        
    def getlistreceivedbyaddress(self, num):
        return self.access.listreceivedbyaddress(num)

    def getBalance(self):
        return self.access.getbalance()

    def isValidAddress(self, addr):
        return self.access.validateaddress(addr)

    def generateAddress(self):
        return self.access.getnewaddress()

    def getAccount(self, addr):
        return self.access.getaccount(addr)

    def getAccountAddr(self, account):
        return self.access.getaccountaddress(account)
    
    def getreceivedbyaddress(self, addr):
        return self.access.getreceivedbyaddress(addr)

    def sendtoaddress(self, addr, amount, comment=""):
        return self.acccess.sendtoaddress(addr, amount, comment)
        
if __name__ == "__main__":
    b = BitcoinService()
    print b.getBalance()

    print b.getAccountAddr("poptarts4liffe@gmail.com")
    
    myAddr2 = "1L55JMwb92nPYv8ph45bpNPUc5bVeUj2L9"
    myAddr = "189wXnbfPDaV7NxGu1GmgauyiuFP6Nk4Df"
    print b.getAccount(myAddr)