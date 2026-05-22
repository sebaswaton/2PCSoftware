import copy
from app.models.user import Usuario


class UsuarioPrototype:
    def __init__(self, usuario: Usuario):
        self._data = {
            k: v for k, v in usuario.__dict__.items()
            if not k.startswith("_")
        }

    def clone(self) -> "UsuarioPrototype":
        return copy.deepcopy(self)

    def set(self, **kwargs) -> "UsuarioPrototype":
        clon = self.clone()
        clon._data.update(kwargs)
        return clon

    def apply(self, usuario: Usuario) -> Usuario:
        for key, value in self._data.items():
            setattr(usuario, key, value)
        return usuario
