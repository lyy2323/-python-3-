def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个涉及，知道没有未打印的涉及未知
    打印每个涉及后，都将其移动到列表completed_models中
    """
    while unprinted_designs:
        current_de