import urllib2
import re
array = []
with open("pages.txt", "r") as ins:
    for line in ins:
        array.append(line)
for page in array:
	print("-----------------------------\n")
	print(x);
	req = urllib2.Request("domain"+page)
	try:
	    resp = urllib2.urlopen(req)
	except urllib2.HTTPError as e:
	    if e.code == 404:
	    	print("404 for " + x)
	    	continue
	        # do something...
	        # ...
	except urllib2.URLError as e:
		if e:
			continue
	    # Not an HTTP-specific error (e.g. connection refused)
	    # ...
	else:
	    tmp = resp.read()
	values  = re.findall(r'stuff\"><b>(.+?)<.*>(.+?)</div>',tmp, re.MULTILINE)
	if values:
		output = open('subDir/'+x[:-1]+'.txt','w')  #subtract extra character '?' from string
		val2  = re.findall(r'otherStuff(.+?)<.*>(.+?)</div>',tmp, re.MULTILINE)
		output.write(x + '\n')
		if val2:
			print(val2)
			for val in val2:
				s = "="
				output.write(s.join(val)+'\n')
		for val in values:
			s = "="
   			output.write(s.join(val)+'\n') 
	  output.close()
	#else:
		#print("noValues");
	getImage = re.findall(r'href="(.+?)" class="image image-thumbnail"',tmp)
	if getImage: #get information from URL found in page, like an image
		#print(getImage[0])
		img = urllib2.urlopen(getImage[0]).read()
		f = open('subDir/' + x[:-1]+'.img','w') #subtract extra character '?' from string
		f.write(img)
		f.close()
	#else:
		#print("NoImage")
