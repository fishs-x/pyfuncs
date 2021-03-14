# coding=utf-8
from collections import OrderedDict


def data_sort(data):
    """支持list、dict 递归排序
    :param list|dict data: 支持list或者dict递归排序
    :rtype list| OrderedDict
    """
    # 判断数据类型, 不是list、dict 不需要排序
    if not isinstance(data, (list, dict)):
        return data

    # 判断数据类型, 如果是list 循环调用即可
    if isinstance(data, list):
        data.sort()
        return [data_sort(x) for x in data]

    # 如果数据类型为 dict
    order_dict = OrderedDict()
    for key in sorted(data):
        if data[key] and isinstance(data[key], list):
            data[key].sort()
            val = [data_sort(x) for x in data[key]]
        elif data[key] and isinstance(data[key], dict):
            val = OrderedDict()
            for k in sorted(data[key].keys()):
                val[k] = data_sort(data[key][k])
        else:
            val = data[key]
        order_dict[key] = val
    return order_dict
