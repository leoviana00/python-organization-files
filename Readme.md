# Python

## 馃尡 Projeto

- Script para `organizar por categoria os arquivos` do diret贸rio download

## Requisitos

- python 3

## Diret贸rio raiz

- O `diret贸rio raiz` 茅 criado de acordo com o Sistema Operacional, no meu caso foi o linux.

## Como funciona
Colque o `script` dentro do diret贸rio `downloads`

![](./imagens/script_in_dir.png)

- Execu莽茫o - Manual

```bash
python3 organization.py
```

- Execu莽茫o `criando log` (Crie um diret贸rio log, dentro do diret贸rio downloads

```bash
python3 organization.py >>~/Downloads/log/log.txt
```

- Nomeando o `log` com a data 

```bash
$ python3 automation.py >>~/Downloads/log/$(date +%Y_%m_%d)-log.txt
```

## Estrutura dos diret贸rios

- Crie o diret贸rio `log` dentro de `downloads`

- Ap贸s rodar o `script` os diret贸rios ser茫o criados e os arquivos ser茫o movidos para suas respectivas pastas.

![](./imagens/dir.png)

## Utilizando cronjob para agendamento do scrip

- Visualizando os `cronjobs` do sistema

```bash
$ sudo crontab -l
```

- Configurando um `cronjob` para rodar de 1 em 1 hora.

```bash
$ sudo crontab -e
```

- Adicione a segunte linha

```
0 */1 * * * cd ~/Downloads && python3 automation.py >> ~/Downloads/log/`date +\%d-\%m-\%y`-organization.log 2>&1
```

# Logs

- Os logs ser谩o armazenados dentro do diret贸rio `log` que voc锚 criou.

![](./imagens/log.png)


## Refer锚ncias

- https://medium.com/swlh/automation-python-organizing-files-5d2b6b933402
- https://dev.to/akashsenta13/python-script-to-organize-files-in-folders-5783
- https://docs.python.org/pt-br/3.7/library/shutil.html
- https://docs.python.org/pt-br/3/library/os.html


