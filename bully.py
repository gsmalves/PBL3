processos = []
class Processos():
    def __init__(self, id_coordenador, id_processo, ativo=True):
       self.id_coordenador = id_coordenador
       self.id_processo = id_processo
       self.ativo = ativo
    
    def get_active(self):
       return self.ativo 
    
    def get_id_process(self):
        return self.id_processo

    def kill_process_by_id(id):
        for i in processos:
            if i.get_id_process() == id:
                i.desativar()

    def get_id_coordenador(self):
        return self.id_coordenador

    def set_id_coordenador(self, id_new_coordenador):
        self.id_coordenador = id_new_coordenador

    def call_all (self, id_called ):
        for j in processos:
            j.set_id_coordenador(id_called)      

    #Função que desativa o coordenador atual, parando de responder para uma nova eleição
    def desativar(self):
        if (self.ativo):
            self.ativo = False
        else:
            self.ativo = True
        print("\nCoordenador do processo {} parou de responder - Estado {}\n".format(self.id_processo, self.ativo))

    #Função que analisa se o processo que pediu a eleição está ativo e se tem algum outro 
    # com prioridade maior que ele, caso tenha, ele sai da eleição
    def eleicao(self):
        for i in processos:
            #Prioridade é de acordo com o id do processo
            if (i.get_id_process() < self.id_processo):
                if (i.get_active()):
                    i.eleicao()
                    break
                if (self.id_coordenador == i.get_id_process()) and (i.get_active() == False):
                    self.id_coordenador = self.id_processo
                    i.call_all(self.id_processo)
        return self.id_coordenador
                            
