
s1 = {1,2,3,7}
s2 = {2,3,4,5,6}


# 1. union
print("\n1.Union\n")
print("Set union:",s1.union(s2))
print("Union method: First set is",s1,"and second set is",s2)  
# using union new set is created and no change happens in the primary set

# 2. update
print("\n2.Update\n")
s1.update(s2)
print("Union using update method: First set is",s1,"and second set is",s2)  
# using update the union is stored in primary set

s1 = {1,2,3,7}
s2 = {2,3,4,5,6}

# 3. intersection
print("\n3.Intersection\n")
print("Intersection is",s1.intersection(s2))

# 4. intersection_update
print("\n4.Intersection Update\n")
s1.intersection_update(s2)
print("Intersection after update method:",s1)

s1 = {1,2,3,7}
s2 = {2,3,4,5,6}

# 5. symmetric difference
print("\n5.Symmetric Difference\n")
print("Symmetric difference:",s1.symmetric_difference(s2))

# 6. symmetric difference update
print("\n6.Symmetric Difference Update\n")
s1.symmetric_difference_update(s2)
print("Symmetric difference using update:",s1)

s1 = {1,2,3,7}
s2 = {2,3,4,5,6}

# 7. Difference
print("\n7.Difference\n")
print("Difference is:",s1.difference(s2))

# 8. Difference Update
print("\n8.Difference Update\n")
s1.difference_update(s2)
print("Difference update:",s1)

s1 = {1,2,3,7}
s2 = {2,3,4,5,6}

# 9. Disjoint sets
print("\nSet Disjoint:",s1.isdisjoint(s2))

# 10. Superset
s1 = {1,2,3,7}
s2 = {2,3}
print("\nIs s1 superset of s2:",s1.issuperset(s2))
print("Is s2 superset of s1:",s2.issuperset(s1))

# 11. Subset
s1 = {1,2,3,7}
s2 = {2,3}
print("\nIs s1 subset of s2:",s1.issubset(s2))
print("Is s2 subset of s1:",s2.issubset(s1))

# 12. Add element in set
s1 = {1,2,3,4,5}
s1.add(10)
print("\nSet after adding 10:",s1)

# 13. Remove element from set
s1.remove(3)
print("\nSet after removing 3:",s1)

# 14. Discard
s1.discard(10)
print("\nSet after discarding 10:",s1)

'''
The difference between remove and discard is if we try to delete an item 
which is not present in set, then remove() raises an error, 
whereas discard() does not raise any error.
'''

# 15. Pop
print("\nPopped element is:",s1.pop()) # removes random element from set

# 16. Del
# completely deletes the set
s2 = {2,3,4,6,8}
del s2

# 17. Clear
s1.clear()
print("\nSet after Clear is:",s1)

# Check if element in set
s1 = {3,2,5,1}
if 10 in s1:
    print("\nYes")
else:
    print("\nNo")
