sample_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
switched_dict = {}

for key in sample_dict.keys():
    switched_dict[sample_dict[key]] = key

print(f"Sample Map: {sample_dict}")
print(f"Switched Map : {switched_dict}")

# Result
# Sample Map: {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
# Switched Map : {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
