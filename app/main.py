import waiter as wt
def print_order(ordered, unavailable):
    ordered_str = ", ".join(ordered)
    unavailable_str = ", ".join(unavailable)

    print(f"Your order is: {ordered_str}")
    print(f"Unfortunately we don't have: {unavailable_str}\n")
    
def mainB():
    backup_order = """
    {
        "dish": "MacCrispy",
        "quantity": 1,
        "comment": "without pickle"
    },
    {
        "dish": "French Fries",
        "quantity": 3,
        "comment": ""
    },
    {
        "dish": "Mac Double",
        "quantity": 2,
        "comment": ""
    },
    {
        "dish": "Chicken Biriani",
        "quantity": 1,
        "comment": "Spicy"
    },
    {
        "dish": "Coke",
        "quantity": 1,
        "comment": ""
    }"""
    waiter = wt.Waiter("")
    dict_order = waiter.json_to_dict(backup_order)
    ordered, unavailable = waiter.process_order(dict_order)
    print_order(ordered, unavailable)

def main():
    order_str = """
    I would like to order McCrispy without pickle and 5 large french fries. Change 2 of french 
    fries to 2 Big Mac and add a Coke. Also add one Chicken Biriani.
    """.strip()
    waiter = wt.Waiter(order_str)
    ordered, unavailable = waiter.take_order()
    print_order(ordered, unavailable)


if __name__ == "__main__":
    # main()
    mainB()