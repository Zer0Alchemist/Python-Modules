def ft_count_harvest_recursive(day=1):
    if day == 1:
        ft_count_harvest_recursive.n = int(input("Days until harvest: "))
    if day > ft_count_harvest_recursive.n:
        print("Harvest time!")
        return
    print("day", day)
    ft_count_harvest_recursive(day + 1)
ft_count_harvest_recursive()
