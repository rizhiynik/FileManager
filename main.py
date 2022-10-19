import os
import shutil

root = input('Укажите абсолютный, где будет создана рабочая папка ')
os.chdir(root)

print(
    'Добро пожаловать в файловый менеджер!\nВнутри него Вы можете управлять файлами Вашей проектной работы при помощи использования специальных команд\nНиже представлен список этих команд:\n')
print('create_dir - Создать папку (с указанием имени)\n'
      'delete_dir - Удалить папку (с указанием имени)\n'
      'swap_dir - Перемещение между папками (реализует два типа ввода)\n1) При указании имени папки перемещает в доступную директорию внутри рабочей папки\n2) При указании ключевого слова up вместо имени папки перемещает на уровень выше\n'
      'show_dir - Выводит содержимое текущей папки\n'
      'create_file - Создать пустой текстовый файл (с указанием имени)\n'
      'write_file - Записать текст в файл (с указанием имени)\n'
      'read_file - Прочитать файл построчно (с указанием имени)\n'
      'delete_file - Удалить файл (с указанием имени)\n'
      'copy_file - Копировать файл в другую директорию (с указанием пути до копируемого файла и пути до места копирования)\n'
      'move_file - Переместить файл в другую директорию (с указанием пути до перемещаемого файла и пути до места перемещения)\n'
      'rename_file - Переименовать файл (с указаниме имени файла, который необходимо переименовать, и нового имени)\n')


class FileManager:
    def create_manager_dir(self):
        try:
            os.mkdir('FileManager')
            os.chdir('FileManager')

            with open('settings.txt', 'w') as f:
                f.write(root)

        except FileExistsError:
            os.chdir('FileManager')

            with open('settings.txt', 'w') as f:
                f.write(root)

    def create_dir(self):
        name = a.split(' ')[1]
        os.mkdir(name)

    def delete_dir(self):
        try:
            name = a.split(' ')[1]
            os.rmdir(name)
        except OSError:
            check = input(
                'Папка, которую вы пытаетесь удалить не является пустой, вы действительно хотите ее удалить? \n(введите yes, если да и no, если нет)')
            if check == 'yes':
                shutil.rmtree(name, ignore_errors=True)

    def swap_dir(self):
        if 'up' in a:
            if os.getcwd() == root:
                print('Покинуть директорию файлового менеджера невозможно')
            else:
                os.chdir('../')
        else:
            name = a.split(' ')[1]
            os.chdir(name)

    def show_dir(self):
        print(os.listdir(os.getcwd()))

    def create_file(self):
        name = a.split(' ')[1]
        f = open(name + '.txt', 'a')
        f.close()

    def write_file(self):
        text = input(
            'Введите текст, который хотите записать в файл (каждый новый ввод осуществляется на новой строке) ')
        name = a.split(' ')[1]
        f = open(name + '.txt', 'a')
        f.write(text + '\n')
        f.close()

    def read_file(self):
        name = a.split(' ')[1]
        f = open(name + '.txt', 'r')
        for line in f.readlines():
            print(line, end='')
        f.close()

    def delete_file(self):
        name = a.split(' ')[1]
        os.remove(name + '.txt')

    def copy_file(self):
        src = a.split(' ')[1]
        dst = a.split(' ')[2]
        shutil.copyfile(src, dst)

    def move_file(self):
        src = a.split(' ')[1]
        dst = a.split(' ')[2]
        shutil.move(src, dst)

    def rename_file(self):
        name = a.split(' ')[1]
        new_name = a.split(' ')[2]
        os.rename(name, new_name)


Manager = FileManager()
Manager.create_manager_dir()

root = os.getcwd()


a = 0

while a != 'break':
    print(os.getcwd())
    a = input('Введите какую-либо команду ')

    if 'create_dir' in a:
        Manager.create_dir()

    elif 'delete_dir' in a:
        Manager.delete_dir()

    elif 'swap_dir' in a:
        Manager.swap_dir()

    elif 'show_dir' in a:
        Manager.show_dir()

    elif 'create_file' in a:
        Manager.create_file()

    elif 'write_file' in a:
        Manager.write_file()

    elif 'read_file' in a:
        Manager.read_file()

    elif 'delete_file' in a:
        Manager.delete_file()

    elif 'copy_file' in a:
        Manager.copy_file()

    elif 'move_file' in a:
        Manager.move_file()

    elif 'rename_file' in a:
        Manager.rename_file()