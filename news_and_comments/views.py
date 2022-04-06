from django.http import HttpResponseRedirect
from .forms import NewsForm, CommentForm, TagsForm
from django.views import View
from django.shortcuts import render
from .models import News, Comments, Tags
from django.views.generic import ListView, DetailView, UpdateView


class IndexNews(ListView):
    model = News
    template_name = 'news_and_comments/index.html'
    context_object_name = 'news_list'
    paginate_by= 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tags.objects.all()
        return context


class NewsDetailView(DetailView):
    model = News
    template_name = 'news_and_comments/news_detail.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        context['comments'] = Comments.objects.filter(news=pk)
        context['comment_form']=CommentForm()
        return context

    def post(self, request, pk):
        comment_form = CommentForm(request.POST)
        if request.user.is_authenticated and comment_form.cleaned_data['text']:
            Comments.objects.create(news_id=pk, username=request.user.username,
                                    user_id=request.user.id, text=comment_form.cleaned_data['text'])
        elif comment_form.is_valid():
            comment_form.cleaned_data['username'] = comment_form.cleaned_data['username'] + ' (anonymous)'
            Comments.objects.create(news_id=pk, **comment_form.cleaned_data)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


class NewsCreateView(View):

    def get(self, request):
        tags_form = TagsForm()
        news_form = NewsForm()

        return render(request, 'news_and_comments/create_news.html',
                      context={'tags_form': tags_form, 'news_form': news_form, })

    def post(self, request):
        news_form = NewsForm(request.POST)
        tags_form = TagsForm(request.POST)
        if news_form.is_valid() and tags_form.is_valid():
            t = Tags.objects.create(name=tags_form.cleaned_data['name'])
            n = News.objects.create(title=news_form.cleaned_data['title'],
                                    description=news_form.cleaned_data['description'])
            t.news.add(n)
            return HttpResponseRedirect('/news')
        return render(request, 'news_and_comments/create_news.html', context={'news_form': news_form})


class NewsUpdateView(UpdateView):
    model = News
    form_class = NewsForm
    template_name = 'news_and_comments/update_news.html'

def News_tags(request):
    tags = Tags.objects.all()
    news = News.objects.all()
    if request.GET.get('tag'):
        news = news.filter(tags__name=request.GET['tag'])
    context = {'news_list': news, 'tags': tags}
    return render(request, 'news_and_comments/index.html', context)
