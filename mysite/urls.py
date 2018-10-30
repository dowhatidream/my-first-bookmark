# 장고 내장 함수 include() 및 url() 임포트
from django.conf.urls import include, url
from django.contrib import admin
from mysite.views import HomeView

# 이 부분은 bookmark.urls 부분으로 옮겼음
# from bookmark.views import BookmarkLV, BookmarkDV

urlpatterns = [
  # admin.site.urls를 include(admin.site.urls)로 변경했으나 사실 동일한 효과를 발휘
  # 다른 앱에서 정의된 url 설정을 재활용할 때 include() 함수를 써야 하지만,
  # 예외적으로 admin.site.urls에 대해서는 include() 함수를 생략해도 무방함
  url(r'^admin/', include(admin.site.urls)),
  url(r'^$', HomeView.as_view(), name='home'),

  # 아래 두 url 패턴에서 뒷 부분에 패턴의 끝을 표시하는 '$' 문자가 없음!!!
  url(r'^bookmark/', include('bookmark.urls', namespace='bookmark')),
  # bookmark.urls를 적용하고, 이름공간을 'bookmark'로 지정
  url(r'^blog/', include('blog.urls', namespace='blog')),
  # blog.urls를 적용하고, 이름공간을 'blog'로 지정
]