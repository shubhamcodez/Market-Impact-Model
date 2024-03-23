import os
import sys
import unittest
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

# Set the directory where the tests are located
tests_dir = 'Tests'

# Create a test suite
suite = unittest.TestSuite()

# Load all test cases from the Tests directory
loader = unittest.TestLoader()
for filename in os.listdir(tests_dir):
    if filename.endswith('.py'):
        test_module = loader.discover(tests_dir, pattern=filename)
        suite.addTests(test_module)

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