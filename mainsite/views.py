from django.shortcuts import redirect
from django.http import HttpResponse
from django.template.loader import get_template
from .models import Post
from datetime import datetime
# Create your views here.


def homepage(request):
    template = get_template('index.html')
    posts = Post.objects.all()
    now = datetime.now()
    html = template.render(locals())
    return HttpResponse(html)


def showpost(request, slug):
    template = get_template('post.html')
    # now = datetime.now()
    try:
        post = Post.objects.get(slug=slug)
        if post is not None:
            html = template.render(locals())
            return HttpResponse(html)
    except:
        return redirect("/")


def showtv(request, tv_id='0'):
    """
            tv_now:当前选择的播放号
    :param request:
    :param tv_id:
    :return:
    """
    template = get_template('watch.html')
    if int(tv_id) < 8:
        tv_list = [
            {'name': '《我们的星球》p1', 'id': '85205638&page=1'},
            {'name': '《我们的星球》p2', 'id': '85234614&page=2'},
            {'name': '《我们的星球》p3', 'id': '85240932&page=3'},
            {'name': '《我们的星球》p4', 'id': '85249048&page=4'},
            {'name': '《我们的星球》p5', 'id': '85255468&page=5'},
            {'name': '《我们的星球》p6', 'id': '85262540&page=6'},
            {'name': '《我们的星球》p7', 'id': '85278217&page=7'},
            {'name': '《我们的星球》p8', 'id': '85286042&page=8'},
                 ]
        tv_now = tv_list[int(tv_id)]
        html = template.render(locals())
        return HttpResponse(html)
    else:
        return HttpResponse('选择的视频号不存在！')
