from django.urls import path 
from .views import BookListView,book_detail_view,send_book_view
from django.contrib.sitemaps.views import sitemap
from .sitemaps import BooksSitemap
from .feeds import BooksFeed

app_name="books"

sitemaps = {
	"books":BooksSitemap,
}

urlpatterns = [
	path("",BookListView.as_view(),name="homepage"),
	path("feed/",BooksFeed(),name="books_feed"),
	path("<slug:book_slug>/",book_detail_view,name="book_detail"),
	path("<slug:book_slug>/share/",send_book_view,name="send_book"),
	path("sitemap.xml/",sitemap,{'sitemaps':sitemaps},name="sitemap")
]