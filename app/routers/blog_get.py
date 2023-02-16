from fastapi import APIRouter, status, Response
from typing import Optional
from enum import Enum

router = APIRouter(
    prefix="/blog",
    tags=["blog"]
)

@router.get(
    "/all", 
    status_code=status.HTTP_200_OK,
    summary="This is the blog page",
    response_description="You get a list of all the articles."
)
def blog_all(
    response: Response, 
    limit: Optional[int] = None, 
    published: Optional[bool] = True
    ):
    '''
    This is the blog page. You get a list of all the articles.

    - **limit**: Sets the limit of articles to get.
    - **published**: Filters by published or not.
    '''
    response.status_code = status.HTTP_200_OK
    return {"message":f"These are all the articles in the blog."}

class Categories(str, Enum):
    a = "a"
    b = "b"
    c = "c"

@router.get(
        "/category/{categories}/all",
        status_code=status.HTTP_200_OK,
        summary="This is a category page",
        response_description="You get a list of all the articles in the category."
)
def blog_category_all_articles(
    categories: Categories, 
    response: Response,
    limit: Optional[int] = None, 
    published: Optional[bool] = True
    ):
    '''
    This is a category page. You get a list of all the articles in the category.

    - **categories**: The category you want to get.
    - **limit**: Sets the limit of articles to get.
    - **published**: Filters by published or not.
    '''
    if categories in Categories:
        response.status_code = status.HTTP_200_OK
        return {"message":f"These are all the articles in the category {categories}."}
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message":f"Category {categories} not found"}

@router.get(
    "category/{categories}/articles/{article_id}",
    status_code=status.HTTP_200_OK,
    summary="This is the article page",
    response_description="You get the specific article with identified by article_id."
)
def get_article(
    article_id:int, 
    response: Response,
    categories: Categories,
    published: Optional[bool] = True
    ):
    '''
    This is the article page. You get the specific article with identified by **article_id**.

    - **article_id**: The id of the article you want to get.
    - **published**: Filters by published or not.

    '''
    if categories in Categories:
        if article_id > 5:
            response.status_code = status.HTTP_404_NOT_FOUND
            return {"message":f"Article {article_id} not found"}
        else:
            response.status_code = status.HTTP_200_OK
            return {"message":f"This is article {article_id} in the category {categories}."}
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message":f"Category {categories} not found"}