from . import RentInfo
from . import ComUser
from . import OrgUser
from . import OrgUserPend
from . import BoardMessage
def useRoute(app):
    RentInfo.useRoute(app)
    ComUser.useRoute(app)
    OrgUser.useRoute(app)
    OrgUserPend.useRoute(app)
    BoardMessage.useRoute(app)