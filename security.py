from werkzeug.security import safe_str_cmp

from models.user import UserModel


#參數帶入尋找系統中的變量   authenticate = 認證
def authenticate(username, password):
    #將傳進來的userName拿去mapping資料庫 , if 有此人 且 密碼相同，則返回user
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user


"""
payload參數 從request來
payload['identity'] which is user id
"""
def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
