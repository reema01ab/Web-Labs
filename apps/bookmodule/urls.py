from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name= "books.index"),
    path('list_books/', views.list_books, name= "books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('html5/links/', views.links, name='books.links'),
    path('html5/text/formatting/', views.formatting, name='books.formatting'),
    path('html5/listing/', views.listing, name='books.listing'),
    path('html5/tables/', views.tables, name='books.tables'),
    path('search', views.search_books, name='search_books'),
    path('simple/query',views.simple_query),
    path('complex/query', views.complex_query),
    path('lab8/task1', views.lab8_task1, name='books.lab8.task1'),
    path('lab8/task2', views.lab8_task2, name='books.lab8.task2'),
    path('lab8/task3', views.lab8_task3, name='books.lab8.task3'),
    path('lab8/task4', views.lab8_task4, name='books.lab8.task4'),
    path('lab8/task5', views.lab8_task5, name='books.lab8.task5'),
    path('lab8/task7', views.lab8_task7, name='books.lab8.task7'),
    path('lab9/task1', views.task1, name='lab9_task1'),
    path('lab9/task2', views.task2, name='lab9_task2'),
    path('lab9/task3', views.task3, name='lab9_task3'),
    path('lab9/task4', views.task4, name='lab9_task4'),
    path('lab9/task5', views.task5, name='lab9_task5'),
    path('lab9/task6', views.task6, name='lab9_task6'),
    path('lab9_part1/listbooks', views.listbooks_part1, name='listbooks_part1'),
    path('lab9_part1/addbook', views.addbook_part1, name='addbook_part1'),
    path('lab9_part1/editbook/<int:id>', views.editbook_part1, name='editbook_part1'),
    path('lab9_part1/deletebook/<int:id>', views.deletebook_part1, name='deletebook_part1'),

    # Part 2 with Django forms
    path('lab9_part2/listbooks', views.listbooks_part2, name='listbooks_part2'),
    path('lab9_part2/addbook', views.addbook_part2, name='addbook_part2'),
    path('lab9_part2/editbook/<int:id>', views.editbook_part2, name='editbook_part2'),
    path('lab9_part2/deletebook/<int:id>', views.deletebook_part2, name='deletebook_part2'),

    path('lab11/task1/', views.student_list, name='student_list'),
    path('lab11/task1/add/', views.student_add, name='student_add'),
    path('lab11/task1/edit/<int:id>/', views.student_edit, name='student_edit'),
    path('lab11/task1/delete/<int:id>/', views.student_delete, name='student_delete'),

    path('lab11/task2/', views.student2_list, name='student2_list'),
    path('lab11/task2/add/', views.student2_add, name='student2_add'),
    path('lab11/task2/edit/<int:id>/', views.student2_edit, name='student2_edit'),
    path('lab11/task2/delete/<int:id>/', views.student2_delete, name='student2_delete'),

    path('lab11/task3/', views.product_list, name='product_list'),
    path('lab11/task3/add/', views.product_add, name='product_add'),
    path('lab11/task3/edit/<int:id>/', views.product_edit, name='product_edit'),
    path('lab11/task3/delete/<int:id>/', views.product_delete, name='product_delete'),
    ]
