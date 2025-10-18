from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from graph.main_graph import app as workflow_app  

class QueryRequest(BaseModel):
    query: str

app = FastAPI(title="LangGraph API", version="1.0")

@app.post("/run")
def run_query(request: QueryRequest):
    if not request.query.strip():
        raise HTTPException(status_code=400, detail="Query cannot be empty")
    try:
        result = workflow_app.invoke({"query": request.query})
        return {"success": True, "result": result["generation"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

