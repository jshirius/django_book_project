from django.shortcuts import render
from django.http import HttpResponse
from .models import MBooks, MGenre

def index(request):

	#通常のクエリ
	book_list = MBooks.objects.filter(genre_id=1).values()
	print(book_list)
	
	#https://docs.djangoproject.com/en/3.0/topics/db/queries/#one-to-many-relationships
	#本(MBooks)とジャンル(MGenre)のリレーション
	#モデル側の設定はgenre = models.ForeignKey(MGenre, on_delete=models.CASCADE)
	#この方法でMGenre側のデータを取ることができる。
	e = MBooks.objects.get(id=2)
	
	#e.genreと指定することでMGenre側のデータを取得できる
	print(e.genre.name)

	
	#１ジャンルで複数の本があるケースでデータ取得
	e = MBooks.objects.filter(genre_id=1)
	print(e[0].genre.name) #配列1番めのジャンル側のデータ取得してみる


	return HttpResponse("Hello, world. You're at the polls index.")
 