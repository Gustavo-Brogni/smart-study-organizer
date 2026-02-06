# Complementador de Anotações com IA

Um sistema que utiliza uma IA local (neste caso o LM Studio) para complementar anotações de aula com informações adicionais que possam ser relevantes diante o contexto.

## Status atual
Em desenvolvimento ativo - Se trata de um projeto de aprendizado

## Funcionalidades atuais
- Leitura de arquivo de anotações (por ora .txt);
- Complementação via IA local (LM Studio);
- Geração de arquivo complementar organizado.

## Tecnologias
- Python 3
- LM Studio (Estou utilizando Mistral 3B)
- Biblioteca requests

## Próximos passos
- [ ] Processar múltiplos arquivos
- [ ] Integração com Google Drive
- [ ] Interface gráfica
- [ ] 'OCR' para cadernos físicos

## Como utilizar
1. Tenha um servidor do LM Studio rodando localmente com algum modelo LLM carregado;
2. Coloque suas anotações em um arquivo 'anotacoes.txt';
3. Execute: 'python complementador.py'
4. Resultado disponível em: 'anotacoes_complementadas.txt'