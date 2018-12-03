# 장고 내장 함수 include() 및 url() 임포트
from django.conf.urls import include, url
from django.contrib import admin
from mysite.views import HomeView
from django.conf.urls.static import static                              # ch10 1/4
# settings 변수는 settings.py 모듈에서 정의한 항목들을 담고 있는 객체에 대한 참조
from django.conf import settings                                        # ch10 2/4



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
  url(r'^photo/', include('photo.urls', namespace='photo')),          # ch10 3/4

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)     # ch10 4/4
# 기존 urlpatterns에 static() 함수가 반환하는 URL 패턴을 추가
# static(prefix, view=django.views.static.serve, **kwargs)
# settings.MEDIA_URL = '/media/' 이런 URL 요청이 오면,
# django.views.static.serve() 뷰 함수가 처리하게 되어 있는데,
# 이 뷰 함수에 다음 인자를 전달함
# document_root = settings.MEDIA_ROOT = os.path.join(BASE_DIR, 'media')