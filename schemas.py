from flask_marshmallow import Marshmallow

from models import Salary

ma = Marshmallow()


class SalarySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Salary
        fields = (
            "id",
            "employeename",
            "jobtitle",
            "basepay",
            "overtimepay",
            "otherpay",
            "benefits",
            "totalpay",
            "totalpaybenefits",
            "year",
            "notes",
            "agency",
            "status")
