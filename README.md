# Aprioripy: Apriori algorithm.
<img src="4742c1dc-c672-4194-96c3-54ee5b88a840.jpeg">

## Apriori algorithm usage:

```python
from aprioripy import Aprioripy


test_table = pd.DataFrame({
    "items": ["1, 3, 4", "2, 3, 5", "1, 2, 3, 5", "2, 5"]
})

print("Test table")
print(test_table)

ap = Aprioripy(table=test_table)

print("\nFrequency table:")
print(ap.frequency_table)

ap.apriori(min_support=0.5)

for i in ap.association_tables.keys():
    print("\nAssociation table " + i)
    print(ap.association_tables[i])

test_table = pd.DataFrame(
    [
        {"1": 1, "2": 0, "3": 1, "4": 1, "5": 0},
        {"1": 0, "2": 1, "3": 1, "4": 0, "5": 1},
        {"1": 1, "2": 1, "3": 1, "4": 0, "5": 1},
        {"1": 0, "2": 1, "3": 0, "4": 0, "5": 1}
    ]
)

print("\nTest table:")
print(test_table)

ap = Aprioripy(table=test_table, convert=False)

print("\nFrequency table:")
print(ap.frequency_table)

ap.apriori(min_support=0.5)

for i in ap.association_tables.keys():
    print("\nAssociation table " + i)
    print(ap.association_tables[i])
```
## Output:

```
Test table
        items
0     1, 3, 4
1     2, 3, 5
2  1, 2, 3, 5
3        2, 5

Frequency table:
  item  frequency
0    1       0.50
1    2       0.75
2    3       0.75
3    4       0.25
4    5       0.75

Association table L1
  item  frequency
0    1       0.50
1    2       0.75
2    3       0.75
4    5       0.75

Association table L2
  itemset  frequency
1  (1, 3)       0.50
4  (2, 3)       0.50
6  (2, 5)       0.75
8  (3, 5)       0.50

Association table L3
     itemset  frequency
7  (2, 3, 5)        0.5

Test table:
   1  2  3  4  5
0  1  0  1  1  0
1  0  1  1  0  1
2  1  1  1  0  1
3  0  1  0  0  1

Frequency table:
  item  frequency
0    1       0.50
1    2       0.75
2    3       0.75
3    4       0.25
4    5       0.75

Association table L1
  item  frequency
0    1       0.50
1    2       0.75
2    3       0.75
4    5       0.75

Association table L2
  itemset  frequency
1  (1, 3)       0.50
4  (2, 3)       0.50
6  (2, 5)       0.75
8  (3, 5)       0.50

Association table L3
     itemset  frequency
7  (2, 3, 5)        0.5
```
