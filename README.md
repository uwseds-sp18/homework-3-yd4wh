# HW3 - Exceptions and testing

In this homework, you'll modify the codes you developed in HW2 to use exceptions and write unittests.

1. (3 points). Create a python module named homework3.py that performs the operates in the same way as create_dataframe in homework 2. But homework3.py should also check that there is a valid path to the database (the function argument). If the path is not valid, a ValueError exception is raised.

2. (4 points). Create a python module named test_homework3.py that tests the code in homework3.py. Write at least 3 tests (e.g., checking column names, number of rows, and verifying which columns constitute a key). Also, write a test to check that the correct exception is generated when an invalid path is provided.
