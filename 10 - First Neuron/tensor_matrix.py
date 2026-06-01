import torch 

X = torch.tensor([
    [10, 11, 12, 13], 
    [38, 39, 40, 41], 
    [100, 101, 102, 103], 
    [150, 151, 152, 153]
])
# print(X.size(1))
print(X[:, 2])