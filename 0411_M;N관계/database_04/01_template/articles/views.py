from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import Article, Comment, Hashtag
from .forms import ArticleForm, CommentForm
from django.views.decorators.http import require_POST


# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {"articles": articles}
    return render(request, "articles/index.html", context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    # comments = article.comment_set.all()
    # Select * from Comment Where parent IS NULL;
    comments = article.comment_set.filter(parent__isnull=True)  # 댓글
    context = {
        "article": article,
        "comment_form": comment_form,
        "comments": comments,
    }
    return render(request, "articles/detail.html", context)


def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            ############## Hashtag저장#########################################################################
            for word in article.content.split():  # 공백을 기준으로 리스트
                if word[0] == "#":
                    # word랑 같은 해시태그가 존재하면, 기존 객체 반환, 없으면 새로운 객체 생성
                    hashtag, created = Hashtag.objects.get_or_create(content=word)
                    # 1. 현재 사이트에 등록된 모든 해시태그 보기
                    # 2. Hashtag 기준으로 filter 해주기.
                    # 3. 게시물 수정시, 새로 등록된 해시태그를 검사 해주기
                    article.hashtags.add(hashtag)
            ###################################################################################################

            return redirect("articles:detail", article.pk)
    else:
        form = ArticleForm()

    context = {"form": form}
    return render(request, "articles/create.html", context)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        article.delete()
        return redirect("articles:index")
    return redirect("articles:detail", article.pk)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        if request.method == "POST":
            form = ArticleForm(request.POST, request.FILES, instance=article)
            if form.is_valid():
                form.save()
                return redirect("articles:detail", pk=article.pk)
        else:
            form = ArticleForm(instance=article)
    else:
        return redirect("articles:detail", article.pk)
    context = {"form": form, "article": article}
    return render(request, "articles/update.html", context)


@require_POST
def comments_create(request, pk):
    if request.user.is_authenticated:
        # 작성할 article 객체 불러오기
        article = Article.objects.get(pk=pk)
        # modelForm
        comment_form = CommentForm(request.POST)  # 사용자 입력값 받아와서, 폼 인스턴스까지
        parent_pk = request.POST.get("parent_pk")

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.user = request.user
            # 얘가 댓글인지 답글인지 확인
            if parent_pk:
                parent_comment = Comment.objects.get(pk=parent_pk)
                comment.parent = parent_comment
            comment.save()
        return redirect("articles:detail", article.pk)
    return redirect("accounts:login")


def comments_delete(request, pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect("articles:detail", pk)


@require_POST
def likes(request, article_pk):
    if request.user.is_authenticated:
        article = Article.objects.get(pk=article_pk)

        if article.like_users.filter(pk=request.user.pk).exists():
            # 만약 article.like.users 중 pk가 = request.user.pk에 존재하면
            # 즉 이미 좋아요를 눌렀다면,
            article.like_users.remove(request.user)
            # 좋아요 취소
        else:
            article.like_users.add(request.user)
            # 아니면 좋아요
        return redirect("articles:index")
    return redirect("accounts:login")


## 2. 클릭 시 hashtag 기준으로 filter 해주기.
# 특정
def hashtag_filtering(request, hash_pk):
    hashtag = get_object_or_404(Hashtag, pk=hash_pk)
    articles = hashtag.article_set.order_by("-pk")
    context = {
        "hashtag": hashtag,
        "articles": articles,
    }

    return render(request, "articles/hashtag.html", context)
