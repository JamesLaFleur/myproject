from rest_framework import permissions

#-----Это наш собственный класс дял ограничения прав доступа, 
# который я пока нигде не использую
class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS: # если запрос безопасный. Safe_methods это запросы только для чтения (GET, HEAD, OPTIONS)
            return True # если запрос безопасный, то предоставляем права доступа для всех
        
        return bool(request.user and request.user.is_staff) # а если метод 
    # не безопасный, то предоставляем права на изменение только для 
    # администратора (данную строчку скопировали из метода has_permission для метода IsAdminUser)



#---Еще один метод, где мы разрешим менять запись только автору (тоже пока не используется). Скопировали из документации
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user == request.user #если пользователь из бд равен пользователю, который пришел с запросом, тогда даем доступ
    
# используем has_object_permisssion, потому что мы должны для конкретной записи 
# сравнивать пользователя с тем пользователем, который пришел по запросу
# в первом методе мы с записями не работаем, поэтому используем просто has_permission 
# а во втором методе мы делаем разрешение на уровне объекта, то есть на уровне 
# одной из записей