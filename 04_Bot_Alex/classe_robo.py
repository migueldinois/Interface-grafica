
import google.generativeai as genai
import ttkbootstrap as ttk



class Gemini_Bot:
    """Classe responsável por gerenciar o modelo do Gemini."""
    
    def __init__(self):
        genai.configure(api_key="AIzaSyAqHTr0DulKHBhwpSIeIEZv4QSo0lfiHX8")
        
        instrucao_sistema = """
            Seu nome é Alex Stocco, pofessor do senai. Você é um professor de aproximadamente 40 anos, é legal, fala de maneira facil e com
            varios exemplos para deixar a materia mais facil, você é especificadamente formado em desenvolvimento de sistemas
            e sabe tudo sobre isso, qualquer pergunta você sabe
            """
        
        self.model = genai.GenerativeModel(
            model_name='gemini-1.5-flash',
            system_instruction=instrucao_sistema
        )
        self.chat = self.model.start_chat()

    def enviar_mensagem(self, mensagem: str, campo_pergunta: str, text_reposta) -> str:
        """Envia mensagem para o modelo e retorna a resposta."""
        self.pergunta = campo_pergunta.get()
        response = self.chat.send_message(mensagem)
        text_reposta.insert(ttk.END, f"{response.text} \n \n \n")
        return response.text
        
    

# Este if só sera executado se eu rodar o arquivo diretamente da classe
# caso eu importe essa parte nao sera executada, podemos utilizar isso para testes
if __name__ == "__main__":
    app = Gemini_Bot()
    resposta = app.enviar_mensagem(mensagem="Salve man")
    print(resposta)