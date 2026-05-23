
def assert_http_business(response,auto_log):
    """
    通用断言
    """
    # 1.判断response是否为空
    if response is None:
        auto_log.error(f"http返回为空")
        raise ConnectionError(f"http请求异常:{response}")

    # 2.断言http状态码
    if response.status_code != 200:
        auto_log.error(f"http请求失败,状态码:{response.status_code}")
        raise RuntimeError(f"http请求异常{response.status_code}")

    # 判断json格式
    try:
        res = response.json()
    except Exception as e:
        auto_log.error("响应不是json格式")
        raise ValueError(f"响应格式异常:{e}")

    # 3.断言业务状态码
    if res.get("code") != 200:
        auto_log.error(f"业务响应失败,code:{res.get('code')},msg:{res.get('msg')}")
        raise AssertionError("业务code校验不通过")

    # 4.断言msg
    msg = res.get("msg","")
    success_keyword = ["成功"]
    if not any(key in msg for key in success_keyword):
        auto_log.error(f"返回信息异常:{msg}")
        raise AssertionError("返回提示不正确")

    return res