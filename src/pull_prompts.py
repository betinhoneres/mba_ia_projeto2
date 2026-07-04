"""
Script para fazer pull de prompts do LangSmith Prompt Hub.

Este script:
1. Conecta ao LangSmith usando credenciais do .env
2. Faz pull dos prompts do Hub
3. Salva localmente em prompts/bug_to_user_story_v1.yml

SIMPLIFICADO: Usa serialização nativa do LangChain para extrair prompts.
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from langchain import hub
from utils import save_yaml, check_env_vars, print_section_header

load_dotenv()


def pull_prompts_from_langsmith():
    """Faz pull do prompt original do LangSmith Hub e salva localmente em YAML."""
    print_section_header("Iniciando Pull do Prompt Original")
    
    # Identificador do prompt de baixa qualidade definido no PRD
    prompt_handle = "leonanluppi/bug_to_user_story_v1"
    
    print(f"Buscando o prompt '{prompt_handle}' no LangSmith Hub...")
    
    try:
        # Faz o download do prompt usando o SDK do LangChain
        prompt_obj = hub.pull(prompt_handle)
        
        # Converte o objeto de prompt do LangChain para um dicionário serializável
        prompt_dict = prompt_obj.to_json()
        
        # Define o caminho de destino conforme a estrutura obrigatória do projeto
        output_dir = Path("prompts")
        output_dir.mkdir(exist_ok=True)
        output_path = output_dir / "bug_to_user_story_v1.yml"
        
        # Salva o dicionário estruturado no formato YAML usando a utilidade do projeto
        save_yaml(prompt_dict, output_path)
        print(f"✅ Prompt salvo com sucesso em: {output_path}")
        return True
        
    except Exception as e:
        print(f"❌ Erro ao fazer pull do prompt: {e}", file=sys.stderr)
        return False


def main():
    """Função principal"""
    # Garante que as chaves obrigatórias do LangSmith e OpenAI estão presentes
    required_vars = ["LANGCHAIN_API_KEY", "OPENAI_API_KEY"]
    if not check_env_vars(required_vars):
        print("❌ Erro: Variáveis de ambiente obrigatórias não encontradas no arquivo .env.")
        return 1
        
    success = pull_prompts_from_langsmith()
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())