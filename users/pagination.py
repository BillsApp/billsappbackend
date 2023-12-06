from rest_framework.pagination import PageNumberPagination


class DefaultPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'per_page'
    max_page_size = 400


class LargePagination(PageNumberPagination):
    page_size = 5000
    page_size_query_param = 'per_page'
