def k2k(temp):
	return ((temp - 32) *(5.0/float(9)) + 273.15)
	
def k2c(temp):
	return temp - 273.15
	
def f2c(temp):
	temp_k = f2k(temp)
	result = k2c(temp_k)
	return result