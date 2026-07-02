import os
import sys
from dotenv import load_dotenv
from langchain import hub
from langchain_core.prompts import ChatPromptTemplate
import yaml

load_dotenv()

def main():
    print("🚀 Iniciando push do prompt...")

    file_path = "prompts/bug_to_user_story_v2.yml"

    # Verifica se o arquivo existe
    if not os.path.exists(file_path):
        print("❌ Arquivo de prompt não encontrado.")
        return 1

    try:
        # Carrega o YAML
        with open(file_path, "r", encoding="utf-8") as f:
            prompt_data = yaml.safe_load(f)

        # Validação básica
        if "system" not in prompt_data or "user" not in prompt_data:
            print("❌ O YAML precisa conter 'system' e 'user'")
            return 1

        # Criar o prompt no formato esperado pelo LangSmith
        prompt = ChatPromptTemplate.from_messages([
            ("system", prompt_data["system"]),
            ("human", prompt_data["user"])
        ])

        # Push (sem username!)
        hub.push("bug_to_user_story_v2", prompt)

        print("✅ Prompt enviado com sucesso: bug_to_user_story_v2")
        return 0

    except Exception as e:
        print(f"❌ Erro ao enviar prompt: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
