import main

test_passed = True

def test():
	passed = True
	result = main.xor(0,0)
	if result == 1:
		passed = False
	result = main.xor(0,1)
	if result == 0:
		passed = False
	result = main.xor(1,0)
	if result == 0:
		passed = False
	result = main.xor(1,1)
	if result == 1:
		passed = False
	return passed

test_passed = test()

if test_passed == True:
	print("Test passed! :)")
elif test_passed == False:
    	print("Test not passed :(")
