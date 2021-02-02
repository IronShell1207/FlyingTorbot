D = {'program':'qbittorrent','parameter1': f"--save-path={0}",'parameter2':None,"file-url-path":'https://droidapps.cf/Files/text.txt'}
if D['program'] is not None:
    print (D['program'])
for key in D:
    print(key, D[key])