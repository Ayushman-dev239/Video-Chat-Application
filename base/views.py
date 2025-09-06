from django.shortcuts import render
from django.http import JsonResponse
from agora_token_builder import RtcTokenBuilder
import random
import time


def getToken(request):
    appId = "8f5bb16832364abc96fb7294c674e266"
    appCertificate = 'bdd2f1304b7240deadbfa162f879aeb8'
    
    channelName = request.GET.get('channel')   # <-- FIXED HERE
    uid = random.randint(1, 230)
    
    expirationTimeInSeconds = 3600 * 24
    currentTimeStamp = int(time.time())  # better to cast to int
    privilegeExpiredTs = currentTimeStamp + expirationTimeInSeconds
    role = 1

    token = RtcTokenBuilder.buildTokenWithUid(
        appId, appCertificate, channelName, uid, role, privilegeExpiredTs
    )
    
    return JsonResponse({'token': token, 'uid': uid}, safe=False)

def lobby(request):
    return render(request,'base/lobby.html')

def room(request):
    return render(request,'base/room.html')
    