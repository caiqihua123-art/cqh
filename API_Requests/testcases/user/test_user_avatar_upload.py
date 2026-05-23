from API_Requests.business.user_api import User
from API_Requests.utils.assert_utils import assert_http_business
from API_Requests.utils.yaml_utils import picture_path

def test_user_avatar_upload(api, auto_log):
    """
    个人中心上传头像
    """
    user = User(api)
    response = user.upload_avatar(file_path=picture_path)
    data = assert_http_business(response, auto_log)

    assert data.get("imgUrl") is not None,"头像地址返回为空"
    auto_log.info(f"个人中心头像上传成功,头像地址:{picture_path}")