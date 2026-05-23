from faker import Faker

def get_user_fake():
    """
    修改用户假数据
    """
    faker = Faker(locale='zh_CN')
    data = {
        "nickName": faker.name(),
        "email": faker.email(),
        "phonenumber": faker.phone_number(),
        "userName": faker.user_name()
    }
    return data


def get_dept_fake():
    """
    修改部门假数据
    """
    faker = Faker(locale='zh_CN')
    data = {
        "parentId": 110,
        'deptName': '研发部门',
        "orderNum": 1,
        "status": "0",
        "delFlag": "0",
        "leader": faker.name(),
        "phone": faker.phone_number(),
        "email": faker.email()
    }
    return data

if __name__ == '__main__':
    print(get_dept_fake())



