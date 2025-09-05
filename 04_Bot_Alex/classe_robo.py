
import google.generativeai as genai
import ttkbootstrap as ttk

class Gemini_Bot:
    """Classe responsável por gerenciar o modelo do Gemini."""
    
    def __init__(self):
        genai.configure(api_key="AIzaSyAqHTr0DulKHBhwpSIeIEZv4QSo0lfiHX8")
        
        instrucao_sistema = open("04_Bot_Alex/instrucoes.txt", "r")
        
        self.model = genai.GenerativeModel(
            model_name='gemini-1.5-flash',
            system_instruction=instrucao_sistema
        )
        self.chat = self.model.start_chat()

    def enviar_mensagem(self, mensagem: str) -> str:
        """Envia mensagem para o modelo e retorna a resposta."""
        response = self.chat.send_message(mensagem)
        return response.text
        
    
    

# Este if só sera executado se eu rodar o arquivo diretamente da classe
# caso eu importe essa parte nao sera executada, podemos utilizar isso para testes
if __name__ == "__main__":
    app = Gemini_Bot()
    resposta = app.enviar_mensagem(mensagem="Salve man")
    print(resposta)