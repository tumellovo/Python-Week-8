# Tuples

my_tuple = (1, 2, 3, 4, 5)

print(my_tuple)
print(my_tuple[0])
print(my_tuple[2])
print(my_tuple[-1])

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

conc_tuple = tuple1 + tuple2
rep_tuple = tuple1 * 3

print(conc_tuple)
print(rep_tuple)

#Tuples are suitable for situations where you want to store a collection of elements that should not be changed throughout your programs execution.
#Some common uses for tuples include storing fixed collections of data such as; coordinates, RGB codes, database records, and so on