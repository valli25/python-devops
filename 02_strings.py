sample_str = "this is a sample string"
print (sample_str)

# How to take individual character from a string

print (sample_str[8])

# slicing

sub_str = sample_str[2:7]
print(sub_str)

sub_str = sample_str[:]
print(sub_str)

sub_str = sample_str[1:]
print(sub_str)

sub_str = sample_str[:5]
print(sub_str)

sub_str = sample_str[::2]
print(sub_str)

# reverse a string
sub_str = sample_str[::-1]
print(sub_str)

# length of a string
len_str = len(sample_str)
print("length of a string:", len_str)