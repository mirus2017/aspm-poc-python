SQL injection demo

uvicorn main:app --reload

http://localhost:8000/

http://localhost:8000/employees/?login=mirek
http://localhost:8000/employees/?login=james

http://localhost:8000/employees/?login=%27+OR+1%3D1+OR+%27

' OR 1=1 OR '
