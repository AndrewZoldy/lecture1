import random


def sort_rows(table):
    for ind in range(len(table)):
        minimum = sum(table[ind])
        minimal_list = table[ind]
        for i in table[ind:]:
            if sum(i) < minimum:
                minimum = sum(i)
                minimal_list = i
        table.insert(ind, table.pop(table.index(minimal_list)))
    return table


def sort_cols(table):
    for ind in range(len(table[0])):
        minimum = 0
        minimal_index = ind
        for i in table:
            minimum += i[ind]
        for ind_2 in range(len(table[0]))[ind:]:
            counter = 0
            for i in table:
                counter += i[ind_2]
            if counter >= minimum:
                continue
            else:
                minimum = counter
                minimal_index = ind_2
        for row_ind in range(len(table)):
            table[row_ind].insert(ind, table[row_ind].pop(minimal_index))
            # table_sorted_cols[row_ind].append(table_sorted[row_ind][minimal_index])
    return table


def generate_table(number):
    unique_set = set()
    table = []
    for n in range(number):
        row = []
        for m in range(number):
            while True:
                integer = random.randint(1, number**2)
                if integer in unique_set:
                    continue
                else:
                    row.append(integer)
                    unique_set.update({integer})
                    break
        table.append(row)
    for row in table:
        print(('{:>5}  '*len(row)).format(*row))
    return table


number = int(input())
table = generate_table(number)
sorted_rows = sort_rows(table)
table_sorted = sort_cols(sorted_rows)
print('\nSorted:\n')
for row in table_sorted:
    print(('{:>5}  '*len(row)).format(*row))