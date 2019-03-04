# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone

def post_list(request):
    qs = Post.objects.all()
    qs = qs.filter(published_date__lte=timezone.now())
    qs = qs.order_by('published_date')
    return render(request, 'blog/post_list.html', {
        'post_list' : qs
    })

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)    # 앞의 pk는 필드명 뒤의 pk는 인자명

    return render(request, 'blog/post_detail.html', {
        'post' : post,
    })