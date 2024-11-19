from api import app, db
from api import models
from ariadne import load_schema_from_path, make_executable_schema, graphql_sync, snake_case_fallback_resolvers, ObjectType
from ariadne.explorer import ExplorerGraphiQL
from flask import request, jsonify
from api.queries import resolve_students, resolve_student, resolve_assignment, resolve_assignments, resolve_scores, resolve_scores_student
from api.mutations import resolve_create_student, resolve_delete_student, resolve_create_assignment, resolve_delete_assignment, resolve_create_score, resolve_delete_score

query = ObjectType("Query")
query.set_field("students", resolve_students)
query.set_field("student", resolve_student)
query.set_field("assignments", resolve_assignments)
query.set_field("assignment", resolve_assignment)
query.set_field("scores", resolve_scores)
query.set_field("scoresStudent", resolve_scores_student)

mutation = ObjectType("Mutation")
mutation.set_field("createStudent", resolve_create_student)
mutation.set_field("deleteStudent", resolve_delete_student)
mutation.set_field("createAssignment", resolve_create_assignment)
mutation.set_field("deleteAssignment", resolve_delete_assignment)
mutation.set_field("createScore", resolve_create_score)
mutation.set_field("deleteScore", resolve_delete_score)


type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(type_defs, [query, mutation], snake_case_fallback_resolvers)


@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return ExplorerGraphiQL().html(None)


@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()

    success, result = graphql_sync(schema,data,context_value=request,debug=app.debug)

    status_code = 200 if success else 400
    return jsonify(result), status_code