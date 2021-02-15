from django.contrib.auth.models import User
import graphene
from graphene_django import DjangoObjectType
from posts.models import Post

class PostType(DjangoObjectType):
    class Meta:
        model = Post
        fields=("id", "title", "body", "created_at")

class Query(graphene.ObjectType):
    all_names = graphene.List(PostType)

    def resolve_all_names(root, info):
        return Post.objects.all()
 
class PostCreate(graphene.Mutation):
    class Arguments:
        title = graphene.String(required = True)
        body = graphene.String(required = True)
 
    post = graphene.Field(PostType)
 
    @classmethod
    def mutate(cls,root,info,title, body):
        post = Post(title = title, body = body)
        post.save()
        return PostCreate(post = post)
 
class PostUpdate(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required = True)
        title = graphene.String(required = True)
        body = graphene.String(required = True)
 
    post = graphene.Field(PostType)
 
    @classmethod
    def mutate(cls,root,info,id, title, body):
        post = Post.objects.get(id = id)
        post.title = title
        post.body = body
        post.save()
        return PostUpdate(post = post)
 
class PostDelete(graphene.Mutation):
    class Arguments:
        id=graphene.ID()
 
    post=graphene.Field(PostType)
 
    @classmethod
    def mutate(cls,root,info,id):
        post=Post.objects.get(id=id)
        post.delete()
        return
 
class Mutation(graphene.ObjectType):
    create_post=PostCreate.Field()
    update_post=PostUpdate.Field()
    delete_post=PostDelete.Field()
 
schema=graphene.Schema(mutation=Mutation, query=Query)