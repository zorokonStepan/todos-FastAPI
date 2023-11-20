# GET
```
    curl http://127.0.0.1:8000/
    
    curl http://127.0.0.1:8000/todo
    
    curl -X "GET" "http://127.0.0.1:8000/todo" -H "accept: application/json"
    
    curl -X "GET" "http://127.0.0.1:8000/todo/1" -H "accept: application/json"
```

# POST
https://github.com/spring-guides/gs-accessing-data-rest/issues/11
```
    curl -X "POST" "http://127.0.0.1:8000/todo" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"id\": 1, \"item\": \"First Todo is to finish this book!\"}"
    
    curl -X "POST" "http://127.0.0.1:8000/todo" -H "accept: application/json" -H "Content-Type: application/json" -d "{}"    
```




# POST
https://github.com/spring-guides/gs-accessing-data-rest/issues/11
```
    curl -X "POST" "http://127.0.0.1:8000/todo" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"id\": 2, \"item\": \"Validation models help with input types\"}"
    
    curl -X POST -H "accept:application/json" -H "Content-Type:application/json" -d "{\"id\":1,\"item\":{\"item\":\"Nested models\",\"status\":\"completed\"}}" 127.0.0.1:8000/todo
    
    curl -X "PUT" "http://127.0.0.1:8000/todo/1" -H "accept:application/json" -H "Content-Type:application/json" -d "{\"item\":{\"item\":\"Read the next chapter of the book.\",\"status\":\"completed\"}}"
```
