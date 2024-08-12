from fastapi import Depends, HTTPException
from fastapi.security import APIKeyHeader

# Define the API key header
api_key_header = APIKeyHeader(name="X-API-KEY")

# Define the API keys
API_KEYS = ["your_api_key_here"]

# Define the API key validation function
async def validate_api_keys(api_key: str = Depends(api_key_header)):
    if api_key not in API_KEYS:
        raise HTTPException(status_code=401, detail="Invalid API key")
    return api_key

