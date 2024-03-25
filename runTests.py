import os
import sys
import unittest

# Set the directory where the tests are located
tests_dir = 'Tests/RegressionTest'

loader = unittest.TestLoader()
suite = loader.discover(start_dir=tests_dir, pattern='Test_*.py')

# Run the test suite
runner = unittest.TextTestRunner()
result = runner.run(suite)

# Print a summary of the test results
num_failures = len(result.failures)
num_errors = len(result.errors)
num_skipped = len(result.skipped)
num_tests = result.testsRun

print(f'Tests run: {num_tests}')
print(f'Failures: {num_failures}')
print(f'Errors: {num_errors}')
print(f'Skipped: {num_skipped}')

# Exit with a non-zero status code if there were any failures or errors
if num_failures or num_errors:
    exit(1)