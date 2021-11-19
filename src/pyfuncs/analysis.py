def profile(module):
    """
    接口分析Api性能, body 需增加__func 调用的方法，其他入参与原Api保存一直
    Example:
        get_todo_list 方法调用
        module: xxx.my_page.repository
        body: {"__func": "Repository().get_todo_list('research_diabetes_dm2_standard', False, None)"}

        patient_list 接口调用
        module: xxx.keyan.detail.service
        body: {"__func": "Service().patient_list()", "project_id":"232c88ee-c474-4135-8e2b-4a433f5aefb0","start":0,"size":50}

    :param module: 要引入的模块
    :return:
    """
    data = WebContext.current().request.data //  body 数据, 需要替换成自己的框架的
    try:
        module = import_module(module)
        assert data.get('__func'), "__func 参数必须存在"
        nums = data.get('__nums', 50)  # 输出条数
        sort_field = data.get('__sort_field', 'cumulative')  # 排序方式

        func = """{}.{}""".format("module", data.get('__func'))
        filename = '/tmp/{}'.format(now('%Y%m%d%H:%M:%S'))
        # 使用locals() 是因为使用import_module否则找不到包
        cProfile.runctx(func, {}, locals(), filename=filename)

        stream = StringIO.StringIO()
        p = pstats.Stats(filename, stream=stream)
        p.sort_stats(sort_field).print_stats(nums)

        # 输出调用的该方法的函数
        if data.get('__callers_name'):
            p.print_callers(.5, data.get('__callers_name'))

        # 输出该方法调用哪些函数
        if data.get('__callees_name'):
            p.print_callees(data.get('__callees_name'))

        os.unlink(filename)
        resp = stream.getvalue()
        stream.close()
        return resp
    except Exception as e:
        return e.message
