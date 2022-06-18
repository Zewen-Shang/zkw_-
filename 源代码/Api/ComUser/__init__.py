from . import AddComUser
# from . import DeleteRentInfo
from . import QueryComUser
from . import UpdateComUser
def useRoute(app):
    app.route("/api/com_user/add",methods=["POST"])(AddComUser.AddComUser)
    # app.route("/api/rent_info/delete",methods=["POST"])(DeleteRentInfo.DeleteRentInfo)
    app.route("/api/com_user/query",methods=["POST"])(QueryComUser.QueryComUser)
    app.route("/api/com_user/update",methods=["POST"])(UpdateComUser.UpdateComUser)