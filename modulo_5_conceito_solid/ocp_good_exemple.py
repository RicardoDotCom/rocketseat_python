from abc import ABC, abstractmethod

class ExameHandler(ABC):
    @abstractmethod
    def verificar_condicoes(self, exame):
        pass


class ExameSangueHandler(ExameHandler):
    def verificar_condicoes(self, exame):
        # Implementar as condições específicas do exame de sangue
        print("Exame sanguíneo aprovado!")
        return True


class ExameRaioXHandler(ExameHandler):
    def verificar_condicoes(self, exame):
        # Implementar as condições específicas do exame de raio-x
        print("Raio-X aprovado!")
        return True


class AprovaExame:
    def __init__(self):
        self.handlers = {}

    def registrar_handler(self, tipo_exame, handler):
        self.handlers[tipo_exame] = handler

    def aprovar_solicitacao_exame(self, exame):
        handler = self.handlers.get(exame.tipo)
        if handler:
            if handler.verificar_condicoes(exame):
                print(f"Exame do tipo '{exame.tipo}' aprovado!")
            else:
                print(f"Exame do tipo '{exame.tipo}' não aprovado.")
        else:
            print(f"Nenhum handler registrado para o tipo de exame '{exame.tipo}'.")


# Exemplo de uso:
class Exame:
    def __init__(self, tipo):
        self.tipo = tipo


exame_sangue = Exame("sangue")
exame_raio_x = Exame("raio-x")

# Registrar os handlers
aprovador = AprovaExame()
aprovador.registrar_handler("sangue", ExameSangueHandler())
aprovador.registrar_handler("raio-x", ExameRaioXHandler())

# Aprovar exames
aprovador.aprovar_solicitacao_exame(exame_sangue)
aprovador.aprovar_solicitacao_exame(exame_raio_x)