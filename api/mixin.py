from rest_framework import mixins

class ViewSetMixin(mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin):

    class Meta:
        abstract = True
