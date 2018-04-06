class Bem():
    def __init__(self, codigo_tipo_bem, descrição_tipo_bem, descrição_detalhada_bem, valor_bem):
        self.__codigo_tipo_bem = codigo_tipo_bem
        self.__descrição_tipo_bem = descrição_tipo_bem
        self.__descrição_detalhada_bem = descrição_detalhada_bem
        self.__valor_bem = valor_bem
    
    def getCodigoTipoBem(self):
        return self.__codigo_tipo_bem
    
    def getDescriçãoTipoBem(self):
        return self.__descrição_tipo_bem
    
    def getDescriçãoDetalhadaBem(self):
        return self.__descrição_detalhada_bem
    
    def getValorBem(self):
        return self.__valor_bem
    
    