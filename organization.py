import os
from shutil import move
from datetime import datetime

# Variáveis
root_dir = os.getcwd()
data_e_hora_atuais = datetime.now()
data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')

print('# ----------------------------------------------------------------------------------------')
print('#  Automação de organização de arquivos com python - Data: {}'.format(data_e_hora_em_texto))
print('# ----------------------------------------------------------------------------------------')

# Função para criar os diretórios
def make_folder(foldername):
    os.chdir(root_dir)
    if os.path.exists(foldername) == True:
        print('Diretório: ' + foldername + ' já existe!')
        return os.getcwd() + os.sep + str(foldername)
    else:
        os.mkdir(str(foldername))
        print('Diretório: ' + foldername + ' criado com sucesso!')
        return os.getcwd() + os.sep + str(foldername)

# Tipo dos arquivos - Categorias
doc_types = ('.doc', '.docx', '.txt', '.pdf', '.xls', '.ppt', '.xlsx', '.pptx')
img_types = ('.jpg', '.jpeg', '.png', '.svg', '.gif', '.tif', '.tiff')
softwares_types = ('.exe', '.pkg', '.dmg','.deb')
iso_types = ('.iso')

def get_non_hidden_files_except_current_file(root_dir):
    return [f for f in os.listdir(root_dir) if os.path.isfile(f) and not f.startswith('.') and not f.__eq__(__file__)]
    
def move_files(files):
    for file in files:
        
        # Criando diretorio `documents` e movendo os arquivos
        if file.endswith(doc_types):
            root_dir = make_folder('documentos')
            move(file, '{}/{}'.format(root_dir, file))
            print('O arquivo {} foi movido para: {}'.format(file, root_dir))
            
            
        # Criando diretorio `images` e movendo os arquivos    
        elif file.endswith(img_types):
            root_dir = make_folder('imagens')
            move(file, '{}/{}'.format(root_dir, file))
            print('O arquivo {} foi movido para: {}'.format(file, root_dir))
            
            
        # Criando diretorio `softwares` e movendo os arquivos
        elif file.endswith(softwares_types):
            root_dir = make_folder('softwares')
            move(file, '{}/{}'.format(root_dir, file))
            print('O arquivo {} foi movido para: {}'.format(file, root_dir))
            
            
        # Criando diretorio `iso` e movendo os arquivos
        elif file.endswith(iso_types):
            root_dir = make_folder('iso')
            move(file, '{}/{}'.format(root_dir, file))
            print('O arquivo {} foi movido para: {}'.format(file, root_dir))
            
            
        # Criando diretorio `others` e movendo os arquivos
        else:
            root_dir = make_folder('outros')
            move(file, '{}/{}'.format(root_dir, file))
            print('O arquivo {} foi movido para: {}'.format(file, root_dir))
            
            
if __name__ == "__main__":
    files = get_non_hidden_files_except_current_file(root_dir)
    move_files(files)
print('# ----------------------------------------------------------------------------------------')