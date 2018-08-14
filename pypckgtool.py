import json                      
import pip

def install(package):                                      
    return pip.main(['install', package])
with open('data.json') as depf:                                       
    data = json.load(depf)
    count =0

    for pckg in data['Dependencies']:
        #print pckg 
        #print data['Dependencies'][pckg]
        package = str(pckg) + '==' + str(data['Dependencies'][pckg])
        result = install(package)
        if result != 0:
            print package+ "installation failed"
        else:
            count = count +1
    if count == len(data['Dependencies']):
        print "success"
