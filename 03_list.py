# create a list

test_list = [1,2,3,4,5,6] # list()

sample_list = ["Ansible","Terraform","jenkins","docker","k8s"]

#indexing, slicing
sample_ele = sample_list[1]
print(sample_ele)

sample_ele = sample_list[5]
print(sample_ele)

sample_ele = sample_list[len(sample_list) - 1] 
#sample_list[-1]

print(sample_ele)

#slicing
sliced_list = sample_list[1:3] # ("terraform","jenkins")
print(sliced_list)

sliced_list_len = len(sliced_list)
print(sliced_list_len)

sample_list[1] = "shell"
print(sample_list)