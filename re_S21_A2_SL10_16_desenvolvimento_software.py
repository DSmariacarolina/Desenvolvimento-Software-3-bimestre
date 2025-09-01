class CalculadoraTarifas:
    """
    Classe com métodos estáticos para centralizar as regras de cálculo de tarifas.
    Não precisa de 'self' pois não guarda estado, apenas executa lógicas.
    """
    @staticmethod
    def calcular_tarifa_base():
        return 5  # Tarifa base de R$ 5 para todas as contas

    @staticmethod
    def calcular_tarifa_transacao(numero_transacoes):
        # R$ 1,50 por transação que exceder as 10 primeiras
        if numero_transacoes > 10:
            return (numero_transacoes - 10) * 1.5
        return 0

    @staticmethod
    def calcular_tarifa_saldo(saldo):
        # Tarifa de R$ 10 para saldos abaixo de R$ 1000
        if saldo < 1000:
            return 10
        return 0


class ContaBancaria:
    def __init__(self, numero_conta, saldo=0):
        self.numero_conta = numero_conta
        self.saldo = saldo
        self.numero_transacoes = 0 # Inicia com zero transações

    def __str__(self):
        # Método especial para facilitar a exibição do status da conta
        return (f"--- Conta: {self.numero_conta} ---\n"
                f"Saldo: R$ {self.saldo:.2f}\n"
                f"Transações no período: {self.numero_transacoes}\n"
                f"--------------------")

    def depositar(self, valor):
        # MELHORIA: Validar se o valor é positivo
        if valor > 0:
            self.saldo += valor
            self.numero_transacoes += 1
            print(f"[Conta {self.numero_conta}] Depósito de R$ {valor:.2f} realizado. Novo saldo: R$ {self.saldo:.2f}")
        else:
            print("[ERRO] O valor do depósito deve ser maior que zero.")

    def sacar(self, valor):
        # CORREÇÃO CRÍTICA: Validar se há saldo suficiente
        if valor <= 0:
            print("[ERRO] O valor do saque deve ser maior que zero.")
            return # Encerra a função aqui
            
        if self.saldo >= valor:
            self.saldo -= valor
            self.numero_transacoes += 1
            print(f"[Conta {self.numero_conta}] Saque de R$ {valor:.2f} realizado. Novo saldo: R$ {self.saldo:.2f}")
        else:
            print(f"[ERRO] Saldo insuficiente. Saldo atual: R$ {self.saldo:.2f}, tentativa de saque: R$ {valor:.2f}")

    def calcular_tarifa_total(self):
        # Este método apenas calcula e retorna a tarifa, sem alterar o saldo
        tarifa_base = CalculadoraTarifas.calcular_tarifa_base()
        tarifa_transacao = CalculadoraTarifas.calcular_tarifa_transacao(self.numero_transacoes)
        tarifa_saldo = CalculadoraTarifas.calcular_tarifa_saldo(self.saldo)
        return tarifa_base + tarifa_transacao + tarifa_saldo
        
    def aplicar_tarifa(self):
        # MELHORIA: Método que calcula E aplica a tarifa no saldo
        tarifa_a_cobrar = self.calcular_tarifa_total()
        print(f"\n[Conta {self.numero_conta}] Calculando tarifas...")
        print(f"Tarifa total calculada: R$ {tarifa_a_cobrar:.2f}")
        self.saldo -= tarifa_a_cobrar
        print(f"Tarifa debitada. Saldo final: R$ {self.saldo:.2f}")
        # Opcional: zerar o contador de transações para o próximo período
        self.numero_transacoes = 0


# Criando uma conta com saldo alto e poucas transações
conta_premium = ContaBancaria(numero_conta="CP-001", saldo=5000)

# Criando uma conta com saldo baixo que fará muitas transações
conta_basica = ContaBancaria(numero_conta="CB-002", saldo=800)

print("--- Contas criadas ---")
print(conta_premium)
print(conta_basica)

print("\n>>> Simulando operações na Conta Básica (CB-002)...")

# Fazendo 11 depósitos de R$ 10
for i in range(11):
    conta_basica.depositar(10)

# Fazendo 1 saque
conta_basica.sacar(50)

# Tentando um saque com saldo insuficiente (para testar a correção)
conta_basica.sacar(1000)

print("\n--- Status final da Conta Básica antes das tarifas ---")
print(conta_basica)
