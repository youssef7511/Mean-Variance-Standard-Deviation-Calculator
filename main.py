import mean_var_std
from unittest import main

# Test the function with the example
result = mean_var_std.calculate([0,1,2,3,4,5,6,7,8])
print("Result for [0,1,2,3,4,5,6,7,8]:")
for key, value in result.items():
    print(f"'{key}': {value}")

print("\n" + "="*50 + "\n")

# Test with error case
try:
    mean_var_std.calculate([1,2,3,4,5])
    print("This shouldn't print - error should be raised")
except ValueError as e:
    print(f"ValueError correctly raised: {e}")

print("\n" + "="*50 + "\n")

# Run unit tests if test_module.py is available
print("Running unit tests...")
try:
    import test_module
    main(module='test_module', exit=False, verbosity=2)
except ImportError:
    print("test_module.py not found - skipping unit tests")