from django.utils import simplejson
from dajaxice.decorators import dajaxice_register
from dajax.core import Dajax
from bitcoinService import BitcoinService
import logging
from random import randint

logger = logging.getLogger(__name__)

@dajaxice_register
def sayhello(request, depositeAddress):
    print "sayhello:", request, depositeAddress
    return simplejson.dumps({'message': 'Hello World',
                             'depositeAddress': depositeAddress})
@dajaxice_register
def getBalance(request, depositeAddress):
    logger.debug("getBalance: %s" % depositeAddress)
    
    b = BitcoinService()
    depositeBalance = b.getreceivedbyaddress(depositeAddress)
    return simplejson.dumps({'depositeBalance': depositeBalance})

@dajaxice_register
def playRound(request, depositeAddress, betAmount):
    logger.debug("playRound: %s %s" % (depositeAddress, betAmount))
    
    b = BitcoinService()
    depositeBalance = b.getreceivedbyaddress(depositeAddress)
    responseDict = {}

    # Valid betAmount?
    if betAmount.strip() == "":
        print "[-] Invalid bet amount:", betAmount
        responseDict['validBet'] = False
        return simplejson.dumps(responseDict)
    responseDict['validBet'] = True

    betAmount = float(betAmount)
    depositeBalance = float(depositeBalance)

    # Sufficent funds?
    if float(betAmount) > float(depositeBalance):
        print "betAmount > depositeBalance"
        responseDict['sufficentFunds'] = False
        return simplejson.dumps(responseDict)
    responseDict['sufficentFunds'] = True

    # isWin?
    isWin = randint(0, 1)
    responseDict['isWin'] = isWin

    # Update accounts
    if isWin:
        depositeBalance += betAmount
    else:
        depositeBalance -= betAmount

    depositeBalance = b.getreceivedbyaddress(depositeAddress)
    
    responseDict['betAmount'] = betAmount
    responseDict['depositeBalance'] = depositeBalance
    return simplejson.dumps(responseDict)

@dajaxice_register
def withdrawFunds(request, depositeAddress, withdrawAddress):
    b = BitcoinService()
    responseDict = {}

    if withdrawAddress.strip() == "" or not b.isValidAddress(withdrawAddress):
        responseDict['isValidAddress'] = False
        return simplejson.dumps(responseDict)
    responseDict['isValidAddress']= True

    depositeBalance = b.getreceivedbyaddress(depositeAddress)
    #b.senttoaddress(withdrawAddress, depositeBalance, "Thanks for playing All or Nothing!")
    greatSuccess = True

    if greatSuccess:
        responseDict['greatSuccess'] = True
        #XXX update model
    
    responseDict['depositeBalance'] = 0
    return simplejson.dumps(responseDict)