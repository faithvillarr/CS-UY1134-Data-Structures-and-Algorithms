import ctypes  # provides low-level arrays

def make_array(n):
    return (n * ctypes.py_object)()

class ArrayList:
    def __init__(self):
        self.data_arr = make_array(1)
        self.capacity = 1
        self.n = 0


    def __len__(self):
        return self.n


    def append(self, val):
        if (self.n == self.capacity):
            self.resize(2 * self.capacity)
        self.data_arr[self.n] = val
        self.n += 1


    def resize(self, new_size):
        print("new size is : "+str(new_size))
        new_array = make_array(new_size)
        for i in range(self.n):
            new_array[i] = self.data_arr[i]
        self.data_arr = new_array
        self.capacity = new_size


    def __getitem__(self, ind):
        if (not (0 <= ind <= self.n - 1)):
            raise IndexError('invalid index')
        return self.data_arr[ind]


    def __setitem__(self, ind, val):
        if (not (0 <= ind <= self.n - 1)):
            raise IndexError('invalid index')
        self.data_arr[ind] = val


    def __iter__(self):
        for i in range(len(self)):
            yield self.data_arr[i]  #could also yield self[i]


    def extend(self, iter_collection):
        for elem in iter_collection:
            self.append(elem)

    def __repr__(self):
        res_str = "["
        for i in range(0,self.n-1):
            res_str += str(self.data_arr[i]) + ", "
        res_str += str(self.data_arr[self.n-1])
        res_str += "]"
        return res_str

    def __add__(self, other):
        res_arr = ArrayList()
        print(str(self.n+other.n))
        new_size = self.n + other.n
        res_arr.resize(new_size)
        print("Size of new array if "+str(res_arr.n))
        for i in range(self.n):
            res_arr[i] = self[i]
        for i in range(self.n, self.n + other.n):
            res_arr[i] = other[i-self.n]
        return res_arr

def main():
    arr1 = ArrayList()
    arr2 = ArrayList()
    for i in range(1,4):
        arr1.append(i)
   # print(arr1)
    for i in range(4,7):
        arr2.append(i)
   # print(arr2)
    arr3 = ArrayList()
    arr3 = arr1 + arr2
    print(arr3)

main()