from fastapi import APIRouter, status, Response, Query, Body, Path
from typing import Optional, List
from pydantic import BaseModel

router = APIRouter(
    prefix="/blog",
    tags=["blog"]
)

class Image(BaseModel):
    url: str
    name: str

class ArticleModel(BaseModel):
    title: str
    content: str
    published: Optional[bool]
    tags: Optional[List[str]] = []
    metadata: Optional[dict] = {"key":"value"}
    image: Optional[Image] = None

@router.post(
    "/create",
    status_code=status.HTTP_201_CREATED,
    summary="Create a new blog post",
    response_description="The blog post was created."
    )
def create_article(
    response: Response,
    article: ArticleModel
    ):
    '''
    Create a new blog post.
    - **title**: The title of the blog post.
    - **body**: The body of the blog post.
    - **published**: The published status of the blog post.
    '''
    response.status_code = status.HTTP_201_CREATED
    return {"message":article}

@router.post("/create/{article_id}/comment")
def create_article_comment(
    article:ArticleModel,
    response: Response,
    article_id: int = Path(..., 
                           gt=0, 
                           description="The article id."
                           ),
    comment_id: int = Query(None, 
                            description="The comment id in the corresponding article."
                            ),
    comment: str = Body(..., 
                        min_length=10,
                        max_length=256,
                        regex="^[\w\s\S]*$"
                        ),
    comment_version: Optional[List[str]] = Query(None)
    ):
    response.status_code = status.HTTP_201_CREATED
    return {
        "article": article,
        "article_id": article_id, 
        "comment_id": comment_id,
        "comment": comment,
        "comment_version": comment_version
        }