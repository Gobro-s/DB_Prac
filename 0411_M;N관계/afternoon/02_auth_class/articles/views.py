from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm, CommentForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    # comment 작성 폼
    commentForm = CommentForm()  # 빈 폼
    # 이미 작성된 Comment List
    comment_list = article.comment_set.all()
    context = {
        'article': article,
        'commentForm': commentForm,
        'comment_list': comment_list,
        }
    return render(request, 'articles/detail.html', context)


def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()

    context = {'form': form}
    return render(request, 'articles/create.html', context)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


def update(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', pk=article.pk)
    else:
        form = ArticleForm(instance=article)

    context = {'form': form, 'article': article}
    return render(request, 'articles/update.html', context)


##########################################################################
############################# COMMENT ####################################
##########################################################################

def create_comment(request, pk):
    # 작성할 article 객체 불러오기
    article = Article.objects.get(pk=pk)
    # modelForm
    commentForm = CommentForm(request.POST)  # 사용자 입력값 받아와서, 인스턴스까지
    if commentForm.is_valid():
        comment = commentForm.save(commit=False)  # TCL
        comment.article = article
    return redirect('articles:detail', article)