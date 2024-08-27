from sqlmodel import Field, SQLModel
from typing import Optional
from sqlmodel import SQLModel, create_engine
from datetime import datetime, date

DATABASE_URL = "mysql+mysqlconnector://root:cisbaf7890380@localhost/dados_sso"

engine = create_engine(DATABASE_URL)

class Relatorio(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    tipo_vtr: str = Field(max_length=255)
    tipo_hd_chamado: str = Field(max_length=255)
    tipo_chamado: str = Field(max_length=255)
    sexo_do_paciente: str = Field(max_length=255)
    prioridade_chamado: str = Field(max_length=255)
    obito: str = Field(max_length=255)
    idade: int = Field(max_length=255)
    idade_do_paciente: str = Field(max_length=255)
    codigo_do_chamado: str = Field(max_length=255)
    cidade: str = Field(max_length=255)
    acao_sem_intervencao: str = Field(max_length=255)
    total: int = Field(max_length=255)
    aph_critico: str = Field(max_length=255)
    aph_regulacao: str = Field(max_length=255)
    aph_tih: str = Field(max_length=255)
    sub_grupo_aph_cena: str = Field(max_length=255)
    prioridade_cena: str = Field(max_length=255)
    conduta: str = Field(max_length=255)
    tipo_estabelecimento: str = Field(max_length=255)
    hospital: str = Field(max_length=255)
    placa: str = Field(max_length=255)
    veiculo_base: str = Field(max_length=255)
    dia_da_semana: str = Field(max_length=255)
    hora: str = Field(max_length=255)
    hd: str = Field(max_length=255)
    data: date = Field(default_factory=datetime.utcnow)
    estabelecimento_origem: str = Field(max_length=255)
    estabelecimento: str = Field(max_length=255)
    encerramento: str = Field(max_length=255)
    usuario_regulacao_chamado: str = Field(max_length=255)
    usuario_abertura_chamado: str = Field(max_length=255)

    @classmethod
    def fill(cls, json_data):
        return Relatorio(**json_data)
    
    def __init__(self, **data):
        super().__init__(**data)
        self.check_datas()
        self.correct_datas()
    
    def check_datas(self):
        if not self.tipo_chamado:
            raise Exception("O tipo do chamado não pode ser vazio!")
        if not self.sexo_do_paciente:
            raise Exception("O sexo do paciente não pode ser vazio!")
        if not self.idade:
            raise Exception("A idade não pode ser vazio!")
        if not self.idade_do_paciente:
            raise Exception("A idade do paciente não pode ser vazio!")
        if not self.codigo_do_chamado:
            raise Exception("O código do chamado não pode ser vazio!")
        if not self.total:
            raise Exception("O total não pode ser vazio!")
        if not self.data:
            raise Exception("A data não pode ser vazia!")
        if not self.hora:
            raise Exception("A hora não pode ser vazia!")
        if not self.encerramento:
            raise Exception("O encerramento não pode ser vazio!")
        # if not self.usuario_abertura_chamado:
        #     raise Exception("O usuario abertorua chamado não pode ser vazio!")


    def correct_datas(self):
        try:
            if '.' in str(self.total):
                self.total = int(str(self.total).split('.')[0])
            else:
                self.total = int(self.total)
            self.idade = int(self.idade)
            self.data = datetime.strptime(self.data, '%d/%m/%Y').date()
        except Exception as e:
            raise Exception("Erro ao tratar dados:", str(e))

SQLModel.metadata.create_all(engine)
