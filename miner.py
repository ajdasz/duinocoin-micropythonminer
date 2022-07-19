import urequests
import uhashlib as hashlib
import urllib
import binascii
import time
import _thread

#Please use only alphanumeric in variables starting at miner!
minerUsername = "ajdasz"
minerPassword = ""
minerIdentifierName = "MicropythonMiningRig"

legacyJobUrl = "http://51.15.127.80/legacy_job"

def displayResponseError(urequestResponse):
        print("General API Error. RAW Response from API: '" + str(urequestResponse.text) + "', status code: " + str(urequestResponse.status_code))

def getJob():
        print("Trying get job..")
        requestResult = urequests.get(legacyJobUrl + "?u=" + str(minerUsername) + "&i=" + str(minerIdentifierName))
        if "," in requestResult.text:
                resultJob = requestResult.text.split(',')
        else:
                resultJob = []
        if len(resultJob) is not 3:
                print("Cannot get job, waiting second and try again.")
                displayResponseError(requestResult)
                time.sleep(1)
                getJob()
        requestResult.close()
        print("Received job, difficulty: " + resultJob[2])
        return resultJob

def sendJobResult(resolveNumber, expectedResult, hashRate, shareTime):
        requestResult = urequests.post(legacyJobUrl + "?u=" + minerUsername + "&r=" + str(resolveNumber) + "&k=" + str(minerPassword) + "&s="+str(minerIdentifierName)+"&i=" + str(minerIdentifierName) + "&j=" + str(expectedResult) + "&h=" + str(hashRate) + "&b=" + str(shareTime))
        if requestResult.text == 'GOOD':
                requestResult.close()
                return True
        if requestResult.text not in ['GOOD']:
                displayResponseError(requestResult)
                requestResult.close()
                return False

def startMine():
    print("Starting mining")
    time.sleep(1)
    print("Mine started")
    while True:
        jobData = getJob()
        jobHash = jobData[0]
        expectedResult = jobData[1]
        difficulty = jobData[2]
        baseHash = hashlib.sha1(str(jobHash).encode('ascii'))
        resolveNumber = 0
        startTime = time.time()
        while resolveNumber < (100 * int(difficulty) + 1):
                resolveNumber += 1
                tempHash = hashlib.sha1(jobHash+str(resolveNumber))
                jobResultHash = binascii.hexlify(tempHash.digest()).decode('ascii')
                if jobResultHash == expectedResult:
                        shareTime = time.time() - startTime
                        hashRate = resolveNumber / shareTime
                        if sendJobResult(resolveNumber,expectedResult, hashRate, shareTime) is True:
                                print("Accepted job")
                        else:
                                print("Not accepted job!")
                        print("Hashrate: "+str(hashRate))
                        print("Sharetime: "+str(shareTime))
                        break


while True:
    startMine()