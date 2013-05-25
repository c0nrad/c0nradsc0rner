# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from bitcoinService import BitcoinService

def allOrNothing(request):

    if not request.POST:
        b = BitcoinService()
        newAddr = "189wXnbfPDaV7NxGu1GmgauyiuFP6Nk4Df" # b.generateAddress()
        depositeBalance = b.getreceivedbyaddress(newAddr)
        return render_to_response('allOrNothing.html', {
            'depositeAddress' : newAddr,
            'depositeBalance' : depositeBalance
        })
    xhr = request.GET.has_key('xhr')
    responseDict = {}
    addr = request.POST.get('addr', False)
    depositeBalance = b.getreceivedbyaddress(addr)
    responseDict.update({'depositeAddress' : addr,
                        'depositeBalance' : depositeBalance})
    if xhr:
        return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript')
    return render_to_response('weblog/ajax_example.html', response_dict)

    