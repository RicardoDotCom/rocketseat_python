import redis

redis_conn = redis.Redis(host="localhost", port=6379, db=0)

# para insert e update
redis_conn.set("chave_1", "alguma_valor")

# para realizar uma busca no Redis
meu_valor_byte = redis_conn.get("chave_1")
print(meu_valor_byte)
print(type(meu_valor_byte))
print()

# decodificando de byte para str
meu_valor = redis_conn.get("chave_1").decode("utf-8")
print(meu_valor)
print(type(meu_valor))

# delete de dados
redis_conn.delete("chave_1")

### comandos para hash
meu_hash = { # chave de exemplo
    "nome": "jose", # field : values
    "idade": 30,
    "cidade": "sao paulo"
}

redis_conn.hset("meu_hash", "nome", "jose")
redis_conn.hset("meu_hash", "idade", "30")
redis_conn.hset("meu_hash", "cidade", "sao paulo")

valor_1 = redis_conn.hget("meu_hash", "nome").decode("utf-8")
print(valor_1)

redis_conn.hdel("meu_hash", "cidade")

### busca por existencia
elem = redis_conn.exists("chave_1")
print(elem)

elem2 = redis_conn.hexists("meu_hash", "nome")
print(elem2)

## Expiração de dados
#### dadso -> TTL -> Time To Live [segundos] 
redis_conn.set("chave_del", "esse valor sera deletado", 12)
redis_conn.expire("meu_hash", 30)
