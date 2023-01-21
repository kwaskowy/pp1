class Arrays():

    @staticmethod
    def print_in_col(array):
        for c in array:
            print(c)
    def print_wit_commas(array):
        for x in array:
            if x==array[-1]:
                print(x)
            else: print(x,end=", ")
    def tesame(number_of_array_elements,value_of_array_elements):
        array=[]
        i=0
        while i<number_of_array_elements:
            array.append(value_of_array_elements)
            i+=1
        print(array)
    def ruzni(number_of_array_elements, value_from, value_to):
        from random import randint
        array=[]
        i=0
        losuwa= randint(value_from,value_to)
        while i<number_of_array_elements:
            array.append(losuwa)
            losuwa= randint(value_from,value_to)
            i+=1
        print(array)
    def szukane(array,value_from,value_to):
        ilosc=0
        print("Content of array:")
        for x in array:
            print(x, end=" ")
        for x in range(len(array)):
            if value_from<=array[x]<=value_to:
                ilosc+=1
        print(f"\nNumber of values in range {value_from}:{value_to} is {ilosc}")

my_array = [4,1,8,7,2]
Arrays.print_in_col(my_array)
print()
Arrays.print_wit_commas(my_array)
print()
Arrays.tesame(10,4)
print()
Arrays.ruzni(20,-7,8)
print()
Arrays.szukane([1,2,1,2,4,5,1,-1,0.5,-0.25,-0.75,1,2,4,1,4,2,-0.88,-0.55,1,7,10],-1,1)
