from decouple import config
from flask import Flask, jsonify, request

from exceptions import APIError
from extensions import db
from models import Salary
from schemas import SalarySchema
from utils import build_link_header, validate_per_page

server = Flask(__name__)

server.config["SQLALCHEMY_DATABASE_URI"] = config('DATABASE_URI')

db.init_app(server)


@server.route("/salaries")
def salaries():
    # process query parameters
    page = request.args.get("page", 1, type=int)
    per_page = validate_per_page(request.args.get("per-page", 100, type=int))

    # query
    salaries = Salary.query.paginate(page=page, per_page=per_page)

    # map with schema
    salaries_schema = SalarySchema()
    salaries_dumped = salaries_schema.dump(salaries.items, many=True)

    # combined results with pagination
    results = {
        "results": salaries_dumped,
        "pagination":
            {
                "count": salaries.total,
                "page": page,
                "per_page": per_page,
                "pages": salaries.pages,
            },
    }

    # paginated link headers
    base_url = config('BASE_URL')
    link_header = build_link_header(
        query=salaries, base_url=base_url, per_page=per_page
    )
    return jsonify(results), 200, link_header


@server.errorhandler(APIError)
def handle_exception(err):
    """Return custom JSON when APIError or its children are raised"""
    # credit:
    response = {"error": err.description, "message": ""}
    if len(err.args) > 0:
        response["message"] = err.args[0]
    # Add some logging so that we can monitor different types of errors
    server.logger.error("{}: {}".format(err.description, response["message"]))
    return jsonify(response), err.code


if __name__ == '__main__':
    server.run(host='0.0.0.0', port=1337)
