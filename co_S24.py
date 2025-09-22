class Encomenda:
    def __init__(self, codigo, destino, remetente):
        self.codigo = codigo
        self.destino = destino
        self.remetente = remetente
        self.status_entrega = "Pendente"

    def registrar_entrega(self):
        self.status_entrega = "Entregue"

    def detalhes(self):
        return f"Código: {self.codigo}, Destino: {self.destino}, Remetente: {self.remetente}, Status: {self.status_entrega}"


class Pacote(Encomenda):
    def __init__(self, codigo, destino, remetente, peso, dimensoes):
        super().__init__(codigo, destino, remetente)
        self.peso = peso
        self.dimensoes = dimensoes  # (largura, altura, profundidade)

    def calcular_frete(self):
        return self.peso * 0.5 + sum(self.dimensoes) * 0.1  # Exemplo de cálculo


class Carta(Encomenda):
    def __init__(self, codigo, destino, remetente, tipo_papel):
        super().__init__(codigo, destino, remetente)
        self.tipo_papel = tipo_papel  # Ex: "A4", "Ofício"

    def definir_prioridade(self):
        if self.tipo_papel == "Urgente":
            return "Alta"
        return "Normal"


class RemessaGrande(Encomenda):
    def __init__(self, codigo, destino, remetente, volume, tipo_conteudo):
        super().__init__(codigo, destino, remetente)
        self.volume = volume  # em metros cúbicos
        self.tipo = tipo_conteudo  # booleano

    def agendar_entrega(self, data):
        return f"Entrega agendada para {data}"
