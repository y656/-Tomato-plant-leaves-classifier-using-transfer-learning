from fastapi import FastAPI
app = FastAPI() # Creates instance of fastapi class

#Our database:
food = {
    'indian' : ["samosa", "dosa"],
    'chinese' : [ "noodles", "manchuriyan"],
    'american' : ["pizza", "burger"]}



#Then I will write my first end point
@app.get("/get_items/{name}") # This hello end point will return me fixed string
# you can supply name as parameter
#Here we are using get method to send http request



async def get_items(name): #The name that someone is supplying 
    return food.get(name)
# hello is essentially my entry point
# The code changes which I do dyanamically are reflected once ur application starts 
# To start the application use uvicorn  main:app --reload 
#Syntax is uvicorn name_of_file:name of instantiation of fastapi --reload
