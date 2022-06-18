from . import AddRentInfo
from . import DeleteRentInfo
from . import QueryRentInfo
from . import UpdateRentInfo
def useRoute(app):
    app.route("/api/rent_info/add",methods=["POST"])(AddRentInfo.AddRentInfo)
    app.route("/api/rent_info/delete",methods=["POST"])(DeleteRentInfo.DeleteRentInfo)
    app.route("/api/rent_info/query",methods=["POST"])(QueryRentInfo.QueryRentInfo)
    app.route("/api/rent_info/update",methods=["POST"])(UpdateRentInfo.UpdateRentInfo)