from pydantic import BaseModel

class WatchlistItemSchema(BaseModel):
    symbol: str
    notes: str | None = None