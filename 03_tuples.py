#there are 2 methods to create a tuple
# 1. ()
# 2. tuple()

# Behaviour: the are immutable
sample_tuple = ("Ansible", "Terraform","jenkins")

sample_ele = sample_tuple[1]
print(sample_ele)

sample_ele = sample_tuple[-1]
print(sample_ele)

# slicing 
sliced_tuple = sample_tuple[1:3]
print(sliced_tuple)

sliced_tuple_len = len(sliced_tuple)
print(sliced_tuple_len)

