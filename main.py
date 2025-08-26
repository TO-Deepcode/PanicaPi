# main.py
from fastapi import FastAPI, Header, HTTPException, Query
from fastapi import Request
import httpx, os
from models import MsgPayload
from typing import Optional

API = "https://cryptopanic.com/api/developer/v2/posts/"
app = FastAPI()
messages_list: dict[int, MsgPayload] = {}

@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Hello"}

@app.get("/about")
def about() -> dict[str, str]:
    return {"message": "This is the about page."}

@app.post("/messages/{msg_name}/")
def add_msg(msg_name: str) -> dict[str, MsgPayload]:
    msg_id = max(messages_list.keys()) + 1 if messages_list else 0
    messages_list[msg_id] = MsgPayload(msg_id=msg_id, msg_name=msg_name)
    return {"message": messages_list[msg_id]}

@app.get("/messages")
def message_items() -> dict[str, dict[int, MsgPayload]]:
    return {"messages": messages_list}

# Hem /posts hem /posts/ çalışsın
@app.get("/posts")
@app.get("/posts/")
async def posts(
    request: Request,
    filter: Optional[str] = None,
    currencies: Optional[str] = None,
    page: int = 1,
    # Opsiyonel: GPT gönderirse CP'ye iletelim
    kind: Optional[str] = Query(default=None, pattern="^(news|media)$"),
    regions: Optional[str] = None,
    public: Optional[bool] = None,
    from_: Optional[str] = Query(default=None, alias="from"),
    x_cp_key: Optional[str] = Header(None, alias="X-CP-KEY"),
):
    key = x_cp_key or os.getenv("CP_KEY")
    if not key:
        raise HTTPException(401, "Missing X-CP-KEY (or CP_KEY env)")

    params = {"auth_token": key, "page": page}
    if filter:     params["filter"] = filter
    if currencies: params["currencies"] = currencies
    if kind:       params["kind"] = kind
    if regions:    params["regions"] = regions
    if public is not None:
        params["public"] = "true" if public else "false"
    if from_:      params["from"] = from_

    # İsteği yap
    async with httpx.AsyncClient(timeout=20) as client:
        r = await client.get(API, params=params, headers={"Accept": "application/json"})
        # Hata varsa olduğu gibi yüzeye çıkar
        if r.status_code >= 400:
            raise HTTPException(status_code=r.status_code, detail=r.text[:500])
        return r.json()
