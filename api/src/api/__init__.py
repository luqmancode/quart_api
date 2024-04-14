from quart import Quart, jsonify, request
from quart_schema import validate_request, validate_response

from api_schema.todo_schema import TodoIn, Todo

app = Quart(__name__)

@app.post("/echo")
async def echo():
    data = await request.get_json()
    return {"input": data, "extra": True} 

@app.get("/example")
async def example():
    return jsonify(["a", "b"])


@app.post("/todos/")
@validate_request(TodoIn)
@validate_response(Todo)
async def create_todo(data: Todo) -> Todo:
    return Todo(id=1, task=data.task, due=data.due)

def run() -> None:
    app.run(debug=True, reload=True)