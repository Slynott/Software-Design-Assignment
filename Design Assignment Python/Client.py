	#consumes data from IoT Gateway
	import urllib2
	import numpy as np
	import matplotlib.pyplot as plt
import time


	plt.title (Time V Light On)
	plt.xlabel(Light On)
	plt.ylabel(Time s)


	response = urllib2.urlopen('http://localhost:8080/')
	resp = response.read()


	plt.show()


	print resp


