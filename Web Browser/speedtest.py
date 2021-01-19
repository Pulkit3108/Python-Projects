import speedtest
test=speedtest.Speedtest()
print('Checking Download Speed....')
down=test.download()
print(f'Downloading Speed : {down/(1000000)} Mbps')
print('Checking Uploading Speed....')
up=test.upload()
print(f'Uploading Speed : {up/(1000000)} Mbps')
