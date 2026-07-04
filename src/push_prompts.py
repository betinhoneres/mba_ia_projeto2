import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from langchain import hub
from langchain_core.load import load
import yaml
from utils import check_env_vars, print_section_header

load_dotenv()

def push_prompts_to_langsmith():
    """Lê o prompt otimizado e faz push para o LangSmith Prompt Hub."""
    print_section_header("Iniciando Push do Prompt Otimizado")
    
    file_path = Path("prompts/bug_to_user_story_v2.yml")
    
    if not file_path.exists():
        print(f"❌ Arquivo de prompt não encontrado em: {file_path}")
        return False

    try:
        print(f"Carregando e desserializando o prompt de {file_path}...")
        
        # Usamos unsafe_load para permitir que o PyYAML processe os objetos Python/LangChain contidos no arquivo v2
        with open(file_path, "r", encoding="utf-8") as f:
            raw_prompt_data = yaml.unsafe_load(f)
        
        # Reconstrói o objeto ChatPromptTemplate nativo
        prompt_obj = load(raw_prompt_data)
        
        # O nome do repositório deve ser APENAS o nome dele. O SDK injeta o tenant/seu_username automaticamente.
        repo_name = "bug_to_user_story_v2"
        print(f"Enviando para o LangSmith Hub como repositório: '{repo_name}'...")
        
        # Faz o push usando as credenciais implícitas do ambiente
        hub.push(repo_name, prompt_obj)
        
        print(f"✅ Prompt enviado com sucesso para o seu Hub!")
        return True

    except Exception as e:
        print(f"❌ Erro ao enviar prompt: {e}", file=sys.stderr)
        return False

def main():
    """Função principal"""
    required_vars = ["LANGCHAIN_API_KEY"]
    if not check_env_vars(required_vars):
        print("❌ Erro: Variáveis de ambiente obrigatórias não encontradas no arquivo .env.")
        return 1
        
    success = push_prompts_to_langsmith()
    return 0 if success else 1

if __name__ == "__main__":
    sys.exit(main())