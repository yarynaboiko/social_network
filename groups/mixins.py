from django.core.exceptions import PermissionDenied


class UserIsAdminMixin(object):
    def dispatch(self, request, *args, **kwargs):
        instance = self.get_object()
        member = instance.members.all().filter(user=request.user).first()

        if not member.is_admin:
            raise PermissionDenied
        return super(UserIsAdminMixin, self).dispatch(request, *args, **kwargs)
