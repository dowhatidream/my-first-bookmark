from django.shortcuts import render
from django.views.generic import ListView,DetailView
from bookmark.models import Bookmark

# 북마크 테이블의 전체 레코드 리스트 출력을 위한 뷰
class BookmarkLV(ListView):
    model = Bookmark

# 북마크 테이블의 특정 레코드 상세 출력을 위한 뷰
class BookmarkDV(DetailView):
    model = Bookmark
