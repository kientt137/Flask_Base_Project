from ..Config import ma
from ..Models import User


class UserSchemaList(ma.SQLAlchemyAutoSchema):
    class Meta:
        model      = User
        include_fk = True
