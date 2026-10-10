from dataclasses import dataclass


@dataclass(frozen=True)
class ServerAddress:
    host: str
    port: int


addr = ServerAddress("10.0.0.5", 443)
print(addr)

try:
    addr.port = 8080
except Exception as e:
    print(f"❌ {type(e).__name__}: {e}")