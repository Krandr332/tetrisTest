# from django.contrib.admin import filters
#
#
# class UserFilterBackend(filters.BaseFilterBackend):
#
#     def filter_queryset(self, request, queryset, view):
#         return queryset.filter(
#             examplemodel__author=request.user
#         )