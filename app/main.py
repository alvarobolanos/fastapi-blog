from fastapi import FastAPI    # To create the API
from app.routers import blog_get    # To import the routes
from app.routers import blog_post    # To import the routes

app = FastAPI() # Create the API
app.include_router(blog_get.router) # Include the routes
app.include_router(blog_post.router)

@app.get(
        "/",
        tags=['index'])   # Create a route
def index():
    '''This is the index page'''
    return {"message":"This works!"}