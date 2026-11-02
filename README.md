docker compose up --build
curl -X POST http://localhost:8000/sessions -H "Content-Type: application/json" -d '{"game_id": 1, "player_name": "Alice"}'
