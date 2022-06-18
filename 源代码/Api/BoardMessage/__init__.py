from . import AddBoardMessage
from . import DeleteBoardMessage
from . import QueryBoardMessage
from . import UpdateBoardMessage
def useRoute(app):
    app.route("/api/board_message/add",methods=["POST"])(AddBoardMessage.AddBoardMessage)
    app.route("/api/board_message/delete",methods=["POST"])(DeleteBoardMessage.DeleteBoardMessage)
    app.route("/api/board_message/query",methods=["POST"])(QueryBoardMessage.QueryBoardMessage)
    app.route("/api/board_message/update",methods=["POST"])(UpdateBoardMessage.UpdateBoardMessage)