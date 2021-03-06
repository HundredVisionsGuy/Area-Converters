# AreaConverters.py
# By ____
# You will write 2 functions: yardsToAcres() and kmToAcres()
# You will want to test the two functions by running this document
# WARNING: you must NOT change the function names, or you will fail the tests
# NOTE: you are welcome to choose the variable names for your parameters
#       (they will not affect the tests).

# TODO: write a function titled, yardsToAcres() that...
#       receives two numbers (width & height)
#       calculates acres: area * 0.000207
#       returns a floating point number (acres)


# TODO: write a function titled, kmToAcres() that...
#       receives two numbers (width & height)
#       calculates acres: area * 247.10538
#       returns a floating point number (acres)


##################################
## DO NOT CHANGE THE CODE BELOW ##
##################################

if __name__ == '__main__':
    # Test yardsToAcres()
    ac = yardsToAcres(100, 300)
    print "An area with a width of 100 yards and a length of 300 yards "
    print "is " + str(ac) + " acres."
    # output should be 6.21

    # Other Sample Inputs w/Expected Outputs
    # 15, 15 => 0.046575
    # 40, 20 => 0.1656

    # Test kmToAcres
    # Sample Inputs => Expected Output
    # 10, 10 => 24710.538
    # 25, 25 => 154440.8625
    # 25, 3 => 18532.9035
    
