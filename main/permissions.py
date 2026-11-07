from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsPortfolioOwnerOrReadOnly(BasePermission):
    message = "Only the portfolio owner can change projects."

    def has_permission(self, request, view): # dijalankan sebelum isi API view
        return (
            request.method in SAFE_METHODS
            or request.user.is_superuser
        )

class IsPortfolioOwnerOrEditorOrReadOnly(BasePermission):
    message = "Akun ini tidak memiliki izin untuk tindakan tersebut."

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS or request.user.is_superuser:
            return True
        return (
            request.method in ("PUT", "PATCH")
            and request.user.is_authenticated
            and request.user.groups.filter(name="Editor").exists()
        )